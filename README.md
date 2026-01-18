# File Organizer with Pathlib, Logging and Typing

## Overview

This project is a Python script that organizes files in a given directory into subfolders based on their file extensions. It is intended to be both a practical utility and a demonstration of professional Python fundamentals. It was built with a focus on **code clarity, safety, and professional best practices**, using:

* `pathlib` for robust and readable filesystem operations
* `logging` for structured runtime information and error reporting
* `typing` for explicit type contracts and better maintainability

The goal of this project is not only to solve a practical problem, but also to demonstrate clean Python design suitable for real-world codebases.

---

## Features

* Automatically creates subfolders based on file extensions
* Skips files when a name collision already exists at the destination
* Supports **dry-run mode** to simulate changes safely
* Clear logging with severity levels (INFO, WARNING, ERROR, CRITICAL)
* Fully type-annotated and documented function

---

## How It Works

1. The script scans the target directory
2. Each file is inspected for its extension
3. A subfolder named after the extension is selected or created
4. The file is moved into the corresponding subfolder
5. If a file with the same name already exists, the operation is skipped

All actions are logged to the console.

---

## Usage

### 1. Configure the target directory

Edit the `BASE_PATH` constant in the script:

```python
BASE_PATH = Path("FILE/PATH/HERE")
```

### 2. Configure valid extensions

```python
VALID_EXTENSIONS = {"txt", "png", "jpg", "pdf", "mp4"}
```

Extensions not listed will be grouped under the **no_extension** folder. Files without any extension are also placed there.

### 3. Run the script

```bash
python organize_files.py
```

### Dry Run Mode

To simulate the operation without moving files:

```python
organize_files(BASE_PATH, VALID_EXTENSIONS, dry_run=True)
```

---

## Logging Output Example

```
2026-01-18 10:15:03 | INFO | Moving file: report.pdf TO -> pdf
2026-01-18 10:15:04 | WARNING | File already exists, skipping: image.png
```

---

## Error Handling

* Invalid directories raise a `ValueError`
* Errors are logged before being raised
* Critical failures are handled in the `__main__` block

---

## Code Quality Notes

* Explicit type annotations using `typing`
* Clear separation between business logic and execution
* Defensive checks before filesystem mutations
* Minimal side effects when `dry_run=True`

---

## Requirements

* Python 3.9+

No third-party dependencies are required.

---

## Author

Sant

This project is part of my ongoing learning process in Python. The focus is on fundamentals that matter in real codebases: correctness, readability, defensive programming, and maintainability.
