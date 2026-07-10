# Remove Illegal Characters

A small Python watcher that monitors a folder in your home directory and automatically renames newly created files or folders to remove illegal or unwanted characters.

## What it does

The script uses `watchdog` to watch for new filesystem events and then applies replacements defined in `illegal_characters.json`.

Examples of default replacements:

- `\` → `_`
- `:` → ` - `
- `*` → space
- `?` and `!` → removed
- `<`, `>` and `|` → replaced with spaces
- newline characters → removed

## Project structure

- `remove_illegal_character.py` — starts the file watcher
- `event_handler.py` — handles created files and folders and performs the renaming
- `config.ini` — configuration for the watched folder and replacement mapping file
- `illegal_characters.json` — mapping of characters to replacement values

## Configuration

The watcher reads settings from [config.ini](config.ini):

```ini
[File]
Folder = Watched_Folder
ReplacementFile = illegal_characters.json
```

The `Folder` value is resolved relative to your home directory. For example, if your home directory is `/home/your-user`, the script watches:

```text
/home/your-user/Watched_Folder
```

## Installation

1. Clone or open the project folder.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the watcher

From the project root, start the watcher with:

```bash
python remove_illegal_character.py
```

The program will keep running in the foreground and monitor the configured directory recursively.

## Notes

- The watcher renames items when they are created.
- A log file named `remove illegal character.log` is created by the event handler.
- You can modify the replacement rules in [illegal_characters.json](illegal_characters.json) to suit your own naming rules.
