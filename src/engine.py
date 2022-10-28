
def top_k_recomm(sim_mat, keys, liked_key, k):
    # ! liked_key may not exists
    course_index = keys[keys == liked_key].index.values[0]
    
    similar_courses = list(enumerate(sim_mat[course_index]))
    sorted_similar_courses = sorted(
        similar_courses,
        key=lambda x:x[1], reverse=True
    )
    idx = [i for i, _ in sorted_similar_courses]
    course_list = keys.iloc[idx]
    return course_list[1:1+k].values.tolist()
