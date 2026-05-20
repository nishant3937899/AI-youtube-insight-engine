import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'app'

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/routes.py",
    f"{project_name}/api/__init__.py",
    f"{project_name}/api/data_client.py",
    f"{project_name}/models/__init__.py",
    f"{project_name}/models/sentiment.py",
    f"{project_name}/models/summarizer.py",
    f"{project_name}/static/css/.gitkeep",
    f"{project_name}/static/js/.gitkeep",
    f"{project_name}/templates/index.html",
    f"{project_name}/templates/results.html",
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "tests/__init__.py",
    "tests/test_api_client.py",
    "tests/test_model_inference.py",
    ".env",
    ".gitignore",
    "requirements.txt",
    "Dockerfile",
    "run.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")