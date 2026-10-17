import json

def update_builder():
    with open("build_bank.py", "r", encoding="utf-8") as f:
        content = f.read()

    # Change the file writer part to use json.loads
    old_writer = """    with open("question_bank.py", "w", encoding="utf-8") as f:
        f.write('\"\"\"\\nSkillTrace AI - Question Bank (45 Unique Questions)\\n15 Numbered Slots: Each slot has 1 Main Question and 2 Same-Concept Alternatives.\\n\"\"\"\\n\\n')
        f.write("QUESTIONS_DATA = ")
        json.dump(questions, f, indent=4)
        f.write("\\n")"""

    new_writer = """    with open("question_bank.py", "w", encoding="utf-8") as f:
        f.write('\"\"\"\\nSkillTrace AI - Question Bank (45 Unique Questions)\\n15 Numbered Slots: Each slot has 1 Main Question and 2 Same-Concept Alternatives.\\n\"\"\"\\nimport json\\n\\n')
        f.write("QUESTIONS_DATA = json.loads('''")
        f.write(json.dumps(questions, indent=2).replace('\\\\', '\\\\\\\\').replace("'''", "\\'\\'\\'"))
        f.write("''')\\n")"""

    content = content.replace(old_writer, new_writer)
    with open("build_bank.py", "w", encoding="utf-8") as f:
        f.write(content)

update_builder()
