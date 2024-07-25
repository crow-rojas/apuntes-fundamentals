import os

# Base directory for exercises
base_dir = "docs/Ejercicios"

# Semesters
semesters = ["2024-2", "2023-2", "2019-2", "2019-1", "2018-2", "2018-1", "2017-2", "2017-1", "2016-2", "2016-1"]

# Categories and courses
categories = {
    "Ciencias": [
        "Dinámica",
        "Electricidad y Magnetismo",
        "Química",
        "Termodinámica"
    ],
    "Ingeniería": [
        "Computación",
        "Economía",
        "Ética"
    ],
    "Matemáticas": [
        "Cálculo I, II y III",
        "Ecuaciones Diferenciales",
        "Probabilidades y Estadística",
        "Álgebra Lineal"
    ]
}

# Function to create a template for each exercise
def create_exercise_template(semester, category, course, exercise_num):
    # Construct the directory path
    dir_path = os.path.join(base_dir, semester, category, course)
    
    # Ensure the directory exists
    os.makedirs(dir_path, exist_ok=True)
    
    # Create the filename and filepath
    filename = f"P{exercise_num}.mdx"
    filepath = os.path.join(dir_path, filename)
    
    # Replace slashes with underscores for the ID
    sanitized_id = f"{semester}_{category}_{course}_P{exercise_num}".replace(" ", "_").replace("/", "_")
    
    # Template content
    template_content = f"""---
id: {sanitized_id}
title: Pregunta {exercise_num}
---

import Image from "@site/src/components/Image";
import MDXDetails from "@site/src/components/MDXDetails";
import Disqus from '@site/src/components/Disqus';

# Pregunta {exercise_num}

Aquí va el enunciado de la pregunta.
<MDXDetails>
<summary>Solución</summary>

Aquí va la solución propuesta de la pregunta. Si deseas proponer una solución alternativa, manda tu solución abriendo
un Pull Request en el [repositorio](https://github.com/crow-rojas/apuntes-fundamentals/pulls) de GitHub con el archivo
mdx correspondiente.

</MDXDetails>

### Comentarios

<Disqus
  url="https://crow-rojas.github.io/apuntes-fundamentals/docs/Ejercicios/{semester}/{category}/{course}/P{exercise_num}"
  identifier="{sanitized_id}"
  title="Pregunta {exercise_num}"
/>
"""
    # Write the template content to the file
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(template_content)

    print(f"Template for Pregunta {exercise_num} created at {filepath}")

# Main function to iterate over all semesters, categories, and courses
def main():
    for semester in semesters:
        for category, courses in categories.items():
            for course in courses:
                create_exercise_template(semester, category, course, 1)

if __name__ == "__main__":
    main()