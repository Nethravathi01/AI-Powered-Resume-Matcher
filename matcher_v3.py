
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer, util

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
model = SentenceTransformer('all-MiniLM-L6-v2')


def clean_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    return " ".join(tokens)

def calculate_tfidf_score(resume, jd):
    texts = [clean_text(resume), clean_text(jd)]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)
    score = (vectors[0] @ vectors[1].T).toarray()[0][0] * 100
    return round(score, 2)

def calculate_sentence_similarity(resume, jd):
    embeddings = model.encode([resume, jd], convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item() * 100
    return round(similarity, 2)

def extract_keywords(text, top_n=10):
    text = clean_text(text)
    important_skills = ["python", "excel", "sql", "mysql", "powerbi", "html", "css", "javascript", "numpy", "pandas",
                        "matplotlib", "flask", "api", "node.js", "react", "angular", "msword", "powerpoint", "git",
                        "github", "vscode", "pycharm", "linux", "data analysis", "data visulaization"]
    found_skills = [skill for skill in important_skills if skill.lower() in text]
    return found_skills[:top_n]


def recommend_skills(jd_keywords, resume_keywords):
    return list(set(jd_keywords) - set(resume_keywords))





