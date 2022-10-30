from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def cos_similarity(description):
    """compute similarity matrix

    Args:
        description (pd.Series): the description of all courses

    Returns:
        ndarray of shape (n_description, n_description): the cos similarity matrix
    """
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(description)
    cosine_sim = cosine_similarity(count_matrix)
    return cosine_sim
