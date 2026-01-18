from pathlib import Path
from typing import Set, List, Tuple
import logging


def organize_files(
        base_path: Path,
        valid_extensions: Set[str], 
        dry_run: bool = False
        ) -> Tuple[List[Tuple[Path, str]], List[Path]]:
    
    """
    Organizes files in a directory into subfolders based on file extensions.

    Args:
        base_path (Path): Directory containing the files to be organized.
        valid_extensions (Set[str]): Set of allowed file extensions.
        dry_run (bool): If True, simulates the operation without moving files.

    Returns:
        Tuple[List[Tuple[Path, str]], List[Path]]:
            Files successfully moved with their destination folder names.
            Files skipped due to name collision at the destination.

    Raises:
        ValueError: If base_path is not a valid directory.
    """
    
    if not base_path.is_dir():
        logging.error(
            "Invalid directory: %s", 
            base_path
            )
        raise ValueError(f"The path '{base_path}' is not a valid directory.")

    moved_files: List[Tuple[Path, str]] = []
    skipped_files: List[Path] = []

    for source_path in base_path.iterdir():
        if not source_path.is_file():
            logging.debug(
                "Skipping non-file: %s", 
                source_path.name
                )
            continue

        extension = source_path.suffix

        if extension:
            ext = extension[1:].lower() 
            folder_name = ext if ext in valid_extensions else 'no_extension'
        else:
            folder_name = 'no_extension'

        target_folder = base_path / folder_name
        target_path = target_folder / source_path.name

        if target_path.exists():
            logging.warning(
                "File already exists, skipping: %s", 
                target_path.name
                )
            skipped_files.append(source_path)
            continue

        logging.info(
            "Moving file: %s TO -> %s%s",
            source_path.name, 
            target_folder.name,
            "(Dry run)" if dry_run else ""
        )

        if not dry_run:
            target_folder.mkdir(exist_ok=True, parents=True)
            source_path.rename(target_path)

        moved_files.append((source_path, folder_name))

    return moved_files, skipped_files

if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(levelname)s | %(message)s'
    )

    BASE_PATH = Path("FILE/PATH/HERE") # Change this to your target directory
    VALID_EXTENSIONS = {"txt", "rar", "bmp", "png", "jpg", "jpeg", "gif", "mp4", "mp3", "pdf", "docx", "xlsx", "pptx", "zip"} # Add more extensions as needed
    try:
        moved, skipped = organize_files(BASE_PATH, VALID_EXTENSIONS, dry_run=False)
    except ValueError as e:
        logging.critical(
            "Fatal error: %s", 
            e
            )