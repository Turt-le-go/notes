import sys
from os import system
from datetime import datetime, date
import config


def commit():
    pass

def write_note(filename, text):
    with open(f"{config.NOTES_DIR}/{filename}", "a") as notes_file:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        len_text = max(len(current_time),len(text))+2
        s = ""
        s += "╔"+"═"*len_text+"╗"+"\n"
        s += "║"+current_time.center(len_text)+"║"+"\n"
        s += "╠"+"═"*len_text+"╣"+"\n"
        s += "║"+text.center(len_text)+"║"+"\n"
        s += "╚"+"═"*len_text+"╝"+"\n"
        s += "\n"
        notes_file.write(s)

def get_args():
    com = ""
    text = ""
    args = sys.argv
    coms = ["help","init","push","pull","rg"]
    coms.extend(config.FILE_SUFFIX)
    if len(args) == 1:
        return com, text
    elif args[1] in coms:
        com = args[1]
        text = " ".join(args[2:])
    else:
        text = " ".join(args[1:])
    return com, text

def main():
    filename = "defaul.txt"
    today = date.today()
    com, text = get_args()
    if com == "help":
        print(config.HELP_MESSAGE)
        return
    elif com == "init":
        system(f"mkdir {config.NOTES_DIR}")
        return
    elif com == "rg":
        system(f"rg {text} -A 1 -B 3 {config.NOTES_DIR}")
        return
    elif com in config.FILE_SUFFIX:
        stoday = today.strftime("%b-%Y")
        filename = f"{com}-{stoday}.txt"
    elif com == "":
        stoday = today.strftime("%d-%b-%Y")
        filename = f"{stoday}.txt"
    if text:
        write_note(filename,text)
    else:
        system(f"{config.EDITOR} {config.NOTES_DIR}/{filename}")

if __name__=="__main__":
    main()
