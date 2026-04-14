from model import TaskDecomposer
from utils import extract_steps, to_json

def main():
    task = input("Enter your task: ")

    decomposer = TaskDecomposer()
    raw_output = decomposer.generate_steps(task)

    steps = extract_steps(raw_output)
    json_output = to_json(task, steps)

    print("\n--- Generated Steps ---")
    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")

    print("\n--- JSON Output ---")
    print(json_output)


if __name__ == "__main__":
    main()
