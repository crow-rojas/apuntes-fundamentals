import os

# Dictionary for Spanish to English translations
translations = {
    "apuntes": "notes",
    "ciencias": "science",
    "dinamica": "dynamics",
    "dinámica": "dynamics",
    "electromagnetismo": "electromagnetism",
    "quimica": "chemistry",
    "química": "chemistry",
    "termodinamica": "thermodynamics",
    "termodinámica": "thermodynamics",
    "ingeniería": "engineering",
    "ingenieria": "engineering",
    "computacion": "computing",
    "computación": "computing",
    "economia": "economics",
    "economía": "economics",
    "etica": "ethics",
    "ética": "ethics",
    "matemáticas": "mathematics",
    "matematicas": "mathematics",
    "probabilidades_y_estadística": "probability_and_statistics",
    "probabilidades_y_estadistica": "probability_and_statistics",
    "algebra_lineal": "linear_algebra",
    "calculo_i": "calculus_i",
    "calculo_ii": "calculus_ii",
    "calculo_iii": "calculus_iii",
    "ecuaciones_diferenciales": "differential_equations",
    "probabilidades_y_estadística": "probability_and_statistics",
    "probabilidades_y_estadistica": "probability_and_statistics",
    "probability_and_statistics": "probability_and_statistics",
    "ejercicios": "exercises",
    "calculo_i,_ii_y_iii": "calculus_i_ii_iii",
    "cálculo_i,_ii_y_iii": "calculus_i_ii_iii",
    "ecuaciones_diferenciales": "differential_equations",
    "álgebra_lineal": "linear_algebra",
    "cálculo_i": "calculus_i",
    "cálculo_ii": "calculus_ii",
    "cálculo_iii": "calculus_iii",
    "probabilidades_y_estadística": "probability_and_statistics",
    "álgebra_lineal": "linear_algebra",
    "introducción": "introduction"
}

# Helper function to convert to snake_case
def to_snake_case(name):
    name = name.replace(" ", "_")
    name = name.replace(",", "_")
    name = name.replace("-", "_")
    name = name.lower()
    return name

# Function to rename files and directories recursively
def rename_items(root):
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        for filename in filenames:
            new_filename = to_snake_case(filename)
            new_filename = translations.get(new_filename, new_filename)
            if filename != new_filename:
                os.rename(
                    os.path.join(dirpath, filename),
                    os.path.join(dirpath, new_filename)
                )
        for dirname in dirnames:
            new_dirname = to_snake_case(dirname)
            new_dirname = translations.get(new_dirname, new_dirname)
            if dirname != new_dirname:
                os.rename(
                    os.path.join(dirpath, dirname),
                    os.path.join(dirpath, new_dirname)
                )

if __name__ == "__main__":
    root_directory = "docs"
    rename_items(root_directory)
