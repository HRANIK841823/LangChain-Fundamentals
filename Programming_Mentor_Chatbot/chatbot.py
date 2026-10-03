
import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableParallel

from schemas import ProgrammingResponse

from prompts import (
    ANSWER_PROMPT,
    EXPLANATION_PROMPT,
    COMPLEXITY_PROMPT,
    CONCEPTS_PROMPT,
    DIFFICULTY_PROMPT,
    FOLLOWUP_PROMPT,
    FINAL_PROMPT,
)


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()


# ============================================================
# MODEL
# ============================================================

model = ChatGroq(
    model=os.getenv("GROQ_MODEL"),
    temperature=0,
)


# ============================================================
# PYDANTIC STRUCTURED OUTPUT MODEL
# ============================================================

structured_model = model.with_structured_output(
    ProgrammingResponse
)


# ============================================================
# OUTPUT PARSER
# ============================================================

parser = StrOutputParser()


# ============================================================
# DOMAIN CHAIN FACTORY
# ============================================================

def create_domain_chain(domain: str):

    # --------------------------------------------------------
    # STEP 1:
    # Add the selected domain to the user's input
    # --------------------------------------------------------

    prepare_input = lambda x: {
        "question": x["question"],
        "domain": domain
    }


    # --------------------------------------------------------
    # STEP 2:
    # RunnableParallel
    #
    # All of these execute from the SAME input simultaneously.
    # --------------------------------------------------------

    parallel_chain = RunnableParallel(

        # Preserve original question
        question=lambda x: x["question"],

        # Preserve selected domain
        domain=lambda x: x["domain"],

        # Generate answer
        answer=(
            ANSWER_PROMPT
            | model
            | parser
        ),

        # Generate explanation
        explanation=(
            EXPLANATION_PROMPT
            | model
            | parser
        ),

        # Generate complexity
        complexity=(
            COMPLEXITY_PROMPT
            | model
            | parser
        ),

        # Generate concepts
        concepts=(
            CONCEPTS_PROMPT
            | model
            | parser
        ),

        # Generate difficulty
        difficulty=(
            DIFFICULTY_PROMPT
            | model
            | parser
        ),

        # Generate follow-up question
        follow_up=(
            FOLLOWUP_PROMPT
            | model
            | parser
        ),
    )


    # --------------------------------------------------------
    # STEP 3:
    # Combine parallel results and convert them into
    # Pydantic structured output
    # --------------------------------------------------------

    final_chain = (
        parallel_chain
        | FINAL_PROMPT
        | structured_model
    )


    # --------------------------------------------------------
    # STEP 4:
    # Complete domain chain
    # --------------------------------------------------------

    return (
        prepare_input
        | final_chain
    )


# ============================================================
# DOMAIN CHAINS
# ============================================================

python_chain = create_domain_chain(
    "Python Programming"
)


ml_chain = create_domain_chain(
    "Machine Learning and Artificial Intelligence"
)


web_chain = create_domain_chain(
    "Web Development and Web APIs"
)


general_chain = create_domain_chain(
    "General Computer Science"
)


# ============================================================
# ROUTING FUNCTIONS
# ============================================================

def is_python_question(inputs):

    question = inputs["question"].lower()

    keywords = [
        "python",
        "pandas",
        "numpy",
        "list comprehension",
        "tuple",
        "dictionary",
        "pip",
        "virtual environment",
        "pycharm",
        "python function",
        "python class",
        "python loop",
    ]

    return any(
        word in question
        for word in keywords
    )


# ------------------------------------------------------------
# Machine Learning / AI
# ------------------------------------------------------------

def is_ml_question(inputs):

    question = inputs["question"].lower()

    keywords = [
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "neural network",
        "cnn",
        "rnn",
        "lstm",
        "transformer",
        "random forest",
        "decision tree",
        "regression",
        "classification",
        "clustering",
        "gradient descent",
        "overfitting",
        "underfitting",
        "feature scaling",
        "feature engineering",
        "pytorch",
        "tensorflow",
        "scikit-learn",
        "sklearn",
        "cross validation",
        "ensemble",
        "nlp",
        "natural language processing",
        "word2vec",
        "tokenization",
        "embedding",
    ]

    return any(
        word in question
        for word in keywords
    )


# ------------------------------------------------------------
# Web Development
# ------------------------------------------------------------

def is_web_question(inputs):

    question = inputs["question"].lower()

    keywords = [
        "html",
        "css",
        "javascript",
        "react",
        "fastapi",
        "django",
        "flask",
        "rest api",
        "api",
        "http",
        "get request",
        "post request",
        "put request",
        "delete request",
        "frontend",
        "backend",
        "node",
        "nodejs",
        "express",
        "expressjs",
        "vite",
        "nextjs",
        "next.js",
        "web development",
        "web application",
        "authentication",
        "jwt",
        "oauth",
        "cors",
    ]

    return any(
        word in question
        for word in keywords
    )


# ============================================================
# RUNNABLE BRANCH
# ============================================================

chatbot = RunnableBranch(

    # --------------------------------------------------------
    # Branch 1: Python
    # --------------------------------------------------------

    (
        is_python_question,
        python_chain
    ),

    # --------------------------------------------------------
    # Branch 2: Machine Learning / AI
    # --------------------------------------------------------

    (
        is_ml_question,
        ml_chain
    ),

    # --------------------------------------------------------
    # Branch 3: Web Development
    # --------------------------------------------------------

    (
        is_web_question,
        web_chain
    ),

    # --------------------------------------------------------
    # Default Branch
    # --------------------------------------------------------

    general_chain
)


# ============================================================
# MAIN CHATBOT FUNCTION
# ============================================================

def ask_chatbot(question: str) -> ProgrammingResponse:

    result = chatbot.invoke(
        {
            "question": question
        }
    )

    return result

