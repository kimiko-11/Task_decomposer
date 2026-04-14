from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class TaskDecomposer:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

    def generate_steps(self, task):
        prompt = f"List 5 clear steps to {task}."

        inputs = self.tokenizer(prompt, return_tensors="pt")

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=150,
            temperature=0.7
        )

        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return result