from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text, jd_text):
    embeddings = OpenAIEmbeddings()

    resume_vec = embeddings.embed_query(resume_text)
    jd_vec = embeddings.embed_query(jd_text)

    score = cosine_similarity([resume_vec], [jd_vec])[0][0]

    return round(score * 100, 2)