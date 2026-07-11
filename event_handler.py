import json
import logging

from pathlib import Path
from watchdog.events import DirCreatedEvent, FileCreatedEvent, FileSystemEventHandler

class RemoveIllegalCharacter(FileSystemEventHandler):
    def __init__(self,illegal_characters_replacement_file:Path) -> None:
        super().__init__()
        absolute_path = Path(__file__).resolve().parent
        logging.basicConfig(
            filename=absolute_path / "remove illegal character.log",
            level=logging.INFO,
            format = "%(asctime)s | %(levelname)s | %(message)s"
        )
        self.logger = logging.getLogger()
        with open(illegal_characters_replacement_file,"r") as f:
            self.illegal_characters = json.load(f)
        self.logger.info("Remove Illegal Character Started")

    def on_created(self, event: DirCreatedEvent | FileCreatedEvent) -> None:
        """Remove any \n or illegal characters as needed"""
        if not event.is_directory:
            # Files: check for illegal char or \n
            filepath = Path(str(event.src_path))
            directory = filepath.parent
            filename = filepath.name
            new_filename = filename
            for key,value in self.illegal_characters.items():
                new_filename = new_filename.replace(key,value)
            if new_filename != filename:
                destination_file = directory / new_filename
                filepath.rename(destination_file)
                self.logger.info(rf"{filepath} moved to {destination_file}")
        else:
            # Folders: check for illegal char or \n
            filepath = str(event.src_path)
            folder_name = filepath.split("/")[-1]
            new_folder_name = folder_name
            file_path = "/".join(filepath.split("/")[:-1])
            for key,value in self.illegal_characters.items():
                new_folder_name = new_folder_name.replace(key,value)
            if folder_name != new_folder_name:
                old_foldername = Path(f"{file_path}/{folder_name}")
                new_foldername = Path(f"{file_path}/{new_folder_name}")
                old_foldername.rename(new_foldername)
                self.logger.info(rf"Folder {old_foldername} renamed as {new_foldername}")

            
