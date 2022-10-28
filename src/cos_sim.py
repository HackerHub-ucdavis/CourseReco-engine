from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def cos_similarity(description):
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(description)
    cosine_sim = cosine_similarity(count_matrix)
    return cosine_sim
