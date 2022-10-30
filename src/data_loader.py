import pandas as pd
import json
import requests

SCHEDGO_URL = "https://api-dev.schedgo.com/"


def get_from_csv(path):
    df = pd.read_csv(path, sep=",")
    return df


def fetch_SchedGo(config, college, term):
    """get courses data from SchedGo
    NOTE: this function is INCOMPLETE
    as for now, it only gets the first 10 courses
    since getting all is very slow

    Args:
        config (dict): CF-Access credentials
        college (str): name of college
        term (int): quarter (e.h. 202301)

    Returns:
        List[dict]: all opening courses
    """
    subjects = fetch_subject_list(config, college=college)

    # wouldn't it be nice if we have currying :(
    def get_subj(subj_code):
        return fetch_subject(config, college, term, subj_code)

    # result = map (\subj -> get_subj(subj["code"])) subjects
    # result = reduce (\a, b -> a + b) result
    # ToDo use concurrent map as shown above
    # this concurrency should work since a fetch (GET) should have no side effect
    # https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.map
    result = []
    for subj in subjects[:10]:
        response = get_subj(subj["code"])
        result += response

    return result


def fetch_subject(config, college, term, subject, limit=1000):
    """get all opening courses for given college, term, and subject

    Args:
        config (dict): CF-Access credentials
        college (str): name of college
        term (int): quarter (e.g. 202301)
        subject (str): code of a subject (ECS)
        limit (int, optional): limit of amount of courses. Defaults to 1000.

    Returns:
        List[dict]: the courses' information
    """
    req_str = SCHEDGO_URL + "colleges/{college}/terms/{term}/courses?subjects={subject}&limit={limit}".format(
        college=college,
        subject=subject,
        term=term,
        limit=limit
    )

    r = requests.get(req_str, headers=config)
    return r.json()


def fetch_subject_list(config, college):
    """get a list of all subjects for given college

    Args:
        config (dict): CF-Access credentials
        college (str): name of college

    Returns:
        List[dict]: subjects with code and name
    """
    req_str = SCHEDGO_URL + "colleges/{college}".format(college=college)

    r = requests.get(req_str, headers=config)
    subjects = r.json()["subjects"]
    return subjects
