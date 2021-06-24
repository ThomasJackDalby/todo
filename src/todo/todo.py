import os, re

DEFAULT_FOLDER_PATH = "."

class Task:
    def __init__(self, id, description, state):
        self.id = id
        self.description = description
        self.state = state

class TaskState:

def init():
    print("init")

def new():
    pass

def __load():
    if not os.path.exists(DEFAULT_FOLDER_PATH):
        os.mkdir(DEFAULT_FOLDER_PATH)

    for file_name in os.listdir(DEFAULT_FOLDER_PATH):
        if not file_name.endswith(".task"):
            continue
        load_file(file_name)

def load_file(file_path):
    with open(file_path, "r", newline="") as file:
        lines = [line.strip() for line in file.readlines()]

    current_state = None
    current_tag = None
    tasks = []
    for line in lines:
        if line.startswith("#"): # set state
            current_state = line[1:].strip().upper()
        elif line.startswith("!#"): # unset state
            current_state = None
        elif line.startswith("-"):
            line = line[1:].strip()
            match = next(re.finditer("\[\d+\]", line), None)
            if match is not None:
                task_id = match.group(0)[1:-1]
                line = line[:match.start(0)-1] + line[match.end(0):]
            task_description = line
            tasks.append(Task(task_id, task_description, current_state))

    for task in tasks:
        print(task.id, task.description, task.state)

if __name__ == "__main__":
    import sys
    if len(sys.argv) <= 1:
        print("Please provide a command")
    else:
        __load()

        command = sys.argv[1]