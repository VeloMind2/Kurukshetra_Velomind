import json

def build_full_question_bank():
    questions = [
        # SLOT 1
        {
            "id": "slot01-main", "slot_number": 1, "is_main": 1,
            "title": "Division Operator Return Type", "concept": "Variables & Data Types",
            "subtopic": "Numeric Types & Float Promotion", "difficulty": "easy",
            "question_type": "logic",
            "prompt": "In modern Python 3, what is the exact data type of variable `result` after executing: `result = 7 / 2`?",
            "code_snippet": "result = 7 / 2\nprint(type(result))",
            "options": ["int", "float", "double", "Fraction"], "correct_answer": "float",
            "test_cases": [], "eval_method": "mcq", "prerequisites": [],
            "common_misconception": "Confusing Python 2 integer truncation division with Python 3 true float division.",
            "explanation": "In Python 3, single-slash division `/` always returns a float (3.5), whereas floor division `//` returns an integer (3).",
            "hints": {
                "hint1": "Consider how Python 3 handles division with numbers that do not divide evenly.",
                "hint2": "Does single `/` truncate fractional parts or preserve decimals as floating-point?",
                "hint3": "7 / 2 evaluates to 3.5, which has a decimal component.",
                "example": "For instance, `4 / 2` also returns `2.0` (a float), not integer `2`."
            },
            "autopsy": {
                "whatTested": "Understanding numeric primitive types and division behavior in Python.",
                "whyWorks": "Python 3 promotes all `/` operations to IEEE-754 double-precision floating-point numbers.",
                "stepByStep": [
                    {"step": 1, "description": "Expression 7 / 2 is parsed.", "state": "Operands 7 and 2 loaded"},
                    {"step": 2, "description": "Floating-point division is invoked.", "state": "Intermediate 3.5 calculated"},
                    {"step": 3, "description": "Type of 3.5 is inspected.", "state": "<class 'float'>"}
                ],
                "edgeCases": "Dividing by zero raises ZeroDivisionError.",
                "complexity": "Time: O(1) | Space: O(1)",
                "commonMistakes": "Assuming integer division occurs like in C or Python 2.",
                "alternative": "Use `7 // 2` if an integer quotient is strictly required.",
                "followUp": "What is the return type of `4 // 2` versus `4 / 2`?"
            },
            "alternatives": ["slot01-alt1", "slot01-alt2"]
        },
        {
            "id": "slot01-alt1", "slot_number": 1, "is_main": 0,
            "title": "Primitive Float Literal Deduction", "concept": "Variables & Data Types",
            "subtopic": "Float Literal Types", "difficulty": "easy",
            "question_type": "logic",
            "prompt": "What data type is assigned to `val` when initialized with a decimal point: `val = 3.14`?",
            "code_snippet": "val = 3.14\nprint(type(val))",
            "options": ["int", "float", "str", "decimal"], "correct_answer": "float",
            "test_cases": [], "eval_method": "mcq", "prerequisites": [],
            "common_misconception": "Thinking decimal literals default to specialized Decimal objects without import.",
            "explanation": "Literals containing a decimal point automatically construct an instance of the built-in `float` type.",
            "hints": {
                "hint1": "Look at the presence of the decimal point.",
                "hint2": "Python's standard floating-point type is named `float`.",
                "hint3": "No special imports are present, so standard built-in types apply.",
                "example": "`x = 0.0` is also of type `float`."
            },
            "autopsy": {
                "whatTested": "Primitive literal syntax in Python.",
                "whyWorks": "The Python lexer categorizes numerals with a dot as floating-point numbers.",
                "stepByStep": [
                    {"step": 1, "description": "Token 3.14 recognized as float literal.", "state": "Type deduced as float"},
                    {"step": 2, "description": "val bound to float object in heap.", "state": "val -> 3.14"}
                ],
                "edgeCases": "Scientific notation like `1e3` also creates a float.",
                "complexity": "Time: O(1) | Space: O(1)",
                "commonMistakes": "Confusing string '3.14' with numeric 3.14.",
                "alternative": "Use `int(3.14)` to truncate to integer 3.",
                "followUp": "How would you parse '3.14' from user input into a float?"
            },
            "alternatives": ["slot01-main", "slot01-alt2"]
        },
        {
            "id": "slot01-alt2", "slot_number": 1, "is_main": 0,
            "title": "Fix String Concatenation TypeError", "concept": "Variables & Data Types",
            "subtopic": "Type Conversion & Casting", "difficulty": "easy",
            "question_type": "debugging",
            "prompt": "The following function fails with `TypeError: can only concatenate str (not \"int\") to str`. Fix the function to convert `raw_val` to an integer before adding `bonus`.",
            "code_snippet": "def calculate_total_score(raw_val, bonus):\n    # Bug: raw_val is a string '42'\n    return int(raw_val) + bonus",
            "options": [], "correct_answer": "int(raw_val) + bonus",
            "test_cases": [
                {"input": ["42", 8], "expected": 50, "description": "String '42' + 8 returns integer 50"},
                {"input": ["100", 25], "expected": 125, "description": "String '100' + 25 returns integer 125"}
            ],
            "eval_method": "code_execution", "prerequisites": [],
            "common_misconception": "Assuming Python automatically coerces numeric strings to numbers during arithmetic.",
            "explanation": "Python is strongly typed and will not implicitly convert string '42' to number 42. Explicit `int(raw_val)` conversion is required.",
            "hints": {
                "hint1": "Python does not implicitly convert strings to numbers in `+` expressions.",
                "hint2": "Use the built-in `int(...)` function to cast `raw_val`.",
                "hint3": "Write `int(raw_val) + bonus` in the return statement.",
                "example": "`int('10') + 5` evaluates to 15."
            },
            "autopsy": {
                "whatTested": "Explicit type casting between string and integer representations.",
                "whyWorks": "`int()` parses numeric characters into an integer representation.",
                "stepByStep": [
                    {"step": 1, "description": "String '42' passed into function.", "state": "raw_val is str"},
                    {"step": 2, "description": "int('42') converts characters to numeric 42.", "state": "42 int"},
                    {"step": 3, "description": "42 + 8 produces 50.", "state": "return 50"}
                ],
                "edgeCases": "Non-numeric characters in string trigger ValueError.",
                "complexity": "Time: O(D) | Space: O(1)",
                "commonMistakes": "Attempting `str(bonus)` which concatenates '428' instead of summing.",
                "alternative": "Use `float(raw_val)` if decimals might be supplied.",
                "followUp": "What happens if raw_val is '42.5' when passed to int()?"
            },
            "alternatives": ["slot01-main", "slot01-alt1"]
        },

        # SLOT 2
        {
            "id": "slot02-main", "slot_number": 2, "is_main": 1,
            "title": "Boolean Operator Precedence", "concept": "Conditions & Operators",
            "subtopic": "Boolean Logic & Short-Circuit Evaluation", "difficulty": "easy",
            "question_type": "logic",
            "prompt": "What does the expression evaluate to: `not False and True or False`?",
            "code_snippet": "ans = not False and True or False\nprint(ans)",
            "options": ["True", "False", "None", "SyntaxError"], "correct_answer": "True",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Variables & Data Types"],
            "common_misconception": "Evaluating left-to-right without respecting operator precedence (`not` > `and` > `or`).",
            "explanation": "Operator precedence: `not` evaluates first (`not False -> True`), then `and` (`True and True -> True`), finally `or` (`True or False -> True`).",
            "hints": {
                "hint1": "Remember operator precedence: `not` has the highest priority, then `and`, then `or`.",
                "hint2": "`not False` becomes `True`.",
                "hint3": "`True and True` produces `True`.",
                "example": "`not A and B` is evaluated as `(not A) and B`."
            },
            "autopsy": {
                "whatTested": "Logical operator evaluation order and short-circuit boolean semantics.",
                "whyWorks": "`not` binds tightest, followed by conjunction `and`, followed by disjunction `or`.",
                "stepByStep": [
                    {"step": 1, "description": "Evaluate `not False`.", "state": "True"},
                    {"step": 2, "description": "Evaluate `True and True`.", "state": "True"},
                    {"step": 3, "description": "Evaluate `True or False`.", "state": "True"}
                ],
                "edgeCases": "Short-circuiting skips the right side of `or` if the left side is True.",
                "complexity": "Time: O(1) | Space: O(1)",
                "commonMistakes": "Assuming `and` and `or` share equal left-to-right associativity.",
                "alternative": "Always use parentheses `(not False) and True` for clarity.",
                "followUp": "How would adding parentheses change `not (False and True)`?"
            },
            "alternatives": ["slot02-alt1", "slot02-alt2"]
        },
        {
            "id": "slot02-alt1", "slot_number": 2, "is_main": 0,
            "title": "Comparison Condition Evaluation", "concept": "Conditions & Operators",
            "subtopic": "Relational Comparisons", "difficulty": "easy",
            "question_type": "logic",
            "prompt": "What is printed by this if/else block when `x = 15`?",
            "code_snippet": "x = 15\nif x > 20:\n    print('A')\nelif x >= 15:\n    print('B')\nelse:\n    print('C')",
            "options": ["'A'", "'B'", "'C'", "None"], "correct_answer": "'B'",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Variables & Data Types"],
            "common_misconception": "Confusing strictly greater than `>` with greater than or equal `>=`.",
            "explanation": "Since x = 15 is not > 20, the first condition fails. The second condition `15 >= 15` is True, so `'B'` is printed.",
            "hints": {
                "hint1": "Test each branch in top-down order.",
                "hint2": "Is 15 strictly greater than 20? No.",
                "hint3": "Is 15 greater than or equal to 15? Yes.",
                "example": "A condition with `>=` includes the boundary value."
            },
            "autopsy": {
                "whatTested": "Branching flow and inclusive relational operators.",
                "whyWorks": "`elif` branches are evaluated in order; the first branch with a True predicate executes.",
                "stepByStep": [
                    {"step": 1, "description": "Check `x > 20` (15 > 20).", "state": "False"},
                    {"step": 2, "description": "Check `x >= 15` (15 >= 15).", "state": "True"},
                    {"step": 3, "description": "Execute branch block: print 'B'.", "state": "'B'"}
                ],
                "edgeCases": "Once an `elif` branch succeeds, subsequent branches are not evaluated.",
                "complexity": "Time: O(1) | Space: O(1)",
                "commonMistakes": "Thinking multiple branches can execute simultaneously.",
                "alternative": "Use independent `if` statements if multiple conditions should trigger.",
                "followUp": "What would print if x was 25?"
            },
            "alternatives": ["slot02-main", "slot02-alt2"]
        },
        {
            "id": "slot02-alt2", "slot_number": 2, "is_main": 0,
            "title": "Valid Score Range Checker", "concept": "Conditions & Operators",
            "subtopic": "Chained Comparisons & Boundary Logic", "difficulty": "easy",
            "question_type": "coding",
            "prompt": "Write a Python function `is_valid_score(score)` that returns `True` if `score` is between 0 and 100 (inclusive), and `False` otherwise.",
            "code_snippet": "def is_valid_score(score):\n    # Return True if score is between 0 and 100 inclusive\n    return 0 <= score <= 100",
            "options": [], "correct_answer": "0 <= score <= 100",
            "test_cases": [
                {"input": [85], "expected": True, "description": "Standard valid score 85"},
                {"input": [0], "expected": True, "description": "Lower boundary 0 is inclusive"},
                {"input": [100], "expected": True, "description": "Upper boundary 100 is inclusive"},
                {"input": [-5], "expected": False, "description": "Negative score is invalid"},
                {"input": [105], "expected": False, "description": "Score above 100 is invalid"}
            ],
            "eval_method": "code_execution", "prerequisites": ["Variables & Data Types"],
            "common_misconception": "Writing `0 <= score and 100` instead of `0 <= score and score <= 100`.",
            "explanation": "Python supports chained comparisons: `0 <= score <= 100` tests both bounds concisely.",
            "hints": {
                "hint1": "Remember both boundary conditions: >= 0 and <= 100.",
                "hint2": "In Python, you can write `0 <= score <= 100` directly.",
                "hint3": "Return the boolean result of this comparison.",
                "example": "`0 <= x <= 10` returns True for any x in [0, 10]."
            },
            "autopsy": {
                "whatTested": "Boundary checks and inclusive range verification.",
                "whyWorks": "Chained comparisons evaluate `(0 <= score) and (score <= 100)` with short-circuiting.",
                "stepByStep": [
                    {"step": 1, "description": "Evaluate lower bound: 0 <= score.", "state": "Boolean"},
                    {"step": 2, "description": "Evaluate upper bound: score <= 100.", "state": "Boolean"},
                    {"step": 3, "description": "Return combined logical conjunction.", "state": "Result"}
                ],
                "edgeCases": "Negative numbers and values strictly exceeding 100.",
                "complexity": "Time: O(1) | Space: O(1)",
                "commonMistakes": "Using `<` instead of `<=` which excludes 0 or 100.",
                "alternative": "`return score >= 0 and score <= 100`",
                "followUp": "How would you handle non-integer input types gracefully?"
            },
            "alternatives": ["slot02-main", "slot02-alt1"]
        },

        # SLOT 3
        {
            "id": "slot03-main", "slot_number": 3, "is_main": 1,
            "title": "Loop Accumulator: Numbers 1 to 5", "concept": "Loops",
            "subtopic": "For Loop & Range Generation", "difficulty": "easy",
            "question_type": "coding",
            "prompt": "Write a Python function `get_numbers_1_to_5()` that uses a loop to return a list containing numbers from 1 to 5 inclusive: `[1, 2, 3, 4, 5]`.",
            "code_snippet": "def get_numbers_1_to_5():\n    # Use a loop to append numbers 1 through 5\n    res = []\n    for i in range(1, 6):\n        res.append(i)\n    return res",
            "options": [], "correct_answer": "[1, 2, 3, 4, 5]",
            "test_cases": [
                {"input": [], "expected": [1, 2, 3, 4, 5], "description": "Returns list [1, 2, 3, 4, 5]"}
            ],
            "eval_method": "code_execution", "prerequisites": ["Conditions & Operators"],
            "common_misconception": "Writing `range(1, 5)` which stops at 4 due to Python's exclusive stop boundary.",
            "explanation": "In Python, `range(start, stop)` is half-open `[start, stop)`. To include 5, the stop argument must be 6: `range(1, 6)`.",
            "hints": {
                "hint1": "Remember that `range(start, stop)` stops at `stop - 1`.",
                "hint2": "To include 5, your stop parameter must be 6 (`range(1, 6)`).",
                "hint3": "Create an empty list, loop with `range(1, 6)`, append each number, and return the list.",
                "example": "`for i in range(1, 4):` produces 1, 2, 3."
            },
            "autopsy": {
                "whatTested": "Basic iteration, range generation, and accumulator list appending.",
                "whyWorks": "`range(1, 6)` yields 1, 2, 3, 4, 5 sequentially.",
                "stepByStep": [
                    {"step": 1, "description": "Initialize empty list `res = []`.", "state": "res = []"},
                    {"step": 2, "description": "Iterate i through 1, 2, 3, 4, 5.", "state": "Items appended"},
                    {"step": 3, "description": "Return accumulated list `[1, 2, 3, 4, 5]`.", "state": "Return"}
                ],
                "edgeCases": "Range stop index is always excluded.",
                "complexity": "Time: O(N) | Space: O(N)",
                "commonMistakes": "Using `range(1, 5)` which produces only 4 elements.",
                "alternative": "`return list(range(1, 6))`",
                "followUp": "How would you write this using a while loop?"
            },
            "alternatives": ["slot03-alt1", "slot03-alt2"]
        },
        {
            "id": "slot03-alt1", "slot_number": 3, "is_main": 0,
            "title": "Loop Accumulator: Numbers 1 to 3", "concept": "Loops",
            "subtopic": "Basic Range Loop", "difficulty": "easy",
            "question_type": "coding",
            "prompt": "Write a Python function `get_numbers_1_to_3()` that uses a loop to return a list of numbers from 1 to 3 inclusive: `[1, 2, 3]`.",
            "code_snippet": "def get_numbers_1_to_3():\n    # Use a loop to return [1, 2, 3]\n    res = []\n    for i in range(1, 4):\n        res.append(i)\n    return res",
            "options": [], "correct_answer": "[1, 2, 3]",
            "test_cases": [
                {"input": [], "expected": [1, 2, 3], "description": "Returns list [1, 2, 3]"}
            ],
            "eval_method": "code_execution", "prerequisites": ["Conditions & Operators"],
            "common_misconception": "Using `range(1, 3)` which only yields 1 and 2.",
            "explanation": "Using `range(1, 4)` generates values 1, 2, and 3. Appending them into a list yields `[1, 2, 3]`.",
            "hints": {
                "hint1": "To generate 1, 2, and 3, what should the stop parameter be in `range(1, ?)`?",
                "hint2": "The stop value must be 4 (`range(1, 4)`).",
                "hint3": "Append each number in the loop and return the list.",
                "example": "`list(range(1, 4))` is `[1, 2, 3]`."
            },
            "autopsy": {
                "whatTested": "Reinforcing loop boundaries on a 3-element iteration.",
                "whyWorks": "Half-open interval `[1, 4)` contains integers 1, 2, 3.",
                "stepByStep": [
                    {"step": 1, "description": "Loop begins with i=1.", "state": "[1]"},
                    {"step": 2, "description": "Loop continues with i=2.", "state": "[1, 2]"},
                    {"step": 3, "description": "Loop finishes with i=3.", "state": "[1, 2, 3]"}
                ],
                "edgeCases": "Empty range if start >= stop.",
                "complexity": "Time: O(1) | Space: O(1)",
                "commonMistakes": "Forgetting the upper bound must be n + 1.",
                "alternative": "`return list(range(1, 4))`",
                "followUp": "What happens if range(3) is used instead?"
            },
            "alternatives": ["slot03-main", "slot03-alt2"]
        },
        {
            "id": "slot03-alt2", "slot_number": 3, "is_main": 0,
            "title": "Loop Progression: Even Numbers Up to N", "concept": "Loops",
            "subtopic": "Stepped Range & Even Filtering", "difficulty": "medium",
            "question_type": "coding",
            "prompt": "Write a Python function `get_even_numbers(n)` that uses a loop to return a list of all even numbers from 2 up to `n` inclusive.",
            "code_snippet": "def get_even_numbers(n):\n    # Return all evens from 2 up to n inclusive\n    res = []\n    for i in range(2, n + 1, 2):\n        res.append(i)\n    return res",
            "options": [], "correct_answer": "range(2, n + 1, 2)",
            "test_cases": [
                {"input": [6], "expected": [2, 4, 6], "description": "Evens up to 6"},
                {"input": [7], "expected": [2, 4, 6], "description": "Odd upper bound 7"},
                {"input": [2], "expected": [2], "description": "Single element boundary 2"},
                {"input": [1], "expected": [], "description": "No evens when n < 2"}
            ],
            "eval_method": "code_execution", "prerequisites": ["Conditions & Operators"],
            "common_misconception": "Forgetting the step parameter or using `range(2, n)` which misses `n` when `n` is even.",
            "explanation": "`range(2, n + 1, 2)` steps by 2, directly generating only even integers from 2 up to `n` without needing an `if` check.",
            "hints": {
                "hint1": "You can provide a step argument to range: `range(start, stop, step)`.",
                "hint2": "Start at 2, step by 2, and use `n + 1` as the stop condition.",
                "hint3": "Alternatively, loop through all numbers and check `if i % 2 == 0:`.",
                "example": "`range(2, 7, 2)` yields 2, 4, 6."
            },
            "autopsy": {
                "whatTested": "Stepped loop traversal and conditional iteration.",
                "whyWorks": "Stepping by 2 bypasses odd numbers entirely, doubling iteration efficiency.",
                "stepByStep": [
                    {"step": 1, "description": "Initialize list `res = []`.", "state": "res = []"},
                    {"step": 2, "description": "Loop with step 2 from 2 to n + 1.", "state": "Evens collected"},
                    {"step": 3, "description": "Return collected evens.", "state": "Result"}
                ],
                "edgeCases": "When n is less than 2, loop should yield an empty list.",
                "complexity": "Time: O(N/2) | Space: O(N/2)",
                "commonMistakes": "Setting stop to `n` instead of `n + 1`, skipping `n` itself when `n` is even.",
                "alternative": "`return [x for x in range(2, n + 1, 2)]`",
                "followUp": "How would you modify this to generate odd numbers starting at 1?"
            },
            "alternatives": ["slot03-main", "slot03-alt1"]
        },

        # SLOT 4
        {
            "id": "slot04-main", "slot_number": 4, "is_main": 1,
            "title": "Debug Off-by-One Range IndexError", "concept": "Loops",
            "subtopic": "Boundary Conditions & Index Traversal", "difficulty": "easy",
            "question_type": "debugging",
            "prompt": "The following function triggers an `IndexError: list index out of range` on the last iteration. Fix the range boundary so it traverses all items safely.",
            "code_snippet": "def extract_elements(items):\n    result = []\n    # Bug: range(len(items) + 1) goes one index too far\n    for i in range(len(items)):\n        result.append(items[i])\n    return result",
            "options": [], "correct_answer": "range(len(items))",
            "test_cases": [
                {"input": [["a", "b", "c"]], "expected": ["a", "b", "c"], "description": "Standard 3-item list"},
                {"input": [[]], "expected": [], "description": "Empty list"}
            ],
            "eval_method": "code_execution", "prerequisites": ["Loops"],
            "common_misconception": "Assuming index reaches `len(items)`, when valid 0-based indices end at `len(items) - 1`.",
            "explanation": "A list of length N has valid indices 0 through N-1. `range(len(items))` produces 0 through N-1 safely.",
            "hints": {
                "hint1": "In Python, 0-based indexing means the last valid index is `len(items) - 1`.",
                "hint2": "`range(len(items) + 1)` attempts to access index `len(items)` which does not exist.",
                "hint3": "Change the loop to `for i in range(len(items)):`.",
                "example": "For a 3-item list, indices are 0, 1, 2. `len(items)` is 3."
            },
            "autopsy": {
                "whatTested": "Detecting fencepost and off-by-one errors in index loops.",
                "whyWorks": "`range(len(items))` automatically bounds indices from 0 up to `len(items) - 1`.",
                "stepByStep": [
                    {"step": 1, "description": "Observe list length N.", "state": "Length = N"},
                    {"step": 2, "description": "Bound index range strictly to [0, N-1].", "state": "range(len(items))"},
                    {"step": 3, "description": "Safe access at each iteration.", "state": "No IndexError"}
                ],
                "edgeCases": "Empty lists have length 0; `range(0)` executes zero times safely.",
                "complexity": "Time: O(N) | Space: O(N)",
                "commonMistakes": "Adding +1 out of habit from 1-based thinking.",
                "alternative": "Prefer idiomatic `for item in items:` over index iteration.",
                "followUp": "When is index-based iteration strictly necessary over item iteration?"
            },
            "alternatives": ["slot04-alt1", "slot04-alt2"]
        },
        {
            "id": "slot04-alt1", "slot_number": 4, "is_main": 0,
            "title": "Iteration Count Prediction", "concept": "Loops",
            "subtopic": "Range Iteration Count", "difficulty": "easy",
            "question_type": "logic",
            "prompt": "How many times does the body of this loop execute: `for i in range(1, 6):`?",
            "code_snippet": "count = 0\nfor i in range(1, 6):\n    count += 1\nprint(count)",
            "options": ["4", "5", "6", "7"], "correct_answer": "5",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Loops"],
            "common_misconception": "Subtracting 6 - 1 = 5, but then doubting if 6 is inclusive.",
            "explanation": "`range(1, 6)` produces values 1, 2, 3, 4, 5. That is exactly 5 iterations (stop - start = 6 - 1 = 5).",
            "hints": {
                "hint1": "Write down the values generated: 1, 2, 3, 4, 5.",
                "hint2": "Stop value 6 is not included.",
                "hint3": "Count the total number of items in that sequence.",
                "example": "`range(0, 5)` and `range(1, 6)` both execute 5 times."
            },
            "autopsy": {
                "whatTested": "Calculating loop iterations from range boundaries.",
                "whyWorks": "Number of steps in `range(start, stop)` equals `stop - start` when step is 1.",
                "stepByStep": [
                    {"step": 1, "description": "Start is 1, stop is 6.", "state": "1 to 5 inclusive"},
                    {"step": 2, "description": "Calculate count: 6 - 1 = 5.", "state": "5 iterations"}
                ],
                "edgeCases": "If stop <= start, iteration count is 0.",
                "complexity": "Time: O(1) | Space: O(1)",
                "commonMistakes": "Assuming stop index 6 is included, guessing 6.",
                "alternative": "`len(range(1, 6))` evaluates to 5 in O(1) time.",
                "followUp": "What is `len(range(0, 100, 2))`?"
            },
            "alternatives": ["slot04-main", "slot04-alt2"]
        },
        {
            "id": "slot04-alt2", "slot_number": 4, "is_main": 0,
            "title": "Sum Excluding Last Element", "concept": "Loops",
            "subtopic": "Loop Boundary Truncation", "difficulty": "medium",
            "question_type": "coding",
            "prompt": "Write a Python function `sum_excluding_last(nums)` that loops through the list and returns the sum of all elements EXCEPT the last element. If the list has 1 or fewer elements, return 0.",
            "code_snippet": "def sum_excluding_last(nums):\n    if len(nums) <= 1:\n        return 0\n    total = 0\n    for i in range(len(nums) - 1):\n        total += nums[i]\n    return total",
            "options": [], "correct_answer": "range(len(nums) - 1)",
            "test_cases": [
                {"input": [[1, 2, 3, 4]], "expected": 6, "description": "1 + 2 + 3 = 6 (excludes 4)"},
                {"input": [[10, 20]], "expected": 10, "description": "Excludes 20, returns 10"},
                {"input": [[5]], "expected": 0, "description": "Single element returns 0"},
                {"input": [[]], "expected": 0, "description": "Empty list returns 0"}
            ],
            "eval_method": "code_execution", "prerequisites": ["Loops"],
            "common_misconception": "Forgetting to handle the single-element or empty list edge case.",
            "explanation": "Iterating over `range(len(nums) - 1)` stops immediately before the last index, summing only preceding elements.",
            "hints": {
                "hint1": "Handle the base case: if `len(nums) <= 1`, return 0.",
                "hint2": "Loop through indices up to `len(nums) - 1`.",
                "hint3": "Accumulate the sum and return it.",
                "example": "In `[1, 2, 3]`, indices to sum are 0 and 1."
            },
            "autopsy": {
                "whatTested": "Boundary-constrained accumulation and empty list handling.",
                "whyWorks": "Stopping at `len(nums) - 1` omits the final element.",
                "stepByStep": [
                    {"step": 1, "description": "Check if length <= 1, return 0.", "state": "Guard clause"},
                    {"step": 2, "description": "Accumulate elements from index 0 to len-2.", "state": "Total summed"},
                    {"step": 3, "description": "Return total.", "state": "Result"}
                ],
                "edgeCases": "Lists of length 0 or 1.",
                "complexity": "Time: O(N) | Space: O(1)",
                "commonMistakes": "Summing all elements and subtracting `nums[-1]` without checking if list is empty.",
                "alternative": "`return sum(nums[:-1])`",
                "followUp": "How would `sum(nums[:-1])` behave on an empty list?"
            },
            "alternatives": ["slot04-main", "slot04-alt1"]
        },

        # SLOT 5
        {
            "id": "slot05-main", "slot_number": 5, "is_main": 1,
            "title": "Debug Missing Return Statement", "concept": "Functions",
            "subtopic": "Function Return Values & None Semantics", "difficulty": "easy",
            "question_type": "debugging",
            "prompt": "The following function computes a sum but currently returns `None` to the caller. Fix the function so it returns the computed `total`.",
            "code_snippet": "def calculate_sum(nums):\n    total = 0\n    for n in nums:\n        total += n\n    # Bug: missing return statement\n    return total",
            "options": [], "correct_answer": "return total",
            "test_cases": [
                {"input": [[10, 20, 30]], "expected": 60, "description": "Sum of 10, 20, 30 is 60"},
                {"input": [[]], "expected": 0, "description": "Empty list sum is 0"}
            ],
            "eval_method": "code_execution", "prerequisites": ["Loops"],
            "common_misconception": "Assuming `print(total)` returns the value to the caller.",
            "explanation": "In Python, functions without an explicit `return` statement return `None` by default. `return total` is required to pass the value back.",
            "hints": {
                "hint1": "What keyword sends a computed value back to where the function was called?",
                "hint2": "Make sure you use `return total`, not `print(total)`.",
                "hint3": "Place `return total` after the for-loop completes.",
                "example": "`def add(a, b): return a + b`"
            },
            "autopsy": {
                "whatTested": "Explicit function return semantics versus default None returns.",
                "whyWorks": "`return` transfers control flow and the calculated object reference back to caller.",
                "stepByStep": [
                    {"step": 1, "description": "Initialize accumulator total = 0.", "state": "total = 0"},
                    {"step": 2, "description": "Loop accumulates all values.", "state": "total = 60"},
                    {"step": 3, "description": "Execute return total.", "state": "Caller receives 60"}
                ],
                "edgeCases": "Indenting return inside the loop terminates the loop prematurely on iteration 1.",
                "complexity": "Time: O(N) | Space: O(1)",
                "commonMistakes": "Indenting `return` inside the loop body.",
                "alternative": "`return sum(nums)`",
                "followUp": "What happens if a return statement is placed inside the for loop?"
            },
            "alternatives": ["slot05-alt1", "slot05-alt2"]
        },
        {
            "id": "slot05-alt1", "slot_number": 5, "is_main": 0,
            "title": "Nested Function Call Tracing", "concept": "Functions",
            "subtopic": "Composed Function Invocations", "difficulty": "easy",
            "question_type": "logic",
            "prompt": "What is the final output of `result` when evaluating nested calls: `add(multiply(2, 3), 4)`?",
            "code_snippet": "def multiply(a, b):\n    return a * b\n\ndef add(a, b):\n    return a + b\n\nresult = add(multiply(2, 3), 4)\nprint(result)",
            "options": ["10", "14", "24", "9"], "correct_answer": "10",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Functions"],
            "common_misconception": "Evaluating outer function before inner function arguments.",
            "explanation": "Inner expression `multiply(2, 3)` evaluates first to `6`. Then `add(6, 4)` evaluates to `10`.",
            "hints": {
                "hint1": "Evaluate the innermost parentheses first: `multiply(2, 3)`.",
                "hint2": "2 * 3 = 6.",
                "hint3": "Now evaluate the outer function: `add(6, 4)`.",
                "example": "`f(g(x))` always computes `g(x)` first."
            },
            "autopsy": {
                "whatTested": "Order of evaluation in composed functional expressions.",
                "whyWorks": "Python resolves argument expressions eagerly before invoking the outer function.",
                "stepByStep": [
                    {"step": 1, "description": "Evaluate multiply(2, 3).", "state": "Returns 6"},
                    {"step": 2, "description": "Pass 6 and 4 into add(6, 4).", "state": "Returns 10"},
                    {"step": 3, "description": "Bind result = 10.", "state": "10"}
                ],
                "edgeCases": "If an inner call throws an exception, outer function is never invoked.",
                "complexity": "Time: O(1) | Space: O(1)",
                "commonMistakes": "Adding 3 + 4 before multiplying.",
                "alternative": "Break into temporary variables.",
                "followUp": "How would you trace add(add(1, 2), add(3, 4))?"
            },
            "alternatives": ["slot05-main", "slot05-alt2"]
        },
        {
            "id": "slot05-alt2", "slot_number": 5, "is_main": 0,
            "title": "Default Parameter Area Function", "concept": "Functions",
            "subtopic": "Default Arguments", "difficulty": "easy",
            "question_type": "coding",
            "prompt": "Write a Python function `calculate_area(length, width=1)` that returns `length * width`. If `width` is not supplied, it should default to 1 (calculating the length of a unit strip).",
            "code_snippet": "def calculate_area(length, width=1):\n    return length * width",
            "options": [], "correct_answer": "length * width",
            "test_cases": [
                {"input": [5, 4], "expected": 20, "description": "5 * 4 = 20"},
                {"input": [7], "expected": 7, "description": "Default width=1: 7 * 1 = 7"},
                {"input": [12, 2], "expected": 24, "description": "12 * 2 = 24"}
            ],
            "eval_method": "code_execution", "prerequisites": ["Functions"],
            "common_misconception": "Placing non-default arguments after default arguments (`def f(a=1, b):`).",
            "explanation": "Default parameters are specified in the function signature: `def calculate_area(length, width=1): return length * width`.",
            "hints": {
                "hint1": "Specify `width=1` in the function parameter list.",
                "hint2": "Multiply `length * width`.",
                "hint3": "Return the calculated product.",
                "example": "`def greet(name, times=1): return name * times`"
            },
            "autopsy": {
                "whatTested": "Default argument assignment and signature definition.",
                "whyWorks": "If the second argument is omitted by caller, the runtime substitutes default value 1.",
                "stepByStep": [
                    {"step": 1, "description": "Check if width provided.", "state": "Use provided or fallback to 1"},
                    {"step": 2, "description": "Multiply length by width.", "state": "Product"},
                    {"step": 3, "description": "Return product.", "state": "Result"}
                ],
                "edgeCases": "Passing width=0 returns 0.",
                "complexity": "Time: O(1) | Space: O(1)",
                "commonMistakes": "Syntactically placing default args before mandatory parameters.",
                "alternative": "`return length * (width if width is not None else 1)`",
                "followUp": "Why should mutable objects like lists never be used as default argument values?"
            },
            "alternatives": ["slot05-main", "slot05-alt1"]
        },

        # SLOT 6
        {
            "id": "slot06-main", "slot_number": 6, "is_main": 1,
            "title": "Negative Index List Retrieval", "concept": "Arrays & Lists",
            "subtopic": "Negative Indexing Semantics", "difficulty": "easy",
            "question_type": "logic",
            "prompt": "What is the return value of `colors[-2]` in this Python list?",
            "code_snippet": "colors = ['red', 'green', 'blue', 'yellow', 'purple']\nprint(colors[-2])",
            "options": ["'yellow'", "'blue'", "'purple'", "'green'"], "correct_answer": "'yellow'",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Variables & Data Types"],
            "common_misconception": "Thinking -1 is the first element, or counting from the left side.",
            "explanation": "In Python, index -1 is the last element ('purple'), and index -2 is the second to last element ('yellow').",
            "hints": {
                "hint1": "Negative indices count backwards from the end of the list.",
                "hint2": "Index -1 is 'purple'.",
                "hint3": "Index -2 is one position before 'purple'.",
                "example": "`lst[-1]` accesses the final element in any non-empty list."
            },
            "autopsy": {
                "whatTested": "End-relative indexing and pointer arithmetic in Python collections.",
                "whyWorks": "Python transforms negative index `-k` to `len(list) - k` (5 - 2 = 3 -> 'yellow').",
                "stepByStep": [
                    {"step": 1, "description": "Length of list is 5.", "state": "len = 5"},
                    {"step": 2, "description": "Index -2 converts to 5 - 2 = 3.", "state": "target index = 3"},
                    {"step": 3, "description": "Element at index 3 is 'yellow'.", "state": "return 'yellow'"}
                ],
                "edgeCases": "Index out of bounds if `-k < -len(list)`.",
                "complexity": "Time: O(1) | Space: O(1)",
                "commonMistakes": "Assuming `-1` is the first element because index 1 is the second element.",
                "alternative": "`colors[len(colors) - 2]`",
                "followUp": "What index represents 'red' using negative indexing?"
            },
            "alternatives": ["slot06-alt1", "slot06-alt2"]
        },
        {
            "id": "slot06-alt1", "slot_number": 6, "is_main": 0,
            "title": "First and Last Element Retrieval", "concept": "Arrays & Lists",
            "subtopic": "Boundary Element Indexing", "difficulty": "easy",
            "question_type": "logic",
            "prompt": "Given `items = [10, 20, 30]`, which expressions access the first and last elements respectively?",
            "code_snippet": "items = [10, 20, 30]",
            "options": ["items[0] and items[-1]", "items[1] and items[3]", "items[0] and items[len(items)]", "items[-1] and items[0]"],
            "correct_answer": "items[0] and items[-1]",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Variables & Data Types"],
            "common_misconception": "Using `items[1]` for first element or `items[len(items)]` which causes IndexError.",
            "explanation": "Python lists are 0-indexed: `items[0]` accesses the first element and `items[-1]` accesses the last element.",
            "hints": {
                "hint1": "0-based indexing starts at 0 for the first item.",
                "hint2": "Negative 1 (-1) cleanly references the last item.",
                "hint3": "`items[len(items)]` raises an IndexError.",
                "example": "`items[0]` is 10, `items[-1]` is 30."
            },
            "autopsy": {
                "whatTested": "Standard boundary indices in 0-based collections.",
                "whyWorks": "Index 0 targets offset 0 from memory start; -1 targets end.",
                "stepByStep": [
                    {"step": 1, "description": "Identify first item index: 0.", "state": "items[0] = 10"},
                    {"step": 2, "description": "Identify last item index: -1.", "state": "items[-1] = 30"}
                ],
                "edgeCases": "Empty lists raise IndexError on either access.",
                "complexity": "Time: O(1) | Space: O(1)",
                "commonMistakes": "Attempting `items[len(items)]` which exceeds valid index range.",
                "alternative": "`items[0]` and `items[len(items) - 1]`",
                "followUp": "How would you safely get the first item without raising IndexError if empty?"
            },
            "alternatives": ["slot06-main", "slot06-alt2"]
        },
        {
            "id": "slot06-alt2", "slot_number": 6, "is_main": 0,
            "title": "Safe Second Element Getter", "concept": "Arrays & Lists",
            "subtopic": "Length Guarded Retrieval", "difficulty": "easy",
            "question_type": "coding",
            "prompt": "Write a Python function `get_second_element(lst)` that returns the second element (`lst[1]`) if the list contains at least 2 items, or `None` if the list has fewer than 2 items.",
            "code_snippet": "def get_second_element(lst):\n    # Return second element or None if not available\n    if len(lst) >= 2:\n        return lst[1]\n    return None",
            "options": [], "correct_answer": "lst[1]",
            "test_cases": [
                {"input": [[10, 20, 30]], "expected": 20, "description": "Second element is 20"},
                {"input": [[5]], "expected": None, "description": "Single element returns None"},
                {"input": [[]], "expected": None, "description": "Empty list returns None"}
            ],
            "eval_method": "code_execution", "prerequisites": ["Arrays & Lists"],
            "common_misconception": "Directly accessing `lst[1]` without checking length, causing IndexError.",
            "explanation": "Guarding with `if len(lst) >= 2:` prevents IndexError on small or empty collections.",
            "hints": {
                "hint1": "First check if `len(lst) >= 2`.",
                "hint2": "If true, return `lst[1]` (remember 0 is first, 1 is second).",
                "hint3": "Otherwise, return `None`.",
                "example": "In `['apple', 'banana']`, index 1 is `'banana'`."
            },
            "autopsy": {
                "whatTested": "Defensive length checks before index dereferencing.",
                "whyWorks": "Checking collection length avoids hardware/runtime fault triggers.",
                "stepByStep": [
                    {"step": 1, "description": "Verify length >= 2.", "state": "Guard check"},
                    {"step": 2, "description": "If true return index 1.", "state": "lst[1]"},
                    {"step": 3, "description": "Else return None.", "state": "Safe None"}
                ],
                "edgeCases": "Lists of length 0 or 1.",
                "complexity": "Time: O(1) | Space: O(1)",
                "commonMistakes": "Confusing second item with index 2 (`lst[2]`).",
                "alternative": "`return lst[1] if len(lst) > 1 else None`",
                "followUp": "How would you do this using try/except IndexError?"
            },
            "alternatives": ["slot06-main", "slot06-alt1"]
        },

        # SLOT 7
        {
            "id": "slot07-main", "slot_number": 7, "is_main": 1,
            "title": "Sub-string Slicing Window", "concept": "Strings",
            "subtopic": "Slice Notation [start:stop]", "difficulty": "medium",
            "question_type": "logic",
            "prompt": "What substring is produced by the slice `text[2:6]`?",
            "code_snippet": "text = 'SkillTrace'\nprint(text[2:6])",
            "options": ["'illT'", "'kill'", "'ill'", "'killT'"], "correct_answer": "'illT'",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Arrays & Lists"],
            "common_misconception": "Including character at stop index 6 ('r') or confusing index 2 with the second letter.",
            "explanation": "0:S, 1:k, 2:i, 3:l, 4:l, 5:T, 6:r. The slice `[2:6]` takes characters at indices 2, 3, 4, 5 -> 'illT' (stop index 6 is excluded).",
            "hints": {
                "hint1": "Write out the 0-based index of each letter in 'SkillTrace'.",
                "hint2": "What character is at index 2? S=0, k=1, i=2.",
                "hint3": "The slice includes indices 2 through 5, excluding index 6.",
                "example": "'ABCDE'[1:3] yields 'BC'."
            },
            "autopsy": {
                "whatTested": "Zero-indexed slicing and half-open interval boundaries on strings.",
                "whyWorks": "String slicing copies characters from `start` up to but not including `stop`.",
                "stepByStep": [
                    {"step": 1, "description": "Map indices: S(0), k(1), i(2), l(3), l(4), T(5), r(6), a(7), c(8), e(9)", "state": "Mapped"},
                    {"step": 2, "description": "Select index range [2, 6): indices 2, 3, 4, 5.", "state": "i, l, l, T"},
                    {"step": 3, "description": "Concatenate slice: 'illT'.", "state": "'illT'"}
                ],
                "edgeCases": "Slicing beyond string length does not throw IndexError; it clamps to string end.",
                "complexity": "Time: O(K) where K is slice length | Space: O(K)",
                "commonMistakes": "Including character at stop index 6 ('r').",
                "alternative": "`''.join([text[i] for i in range(2, 6)])`",
                "followUp": "What does `text[::2]` produce?"
            },
            "alternatives": ["slot07-alt1", "slot07-alt2"]
        },
        {
            "id": "slot07-alt1", "slot_number": 7, "is_main": 0,
            "title": "String Prefix Slicing", "concept": "Strings",
            "subtopic": "Omitted Start Prefix", "difficulty": "easy",
            "question_type": "logic",
            "prompt": "What does `s[:3]` produce when `s = 'Python'`?",
            "code_snippet": "s = 'Python'\nprint(s[:3])",
            "options": ["'Pyt'", "'Pyth'", "'yth'", "'on'"], "correct_answer": "'Pyt'",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Strings"],
            "common_misconception": "Assuming omitting the start parameter starts at index 1 instead of 0.",
            "explanation": "When the start index is omitted, slicing defaults to index 0: taking indices 0, 1, 2 ('P', 'y', 't').",
            "hints": {
                "hint1": "Omitting the start index `[:stop]` defaults to index 0.",
                "hint2": "It takes the first 3 characters: index 0, 1, 2.",
                "hint3": "Indices in 'Python': 0=P, 1=y, 2=t.",
                "example": "'Hello'[:2] gives 'He'."
            },
            "autopsy": {
                "whatTested": "Default start index semantics in slice notation.",
                "whyWorks": "Python assigns `start = 0` whenever `start` is None.",
                "stepByStep": [
                    {"step": 1, "description": "Omitted start defaults to 0.", "state": "start = 0"},
                    {"step": 2, "description": "Stop is 3, indices [0, 1, 2].", "state": "P, y, t"},
                    {"step": 3, "description": "Returns 'Pyt'.", "state": "'Pyt'"}
                ],
                "edgeCases": "If stop > len(s), returns entire string.",
                "complexity": "Time: O(K) | Space: O(K)",
                "commonMistakes": "Taking 4 characters assuming 3 is inclusive.",
                "alternative": "`s[0:3]`",
                "followUp": "What does `s[3:]` produce?"
            },
            "alternatives": ["slot07-main", "slot07-alt2"]
        },
        {
            "id": "slot07-alt2", "slot_number": 7, "is_main": 0,
            "title": "Palindrome Checker Function", "concept": "Strings",
            "subtopic": "String Reversal & Case Normalization", "difficulty": "medium",
            "question_type": "coding",
            "prompt": "Write a Python function `is_palindrome(text)` that returns `True` if `text` reads the same forwards and backwards, ignoring casing. Return `False` otherwise.",
            "code_snippet": "def is_palindrome(text):\n    clean = text.lower().replace(' ', '')\n    return clean == clean[::-1]",
            "options": [], "correct_answer": "clean == clean[::-1]",
            "test_cases": [
                {"input": ["Racecar"], "expected": True, "description": "'Racecar' is palindrome ignoring case"},
                {"input": ["hello"], "expected": False, "description": "'hello' is not palindrome"},
                {"input": ["A"], "expected": True, "description": "Single character is palindrome"},
                {"input": ["Madam"], "expected": True, "description": "'Madam' is palindrome"}
            ],
            "eval_method": "code_execution", "prerequisites": ["Strings"],
            "common_misconception": "Comparing without lowercasing, causing 'Racecar' != 'racecaR' to fail.",
            "explanation": "Lowercasing normalizes the characters, and slice step -1 `[::-1]` cleanly reverses the string for comparison.",
            "hints": {
                "hint1": "Convert the string to lowercase first using `.lower()`.",
                "hint2": "Use slice `[::-1]` to reverse a string.",
                "hint3": "Compare the lowercased string to its reverse.",
                "example": "'radar'[::-1] == 'radar' is True."
            },
            "autopsy": {
                "whatTested": "String normalization, reverse slicing, and equality comparisons.",
                "whyWorks": "Slice step `-1` traverses backwards from end to start in O(N) time.",
                "stepByStep": [
                    {"step": 1, "description": "Convert string to lowercase.", "state": "normalized"},
                    {"step": 2, "description": "Reverse string with clean[::-1].", "state": "reversed"},
                    {"step": 3, "description": "Compare clean == reversed.", "state": "boolean"}
                ],
                "edgeCases": "Empty string or single character strings are trivially palindromes.",
                "complexity": "Time: O(N) | Space: O(N)",
                "commonMistakes": "Forgetting `.lower()`, failing case-insensitive tests.",
                "alternative": "Two-pointer comparison from both ends without allocating new reverse string.",
                "followUp": "How would you solve this in O(1) auxiliary space using two pointers?"
            },
            "alternatives": ["slot07-main", "slot07-alt1"]
        },

        # SLOT 8
        {
            "id": "slot08-main", "slot_number": 8, "is_main": 1,
            "title": "Parity Filtering Accumulator", "concept": "Basic Algorithms",
            "subtopic": "Conditional Accumulator Tracing", "difficulty": "medium",
            "question_type": "logic",
            "prompt": "What is the final value of `total` after the loop processes all elements in the list?",
            "code_snippet": "total = 0\nfor x in [3, 6, 9, 12, 15]:\n    if x % 2 == 0:\n        total += x\n    else:\n        total -= 1\nprint(total)",
            "options": ["15", "18", "12", "21"], "correct_answer": "15",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Loops", "Conditions & Operators"],
            "common_misconception": "Subtracting `x` instead of 1 on odd numbers.",
            "explanation": "Even numbers (6, 12) add +18. Odd numbers (3, 9, 15) subtract 1 three times (-3). Total = 18 - 3 = 15.",
            "hints": {
                "hint1": "Identify which numbers are even: 6, 12.",
                "hint2": "Sum of evens: 6 + 12 = 18.",
                "hint3": "Notice the else block: `total -= 1`, NOT `total -= x`. There are 3 odd numbers (3, 9, 15).",
                "example": "18 - (1 * 3) = 15."
            },
            "autopsy": {
                "whatTested": "Modulo arithmetic for parity determination and state accumulation.",
                "whyWorks": "`x % 2 == 0` evaluates True for evens and False for odds.",
                "stepByStep": [
                    {"step": 1, "description": "x=3 (odd): total -= 1", "state": "total = -1"},
                    {"step": 2, "description": "x=6 (even): total += 6", "state": "total = 5"},
                    {"step": 3, "description": "x=9 (odd): total -= 1", "state": "total = 4"},
                    {"step": 4, "description": "x=12 (even): total += 12", "state": "total = 16"},
                    {"step": 5, "description": "x=15 (odd): total -= 1", "state": "total = 15"}
                ],
                "edgeCases": "Zero is even (0 % 2 == 0).",
                "complexity": "Time: O(N) | Space: O(1)",
                "commonMistakes": "Subtracting 3, 9, and 15 instead of subtracting 1 each time.",
                "alternative": "`sum(x for x in nums if x % 2 == 0) - sum(1 for x in nums if x % 2 != 0)`",
                "followUp": "What would total be if all numbers in list were even?"
            },
            "alternatives": ["slot08-alt1", "slot08-alt2"]
        },
        {
            "id": "slot08-alt1", "slot_number": 8, "is_main": 0,
            "title": "Filter Positive Numbers Function", "concept": "Basic Algorithms",
            "subtopic": "Linear Filtering", "difficulty": "easy",
            "question_type": "coding",
            "prompt": "Write a Python function `filter_positives(nums)` that returns a new list containing only the numbers from `nums` that are strictly greater than 0.",
            "code_snippet": "def filter_positives(nums):\n    res = []\n    for n in nums:\n        if n > 0:\n            res.append(n)\n    return res",
            "options": [], "correct_answer": "n > 0",
            "test_cases": [
                {"input": [[-2, 5, 0, -1, 8]], "expected": [5, 8], "description": "Filters out negative numbers and zero"},
                {"input": [[-1, -2]], "expected": [], "description": "All negatives returns empty list"},
                {"input": [[1, 2, 3]], "expected": [1, 2, 3], "description": "All positives retained"}
            ],
            "eval_method": "code_execution", "prerequisites": ["Arrays & Lists"],
            "common_misconception": "Using `>= 0` which includes zero, violating strictly positive definition.",
            "explanation": "Strictly positive means `n > 0`. Zero is neither positive nor negative.",
            "hints": {
                "hint1": "Remember that positive numbers are strictly greater than 0 (`n > 0`).",
                "hint2": "Loop through `nums` and append matching numbers.",
                "hint3": "Return the filtered list.",
                "example": "`[x for x in nums if x > 0]`"
            },
            "autopsy": {
                "whatTested": "Linear list filtering and strict comparison predicates.",
                "whyWorks": "`if n > 0:` filters elements matching the predicate.",
                "stepByStep": [
                    {"step": 1, "description": "Iterate over input items.", "state": "Inspection"},
                    {"step": 2, "description": "Append if strictly > 0.", "state": "Positive items kept"},
                    {"step": 3, "description": "Return collected items.", "state": "Result"}
                ],
                "edgeCases": "Zero must be excluded because 0 is not positive.",
                "complexity": "Time: O(N) | Space: O(N)",
                "commonMistakes": "Using `>= 0` which includes 0.",
                "alternative": "`return [x for x in nums if x > 0]`",
                "followUp": "How would you do this in-place without creating a new list?"
            },
            "alternatives": ["slot08-main", "slot08-alt2"]
        },
        {
            "id": "slot08-alt2", "slot_number": 8, "is_main": 0,
            "title": "Debug Product Accumulator Initial Value", "concept": "Basic Algorithms",
            "subtopic": "Accumulator Identity Values", "difficulty": "medium",
            "question_type": "debugging",
            "prompt": "The following function is supposed to calculate the product of all numbers in a list, but it always returns 0! Fix the initial accumulator value so multiplication calculates correctly.",
            "code_snippet": "def calculate_product(nums):\n    # Bug: initialized to 0 instead of multiplicative identity 1\n    product = 1\n    for n in nums:\n        product *= n\n    return product",
            "options": [], "correct_answer": "product = 1",
            "test_cases": [
                {"input": [[2, 3, 4]], "expected": 24, "description": "2 * 3 * 4 = 24"},
                {"input": [[5]], "expected": 5, "description": "Single element 5 returns 5"},
                {"input": [[-2, 3]], "expected": -6, "description": "-2 * 3 = -6"}
            ],
            "eval_method": "code_execution", "prerequisites": ["Basic Algorithms"],
            "common_misconception": "Initializing multiplication accumulators to 0 like addition accumulators.",
            "explanation": "The identity element for addition is 0, but for multiplication it is 1. Initializing to 0 causes `0 * n = 0` on every subsequent step.",
            "hints": {
                "hint1": "What happens when you multiply any number by 0?",
                "hint2": "What is the identity element for multiplication (the number where x * 1 = x)?",
                "hint3": "Change `product = 0` to `product = 1`.",
                "example": "For summing use 0, for product use 1."
            },
            "autopsy": {
                "whatTested": "Mathematical identity elements in accumulator patterns.",
                "whyWorks": "1 is the multiplicative identity: `1 * x = x`.",
                "stepByStep": [
                    {"step": 1, "description": "Initialize product = 1.", "state": "product = 1"},
                    {"step": 2, "description": "Multiply sequentially by each item.", "state": "product accumulates"},
                    {"step": 3, "description": "Return non-zero product.", "state": "Correct result"}
                ],
                "edgeCases": "If list contains a 0, product correctly absorbs to 0.",
                "complexity": "Time: O(N) | Space: O(1)",
                "commonMistakes": "Copy-pasting sum patterns with `total = 0` into multiplication functions.",
                "alternative": "`import math; return math.prod(nums)`",
                "followUp": "What should calculate_product return for an empty list?"
            },
            "alternatives": ["slot08-main", "slot08-alt1"]
        },

        # SLOT 9
        {
            "id": "slot09-main", "slot_number": 9, "is_main": 1,
            "title": "Variable Shadowing and Scope Isolation", "concept": "Functions",
            "subtopic": "LEGB Scope & Local Shadowing", "difficulty": "medium",
            "question_type": "logic",
            "prompt": "What is printed to stdout when the following script runs?",
            "code_snippet": "x = 10\n\ndef modify():\n    x = 20\n    return x\n\nmodify()\nprint(x)",
            "options": ["10", "20", "UnboundLocalError", "None"], "correct_answer": "10",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Functions"],
            "common_misconception": "Believing assignment inside a function mutates the outer global variable by default.",
            "explanation": "`x = 20` inside `modify()` creates a local variable that shadows the global `x`. The global `x` remains `10`.",
            "hints": {
                "hint1": "Does assigning to a variable inside a function change the global variable without the `global` keyword?",
                "hint2": "`x = 20` creates a new local scope variable.",
                "hint3": "When `print(x)` is executed outside the function, it accesses the global `x`.",
                "example": "Without `global x`, outer variables are not modified by local assignments."
            },
            "autopsy": {
                "whatTested": "LEGB scope resolution (Local, Enclosing, Global, Built-in) and variable shadowing.",
                "whyWorks": "Python assigns scope at compile time: binding a variable name inside a function marks it as local.",
                "stepByStep": [
                    {"step": 1, "description": "Global x bound to 10 in module scope.", "state": "Global x = 10"},
                    {"step": 2, "description": "Function modify() creates local frame with local x = 20.", "state": "Local x = 20"},
                    {"step": 3, "description": "Function returns, local frame destroyed.", "state": "Global scope active"},
                    {"step": 4, "description": "print(x) accesses global x.", "state": "Prints 10"}
                ],
                "edgeCases": "If a function reads `x` before assigning to `x` in the same scope, `UnboundLocalError` is raised.",
                "complexity": "Time: O(1) | Space: O(1)",
                "commonMistakes": "Assuming local assignments automatically overwrite global values.",
                "alternative": "Use `global x` if global mutation is strictly required (generally discouraged).",
                "followUp": "What happens if we do `print(x)` inside modify() before `x = 20`?"
            },
            "alternatives": ["slot09-alt1", "slot09-alt2"]
        },
        {
            "id": "slot09-alt1", "slot_number": 9, "is_main": 0,
            "title": "Block Scope in Python", "concept": "Functions",
            "subtopic": "If-Block Scope Rules", "difficulty": "easy",
            "question_type": "logic",
            "prompt": "Does Python create a new scope for `if` statements or `for` loops?",
            "code_snippet": "if True:\n    msg = 'hello'\nprint(msg)",
            "options": [
                "No, Python blocks do not create new scope; msg is accessible outside",
                "Yes, msg is private to the if block and causes NameError",
                "Only in Python 2, not in Python 3",
                "Only if msg is declared with let"
            ],
            "correct_answer": "No, Python blocks do not create new scope; msg is accessible outside",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Functions"],
            "common_misconception": "Assuming Python has block scope like C++, Java, or JavaScript `let`.",
            "explanation": "Python does NOT have block scope. Variables defined inside `if`, `for`, or `while` blocks belong to the enclosing function or module.",
            "hints": {
                "hint1": "In Python, only modules, classes, and functions create new scopes.",
                "hint2": "Variables created inside an `if` block remain accessible after the `if` block.",
                "hint3": "`msg` will print 'hello' without error.",
                "example": "Loops and if blocks do not create private scopes."
            },
            "autopsy": {
                "whatTested": "Differences between block scope and function/module scope in Python.",
                "whyWorks": "Python resolves names to function or module namespaces, ignoring control blocks.",
                "stepByStep": [
                    {"step": 1, "description": "if statement executes.", "state": "Block entered"},
                    {"step": 2, "description": "msg assigned in enclosing module scope.", "state": "msg in module scope"},
                    {"step": 3, "description": "print(msg) successfully prints 'hello'.", "state": "'hello'"}
                ],
                "edgeCases": "If the `if` condition evaluates to False, `msg` is never created, triggering `NameError`.",
                "complexity": "Time: O(1) | Space: O(1)",
                "commonMistakes": "Assuming C/Java style curly-bracket scoping applies to Python.",
                "alternative": "Encapsulate in a function if scope isolation is required.",
                "followUp": "What happens if the if condition is `if False:` instead?"
            },
            "alternatives": ["slot09-main", "slot09-alt2"]
        },
        {
            "id": "slot09-alt2", "slot_number": 9, "is_main": 0,
            "title": "Pure List Append Function", "concept": "Functions",
            "subtopic": "Immutability & Pure Functions", "difficulty": "medium",
            "question_type": "coding",
            "prompt": "Write a pure Python function `append_pure(lst, val)` that returns a NEW list with `val` appended at the end, without mutating the original input `lst`.",
            "code_snippet": "def append_pure(lst, val):\n    # Return a new list containing all items in lst plus val\n    return lst + [val]",
            "options": [], "correct_answer": "lst + [val]",
            "test_cases": [
                {"input": [[1, 2], 3], "expected": [1, 2, 3], "description": "Appends 3 to [1, 2]"},
                {"input": [[], 42], "expected": [42], "description": "Appends to empty list"},
                {"input": [["a"], "b"], "expected": ["a", "b"], "description": "String element appending"}
            ],
            "eval_method": "code_execution", "prerequisites": ["Functions", "Arrays & Lists"],
            "common_misconception": "Calling `lst.append(val)` which mutates the original list in place and returns None.",
            "explanation": "`lst + [val]` or `[*lst, val]` constructs and returns a new list in heap memory without modifying the caller's input list.",
            "hints": {
                "hint1": "Do not call `lst.append(val)` as that modifies the input list.",
                "hint2": "You can concatenate lists: `lst + [val]`.",
                "hint3": "Alternatively, copy first: `new_lst = lst.copy(); new_lst.append(val); return new_lst`.",
                "example": "`[1, 2] + [3]` creates a brand new list `[1, 2, 3]`."
            },
            "autopsy": {
                "whatTested": "Pure functional semantics versus in-place collection mutation.",
                "whyWorks": "List concatenation creates a new list object without altering input operand addresses.",
                "stepByStep": [
                    {"step": 1, "description": "Receive input list reference.", "state": "lst intact"},
                    {"step": 2, "description": "Allocate new list combining elements.", "state": "New list at 0xB"},
                    {"step": 3, "description": "Return new list.", "state": "Original list unchanged"}
                ],
                "edgeCases": "Works cleanly with empty input lists.",
                "complexity": "Time: O(N) | Space: O(N)",
                "commonMistakes": "Using `return lst.append(val)` which returns None and mutates input.",
                "alternative": "`return [*lst, val]`",
                "followUp": "Why are pure functions beneficial in multithreaded programs?"
            },
            "alternatives": ["slot09-main", "slot09-alt1"]
        },

        # SLOT 10
        {
            "id": "slot10-main", "slot_number": 10, "is_main": 1,
            "title": "Dictionary Frequency Counter Tracing", "concept": "Basic Algorithms",
            "subtopic": "Hash Maps & Frequency Counting", "difficulty": "medium",
            "question_type": "logic",
            "prompt": "What does the dictionary `counts` contain after processing: `['apple', 'banana', 'apple']`?",
            "code_snippet": "words = ['apple', 'banana', 'apple']\ncounts = {}\nfor w in words:\n    counts[w] = counts.get(w, 0) + 1\nprint(counts)",
            "options": [
                "{'apple': 2, 'banana': 1}",
                "{'apple': 1, 'banana': 1}",
                "{'apple': 3, 'banana': 0}",
                "KeyError: 'apple'"
            ],
            "correct_answer": "{'apple': 2, 'banana': 1}",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Arrays & Lists"],
            "common_misconception": "Thinking `.get(w, 0)` throws a KeyError when a key is missing.",
            "explanation": "`.get(w, 0)` safely returns 0 when the key is not present. 'apple' occurs twice (+2), 'banana' occurs once (+1).",
            "hints": {
                "hint1": "Count how many times each string appears in `words`.",
                "hint2": "'apple' appears at index 0 and index 2.",
                "hint3": "'banana' appears once at index 1.",
                "example": "Frequency map of ['a', 'a', 'b'] is {'a': 2, 'b': 1}."
            },
            "autopsy": {
                "whatTested": "Dictionary key-value mappings and safe lookup with default values.",
                "whyWorks": "Hash tables provide average O(1) key lookups and insertions.",
                "stepByStep": [
                    {"step": 1, "description": "First 'apple': not in dict, get()=0, set to 1.", "state": "{'apple': 1}"},
                    {"step": 2, "description": "'banana': not in dict, get()=0, set to 1.", "state": "{'apple': 1, 'banana': 1}"},
                    {"step": 3, "description": "Second 'apple': present, get()=1, set to 2.", "state": "{'apple': 2, 'banana': 1}"}
                ],
                "edgeCases": "Keys must be hashable immutable types (strings, numbers, tuples).",
                "complexity": "Time: O(N) | Space: O(U) where U is unique words",
                "commonMistakes": "Using `counts[w] += 1` without initialization, causing KeyError.",
                "alternative": "`from collections import Counter; return dict(Counter(words))`",
                "followUp": "What happens if a mutable list is used as a dictionary key?"
            },
            "alternatives": ["slot10-alt1", "slot10-alt2"]
        },
        {
            "id": "slot10-alt1", "slot_number": 10, "is_main": 0,
            "title": "Safe Dictionary Lookup with .get()", "concept": "Basic Algorithms",
            "subtopic": "Defensive Dictionary Access", "difficulty": "easy",
            "question_type": "logic",
            "prompt": "What does `user.get('age', 18)` return when `user = {'name': 'Alice'}`?",
            "code_snippet": "user = {'name': 'Alice'}\nprint(user.get('age', 18))",
            "options": ["18", "None", "KeyError: 'age'", "'Alice'"], "correct_answer": "18",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Variables & Data Types"],
            "common_misconception": "Expecting a KeyError like direct bracket access `user['age']`.",
            "explanation": "`.get(key, default)` returns the provided default value (18) if `key` is absent, preventing a KeyError.",
            "hints": {
                "hint1": "Does 'age' exist in the dictionary `user`?",
                "hint2": "No, so `.get()` falls back to the second argument.",
                "hint3": "The second argument is 18.",
                "example": "`d.get('missing', 'fallback')` returns 'fallback'."
            },
            "autopsy": {
                "whatTested": "Key existence safety and default value fallback in dictionaries.",
                "whyWorks": "`.get()` handles missing keys gracefully without raising exceptions.",
                "stepByStep": [
                    {"step": 1, "description": "Hash lookup for 'age' in user.", "state": "Key not found"},
                    {"step": 2, "description": "Default parameter 18 is substituted.", "state": "Returns 18"}
                ],
                "edgeCases": "If key exists with value None, `user.get('age', 18)` returns None, not 18.",
                "complexity": "Time: O(1) | Space: O(1)",
                "commonMistakes": "Using `user['age']` which crashes with KeyError.",
                "alternative": "`user['age'] if 'age' in user else 18`",
                "followUp": "What would user.get('name', 'Bob') return?"
            },
            "alternatives": ["slot10-main", "slot10-alt2"]
        },
        {
            "id": "slot10-alt2", "slot_number": 10, "is_main": 0,
            "title": "Character Frequency Counter", "concept": "Basic Algorithms",
            "subtopic": "Character Map Construction", "difficulty": "medium",
            "question_type": "coding",
            "prompt": "Write a Python function `char_frequency(text)` that returns a dictionary mapping each character in `text` to the number of times it appears.",
            "code_snippet": "def char_frequency(text):\n    counts = {}\n    for ch in text:\n        counts[ch] = counts.get(ch, 0) + 1\n    return counts",
            "options": [], "correct_answer": "counts.get(ch, 0) + 1",
            "test_cases": [
                {"input": ["banana"], "expected": {"b": 1, "a": 3, "n": 2}, "description": "Counts in 'banana'"},
                {"input": [""], "expected": {}, "description": "Empty string returns empty dict"},
                {"input": ["abc"], "expected": {"a": 1, "b": 1, "c": 1}, "description": "Unique characters"}
            ],
            "eval_method": "code_execution", "prerequisites": ["Strings", "Basic Algorithms"],
            "common_misconception": "Directly incrementing `counts[ch] += 1` before checking key presence.",
            "explanation": "Iterating over characters and using `counts.get(ch, 0) + 1` builds an accurate frequency map in O(N) linear time.",
            "hints": {
                "hint1": "Initialize an empty dictionary `counts = {}`.",
                "hint2": "Loop through each character in `text`.",
                "hint3": "Update counts with `counts[ch] = counts.get(ch, 0) + 1`.",
                "example": "'aba' produces {'a': 2, 'b': 1}."
            },
            "autopsy": {
                "whatTested": "Frequency distribution mapping using hash tables.",
                "whyWorks": "Single traversal counts character occurrences in linear time.",
                "stepByStep": [
                    {"step": 1, "description": "Initialize empty dict.", "state": "counts = {}"},
                    {"step": 2, "description": "Iterate chars, updating count.", "state": "Frequencies updated"},
                    {"step": 3, "description": "Return dictionary.", "state": "Result"}
                ],
                "edgeCases": "Empty string returns empty dictionary.",
                "complexity": "Time: O(N) | Space: O(K) where K is alphabet size",
                "commonMistakes": "Using string `.count()` inside the loop, turning an O(N) algorithm into slow O(N^2).",
                "alternative": "`from collections import Counter; return dict(Counter(text))`",
                "followUp": "Why is using text.count(ch) inside a loop inefficient?"
            },
            "alternatives": ["slot10-main", "slot10-alt1"]
        },

        # SLOT 11
        {
            "id": "slot11-main", "slot_number": 11, "is_main": 1,
            "title": "2D Matrix Column Extraction", "concept": "Edge Cases",
            "subtopic": "Nested List Row-Major Indexing", "difficulty": "hard",
            "question_type": "logic",
            "prompt": "Given `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`, what expression extracts the middle element (value 5)?",
            "code_snippet": "matrix = [\n    [1, 2, 3],\n    [4, 5, 6],\n    [7, 8, 9]\n]\nprint(matrix[1][1])",
            "options": ["matrix[1][1]", "matrix[2][2]", "matrix[1, 1]", "matrix[0][1]"], "correct_answer": "matrix[1][1]",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Arrays & Lists"],
            "common_misconception": "Using comma indexing `matrix[1, 1]` which causes TypeError on standard Python lists.",
            "explanation": "Standard Python lists are indexed with chained brackets: `matrix[row][col]`. Row index 1, col index 1 is `5`.",
            "hints": {
                "hint1": "0-indexed rows: row 0 is [1, 2, 3], row 1 is [4, 5, 6].",
                "hint2": "0-indexed columns: in row 1, index 0 is 4, index 1 is 5.",
                "hint3": "Chain brackets: `matrix[row][col]`.",
                "example": "`matrix[0][0]` accesses top-left element 1."
            },
            "autopsy": {
                "whatTested": "Row-major nested list indexing syntax.",
                "whyWorks": "`matrix[1]` dereferences the inner list; `[1]` indexes into that inner list.",
                "stepByStep": [
                    {"step": 1, "description": "matrix[1] evaluates to row [4, 5, 6].", "state": "Inner list reference"},
                    {"step": 2, "description": "[4, 5, 6][1] evaluates to 5.", "state": "5"}
                ],
                "edgeCases": "Jagged matrices where inner rows have variable lengths.",
                "complexity": "Time: O(1) | Space: O(1)",
                "commonMistakes": "Writing `matrix[1, 1]` (valid in NumPy, invalid in standard Python lists).",
                "alternative": "`[row[1] for row in matrix]` to extract an entire column.",
                "followUp": "How would you extract all elements of column 0 as a list?"
            },
            "alternatives": ["slot11-alt1", "slot11-alt2"]
        },
        {
            "id": "slot11-alt1", "slot_number": 11, "is_main": 0,
            "title": "Matrix Dimension Inspection", "concept": "Edge Cases",
            "subtopic": "2D Matrix Dimensions", "difficulty": "easy",
            "question_type": "logic",
            "prompt": "For `grid = [[1, 2, 3, 4], [5, 6, 7, 8]]`, what are the number of rows and columns?",
            "code_snippet": "grid = [[1, 2, 3, 4], [5, 6, 7, 8]]",
            "options": ["2 rows, 4 columns", "4 rows, 2 columns", "2 rows, 8 columns", "8 rows, 1 column"],
            "correct_answer": "2 rows, 4 columns",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Arrays & Lists"],
            "common_misconception": "Confusing outer list length (rows) with inner list length (columns).",
            "explanation": "The outer list has 2 elements (`len(grid) == 2` rows), and each inner list has 4 elements (`len(grid[0]) == 4` columns).",
            "hints": {
                "hint1": "Count how many inner lists are inside `grid` (that's rows).",
                "hint2": "Count how many items are inside the first inner list (that's columns).",
                "hint3": "There are 2 inner lists, each containing 4 numbers.",
                "example": "len(grid) = rows, len(grid[0]) = columns."
            },
            "autopsy": {
                "whatTested": "2D dimension calculation from nested collection lengths.",
                "whyWorks": "Outer length gives rows; inner length gives column count.",
                "stepByStep": [
                    {"step": 1, "description": "len(grid) evaluates to 2.", "state": "2 rows"},
                    {"step": 2, "description": "len(grid[0]) evaluates to 4.", "state": "4 columns"}
                ],
                "edgeCases": "Empty grid `[]` has 0 rows and no columns.",
                "complexity": "Time: O(1) | Space: O(1)",
                "commonMistakes": "Inverting row and column counts.",
                "alternative": "`rows, cols = len(grid), len(grid[0])`",
                "followUp": "What is the total element count in an R x C grid?"
            },
            "alternatives": ["slot11-main", "slot11-alt2"]
        },
        {
            "id": "slot11-alt2", "slot_number": 11, "is_main": 0,
            "title": "2x2 Matrix Transposition", "concept": "Edge Cases",
            "subtopic": "Matrix Row/Col Inversion", "difficulty": "hard",
            "question_type": "coding",
            "prompt": "Write a Python function `transpose_2x2(matrix)` that takes a 2x2 matrix and returns its transpose (swapping rows and columns).",
            "code_snippet": "def transpose_2x2(matrix):\n    return [\n        [matrix[0][0], matrix[1][0]],\n        [matrix[0][1], matrix[1][1]]\n    ]",
            "options": [], "correct_answer": "matrix[1][0]",
            "test_cases": [
                {"input": [[[1, 2], [3, 4]]], "expected": [[1, 3], [2, 4]], "description": "Transposing [[1, 2], [3, 4]]"},
                {"input": [[[5, 0], [0, 5]]], "expected": [[5, 0], [0, 5]], "description": "Symmetric identity diagonal"}
            ],
            "eval_method": "code_execution", "prerequisites": ["Arrays & Lists", "Edge Cases"],
            "common_misconception": "Returning `matrix[::-1]` which reverses row order instead of transposing columns into rows.",
            "explanation": "Transposition swaps elements across the main diagonal: element at (r, c) moves to (c, r).",
            "hints": {
                "hint1": "Row 0 of the result should be `[matrix[0][0], matrix[1][0]]`.",
                "hint2": "Row 1 of the result should be `[matrix[0][1], matrix[1][1]]`.",
                "hint3": "Notice the diagonal elements (top-left, bottom-right) remain unchanged.",
                "example": "[[1, 2], [3, 4]] becomes [[1, 3], [2, 4]]."
            },
            "autopsy": {
                "whatTested": "Coordinate transformation across 2D matrix arrays.",
                "whyWorks": "Swapping row and column index maps `matrix[i][j]` to `result[j][i]`.",
                "stepByStep": [
                    {"step": 1, "description": "Extract column 0 as new row 0.", "state": "[1, 3]"},
                    {"step": 2, "description": "Extract column 1 as new row 1.", "state": "[2, 4]"},
                    {"step": 3, "description": "Combine into [[1, 3], [2, 4]].", "state": "Transposed"}
                ],
                "edgeCases": "Symmetric matrices equal their own transpose.",
                "complexity": "Time: O(1) for 2x2 | Space: O(1)",
                "commonMistakes": "Confusing transpose with 90-degree clockwise rotation.",
                "alternative": "`return [list(row) for row in zip(*matrix)]`",
                "followUp": "How does `zip(*matrix)` transpose arbitrary N x M matrices?"
            },
            "alternatives": ["slot11-main", "slot11-alt1"]
        },

        # SLOT 12
        {
            "id": "slot12-main", "slot_number": 12, "is_main": 1,
            "title": "Binary Search Midpoint and Shrinkage", "concept": "Basic Algorithms",
            "subtopic": "Logarithmic Search Division", "difficulty": "medium",
            "question_type": "logic",
            "prompt": "In binary search on a sorted list, if `nums[mid] < target`, what is the correct update to search boundaries?",
            "code_snippet": "# Binary Search\nif nums[mid] < target:\n    # Target must be in the right half\n    low = mid + 1",
            "options": ["low = mid + 1", "high = mid - 1", "low = mid", "high = mid"],
            "correct_answer": "low = mid + 1",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Basic Algorithms"],
            "common_misconception": "Setting `low = mid` which can cause infinite loops when `low + 1 == high`.",
            "explanation": "Since `nums[mid]` is strictly less than target and the list is sorted, target must reside strictly to the right of `mid`. Thus `low = mid + 1`.",
            "hints": {
                "hint1": "The array is sorted in ascending order.",
                "hint2": "If the middle element is too small, can target be at or to the left of mid? No.",
                "hint3": "Move the lower bound to `mid + 1`.",
                "example": "If mid is index 4 and too small, search begins at index 5."
            },
            "autopsy": {
                "whatTested": "Boundary shrinkage invariants in divide-and-conquer algorithms.",
                "whyWorks": "Eliminates the entire left half of the search interval in O(1) comparisons.",
                "stepByStep": [
                    {"step": 1, "description": "Evaluate nums[mid] < target.", "state": "True"},
                    {"step": 2, "description": "Conclude target > nums[mid].", "state": "Target in right half"},
                    {"step": 3, "description": "Update low = mid + 1.", "state": "Search window halved"}
                ],
                "edgeCases": "Setting `low = mid` risks infinite looping if integer division truncates.",
                "complexity": "Time: O(log N) overall | Space: O(1)",
                "commonMistakes": "Writing `low = mid` without adding 1.",
                "alternative": "`bisect.bisect_left(nums, target)`",
                "followUp": "How would the boundary update change if nums[mid] > target?"
            },
            "alternatives": ["slot12-alt1", "slot12-alt2"]
        },
        {
            "id": "slot12-alt1", "slot_number": 12, "is_main": 0,
            "title": "Binary Search Prerequisite Check", "concept": "Basic Algorithms",
            "subtopic": "Algorithm Invariants", "difficulty": "easy",
            "question_type": "logic",
            "prompt": "What essential property must a list have before binary search can be applied?",
            "code_snippet": "# Binary Search Requirement",
            "options": [
                "The list must be sorted in order",
                "The list must contain only positive numbers",
                "The list must have an even length",
                "The list must not contain duplicates"
            ],
            "correct_answer": "The list must be sorted in order",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Basic Algorithms"],
            "common_misconception": "Believing binary search works on arbitrary unsorted lists.",
            "explanation": "Binary search relies on monotonicity: discarding half the elements only works if elements are sorted.",
            "hints": {
                "hint1": "Binary search divides the search space assuming values increase predictably.",
                "hint2": "Without this property, a target could be anywhere in either half.",
                "hint3": "The list must be sorted.",
                "example": "Looking up a name in a printed dictionary works because names are alphabetized."
            },
            "autopsy": {
                "whatTested": "Preconditions and invariants required for logarithmic search.",
                "whyWorks": "Sorted order guarantees that all elements left of mid are <= mid.",
                "stepByStep": [
                    {"step": 1, "description": "Verify list is sorted.", "state": "Sorted invariant holds"},
                    {"step": 2, "description": "Safely discard half the elements at each step.", "state": "O(log N)"}
                ],
                "edgeCases": "Applying binary search on unsorted data produces incorrect answers unpredictably.",
                "complexity": "Time: O(log N) if sorted | O(N log N) if sorting required first",
                "commonMistakes": "Applying binary search on raw unsorted input.",
                "alternative": "Use linear search O(N) or sort first in O(N log N).",
                "followUp": "When is linear search faster than sorting and binary searching?"
            },
            "alternatives": ["slot12-main", "slot12-alt2"]
        },
        {
            "id": "slot12-alt2", "slot_number": 12, "is_main": 0,
            "title": "Iterative Binary Search Implementation", "concept": "Basic Algorithms",
            "subtopic": "Logarithmic Search Implementation", "difficulty": "hard",
            "question_type": "coding",
            "prompt": "Write a Python function `binary_search(nums, target)` that returns the 0-based index of `target` in the sorted list `nums`, or `-1` if `target` is not found.",
            "code_snippet": "def binary_search(nums, target):\n    low = 0\n    high = len(nums) - 1\n    while low <= high:\n        mid = (low + high) // 2\n        if nums[mid] == target:\n            return mid\n        elif nums[mid] < target:\n            low = mid + 1\n        else:\n            high = mid - 1\n    return -1",
            "options": [], "correct_answer": "return mid",
            "test_cases": [
                {"input": [[1, 3, 5, 7, 9], 5], "expected": 2, "description": "Finds 5 at index 2"},
                {"input": [[1, 3, 5, 7, 9], 4], "expected": -1, "description": "Missing element returns -1"},
                {"input": [[2], 2], "expected": 0, "description": "Single element found at index 0"},
                {"input": [[], 10], "expected": -1, "description": "Empty list returns -1"}
            ],
            "eval_method": "code_execution", "prerequisites": ["Basic Algorithms"],
            "common_misconception": "Writing `while low < high` which fails to check the single remaining element when `low == high`.",
            "explanation": "Iterative binary search maintains `low <= high`. Each step calculates `mid = (low + high) // 2` and halves the search space.",
            "hints": {
                "hint1": "Initialize `low = 0` and `high = len(nums) - 1`.",
                "hint2": "Use `while low <= high:` so single-element ranges are tested.",
                "hint3": "Calculate `mid = (low + high) // 2`. If match, return mid.",
                "example": "Searching for 7 in [1, 3, 5, 7, 9] inspects 5, then 7."
            },
            "autopsy": {
                "whatTested": "Implementing binary search loop with strict boundary invariants.",
                "whyWorks": "Halves the active window on every iteration, guaranteeing completion in <= log2(N) steps.",
                "stepByStep": [
                    {"step": 1, "description": "Set low=0, high=len-1.", "state": "Window established"},
                    {"step": 2, "description": "Compute mid.", "state": "mid = (low + high) // 2"},
                    {"step": 3, "description": "Compare nums[mid] to target.", "state": "Branch to left or right"},
                    {"step": 4, "description": "If exhausted return -1.", "state": "Not found"}
                ],
                "edgeCases": "Empty arrays and target smaller/larger than all elements.",
                "complexity": "Time: O(log N) | Space: O(1)",
                "commonMistakes": "Using `while low < high` which misses targets on boundary.",
                "alternative": "`import bisect; idx = bisect.bisect_left(nums, target); return idx if idx < len(nums) and nums[idx] == target else -1`",
                "followUp": "How many comparisons does binary search take for 1,000,000 items?"
            },
            "alternatives": ["slot12-main", "slot12-alt1"]
        },

        # SLOT 13
        {
            "id": "slot13-main", "slot_number": 13, "is_main": 1,
            "title": "Recursive Call Stack Unwinding", "concept": "Basic Algorithms",
            "subtopic": "Recursion Frame Stacking & Base Cases", "difficulty": "hard",
            "question_type": "logic",
            "prompt": "What value does `recur(4)` return given the definition below?",
            "code_snippet": "def recur(n):\n    if n <= 1:\n        return 1\n    return n + recur(n - 1)\n\nprint(recur(4))",
            "options": ["10", "24", "7", "15"], "correct_answer": "10",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Functions"],
            "common_misconception": "Multiplying instead of adding (confusing triangular sum with factorial).",
            "explanation": "`recur(4) = 4 + recur(3) = 4 + (3 + recur(2)) = 4 + (3 + (2 + recur(1))) = 4 + 3 + 2 + 1 = 10`.",
            "hints": {
                "hint1": "What is the base case condition that stops recursion? `n <= 1` returns 1.",
                "hint2": "Expand the chain: `4 + (3 + (2 + recur(1)))`.",
                "hint3": "Sum the numbers 4 + 3 + 2 + 1.",
                "example": "`recur(2)` = 2 + 1 = 3."
            },
            "autopsy": {
                "whatTested": "Recursive base cases, frame stacking, and post-order unwinding.",
                "whyWorks": "Each activation frame suspends until its sub-call completes, accumulating the sum.",
                "stepByStep": [
                    {"step": 1, "description": "Frame 1: recur(4) -> 4 + recur(3)", "state": "Waiting for recur(3)"},
                    {"step": 2, "description": "Frame 2: recur(3) -> 3 + recur(2)", "state": "Waiting for recur(2)"},
                    {"step": 3, "description": "Frame 3: recur(2) -> 2 + recur(1)", "state": "Waiting for recur(1)"},
                    {"step": 4, "description": "Frame 4: recur(1) hits base case n<=1 -> returns 1", "state": "Returns 1"},
                    {"step": 5, "description": "Unwind: 2 + 1 = 3 -> 3 + 3 = 6 -> 4 + 6 = 10", "state": "Returns 10"}
                ],
                "edgeCases": "Calling with negative numbers returns 1 immediately due to `n <= 1`.",
                "complexity": "Time: O(N) | Space: O(N) call stack frames",
                "commonMistakes": "Multiplying instead of adding.",
                "alternative": "Gauss formula `n * (n + 1) // 2` in O(1) time.",
                "followUp": "What formula calculates this in O(1) time without looping or recursion?"
            },
            "alternatives": ["slot13-alt1", "slot13-alt2"]
        },
        {
            "id": "slot13-alt1", "slot_number": 13, "is_main": 0,
            "title": "Debug Missing Recursion Base Case", "concept": "Basic Algorithms",
            "subtopic": "Infinite Recursion Trapping", "difficulty": "medium",
            "question_type": "debugging",
            "prompt": "The following function triggers `RecursionError: maximum recursion depth exceeded`. Add the base case `if n == 0:` returning `[0]` so countdown terminates safely.",
            "code_snippet": "def countdown(n):\n    # Fix: add base case when n <= 0\n    if n <= 0:\n        return [0]\n    return [n] + countdown(n - 1)",
            "options": [], "correct_answer": "if n <= 0:",
            "test_cases": [
                {"input": [3], "expected": [3, 2, 1, 0], "description": "Countdown from 3 to 0"},
                {"input": [0], "expected": [0], "description": "Countdown from 0"}
            ],
            "eval_method": "code_execution", "prerequisites": ["Basic Algorithms"],
            "common_misconception": "Omitting base cases, causing stack overflow as `n` decreases infinitely into negative numbers.",
            "explanation": "Every recursive function must possess at least one terminating base case that returns without making another recursive call.",
            "hints": {
                "hint1": "Without a base case, `countdown` calls itself forever with negative numbers.",
                "hint2": "Add `if n <= 0: return [0]` at the very start of the function.",
                "hint3": "This stops the recursion when n reaches 0.",
                "example": "Base cases prevent stack overflows."
            },
            "autopsy": {
                "whatTested": "Base case definition and stack overflow prevention.",
                "whyWorks": "A base case returns a concrete value without allocating further stack frames.",
                "stepByStep": [
                    {"step": 1, "description": "Check if n <= 0.", "state": "Base case hit"},
                    {"step": 2, "description": "Return [0] without recursion.", "state": "Stack unwinds"}
                ],
                "edgeCases": "Passing negative initial values.",
                "complexity": "Time: O(N) | Space: O(N) frames",
                "commonMistakes": "Placing recursive call before the base case check.",
                "alternative": "Use an iterative while loop.",
                "followUp": "What is Python's default recursion limit?"
            },
            "alternatives": ["slot13-main", "slot13-alt2"]
        },
        {
            "id": "slot13-alt2", "slot_number": 13, "is_main": 0,
            "title": "Recursive Sum of Digits", "concept": "Basic Algorithms",
            "subtopic": "Recursive Integer Decomposition", "difficulty": "hard",
            "question_type": "coding",
            "prompt": "Write a recursive Python function `sum_digits(n)` that returns the sum of all digits of non-negative integer `n`. Example: `sum_digits(1234)` -> `1 + 2 + 3 + 4 = 10`.",
            "code_snippet": "def sum_digits(n):\n    if n < 10:\n        return n\n    return (n % 10) + sum_digits(n // 10)",
            "options": [], "correct_answer": "(n % 10) + sum_digits(n // 10)",
            "test_cases": [
                {"input": [1234], "expected": 10, "description": "1 + 2 + 3 + 4 = 10"},
                {"input": [9], "expected": 9, "description": "Single digit 9"},
                {"input": [1005], "expected": 6, "description": "1 + 0 + 0 + 5 = 6"}
            ],
            "eval_method": "code_execution", "prerequisites": ["Basic Algorithms"],
            "common_misconception": "Converting to string and summing in a loop instead of performing recursive division.",
            "explanation": "Base case: single digit `n < 10` returns `n`. Recursive step: extract last digit `n % 10` and recur on remaining digits `n // 10`.",
            "hints": {
                "hint1": "How do you extract the last digit? `n % 10`.",
                "hint2": "How do you strip the last digit? `n // 10`.",
                "hint3": "Base case: when `n < 10`, return `n`.",
                "example": "123 % 10 is 3, 123 // 10 is 12."
            },
            "autopsy": {
                "whatTested": "Mathematical digit extraction and recursive decomposition.",
                "whyWorks": "Base-10 modulo and floor division peel off one digit per stack frame.",
                "stepByStep": [
                    {"step": 1, "description": "Extract last digit: n % 10.", "state": "Current digit"},
                    {"step": 2, "description": "Recur on remainder: n // 10.", "state": "Smaller integer"},
                    {"step": 3, "description": "Sum returns on unwind.", "state": "Total digit sum"}
                ],
                "edgeCases": "Single digit integers return immediately.",
                "complexity": "Time: O(log10 N) | Space: O(log10 N) stack frames",
                "commonMistakes": "Using float division `/` instead of integer floor division `//`.",
                "alternative": "`return sum(int(d) for d in str(n))`",
                "followUp": "How would you handle negative integers?"
            },
            "alternatives": ["slot13-main", "slot13-alt1"]
        },

        # SLOT 14
        {
            "id": "slot14-main", "slot_number": 14, "is_main": 1,
            "title": "2D Matrix Replication Aliasing Bug", "concept": "Edge Cases",
            "subtopic": "Shallow Multiplication Pointer Duplication", "difficulty": "hard",
            "question_type": "logic",
            "prompt": "What does the following snippet print to stdout?",
            "code_snippet": "grid = [[0] * 3] * 3\ngrid[0][0] = 9\nprint(grid[1][0])",
            "options": ["0", "9", "IndexError", "[9, 0, 0]"], "correct_answer": "9",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Arrays & Lists", "Edge Cases"],
            "common_misconception": "Assuming `*` operator performs deep cloning of inner list objects.",
            "explanation": "`[[0] * 3] * 3` creates a list containing 3 references to the EXACT SAME sublist in heap memory. Mutating `grid[0][0]` mutates every row's first column, so `grid[1][0]` is also 9.",
            "hints": {
                "hint1": "Does the multiplication operator `*` create independent copies of objects, or duplicate references?",
                "hint2": "Check if `id(grid[0]) == id(grid[1])` would be True.",
                "hint3": "All three rows in `grid` point to the identical list in heap memory.",
                "example": "To avoid this, use a list comprehension: `[[0]*3 for _ in range(3)]`."
            },
            "autopsy": {
                "whatTested": "Shallow object replication, pointer aliasing, and 2D collection allocation.",
                "whyWorks": "List multiplication repeats pointer addresses. The outer list holds 3 pointers to the single inner list.",
                "stepByStep": [
                    {"step": 1, "description": "`[0] * 3` creates a single inner list `[0, 0, 0]` at heap address 0xA.", "state": "List at 0xA"},
                    {"step": 2, "description": "`[0xA] * 3` creates outer list `[0xA, 0xA, 0xA]`.", "state": "All rows point to 0xA"},
                    {"step": 3, "description": "`grid[0][0] = 9` mutates index 0 of list 0xA to 9.", "state": "0xA is now [9, 0, 0]"},
                    {"step": 4, "description": "`grid[1][0]` inspects index 0 of list 0xA, yielding 9.", "state": "9"}
                ],
                "edgeCases": "Immutable elements like `[0] * 3` are safe because integers cannot be mutated in place.",
                "complexity": "Time: O(Rows * Cols) | Space: O(Cols) due to unintended sharing",
                "commonMistakes": "Assuming `*` performs deep cloning.",
                "alternative": "`grid = [[0] * 3 for _ in range(3)]` creates independent row objects.",
                "followUp": "How would you initialize a 3x3 grid where each row is an independent list?"
            },
            "alternatives": ["slot14-alt1", "slot14-alt2"]
        },
        {
            "id": "slot14-alt1", "slot_number": 14, "is_main": 0,
            "title": "Reference Assignment vs Shallow Copy", "concept": "Edge Cases",
            "subtopic": "Pointer Assignment vs .copy()", "difficulty": "medium",
            "question_type": "logic",
            "prompt": "What is `a` after running: `a = [1, 2]; b = a; b.append(3)`?",
            "code_snippet": "a = [1, 2]\nb = a\nb.append(3)\nprint(a)",
            "options": ["[1, 2, 3]", "[1, 2]", "[3]", "AttributeError"], "correct_answer": "[1, 2, 3]",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Arrays & Lists"],
            "common_misconception": "Believing `b = a` copies the list elements.",
            "explanation": "In Python, `b = a` binds variable `b` to the same list object in memory as `a`. Mutating `b` mutates `a`.",
            "hints": {
                "hint1": "Does assignment `=` create a new object or copy the pointer address?",
                "hint2": "Both `a` and `b` reference the exact same list in heap memory.",
                "hint3": "Appending to `b` alters the list that `a` also points to.",
                "example": "Use `b = a.copy()` if you want an independent copy."
            },
            "autopsy": {
                "whatTested": "Object identity, reference semantics, and in-place list mutations.",
                "whyWorks": "Variables in Python are pointers to heap objects; `=` simply aliases the reference.",
                "stepByStep": [
                    {"step": 1, "description": "a points to list [1, 2] at address 0x1.", "state": "a -> 0x1"},
                    {"step": 2, "description": "b = a copies pointer 0x1 to b.", "state": "b -> 0x1"},
                    {"step": 3, "description": "b.append(3) mutates object at 0x1.", "state": "0x1 is now [1, 2, 3]"},
                    {"step": 4, "description": "a inspects 0x1, seeing [1, 2, 3].", "state": "[1, 2, 3]"}
                ],
                "edgeCases": "Rebinding `b = [4, 5]` breaks the link without mutating `a`.",
                "complexity": "Time: O(1) | Space: O(1)",
                "commonMistakes": "Expecting pass-by-value semantics for collections.",
                "alternative": "`b = a.copy()` or `b = list(a)`",
                "followUp": "How does `copy.deepcopy()` differ from `a.copy()`?"
            },
            "alternatives": ["slot14-main", "slot14-alt2"]
        },
        {
            "id": "slot14-alt2", "slot_number": 14, "is_main": 0,
            "title": "Debug Mutable Default Argument Trap", "concept": "Edge Cases",
            "subtopic": "Default Parameter Allocation Lifecycle", "difficulty": "hard",
            "question_type": "debugging",
            "prompt": "The function below suffers from the notorious Python mutable default argument bug: calls share the same list! Fix it using the canonical `lst=None` pattern.",
            "code_snippet": "def append_item(val, lst=None):\n    if lst is None:\n        lst = []\n    lst.append(val)\n    return lst",
            "options": [], "correct_answer": "lst is None",
            "test_cases": [
                {"input": [1], "expected": [1], "description": "First call with default creates fresh list [1]"},
                {"input": [2], "expected": [2], "description": "Second call with default must NOT retain 1, returns [2]"}
            ],
            "eval_method": "code_execution", "prerequisites": ["Functions", "Edge Cases"],
            "common_misconception": "Assuming default parameters are evaluated each time the function is called.",
            "explanation": "Default argument expressions are evaluated ONCE when the function definition is executed, not at each call. A mutable default like `lst=[]` is shared across all calls unless guarded with `None`.",
            "hints": {
                "hint1": "Change the default argument in the signature to `lst=None`.",
                "hint2": "Inside the function, check `if lst is None: lst = []`.",
                "hint3": "This ensures a brand-new list is created on each call.",
                "example": "Always use None as default for mutable arguments (lists, dicts, sets)."
            },
            "autopsy": {
                "whatTested": "Function object creation lifecycle and shared mutable default parameters.",
                "whyWorks": "`lst=None` defers list instantiation to runtime inside the function body.",
                "stepByStep": [
                    {"step": 1, "description": "Function called with lst=None.", "state": "lst is None"},
                    {"step": 2, "description": "Guard clause creates new list [] in current frame.", "state": "Fresh list"},
                    {"step": 3, "description": "Append item and return.", "state": "No pollution across calls"}
                ],
                "edgeCases": "Explicitly passing `lst=my_list` operates on the provided list correctly.",
                "complexity": "Time: O(1) | Space: O(1)",
                "commonMistakes": "Writing `def f(val, lst=[]):`.",
                "alternative": "`lst = [] if lst is None else lst`",
                "followUp": "Why are integers and strings immune to this default argument trap?"
            },
            "alternatives": ["slot14-main", "slot14-alt1"]
        },

        # SLOT 15
        {
            "id": "slot15-main", "slot_number": 15, "is_main": 1,
            "title": "Optimal Duplicate Detection Complexity", "concept": "Basic Algorithms",
            "subtopic": "Time-Space Trade-off Analysis", "difficulty": "hard",
            "question_type": "logic",
            "prompt": "Which algorithm finds if an unsorted array of N integers contains any duplicate in O(N) average time and O(N) auxiliary space?",
            "code_snippet": "# Target: O(N) time and O(N) space",
            "options": [
                "Nested loops comparing every pair (i, j)",
                "In-place QuickSort followed by single-pass adjacent element check",
                "Hash Set membership checking during a single linear traversal",
                "Recursive binary search on the unsorted list"
            ],
            "correct_answer": "Hash Set membership checking during a single linear traversal",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Basic Algorithms"],
            "common_misconception": "Choosing sorting when strictly linear O(N) time is demanded.",
            "explanation": "A hash set allows O(1) average lookup and insertion. A single pass over N elements checks and inserts in O(N) total time, using O(N) memory for the set.",
            "hints": {
                "hint1": "What data structure provides O(1) average time lookups?",
                "hint2": "Nested loops take O(N^2) time; sorting takes O(N log N) time.",
                "hint3": "Hash sets trade O(N) extra memory to achieve linear O(N) speed.",
                "example": "Using `seen = set()` in Python."
            },
            "autopsy": {
                "whatTested": "Time vs. space trade-offs and choosing hash-based lookup tables over comparison sorts.",
                "whyWorks": "Hash tables compute array buckets via hashing algorithms, bypassing linear comparison scans.",
                "stepByStep": [
                    {"step": 1, "description": "Nested loops: O(N^2) time, O(1) space (Too slow).", "state": "Eliminated"},
                    {"step": 2, "description": "Sorting: O(N log N) time, O(1) space (Acceptable space, suboptimal time).", "state": "Eliminated"},
                    {"step": 3, "description": "Hash Set: O(N) average time, O(N) space (Optimal time target matched).", "state": "Selected"}
                ],
                "edgeCases": "Worst-case hash collisions can degrade hash lookups to O(N), but average is O(1).",
                "complexity": "Time: O(N) | Space: O(N)",
                "commonMistakes": "Choosing sorting when strictly linear O(N) time is demanded.",
                "alternative": "If numbers are guaranteed in range [1, N], in-place index negation achieves O(N) time and O(1) space.",
                "followUp": "How could duplicate detection be solved in O(1) space if the array was pre-sorted?"
            },
            "alternatives": ["slot15-alt1", "slot15-alt2"]
        },
        {
            "id": "slot15-alt1", "slot_number": 15, "is_main": 0,
            "title": "Nested Loop vs Hash Lookup Complexity", "concept": "Basic Algorithms",
            "subtopic": "Big-O Asymptotic Complexity Comparison", "difficulty": "medium",
            "question_type": "logic",
            "prompt": "What is the worst-case time complexity of finding duplicates using two nested for-loops over a list of N elements?",
            "code_snippet": "for i in range(len(nums)):\n    for j in range(i + 1, len(nums)):\n        if nums[i] == nums[j]:\n            return True",
            "options": ["O(N^2)", "O(N)", "O(N log N)", "O(1)"], "correct_answer": "O(N^2)",
            "test_cases": [], "eval_method": "mcq", "prerequisites": ["Basic Algorithms"],
            "common_misconception": "Confusing linear O(N) scans with quadratic nested iterations.",
            "explanation": "Nested loops comparing every pair perform N * (N - 1) / 2 comparisons, scaling quadratically as O(N^2).",
            "hints": {
                "hint1": "The outer loop runs N times.",
                "hint2": "For each outer step, the inner loop runs roughly N/2 times on average.",
                "hint3": "N * N yields quadratic complexity: O(N^2).",
                "example": "If N=10,000, O(N^2) requires ~50,000,000 operations."
            },
            "autopsy": {
                "whatTested": "Recognizing quadratic time complexity in nested loop patterns.",
                "whyWorks": "Number of pairwise comparisons is given by combination formula C(N, 2) = N*(N-1)/2.",
                "stepByStep": [
                    {"step": 1, "description": "Outer loop iterates N times.", "state": "O(N)"},
                    {"step": 2, "description": "Inner loop compares remaining elements.", "state": "Sum of 1 to N-1"},
                    {"step": 3, "description": "Total steps = N(N-1)/2 -> O(N^2).", "state": "Quadratic"}
                ],
                "edgeCases": "Very small lists (N < 20) where constant factors dominate.",
                "complexity": "Time: O(N^2) | Space: O(1)",
                "commonMistakes": "Thinking it is O(N) because the inner loop starts at i + 1.",
                "alternative": "Use a hash set to drop complexity from O(N^2) to O(N).",
                "followUp": "How would the execution time change if N doubles?"
            },
            "alternatives": ["slot15-main", "slot15-alt2"]
        },
        {
            "id": "slot15-alt2", "slot_number": 15, "is_main": 0,
            "title": "First Repeating Element in O(N) Time", "concept": "Basic Algorithms",
            "subtopic": "Linear Hash Set Traversal", "difficulty": "hard",
            "question_type": "coding",
            "prompt": "Write a Python function `first_repeating(nums)` that returns the first element that appears more than once, in O(N) time using a hash set. Return `-1` if no duplicates exist.",
            "code_snippet": "def first_repeating(nums):\n    seen = set()\n    for x in nums:\n        if x in seen:\n            return x\n        seen.add(x)\n    return -1",
            "options": [], "correct_answer": "if x in seen: return x",
            "test_cases": [
                {"input": [[10, 5, 3, 4, 3, 5, 6]], "expected": 3, "description": "First duplicate encountered is 3"},
                {"input": [[1, 2, 3, 4]], "expected": -1, "description": "No duplicates returns -1"},
                {"input": [[7, 7]], "expected": 7, "description": "Immediate duplicate pair returns 7"}
            ],
            "eval_method": "code_execution", "prerequisites": ["Basic Algorithms"],
            "common_misconception": "Sorting the array first, which disrupts the original encounter order and changes the 'first repeating' definition.",
            "explanation": "Traversing linearly and checking `if x in seen:` identifies the first duplicate at the exact moment of its second appearance in O(N) time and O(N) space.",
            "hints": {
                "hint1": "Initialize an empty set: `seen = set()`.",
                "hint2": "Loop through `nums`: if `x in seen`, immediately return `x`.",
                "hint3": "Otherwise, add `x` to `seen`. If the loop finishes, return `-1`.",
                "example": "In [1, 2, 1], when visiting the second 1, it is already in `seen`."
            },
            "autopsy": {
                "whatTested": "Optimal early-exit duplicate detection using hash sets.",
                "whyWorks": "Set lookup `x in seen` runs in O(1) average time, keeping total traversal to O(N).",
                "stepByStep": [
                    {"step": 1, "description": "seen = set() created.", "state": "Empty hash table"},
                    {"step": 2, "description": "Iterate nums, check membership in O(1).", "state": "Checking seen"},
                    {"step": 3, "description": "Return duplicate on first repeat.", "state": "Early return"}
                ],
                "edgeCases": "All elements unique returns -1. Immediate adjacent duplicates handled correctly.",
                "complexity": "Time: O(N) | Space: O(N)",
                "commonMistakes": "Using a list instead of a set for `seen` (`seen = []`), which makes `x in seen` take O(N) resulting in O(N^2) total time.",
                "alternative": "If numbers are bound to [1, N], in-place index marking in O(1) space.",
                "followUp": "Why does using `seen = []` instead of `seen = set()` destroy O(N) performance?"
            },
            "alternatives": ["slot15-main", "slot15-alt1"]
        }
    ]

    with open("question_bank.py", "w", encoding="utf-8") as f:
        f.write('"""\nSkillTrace AI - Question Bank (45 Unique Questions)\n15 Numbered Slots: Each slot has 1 Main Question and 2 Same-Concept Alternatives.\n"""\nimport json\n\n')
        f.write("QUESTIONS_DATA = json.loads('''")
        f.write(json.dumps(questions, indent=2).replace('\\', '\\\\').replace("'''", "\'\'\'"))
        f.write("''')\n")

    print(f"Successfully generated question_bank.py with {len(questions)} unique questions across 15 slots!")

if __name__ == "__main__":
    build_full_question_bank()
