# LangChain Fundamentals

A practical collection of **LangChain fundamentals and examples** designed to understand how to build LLM-powered applications using LangChain.

This repository covers core LangChain concepts such as prompts, chat models, output parsers, LCEL, Runnables, structured outputs, and different workflow patterns.

## 🚀 Project Overview

The purpose of this repository is to learn and practice the fundamental building blocks of **LangChain** through simple, practical implementations.

It focuses on understanding how individual LangChain components work and how they can be combined to create useful AI applications and workflows.

## 📚 Topics Covered

### 1. Prompt Templates

Learn how to create reusable prompts using LangChain's prompt template system.

* `PromptTemplate`
* Dynamic prompt variables
* Reusable prompts

### 2. Chat Models

Working with LLMs through LangChain chat model integrations.

* `ChatGroq`
* Model configuration
* Temperature
* Message-based interactions

### 3. Output Parsers

Convert LLM responses into clean and usable output.

* `StrOutputParser`
* Processing model responses
* Creating structured workflows

### 4. LCEL

Understanding **LangChain Expression Language (LCEL)** and how components can be connected together.

Example workflow:

```text
Prompt → Model → Output Parser
```

### 5. Runnables

Exploring LangChain's Runnable interface and composable workflows.

Covered concepts include:

* `RunnableSequence`
* `RunnableParallel`
* `RunnableBranch`
* Runnable composition

### 6. RunnableParallel

Run multiple chains or operations in parallel and combine their results.

Example:

```text
                 ┌── Chain 1 ──┐
Input ───────────┼── Chain 2 ──┼── Combined Output
                 └── Chain 3 ──┘
```

### 7. RunnableBranch

Create conditional workflows where different chains are executed depending on the input.

Example:

```text
Input
  │
  ▼
Condition
  │
  ├── Programming → Programming Chain
  │
  ├── ML & AI → ML Chain
  │
  └── General → General Chain
```

### 8. Pydantic Structured Output

Learn how to force LLM responses into a predefined structure using **Pydantic models**.

Example:

```python
class JobApplication(BaseModel):
    name: str
    experience: Optional[int] = None
    email: EmailStr
    expected_salary: int
```

This makes LLM responses easier to validate and use inside applications.

### 9. Chat History

Working with LangChain message types and maintaining conversations.

* `HumanMessage`
* `AIMessage`
* `SystemMessage`
* Conversation history

### 10. Practical Chatbot Workflows

The concepts are combined to create practical LLM applications such as:

* AI learning mentor
* Programming mentor chatbot
* Science teacher chatbot
* Structured information extraction
* Multi-chain workflows

## 🛠️ Technologies Used

* **Python**
* **LangChain**
* **LangChain Core**
* **LangChain Groq**
* **Pydantic**
* **Streamlit**
* **Groq LLMs**
* **python-dotenv**

## 📁 Repository Structure

```text
LangChain-Fundamentals/
│
├── prompts/
│
├── models/
│
├── output_parsers/
│
├── runnables/
│   ├── runnable_sequence/
│   ├── runnable_parallel/
│   └── runnable_branch/
│
├── structured_output/
│
├── chatbots/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

> The exact folder structure may vary depending on the examples included in the repository.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/LangChain-Fundamentals.git
```

### 2. Navigate to the project

```bash
cd LangChain-Fundamentals
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Do **not** upload your `.env` file or API keys to GitHub.

Make sure `.env` is included in `.gitignore`:

```text
.env
venv/
__pycache__/
```

## ▶️ Running the Project

For Python examples:

```bash
python filename.py
```

For Streamlit applications:

```bash
streamlit run app.py
```

## 🎯 Learning Goals

Through this repository, I aim to understand:

* How LangChain components work
* How to build LLM chains
* How LCEL simplifies chain composition
* How Runnables can be combined
* How to execute multiple chains in parallel
* How to create conditional workflows
* How to generate structured LLM responses
* How to maintain conversational history
* How to build practical AI applications with LangChain

## 📌 Key Concepts

The overall workflow can be summarized as:

```text
User Input
    ↓
Prompt Template
    ↓
Chat Model / LLM
    ↓
Runnable Workflow
    ↓
Output Parser / Structured Output
    ↓
Application Response
```

## 📖 Learning Status

This repository is part of my ongoing journey of learning **Generative AI, LangChain, and LLM application development**.

More advanced topics such as **RAG, Vector Databases, Agents, Tool Calling, and LLM-powered applications** will be explored in future projects.

## 👨‍💻 Author

**Habibur Rahman Anik**

Computer Science & Engineering Student
Interested in **Machine Learning, Deep Learning, Generative AI, and LLM Application Development**.
