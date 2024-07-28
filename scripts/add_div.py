import os
import re

def wrap_exercise_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Match the pattern for the question text and wrap it in <div class="exercise">
    new_content = re.sub(
        r'(# Pregunta \d+\n\n)([^<]+?)(\n\n<MDXDetails>)',
        r'\1<div className="exercise">\n\2\n</div>\3',
        content,
        flags=re.DOTALL
    )

    # Only write back if changes were made
    if content != new_content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {file_path}")

def process_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.mdx'):
                wrap_exercise_text(os.path.join(root, file))

if __name__ == "__main__":
    base_directory = 'docs'
    process_files(base_directory)
