#! usr/bin/env python3

import os
from pathlib import Path

current_dir = Path(__file__).resolve().parent 
INPUT_FILE_PATH = current_dir.parent / "docs" / 'mystery_alphabet.txt'
OUTPUT_FILE_PATH = current_dir.parent / "docs" / 'reconstructed_alphabet.txt'

def infer(file_path):
    try:
        edges = set()
        if not os.path.exists(file_path):
            print("Error: File does not exist.")
            return
        with open(file_path, "r", encoding="utf-8") as f:
            paragraphs = [line.strip() for line in f if line.strip()]

        for index in range(len(paragraphs) - 1):
            paragraph1 = paragraphs[index]
            paragraph2 = paragraphs[index + 1]

            for i in range(min(len(paragraph1), len(paragraph2))):
                if paragraph1[i] != paragraph2[i]:
                    edges.add((paragraph1[i], paragraph2[i]))
                    break
        return edges
    
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied. Unable to access the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        if f is not None and not f.closed:
            f.close()

def write_to_file(content, file_path):
    try:
        print("Reading content...")
        if content is None:
            print("Provide content is empty!")
            print("Operation cancelled!")
            return
        print("Content loaded completed.\n")

        if isinstance(content, set):
            newContent = "".join("".join(data) for data in content)
        else:
            newContent = content
        
        newContent = str(newContent)
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w') as f:
            print("Writing new content to file...")
            f.write(newContent)
            print("File write up completed.\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return
    finally:
        if f is not None and not f.closed:
            f.close()
        print("File closed successfully.")

result = infer(INPUT_FILE_PATH)
if result:
    write_to_file(result, OUTPUT_FILE_PATH)
else:
    print(result)