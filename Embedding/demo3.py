from langchain_huggingface import HuggingFaceEndpointEmbeddings


embedding=HuggingFaceEndpointEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")


document=[
    "I love AI",
    "I love Machine Learning",
    "I Love Deep Learning"
]

vector=embedding.embed_documents(document)

print(len(vector))
print(vector[0])