import json
import re

def extract_steps(text):
    steps = []
    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if re.match(r"^\d+[\).\s-]", line):
            step = re.sub(r"^\d+[\).\s-]*", "", line)
            steps.append(step)

    return steps


def to_json(task, steps):
    return json.dumps({
        "task": task,
        "steps": steps
    }, indent=4)