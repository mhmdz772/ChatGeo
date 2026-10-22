# ChatGeo 🌍🤖

**ChatGeo** is an interactive, privacy-focused geographical AI assistant. Powered by a local Llama 3 model, ChatGeo uses custom system guardrails to strictly answer questions about world geography, physical and political features, cartography, and earth sciences—politely declining any out-of-scope topics.

---

### ✨ Key Features

* **Strict Geographical Guardrails:** Employs targeted system prompting to ensure the assistant exclusively answers geography and cartography questions while refusing non-geographical prompts.
* **Local LLM Execution:** Runs fully local inference using Llama 3 via Ollama (no external API keys or cloud dependencies needed).
* **Interactive Chat UI:** Built with Streamlit for a smooth chat experience featuring real-time response streaming.
* **Session Context:** Preserves full conversation history within active sessions for natural, multi-turn dialogues.

---

### 💻 Tech Stack

* **Language:** Python
* **UI Framework:** Streamlit
* **LLM Engine:** Ollama
* **Model:** Llama 3

---

### 🚀 Getting Started

#### 1. Prerequisites
Ensure you have [Ollama](https://ollama.com/) installed on your machine, then download the Llama 3 model:
```
ollama pull llama3
```
#### 2. Python Dependencies
```
pip install streamlit ollama
```
#### 3. Run the application
```
streamlit run app.py
```
