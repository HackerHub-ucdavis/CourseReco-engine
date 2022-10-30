import pandas as pd
import json
import requests

SCHEDGO_URL = "https://api-dev.schedgo.com/"


def get_from_csv(path):
    df = pd.read_csv(path, sep=",")
    return df


def fetch_SchedGo(config, college, term, subjects):
    """get courses data from SchedGo

    Args:
        config (dict): CF-Access credentials
        college (str): name of college
        term (int): quarter (e.h. 202301)
        subjects (List[str]): list of course codes

    Returns:
        List[dict]: all opening courses for given subjects
    """

    # construct the GET request to SchedGo
    req_str = SCHEDGO_URL + "colleges/{college}/terms/{term}/courses?".format(
        college=college,
        term=term
    )
    for code in subjects:
        req_str += "subjects=" + code + "&"
    req_str += "limit=1000"

    r = requests.get(req_str, headers=config)
    return r.json()


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
