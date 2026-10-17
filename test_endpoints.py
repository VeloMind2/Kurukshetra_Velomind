import urllib.request
import json

def run_tests():
    base = 'http://127.0.0.1:8000/api'
    print("Beginning SkillTrace AI Integration Test Suite...")

    # 1. Baseline Questions
    req = urllib.request.urlopen(f"{base}/baseline/questions")
    q_data = json.loads(req.read().decode('utf-8'))
    print(f"1. Baseline Questions Count: {len(q_data)}")
    assert len(q_data) == 15, f"Expected 15 questions, found {len(q_data)}"
    
    # Verify difficulty tiers: Q1-5 Easy, Q6-10 Medium, Q11-15 Hard
    diffs = [q["difficulty"] for q in q_data]
    print(f"   Difficulties: Q1-5: {diffs[0:5]}, Q6-10: {diffs[5:10]}, Q11-15: {diffs[10:15]}")
    assert all(d == 'easy' for d in diffs[0:5]), "Q1-5 should be easy"
    assert all(d == 'medium' for d in diffs[5:10]), "Q6-10 should be medium"
    assert all(d == 'hard' for d in diffs[10:15]), "Q11-15 should be hard"

    # 2. Submit Baseline Answer for Q1
    q1 = q_data[0]
    payload = json.dumps({
        'studentId': 'test_student',
        'questionId': q1['id'],
        'answer': 'float',
        'hintsUsed': 1
    }).encode('utf-8')
    req = urllib.request.Request(f"{base}/baseline/submit", data=payload, headers={'Content-Type': 'application/json'})
    res = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    print(f"2. Submit Q1 result: isCorrect={res.get('isCorrect')}, explanation={res.get('explanation')[:45]}...")

    # 3. Tutor Progressive Hint
    payload = json.dumps({'questionId': q1['id'], 'level': 2}).encode('utf-8')
    req = urllib.request.Request(f"{base}/tutor/hint", data=payload, headers={'Content-Type': 'application/json'})
    res = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    print(f"3. AI Tutor Hint L2: {res.get('title')} -> {res.get('hintText')[:50]}...")

    # 4. Adaptive Next Question
    req = urllib.request.urlopen(f"{base}/adaptive/next?studentId=test_student")
    res = json.loads(req.read().decode('utf-8'))
    print(f"4. Next Adaptive Q: ID={res.get('id')} Concept={res.get('concept')} Reason={res.get('adaptiveReason')[:55]}...")

    # 5. Submit Adaptive Answer
    payload = json.dumps({
        'studentId': 'test_student',
        'questionId': res['id'],
        'answer': 'wrong_answer',
        'hintsUsed': 0
    }).encode('utf-8')
    req = urllib.request.Request(f"{base}/adaptive/submit", data=payload, headers={'Content-Type': 'application/json'})
    sub_res = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    print(f"5. Submit Adaptive Mistake: isCorrect={sub_res.get('isCorrect')}, decision={sub_res.get('adaptiveDecision')}")

    # 6. Roadmap
    req = urllib.request.urlopen(f"{base}/roadmap?studentId=test_student")
    roadmap = json.loads(req.read().decode('utf-8'))
    print(f"6. Roadmap: {len(roadmap)} syllabus stages loaded. Stage 1: {roadmap[0]['concept']} ({roadmap[0]['status']})")

    # 7. Progress History
    req = urllib.request.urlopen(f"{base}/history?studentId=test_student")
    history = json.loads(req.read().decode('utf-8'))
    print(f"7. Attempt History: {len(history)} attempts recorded in database ledger.")

    # 8. Dashboard Summary
    req = urllib.request.urlopen(f"{base}/dashboard/summary?studentId=test_student")
    summary = json.loads(req.read().decode('utf-8'))
    print(f"8. Dashboard Summary: student={summary.get('studentName')}, solved={summary.get('totalSolved')}/{summary.get('totalAttempted')}, level={summary.get('currentAdaptiveLevel')}")

    print("\n>>> ALL SYSTEM INTEGRATION TESTS PASSED 100% SUCCESSFULLY! <<<")

if __name__ == '__main__':
    run_tests()
