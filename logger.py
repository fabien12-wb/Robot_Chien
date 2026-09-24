import json
from datetime import datetime
from pathlib import Path


LOG_FILE = Path("logs") / "commands.jsonl"


def log_command(command, actions, mode):

    LOG_FILE.parent.mkdir(exist_ok=True)

    entry = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "mode": mode,
        "command": command,
        "actions": actions
    }

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(
            json.dumps(entry, ensure_ascii=False) + "\n"
        )