import os
import re

def fix_disqus_component(file_path, base_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Extract question number from the file name
    question_number = os.path.basename(file_path).replace('p', '').replace('.mdx', '')
    formatted_question_number = f"{int(question_number):02d}"

    # Extract the title content
    title_match = re.search(r'title="([^"]*)"', content)
    if title_match:
        title_content = title_match.group(1)
    else:
        print(f"Title not found in {file_path}")
        return

    # Create the correct url and identifier
    relative_path = os.path.relpath(file_path, base_path).replace('\\', '/').rsplit('/', 1)[0]
    relative_path = 'docs/' + relative_path.replace('docs/', '')

    # Correct Disqus component
    new_disqus_component = f"""<Disqus
  url="https://crow-rojas.github.io/apuntes-fundamentals/{relative_path}/p{formatted_question_number}"
  identifier="{relative_path}/p{formatted_question_number}"
  title="{title_content}"
/>"""

    # Replace old Disqus component with the new one
    new_content = re.sub(
        r'<Disqus[^>]*>',
        new_disqus_component,
        content,
        flags=re.DOTALL
    )

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
    print(f"Fixed Disqus component in {file_path}")

def process_files(directory, base_path):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.mdx'):
                fix_disqus_component(os.path.join(root, file), base_path)

if __name__ == "__main__":
    base_directory = 'docs/mathematics/calculus-1-2-3/exercises'
    process_files(base_directory, 'docs')
