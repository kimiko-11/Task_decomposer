 
import streamlit as st
from model import TaskDecomposer
from utils import extract_steps, to_json

st.set_page_config(
    page_title="Task Decomposer",
    page_icon="🧩",
    layout="centered"
)

st.title("🧩 LLM Task Decomposition Agent")

task = st.text_input("Enter a task:")

if st.button("Generate"):
    if task.strip():
        decomposer = TaskDecomposer()

        with st.spinner("Generating..."):
            raw_output = decomposer.generate_steps(task)
            steps = extract_steps(raw_output)

        if not steps:
            st.error("Could not extract steps. Showing raw output:")
            st.write(raw_output)
        else:
            st.subheader("Step-by-Step Plan")

            for i, step in enumerate(steps, 1):
                st.write(f"{i}. {step}")

            json_output = to_json(task, steps)
            st.subheader("JSON Output")
            st.code(json_output, language="json")

    else:
        st.warning("Please enter a task")