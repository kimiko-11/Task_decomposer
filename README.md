# 🧩 LLM-Based Task Decomposition Agent

## 📌 Overview
This project is a Streamlit-based AI application that converts high-level user tasks into structured, step-by-step execution plans using a Large Language Model (LLM).  

Example:
> Input: "Build an object detection system"  
> Output: 5 clear actionable steps

The system uses Hugging Face transformer models and prompt engineering to generate structured task breakdowns.

---

## 🚀 Features
- Converts natural language tasks into step-by-step plans
- Generates structured JSON output
- Simple Streamlit UI for interaction
- Lightweight and CPU-friendly implementation
- Supports general task planning (ML / CV / software tasks)

---

## 🧠 Models Used

### 1. Primary Model
- **Model:** `google/flan-t5-base`
- **Type:** Seq2Seq Transformer (Text-to-Text)
- **Library:** Hugging Face Transformers
- **Purpose:** Generates structured step-by-step task decomposition

---

## ⚙️ Tech Stack
- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- Regular Expressions (for parsing output)
- JSON (for structured output)

---

## 🧱 System Pipeline
