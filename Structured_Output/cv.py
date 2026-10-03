from langchain_core.prompts import PromptTemplate

template=PromptTemplate(
    template=(
        """My name is  Mahir Tajuar Akash. I am a Computer Science graduate with two years
    of experience working as a Machine Learning Engineer.

    I have experience with Python, PyTorch, TensorFlow, Scikit-learn,
    FastAPI, Docker, Kubernetes, MLflow, and AWS. I have built machine
    learning pipelines, deployed deep learning models, and developed
    REST APIs for AI applications.

    I also have experience working with LangChain and Retrieval-Augmented
    Generation (RAG) systems.

    My main strength is my ability to build complete machine learning
    systems from data preprocessing to deployment. However, I have limited
    experience managing large engineering teams and need to improve my
    system design skills.

    Education:
    BSc in Computer Science and Engineering.
"""
    )
)

template.save('cv.json')