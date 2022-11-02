from functools import reduce


def dump_csv(xs):
    """_summary_

    Args:
        xs (List[str]): a list of string to construct the csv

    Returns:
        str: csv form of this list of string
    """
    return reduce(lambda a, b: a + "," + b, xs)
