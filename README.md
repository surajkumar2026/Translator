#  Language Translator using LangChain & Groq

This is a simple yet powerful language translation web application built using **LangChain**, **Groq**, and **Streamlit**. It leverages the `Gemma2-9b-It` language model hosted on the Groq platform to provide accurate translations in real-time. The user can input any text and select a target language for translation via an interactive Streamlit interface.

 **Live Demo**: [Click here to use the Translator App](https://translator-langchain-groq.streamlit.app/)

---

##  Features

*  Translate text into multiple languages.
*  Fast and lightweight thanks to the Groq inference engine.
*  Built with LangChain's modular chain interface.
*  Clean and minimal UI built using Streamlit.

---

##  Tech Stack

* **Python** – Backend logic
* **LangChain** – For chaining prompts, model calls, and output parsing
* **Groq** – Hosting and running the `Gemma2-9b-It` model
* **Streamlit** – UI framework for creating interactive web apps
* **Dotenv** – Secure management of API keys

---

##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/surajkumar2026/Translator.git
cd Translator
```

### 2. Create and Activate a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the App Locally

```bash
streamlit run app.py
```

---

## Example Usage

### Input

* Text: `"How are you?"`
* Language: `German`

### Output

* Translated Text: `"Wie geht es dir?"`

---

