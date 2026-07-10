import configparser
import time
from watchdog.observers import Observer
from pathlib import Path

from event_handler import RemoveIllegalCharacter



def main():
    absolute_path = Path(__file__).resolve().parent
    config = configparser.ConfigParser()
    config_filename = absolute_path / "config.ini"
    config.read(config_filename)
    filepath  = config["File"]["Folder"]
    replacement_file = config["File"]["ReplacementFile"]
    replacement_file = replacement_file
    filepath = str(Path.joinpath(Path.home(),filepath))
    event_handler = RemoveIllegalCharacter(absolute_path / replacement_file)
    observer = Observer()
    observer.schedule(event_handler,filepath,recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    main()