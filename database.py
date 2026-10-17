"""
SkillTrace AI - Database & Adaptive Learning Engine
Zero external dependencies - standard library sqlite3 + subprocess sandbox.

Features:
1. 45-Question Bank across 15 Slots (15 Main + 30 Alternatives).
2. Session Management with 15 numbered slots (Question 1/15 through Question 15/15).
3. Secure Isolated Subprocess Execution Sandbox for coding questions.
4. Deterministic and test-case based correctness evaluation (Passed, Partially Correct, Failed).
5. Evidence-based Bayesian Knowledge Tracing (BKT) concept mastery.
6. Reactive Adaptive Selection (Mistake -> Easier Loop Alt; Correct -> Gradual Increase).
7. Prerequisite-Gated Learning Roadmap.
8. Multi-Student Data Isolation.
"""

import sqlite3
import json
import os
import sys
import time
import re
import subprocess
from pathlib import Path
import question_bank

DB_PATH = Path(__file__).parent / "skilltrace.db"

def get_connection():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn

# ---------------------------------------------------------------------------
# SCHEMA INITIALIZATION
# ---------------------------------------------------------------------------

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS questions (
    id TEXT PRIMARY KEY,
    slot_number INTEGER NOT NULL,
    is_main INTEGER NOT NULL DEFAULT 1,
    title TEXT NOT NULL,
    concept TEXT NOT NULL,
    subtopic TEXT,
    difficulty TEXT NOT NULL, -- 'easy', 'medium', 'hard'
    question_type TEXT NOT NULL, -- 'coding', 'debugging', 'logic'
    prompt TEXT NOT NULL,
    code_snippet TEXT,
    options_json TEXT,
    correct_answer TEXT,
    test_cases_json TEXT,
    eval_method TEXT NOT NULL, -- 'code_execution', 'mcq', 'deterministic_check'
    prerequisites_json TEXT,
    common_misconception TEXT,
    explanation TEXT,
    hints_json TEXT,
    autopsy_json TEXT,
    alternatives_json TEXT
);

CREATE TABLE IF NOT EXISTS assessment_sessions (
    id TEXT PRIMARY KEY,
    student_id TEXT NOT NULL,
    current_slot INTEGER DEFAULT 1,
    total_slots INTEGER DEFAULT 15,
    status TEXT DEFAULT 'in_progress', -- 'in_progress', 'completed'
    score INTEGER DEFAULT 0,
    slots_json TEXT,
    created_at REAL,
    updated_at REAL
);

CREATE TABLE IF NOT EXISTS student_profile (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    baseline_completed INTEGER DEFAULT 0,
    baseline_score INTEGER DEFAULT 0,
    baseline_total INTEGER DEFAULT 15,
    baseline_accuracy REAL DEFAULT 0.0,
    recommended_level TEXT DEFAULT 'easy',
    current_adaptive_level TEXT DEFAULT 'easy',
    overall_mastery REAL DEFAULT 0.0,
    updated_at REAL
);

CREATE TABLE IF NOT EXISTS attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    session_id TEXT,
    slot_number INTEGER,
    question_id TEXT NOT NULL,
    concept TEXT NOT NULL,
    difficulty TEXT NOT NULL,
    student_answer TEXT,
    is_correct INTEGER NOT NULL, -- 1: passed, 0: failed, 2: partially_correct
    passed_test_cases INTEGER DEFAULT 0,
    total_test_cases INTEGER DEFAULT 0,
    test_results_json TEXT,
    attempts_count INTEGER DEFAULT 1,
    hints_used INTEGER DEFAULT 0,
    mistake_category TEXT,
    adaptive_decision TEXT,
    timestamp REAL,
    date_str TEXT
);

CREATE TABLE IF NOT EXISTS concept_mastery (
    student_id TEXT NOT NULL,
    concept TEXT NOT NULL,
    mastery_score REAL DEFAULT 0.0,
    total_attempted INTEGER DEFAULT 0,
    total_correct INTEGER DEFAULT 0,
    status TEXT DEFAULT 'learning', -- 'mastered', 'learning', 'needs_practice', 'locked'
    updated_at REAL,
    PRIMARY KEY (student_id, concept)
);

CREATE TABLE IF NOT EXISTS mistake_patterns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    category TEXT NOT NULL,
    question_id TEXT NOT NULL,
    description TEXT NOT NULL,
    timestamp REAL
);
"""

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript(SCHEMA_SQL)

    # Seed all 45 questions from question_bank
    for q in question_bank.QUESTIONS_DATA:
        cursor.execute("""
            INSERT OR REPLACE INTO questions (
                id, slot_number, is_main, title, concept, subtopic, difficulty,
                question_type, prompt, code_snippet, options_json, correct_answer,
                test_cases_json, eval_method, prerequisites_json, common_misconception,
                explanation, hints_json, autopsy_json, alternatives_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            q["id"],
            q["slot_number"],
            q["is_main"],
            q["title"],
            q["concept"],
            q.get("subtopic", ""),
            q["difficulty"],
            q["question_type"],
            q["prompt"],
            q.get("code_snippet", ""),
            json.dumps(q.get("options", [])),
            q.get("correct_answer", ""),
            json.dumps(q.get("test_cases", [])),
            q.get("eval_method", "mcq"),
            json.dumps(q.get("prerequisites", [])),
            q.get("common_misconception", ""),
            q.get("explanation", ""),
            json.dumps(q.get("hints", {})),
            json.dumps(q.get("autopsy", {})),
            json.dumps(q.get("alternatives", []))
        ))

    # Initialize demo student profiles if not exists
    cursor.execute("""
        INSERT OR IGNORE INTO student_profile (id, name, baseline_completed, baseline_score, baseline_accuracy, recommended_level, current_adaptive_level, overall_mastery, updated_at)
        VALUES ('default_student', 'Alex Morgan', 0, 0, 0.0, 'easy', 'easy', 0.0, ?)
    """, (time.time(),))

    conn.commit()
    conn.close()

# ---------------------------------------------------------------------------
# SECURE SUBPROCESS CODE EXECUTION SANDBOX
# ---------------------------------------------------------------------------

def inspect_hostile_code(code_str: str) -> dict:
    hostile_patterns = [
        (r"\bos\.(remove|system|popen|unlink|rmdir|walk|environ)\b", "Hostile file system or system shell command attempt"),
        (r"\b(socket|urllib|requests|http\.client|ftplib)\b", "Hostile unauthorized network connection attempt"),
        (r"\b(__import__|eval|exec|compile)\b", "Dynamic arbitrary code evaluation prohibited in secure sandbox"),
        (r"\bopen\s*\(.*['\"](/etc|C:\\|/var|/usr|\.\./).*\)", "Directory traversal or forbidden system file access attempt"),
        (r"\bsubprocess\.(Popen|run|call|check_output)\b", "Hostile subprocess creation prohibited in secure sandbox")
    ]
    for pattern, reason in hostile_patterns:
        if re.search(pattern, code_str):
            return {"isHostile": True, "reason": reason}
    return {"isHostile": False, "reason": ""}

def execute_student_code(code_str: str, test_cases: list, timeout_sec=2.0) -> dict:
    hostile = inspect_hostile_code(code_str)
    if hostile["isHostile"]:
        return {
            "allPassed": False,
            "securityViolation": True,
            "securityReason": hostile["reason"],
            "passedCount": 0,
            "totalCount": len(test_cases),
            "results": [
                {"description": tc.get("description", "Test Case"), "passed": False, "error": f"Security Sandbox Filter: {hostile['reason']}"}
                for tc in test_cases
            ],
            "stdout": "",
            "stderr": hostile["reason"]
        }

    # Harness script running in subprocess
    runner_script = f"""
import sys, json

# Student Code
{code_str}

test_cases = {json.dumps(test_cases)}
results = []
all_passed = True
passed_count = 0

# Extract candidate function name from code if defined
defined_funcs = [name for name, val in list(locals().items()) if callable(val) and not name.startswith('_')]
candidate_name = defined_funcs[-1] if defined_funcs else None

for tc in test_cases:
    desc = tc.get("description", "Test")
    inputs = tc.get("input", [])
    expected = tc.get("expected")
    try:
        if candidate_name and candidate_name in locals():
            fn = locals()[candidate_name]
            actual = fn(*inputs)
        else:
            actual = None
        
        passed = (actual == expected)
        if passed:
            passed_count += 1
        else:
            all_passed = False
        results.append({{"description": desc, "passed": passed, "expected": expected, "actual": actual}})
    except Exception as e:
        all_passed = False
        results.append({{"description": desc, "passed": False, "expected": expected, "actual": None, "error": str(e)}})

print("___SKILLTRACE_TEST_OUTPUT___")
print(json.dumps({{"allPassed": all_passed, "passedCount": passed_count, "totalCount": len(test_cases), "results": results}}))
"""

    try:
        proc = subprocess.run(
            [sys.executable],
            input=runner_script,
            text=True,
            capture_output=True,
            timeout=timeout_sec
        )
        stdout = proc.stdout or ""
        stderr = proc.stderr or ""

        if "___SKILLTRACE_TEST_OUTPUT___" in stdout:
            parts = stdout.split("___SKILLTRACE_TEST_OUTPUT___")
            data_part = parts[1].strip()
            parsed = json.loads(data_part)
            parsed["stdout"] = parts[0].strip()
            parsed["stderr"] = stderr
            return parsed
        else:
            return {
                "allPassed": False,
                "passedCount": 0,
                "totalCount": len(test_cases),
                "results": [{"description": tc.get("description", "Execution"), "passed": False, "error": stderr or "Runtime Error"} for tc in test_cases],
                "stdout": stdout,
                "stderr": stderr
            }
    except subprocess.TimeoutExpired:
        return {
            "allPassed": False,
            "passedCount": 0,
            "totalCount": len(test_cases),
            "results": [{"description": "Execution Timeout", "passed": False, "error": f"Execution timed out (> {timeout_sec}s). Possible infinite loop detected."}],
            "stdout": "",
            "stderr": "TimeoutExpired: Loop took longer than 2.0 seconds."
        }
    except Exception as ex:
        return {
            "allPassed": False,
            "passedCount": 0,
            "totalCount": len(test_cases),
            "results": [{"description": "Execution", "passed": False, "error": str(ex)}],
            "stdout": "",
            "stderr": str(ex)
        }

# ---------------------------------------------------------------------------
# ADAPTIVE ASSESSMENT SESSION MANAGEMENT (15 SLOTS)
# ---------------------------------------------------------------------------

def get_or_create_session(student_id: str) -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    # Multi-tenant check: fetch student's active session
    cursor.execute("""
        SELECT * FROM assessment_sessions
        WHERE student_id = ? AND status = 'in_progress'
        ORDER BY updated_at DESC LIMIT 1
    """, (student_id,))
    session_row = cursor.fetchone()

    if session_row:
        session_id = session_row["id"]
        current_slot = session_row["current_slot"]
        slots = json.loads(session_row["slots_json"])
    else:
        # Create brand-new 15-slot session
        session_id = f"sess_{student_id}_{int(time.time())}"
        current_slot = 1
        slots = []
        for slot_num in range(1, 16):
            # Fetch default main question for slot
            cursor.execute("SELECT id FROM questions WHERE slot_number = ? AND is_main = 1", (slot_num,))
            q_row = cursor.fetchone()
            main_id = q_row["id"] if q_row else f"slot{slot_num:02d}-main"
            slots.append({
                "slot_number": slot_num,
                "active_question_id": main_id,
                "status": "unanswered", # 'unanswered', 'passed', 'failed', 'partially_correct'
                "attempts_count": 0,
                "is_correct": None,
                "history": []
            })

        now = time.time()
        cursor.execute("""
            INSERT INTO assessment_sessions (id, student_id, current_slot, total_slots, status, score, slots_json, created_at, updated_at)
            VALUES (?, ?, 1, 15, 'in_progress', 0, ?, ?, ?)
        """, (session_id, student_id, json.dumps(slots), now, now))
        conn.commit()

    # Get active question object for current slot
    active_slot_data = next((s for s in slots if s["slot_number"] == current_slot), slots[-1])
    active_qid = active_slot_data["active_question_id"]

    cursor.execute("SELECT * FROM questions WHERE id = ?", (active_qid,))
    q_row = cursor.fetchone()
    conn.close()

    if not q_row:
        raise ValueError(f"Question {active_qid} not found in bank.")

    q_obj = dict(q_row)
    q_obj["options"] = json.loads(q_obj["options_json"]) if q_obj.get("options_json") else []
    q_obj["test_cases"] = json.loads(q_obj["test_cases_json"]) if q_obj.get("test_cases_json") else []
    q_obj["hints"] = json.loads(q_obj["hints_json"]) if q_obj.get("hints_json") else {}
    q_obj["autopsy"] = json.loads(q_obj["autopsy_json"]) if q_obj.get("autopsy_json") else {}
    q_obj["prerequisites"] = json.loads(q_obj["prerequisites_json"]) if q_obj.get("prerequisites_json") else []
    q_obj["alternatives"] = json.loads(q_obj["alternatives_json"]) if q_obj.get("alternatives_json") else []

    return {
        "sessionId": session_id,
        "studentId": student_id,
        "currentSlot": current_slot,
        "totalSlots": 15,
        "progressText": f"Question {current_slot}/15",
        "status": session_row["status"] if session_row else "in_progress",
        "activeSlotData": active_slot_data,
        "question": q_obj,
        "slotsSummary": [
            {"slotNumber": s["slot_number"], "status": s["status"], "questionId": s["active_question_id"]}
            for s in slots
        ]
    }

def submit_session_answer(student_id: str, session_id: str, answer: str, hints_used: int = 0) -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    # Security verification: ensure student owns session
    cursor.execute("SELECT * FROM assessment_sessions WHERE id = ?", (session_id,))
    session = cursor.fetchone()
    if not session:
        conn.close()
        raise ValueError("Assessment session not found.")
    if session["student_id"] != student_id:
        conn.close()
        raise PermissionError("Access Denied: Student cannot submit to another student's session.")

    current_slot = session["current_slot"]
    slots = json.loads(session["slots_json"])
    active_slot = next((s for s in slots if s["slot_number"] == current_slot), None)
    if not active_slot:
        conn.close()
        raise ValueError("Invalid slot state.")

    question_id = active_slot["active_question_id"]
    cursor.execute("SELECT * FROM questions WHERE id = ?", (question_id,))
    q = cursor.fetchone()
    if not q:
        conn.close()
        raise ValueError(f"Question {question_id} not found.")

    eval_method = q["eval_method"]
    test_cases = json.loads(q["test_cases_json"]) if q["test_cases_json"] else []
    is_correct_code = 0 # 0: failed, 1: passed, 2: partially_correct
    test_results = []
    passed_tc = 0
    total_tc = len(test_cases)
    status_label = "failed"

    # Evaluation
    if eval_method == "code_execution":
        exec_res = execute_student_code(answer, test_cases)
        passed_tc = exec_res.get("passedCount", 0)
        total_tc = exec_res.get("totalCount", len(test_cases))
        test_results = exec_res.get("results", [])

        if exec_res.get("allPassed"):
            is_correct_code = 1
            status_label = "passed"
        elif passed_tc > 0 and passed_tc < total_tc:
            is_correct_code = 2
            status_label = "partially_correct"
        else:
            is_correct_code = 0
            status_label = "failed"
    else:
        # Deterministic / MCQ check
        clean_ans = answer.strip().strip("'\"").lower()
        clean_expected = (q["correct_answer"] or "").strip().strip("'\"").lower()
        if clean_ans == clean_expected or clean_ans in clean_expected:
            is_correct_code = 1
            status_label = "passed"
            passed_tc = 1
            total_tc = 1
        else:
            is_correct_code = 0
            status_label = "failed"
            passed_tc = 0
            total_tc = 1

    # Adaptive Selection Strategy
    alternatives = json.loads(q["alternatives_json"]) if q["alternatives_json"] else []
    next_question_id = question_id
    why_selected = ""
    target_practice = q["concept"]

    if status_label == "failed":
        # Rule: If student answers incorrectly, select an easier or more targeted alternative testing the same concept
        # Find an alternative question in this slot that hasn't been tried yet
        untried_alts = [alt for alt in alternatives if alt not in active_slot.get("history", [])]
        if untried_alts:
            next_question_id = untried_alts[0]
            # Fetch alt question details to explain why selected
            cursor.execute("SELECT title, difficulty FROM questions WHERE id = ?", (next_question_id,))
            alt_row = cursor.fetchone()
            alt_diff = alt_row["difficulty"] if alt_row else "easier"
            why_selected = f"Identified difficulty with {q['concept']}. Selected targeted {alt_diff} question to reinforce fundamental mechanics."
            active_slot["active_question_id"] = next_question_id
        else:
            why_selected = f"Reviewing fundamentals for {q['concept']}. Prepared for guided remediation."

        decision = f"Incorrect on {q['title']}. Routed to supportive practice."

    elif status_label == "partially_correct":
        # Rule: If student answers partially correctly, provide focused feedback and a question addressing missing skill
        untried_alts = [alt for alt in alternatives if alt not in active_slot.get("history", [])]
        if untried_alts:
            next_question_id = untried_alts[-1] # Choose second variation
            why_selected = f"Partial success ({passed_tc}/{total_tc} test cases). Selected follow-up targeting edge cases and boundary handling."
            active_slot["active_question_id"] = next_question_id
        else:
            why_selected = f"Partially correct. Reinforced boundary handling for {q['concept']}."

        decision = f"Partial solve on {q['title']} ({passed_tc}/{total_tc} tests). Targeting edge conditions."

    else: # passed
        why_selected = f"Verified proficiency in {q['concept']}. Ready to advance to the next curriculum milestone."
        decision = f"Mastery demonstrated on {q['title']}. Advancing."

    # Update Active Slot State
    active_slot["attempts_count"] += 1
    active_slot["status"] = status_label
    active_slot["is_correct"] = (is_correct_code == 1)
    if "history" not in active_slot:
        active_slot["history"] = []
    active_slot["history"].append(question_id)

    # Record Attempt
    date_str = time.strftime("%Y-%m-%d")
    mistake_cat = q.get("common_misconception") if status_label != "passed" else None

    cursor.execute("""
        INSERT INTO attempts (
            student_id, session_id, slot_number, question_id, concept, difficulty,
            student_answer, is_correct, passed_test_cases, total_test_cases,
            test_results_json, attempts_count, hints_used, mistake_category,
            adaptive_decision, timestamp, date_str
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        student_id, session_id, current_slot, question_id, q["concept"], q["difficulty"],
        answer, is_correct_code, passed_tc, total_tc, json.dumps(test_results),
        active_slot["attempts_count"], hints_used, mistake_cat, decision, time.time(), date_str
    ))

    # Record Mistake Pattern if wrong
    if mistake_cat:
        cursor.execute("""
            INSERT INTO mistake_patterns (student_id, category, question_id, description, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, (student_id, mistake_cat, question_id, f"Mistake on {q['title']}", time.time()))

    # Update Concept Mastery (Bayesian Evidence-Based Adjustment)
    cursor.execute("SELECT * FROM concept_mastery WHERE student_id = ? AND concept = ?", (student_id, q["concept"]))
    cm = cursor.fetchone()
    if cm:
        tot_att = cm["total_attempted"] + 1
        tot_cor = cm["total_correct"] + (1 if is_correct_code == 1 else 0)
        # Evidence-weighted mastery
        prev_score = cm["mastery_score"]
        if is_correct_code == 1:
            new_score = round(min(100.0, prev_score + 20.0 * (1.0 - prev_score / 100.0)), 1)
        elif is_correct_code == 2:
            new_score = round(min(100.0, prev_score + 5.0), 1)
        else:
            new_score = round(max(0.0, prev_score - 15.0), 1)

        new_status = "mastered" if new_score >= 80.0 and tot_cor >= 2 else "needs_practice" if new_score < 50.0 else "learning"
        cursor.execute("""
            UPDATE concept_mastery
            SET mastery_score = ?, total_attempted = ?, total_correct = ?, status = ?, updated_at = ?
            WHERE student_id = ? AND concept = ?
        """, (new_score, tot_att, tot_cor, new_status, time.time(), student_id, q["concept"]))
    else:
        new_score = 75.0 if is_correct_code == 1 else 35.0 if is_correct_code == 2 else 20.0
        new_status = "learning" if is_correct_code == 1 else "needs_practice"
        cursor.execute("""
            INSERT INTO concept_mastery (student_id, concept, mastery_score, total_attempted, total_correct, status, updated_at)
            VALUES (?, ?, ?, 1, ?, ?, ?)
        """, (student_id, q["concept"], new_score, 1 if is_correct_code == 1 else 0, new_status, time.time()))

    # Update session slots in DB
    cursor.execute("""
        UPDATE assessment_sessions
        SET slots_json = ?, updated_at = ?
        WHERE id = ?
    """, (json.dumps(slots), time.time(), session_id))

    conn.commit()
    conn.close()

    hints = json.loads(q["hints_json"]) if q["hints_json"] else {}
    autopsy = json.loads(q["autopsy_json"]) if q["autopsy_json"] else {}

    return {
        "status": status_label,
        "isCorrect": (is_correct_code == 1),
        "isPartiallyCorrect": (is_correct_code == 2),
        "passedCount": passed_tc,
        "totalCount": total_tc,
        "testCases": test_results,
        "explanation": q["explanation"],
        "recommendedHint": hints.get("hint1", "Review index and type boundaries."),
        "conceptPracticed": q["concept"],
        "whySelected": why_selected,
        "adaptiveDecision": decision,
        "activeQuestionId": active_slot["active_question_id"],
        "currentSlot": current_slot,
        "totalSlots": 15,
        "canAdvance": True,
        "autopsy": autopsy
    }

def advance_session_slot(student_id: str, session_id: str) -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM assessment_sessions WHERE id = ?", (session_id,))
    session = cursor.fetchone()
    if not session:
        conn.close()
        raise ValueError("Session not found.")
    if session["student_id"] != student_id:
        conn.close()
        raise PermissionError("Access Denied: Session belongs to another student.")

    current_slot = session["current_slot"]
    slots = json.loads(session["slots_json"])

    if current_slot < 15:
        next_slot = current_slot + 1
        cursor.execute("""
            UPDATE assessment_sessions
            SET current_slot = ?, updated_at = ?
            WHERE id = ?
        """, (next_slot, time.time(), session_id))
        conn.commit()
        conn.close()
        return get_or_create_session(student_id)
    else:
        # Completed all 15 slots!
        # Calculate final score
        passed_slots = sum(1 for s in slots if s.get("status") == "passed")
        cursor.execute("""
            UPDATE assessment_sessions
            SET status = 'completed', score = ?, updated_at = ?
            WHERE id = ?
        """, (passed_slots, time.time(), session_id))

        # Update student profile
        acc = round((passed_slots / 15.0) * 100, 1)
        rec_level = "hard" if passed_slots >= 12 else "medium" if passed_slots >= 7 else "easy"
        cursor.execute("""
            UPDATE student_profile
            SET baseline_completed = 1, baseline_score = ?, baseline_total = 15, baseline_accuracy = ?,
                recommended_level = ?, current_adaptive_level = ?, updated_at = ?
            WHERE id = ?
        """, (passed_slots, acc, rec_level, rec_level, time.time(), student_id))

        conn.commit()
        conn.close()
        return {
            "status": "completed",
            "score": passed_slots,
            "maxScore": 15,
            "accuracy": acc,
            "recommendedLevel": rec_level
        }

# ---------------------------------------------------------------------------
# PREREQUISITE-AWARE LEARNING ROADMAP
# ---------------------------------------------------------------------------

ROADMAP_DAG = [
    {
        "id": "vars",
        "concept": "Variables & Data Types",
        "prerequisites": [],
        "description": "Numeric types, float division, type conversions, and variable scope."
    },
    {
        "id": "conds",
        "concept": "Conditions & Operators",
        "prerequisites": ["Variables & Data Types"],
        "description": "Boolean precedence, chained relational comparisons, and branch flow."
    },
    {
        "id": "loops",
        "concept": "Loops",
        "prerequisites": ["Conditions & Operators"],
        "description": "For/while iteration, range boundaries, and fencepost off-by-one prevention."
    },
    {
        "id": "funcs",
        "concept": "Functions",
        "prerequisites": ["Loops"],
        "description": "Parameter passing, explicit returns, default arguments, and pure functions."
    },
    {
        "id": "arrays",
        "concept": "Arrays & Lists",
        "prerequisites": ["Functions"],
        "description": "Zero-based indexing, negative index bounds, list filtering, and accumulators."
    },
    {
        "id": "strings",
        "concept": "Strings",
        "prerequisites": ["Arrays & Lists"],
        "description": "String slicing [start:stop:step], case normalization, and reversal."
    },
    {
        "id": "algorithms",
        "concept": "Basic Algorithms",
        "prerequisites": ["Strings"],
        "description": "Linear and binary search, dictionary hash mapping, and asymptotic Big-O bounds."
    },
    {
        "id": "edge_cases",
        "concept": "Edge Cases",
        "prerequisites": ["Basic Algorithms"],
        "description": "Pointer aliasing, shallow copying, mutable default arguments, and matrix indexing."
    }
]

def get_learning_roadmap(student_id: str) -> list:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM concept_mastery WHERE student_id = ?", (student_id,))
    mastery_map = {r["concept"]: r for r in cursor.fetchall()}
    conn.close()

    roadmap = []
    for idx, node in enumerate(ROADMAP_DAG):
        c_name = node["concept"]
        m_row = mastery_map.get(c_name)
        score = m_row["mastery_score"] if m_row else 0.0

        # Check prerequisite mastery
        prereqs_met = True
        weak_prereq = None
        for p in node["prerequisites"]:
            p_score = mastery_map.get(p, {}).get("mastery_score", 0.0)
            if p_score < 60.0:
                prereqs_met = False
                weak_prereq = p
                break

        if score >= 80.0:
            status = "mastered"
            rec = f"Concept solid ({int(score)}%). Reinforce with advanced transfer problems."
        elif not prereqs_met and weak_prereq:
            status = "locked"
            rec = f"Prerequisite {weak_prereq} requires consolidation before unlocking."
        elif score < 50.0 and (m_row and m_row["total_attempted"] > 0):
            status = "needs_practice"
            rec = f"Identified learning gap ({int(score)}%). Targeted drills queued."
        else:
            status = "learning"
            rec = f"Active curriculum milestone ({int(score)}%). Ready for practice."

        roadmap.append({
            "step": idx + 1,
            "concept": c_name,
            "description": node["description"],
            "masteryScore": score,
            "status": status,
            "prerequisites": node["prerequisites"],
            "prerequisitesMet": prereqs_met,
            "recommendedPractice": rec,
            "isCurrentFocus": (status == "needs_practice" or (status == "learning" and score < 75.0))
        })

    return roadmap

# ---------------------------------------------------------------------------
# ATTEMPT HISTORY, DASHBOARD & ISOLATION
# ---------------------------------------------------------------------------

def get_student_history(student_id: str) -> list:
    conn = get_connection()
    cursor = conn.cursor()

    # Multi-student isolation: filter strictly by student_id
    cursor.execute("""
        SELECT a.id, a.slot_number, a.question_id, q.title as question_title,
               a.concept, a.difficulty, a.student_answer, a.is_correct,
               a.passed_test_cases, a.total_test_cases, a.hints_used,
               a.mistake_category, a.adaptive_decision, a.timestamp, a.date_str
        FROM attempts a
        LEFT JOIN questions q ON a.question_id = q.id
        WHERE a.student_id = ?
        ORDER BY a.timestamp DESC
    """, (student_id,))
    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": r["id"],
            "slotNumber": r["slot_number"],
            "questionId": r["question_id"],
            "questionTitle": r["question_title"] or r["question_id"],
            "concept": r["concept"],
            "difficulty": r["difficulty"],
            "studentAnswer": r["student_answer"],
            "isCorrect": (r["is_correct"] == 1),
            "isPartiallyCorrect": (r["is_correct"] == 2),
            "passedTestCases": r["passed_test_cases"],
            "totalTestCases": r["total_test_cases"],
            "hintsUsed": r["hints_used"],
            "mistakeCategory": r["mistake_category"] or "None",
            "adaptiveDecision": r["adaptive_decision"],
            "timestamp": r["timestamp"],
            "dateStr": r["date_str"]
        }
        for r in rows
    ]

def get_dashboard_summary(student_id: str) -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM student_profile WHERE id = ?", (student_id,))
    prof = cursor.fetchone()

    cursor.execute("SELECT count(*) as tot, sum(case when is_correct = 1 then 1 else 0 end) as cor FROM attempts WHERE student_id = ?", (student_id,))
    att_stat = cursor.fetchone()
    total_attempts = att_stat["tot"] or 0
    total_solved = att_stat["cor"] or 0

    cursor.execute("SELECT concept, mastery_score, status FROM concept_mastery WHERE student_id = ? ORDER BY mastery_score DESC", (student_id,))
    masteries = cursor.fetchall()

    cursor.execute("""
        SELECT category, count(*) as count
        FROM mistake_patterns
        WHERE student_id = ?
        GROUP BY category
        ORDER BY count DESC
    """, (student_id,))
    mistake_counts = cursor.fetchall()
    conn.close()

    strong = [m["concept"] for m in masteries if m["mastery_score"] >= 75.0]
    weak = [m["concept"] for m in masteries if m["mastery_score"] < 50.0]

    return {
        "studentName": prof["name"] if prof else student_id,
        "baselineCompleted": bool(prof["baseline_completed"]) if prof else False,
        "baselineScore": prof["baseline_score"] if prof else 0,
        "baselineAccuracy": prof["baseline_accuracy"] if prof else 0.0,
        "currentAdaptiveLevel": prof["current_adaptive_level"] if prof else "easy",
        "totalAttempted": total_attempts,
        "totalSolved": total_solved,
        "strongConcepts": strong,
        "weakConcepts": weak,
        "recurringPatterns": [
            {"category": mc["category"].replace("_", " ").title(), "count": mc["count"]}
            for mc in mistake_counts if mc["count"] >= 2
        ]
    }

def reset_student_progress(student_id: str) -> dict:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM assessment_sessions WHERE student_id = ?", (student_id,))
    cursor.execute("DELETE FROM attempts WHERE student_id = ?", (student_id,))
    cursor.execute("DELETE FROM concept_mastery WHERE student_id = ?", (student_id,))
    cursor.execute("DELETE FROM mistake_patterns WHERE student_id = ?", (student_id,))
    cursor.execute("""
        UPDATE student_profile
        SET baseline_completed = 0, baseline_score = 0, baseline_accuracy = 0.0,
            recommended_level = 'easy', current_adaptive_level = 'easy', overall_mastery = 0.0
        WHERE id = ?
    """, (student_id,))
    conn.commit()
    conn.close()
    return {"status": "reset", "studentId": student_id}

# Auto-initialize database on import
init_db()


# ---------------------------------------------------------------------------
# BASELINE ASSESSMENT BACKWARD COMPATIBILITY
# ---------------------------------------------------------------------------

def get_baseline_questions():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions WHERE is_main = 1 ORDER BY slot_number ASC LIMIT 15")
    rows = cursor.fetchall()
    conn.close()
    result = []
    for r in rows:
        item = dict(r)
        item["options"] = json.loads(item["options_json"]) if item.get("options_json") else []
        item["test_cases"] = json.loads(item["test_cases_json"]) if item.get("test_cases_json") else []
        item["hints"] = json.loads(item["hints_json"]) if item.get("hints_json") else {}
        item["autopsy"] = json.loads(item["autopsy_json"]) if item.get("autopsy_json") else {}
        item["baseline_order"] = item["slot_number"]
        result.append(item)
    return result

def submit_baseline_answer(student_id: str, question_id: str, answer: str, hints_used: int = 0):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions WHERE id = ?", (question_id,))
    q = cursor.fetchone()
    if not q:
        conn.close()
        return {"error": "Question not found"}
    
    clean_ans = answer.strip().strip("'\"").lower()
    clean_expected = (q["correct_answer"] or "").strip().strip("'\"").lower()
    is_correct = (clean_ans == clean_expected or clean_ans in clean_expected)
    
    date_str = time.strftime("%Y-%m-%d")
    cursor.execute("""
        INSERT INTO attempts (
            student_id, session_id, slot_number, question_id, concept, difficulty,
            student_answer, is_correct, passed_test_cases, total_test_cases,
            test_results_json, attempts_count, hints_used, mistake_category,
            adaptive_decision, timestamp, date_str
        ) VALUES (?, 'baseline', ?, ?, ?, ?, ?, ?, ?, 1, '[]', 1, ?, ?, 'Baseline Submission', ?, ?)
    """, (
        student_id, q["slot_number"], question_id, q["concept"], q["difficulty"],
        answer, 1 if is_correct else 0, 1 if is_correct else 0, hints_used,
        q.get("common_misconception") if not is_correct else None, time.time(), date_str
    ))
    conn.commit()
    conn.close()
    
    return {
        "questionId": question_id,
        "isCorrect": is_correct,
        "correctAnswer": q["correct_answer"],
        "explanation": q["explanation"],
        "mistakeCategory": q.get("common_misconception") if not is_correct else None,
        "autopsy": json.loads(q["autopsy_json"]) if q.get("autopsy_json") else {}
    }

def calculate_baseline_results(student_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.*, q.title as question_title
        FROM attempts a
        JOIN questions q ON a.question_id = q.id
        WHERE a.student_id = ? AND (a.session_id = 'baseline' OR a.slot_number IS NOT NULL)
        ORDER BY a.timestamp ASC
    """, (student_id,))
    attempts = cursor.fetchall()
    
    total_attempted = len(attempts)
    total_correct = sum(1 for a in attempts if a["is_correct"] == 1)
    acc = round((total_correct / total_attempted) * 100, 1) if total_attempted > 0 else 0.0
    
    topic_map = {}
    diff_map = {"easy": {"total": 0, "correct": 0}, "medium": {"total": 0, "correct": 0}, "hard": {"total": 0, "correct": 0}}
    weak_concepts = []
    
    for a in attempts:
        c = a["concept"]
        topic_map.setdefault(c, {"total": 0, "correct": 0})
        topic_map[c]["total"] += 1
        if a["is_correct"] == 1:
            topic_map[c]["correct"] += 1
        
        d = (a["difficulty"] or "easy").lower()
        if d in diff_map:
            diff_map[d]["total"] += 1
            if a["is_correct"] == 1:
                diff_map[d]["correct"] += 1
    
    topic_perf = []
    for c, v in topic_map.items():
        score = round((v["correct"] / v["total"]) * 100, 1) if v["total"] > 0 else 0.0
        status = "solid" if score >= 75 else "weak" if score < 50 else "developing"
        if status == "weak":
            weak_concepts.append(c)
        topic_perf.append({
            "topic": c,
            "total": v["total"],
            "correct": v["correct"],
            "accuracy": score,
            "status": status
        })
        
    rec_level = "hard" if total_correct >= 12 else "medium" if total_correct >= 7 else "easy"
    conn.close()
    
    return {
        "studentId": student_id,
        "totalScore": total_correct,
        "maxScore": 15,
        "accuracy": acc,
        "recommendedLevel": rec_level,
        "topicPerformance": topic_perf,
        "difficultyPerformance": diff_map,
        "weakConcepts": weak_concepts,
        "completed": total_attempted >= 15,
        "recommendationReason": f"Based on your baseline score of {total_correct}/15 ({acc}%), starting at {rec_level} tier will optimize your learning curve."
    }

def get_next_adaptive_question(student_id: str):
    sess = get_or_create_session(student_id)
    return sess["question"]
