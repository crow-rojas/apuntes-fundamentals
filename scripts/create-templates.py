import sys
import os

# Usage:
# To create a single file:
# python create-templates.py <final_path> <year_semester> <curso> <question_number>
# Example:
# python create-templates.py docs/mathematics/probability-and-statistics/exercises/2019-2/ 2019-2 "Probabilidades y Estadística" 8
#
# To create multiple files for a range:
# python create-templates.py <final_path> <year_semester> <curso> <start-end>
# Example:
# python create-templates.py docs/mathematics/probability-and-statistics/exercises/2019-2/ 2019-2 "Probabilidades y Estadística" 5-8

template = """---
title: Pregunta {question_number}
---

import Image from "@site/src/components/Image";
import MDXDetails from "@site/src/components/MDXDetails";
import Disqus from '@site/src/components/Disqus';

# Pregunta {question_number}

Aquí va el enunciado de la pregunta.

<MDXDetails>
<summary>Solución propuesta</summary>

Aún no hay solución propuesta 🥲

:::info
Esta solución podría estar incorrecta. Si deseas proponer una solución alternativa, manda tu solución abriendo
un Pull Request en el [repositorio](https://github.com/crow-rojas/apuntes-fundamentals/pulls) de GitHub con el archivo
`.mdx` correspondiente.
:::

</MDXDetails>

### Comentarios

<Disqus
  url="https://crow-rojas.github.io/apuntes-fundamentals/{final_path}p{formatted_question_number}"
  identifier="{final_path}p{formatted_question_number}"
  title="{year_semester} {curso} - Pregunta {formatted_question_number}"
/>
"""

def create_template(final_path, year_semester, curso, question_number):
    formatted_question_number = f"{int(question_number):02d}"
    content = template.format(
        question_number=question_number,
        year_semester=year_semester,
        curso=curso,
        formatted_question_number=formatted_question_number,
        final_path=final_path
    )
    
    os.makedirs(final_path, exist_ok=True)
    with open(os.path.join(final_path, f"p{formatted_question_number}.mdx"), 'w') as file:
        file.write(content)
    print(f"Template created at {os.path.join(final_path, f'p{formatted_question_number}.mdx')}")

def process_question_numbers(final_path, year_semester, curso, question_numbers):
    if '-' in question_numbers:
        start, end = map(int, question_numbers.split('-'))
        for number in range(start, end + 1):
            create_template(final_path, year_semester, curso, str(number))
    else:
        create_template(final_path, year_semester, curso, question_numbers)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python create-templates.py <final_path> <year_semester> <curso> <question_numbers>")
        sys.exit(1)
    
    final_path = sys.argv[1]
    year_semester = sys.argv[2]
    curso = sys.argv[3]
    question_numbers = sys.argv[4]
    
    process_question_numbers(final_path, year_semester, curso, question_numbers)
