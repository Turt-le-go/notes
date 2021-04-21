import os


HOME_DIR = os.environ.get("HOME") 
NOTES_DIR = HOME_DIR + "/Notes"
EDITOR = os.environ.get("EDITOR")
FILE_SUFFIX = ("work","home","todo")


HELP_MESSAGE = """
    --help - вивести це повідомлення

    notes *args - зберегти args в сьогоднішню нотатку
    notes work,todo,home *args - зберегти args в нотатку з таким суфіксом (суфікси можна змінити в config.py)
    notes init - створити папку (і репозиторій) для нотаток
    notes push *args - зберегти нотатки в github
    notes pull - стягнути всі нотатки з github
    notes - відкрити нотатку за сьогодні
"""

