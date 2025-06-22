"""
Project overview
Module	What it demonstrates from your list
Word Search	1, 6, 7 – find words, show line numbers
Hi-Score Manager	2 – read / update Hi-score.txt
Table Generator	3 – write 2-to-20 tables into a child-friendly folder
Censor Tool	4, 5 – replace forbidden words in-place
Copy / Compare / Wipe / Rename	8, 9, 10, 11 – classic file ops

The code is written in modern style with:

pathlib (clean cross-platform paths)

shutil & filecmp for safe file handling

docstrings + type hints for clarity


"""

#!/usr/bin/env python3
"""
file_toolkit.py – A mini utility suite that groups together
common beginner file-handling exercises (word search, hi-score,
table generation, censoring, copying, comparing, wiping, renaming).

Author: <you>
"""

from pathlib import Path
import shutil
import filecmp
import re
from typing import List

# ----------------------------------------------------------------------
# 1. WORD / LOG SEARCH
# ----------------------------------------------------------------------

def contains_word(file_path: Path, word: str, show_lines: bool = False) -> bool:
    """
    Return True if 'word' (case-insensitive) is found in file.
    If show_lines is True, also print the line numbers that contain it.
    """
    found = False
    with file_path.open(encoding="utf-8") as f:
        for idx, line in enumerate(f, 1):
            if word.lower() in line.lower():
                found = True
                if show_lines:
                    print(f"Line {idx}: {line.strip()}")
    return found


# ----------------------------------------------------------------------
# 2. HI-SCORE HANDLER
# ----------------------------------------------------------------------

HS_FILE = Path("Hi-score.txt")

def game() -> int:
    """Stub game – replace with real logic. Returns a random score."""
    import random
    return random.randint(0, 100)

def update_hi_score() -> None:
    """Run the game once and update Hi-score.txt if a new high is hit."""
    current_score = game()
    print(f"▶  You scored: {current_score}")

    high = 0
    if HS_FILE.exists():
        txt = HS_FILE.read_text().strip()
        if txt.isdigit():
            high = int(txt)

    if current_score > high:
        HS_FILE.write_text(str(current_score))
        print(f"🏆  New Hi-score! ({current_score} > {high})")
    else:
        print(f"No new hi-score. Current record remains {high}.")


# ----------------------------------------------------------------------
# 3. MULTIPLICATION TABLE GENERATOR
# ----------------------------------------------------------------------

def write_tables(folder: Path) -> None:
    """
    Generate tables 2×…20×10 and save each as a text file
    inside 'folder' (created if needed).
    """
    folder.mkdir(parents=True, exist_ok=True)
    for n in range(2, 21):
        table_lines = [f"{n} x {i} = {n*i}" for i in range(1, 11)]
        (folder / f"table_{n}.txt").write_text("\n".join(table_lines))
    print(f"📝  Tables 2-20 saved to {folder.resolve()}")


# ----------------------------------------------------------------------
# 4–5. CENSOR TOOL
# ----------------------------------------------------------------------

def censor_in_file(file_path: Path, forbidden: List[str]) -> None:
    """
    Replace each word in 'forbidden' with ##### (case-insensitive)
    directly inside file_path.
    """
    pattern = re.compile("|".join(re.escape(w) for w in forbidden), re.I)
    content = file_path.read_text(encoding="utf-8")
    new_content = pattern.sub("#####", content)
    file_path.write_text(new_content, encoding="utf-8")
    print(f"🔒  Censored {len(forbidden)} word(s) in {file_path.name}")


# ----------------------------------------------------------------------
# 8–11. GENERIC FILE OPS
# ----------------------------------------------------------------------

def copy_file(src: Path, dst: Path) -> None:
    shutil.copy2(src, dst)
    print(f"📋  Copied {src.name} ➜ {dst.name}")

def compare_files(f1: Path, f2: Path) -> None:
    same = filecmp.cmp(f1, f2, shallow=False)
    msg = "✅  Files are identical." if same else "❌  Files differ."
    print(msg)

def wipe_file(fp: Path) -> None:
    fp.write_text("")
    print(f"🧹  Wiped content of {fp.name}")

def rename_file(fp: Path, new_name: str) -> None:
    new_path = fp.with_name(new_name)
    fp.rename(new_path)
    print(f"✏️   Renamed to {new_path.name}")


# ----------------------------------------------------------------------
#  SIMPLE CLI
# ----------------------------------------------------------------------

MENU = """
================  File Toolkit  =================
1.  Search word in file (show lines)
2.  Play game and update Hi-score
3.  Generate tables 2-20 (folder: tables_13yo)
4.  Censor single word 'Donkey' in a file
5.  Censor a custom word list in a file
6.  Search 'python' in log file (with lines)
7.  Copy a file
8.  Compare two files
9.  Wipe file content
10. Rename a file ➜ renamed_by_python.txt
0.  Exit
=================================================
"""

def prompt_path(prompt: str) -> Path:
    path = Path(input(prompt).strip())
    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist.")
    return path

def main() -> None:
    while True:
        try:
            print(MENU)
            choice = input("Select option: ").strip()
            if choice == "1":
                fp = prompt_path("File path: ")
                word = input("Word to search: ")
                found = contains_word(fp, word, show_lines=True)
                if not found:
                    print("Word not found.")
            elif choice == "2":
                update_hi_score()
            elif choice == "3":
                write_tables(Path("tables_13yo"))
            elif choice == "4":
                fp = prompt_path("File path: ")
                censor_in_file(fp, ["Donkey"])
            elif choice == "5":
                fp = prompt_path("File path: ")
                words = input("Comma-separated words: ").split(",")
                censor_in_file(fp, [w.strip() for w in words if w.strip()])
            elif choice == "6":
                fp = prompt_path("Log file path: ")
                contains_word(fp, "python", show_lines=True)
            elif choice == "7":
                src = prompt_path("Source file: ")
                dst = Path(input("Destination path: ").strip())
                copy_file(src, dst)
            elif choice == "8":
                f1 = prompt_path("First file: ")
                f2 = prompt_path("Second file: ")
                compare_files(f1, f2)
            elif choice == "9":
                fp = prompt_path("File to wipe: ")
                wipe_file(fp)
            elif choice == "10":
                fp = prompt_path("File to rename: ")
                rename_file(fp, "renamed_by_python.txt")
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid option.")
        except Exception as e:
            print(f"⚠️  Error: {e}")

if __name__ == "__main__":
    main()
