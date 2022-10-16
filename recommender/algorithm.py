import numpy as np
from numpy import ndarray


def standardize(user: ndarray) -> ndarray:
    """
    Standardized the user data so that it centers around 0 and has variance of 1
    :param user: 1d data vector of user
    :return: standardized data vector
    """
    return (user - np.mean(user)) / np.var(user)


def get_unit_vector(user: ndarray) -> ndarray:
    """
    Get unit vector of the user data
    :param user: 1d data vector of user
    :return: normalized data vector
    """
    return user / np.linalg.norm(user)


def normalize(user: ndarray) -> ndarray:
    """
    Apply min-max normalization to the user data
    :param user: 1d data vector of user
    :return: normalized data vector
    """
    return (user - np.amin(user)) / np.ptp(user)


def weight_data(user: ndarray, weight: ndarray) -> ndarray:
    """
    Apply weight to the user data
    :param user: 1d data vector of user
    :param weight: 1d vector with the weight of each element
    :return: a weighted 1d user data vector
    """
    return np.multiply(user, weight)


def match_score(user1: ndarray, user2: ndarray, metric: str = "euclidean") -> float:
    """
    Calculate the similarity between two user data, cosine similarity does not need to be normalized
    :param user1: 1d data vector of user 1
    :param user2: 1d data vector of user 2
    :param metric: string that specify the type of similarity would like to calculate, default as euclidean
    :return: float that shows the similarity between two vectors, for euclidean distance the lower the better
    , for cosine similarity the higher the better
    """
    if metric == "euclidean":
        return np.linalg.norm(user1 - user2)
    elif metric == "cosine":
        return np.dot(user1, user2) / (np.linalg.norm(user1) * np.linalg.norm(user2))
    elif metric == "dot":
        return float(np.dot(user1, user2))


def get_match_score(user1: ndarray, weight1: ndarray, user2: ndarray, weight2: ndarray) -> float:
    """
    An all-in-one function that accepts two raw user data and give similarity between them
    :param user1: 1d raw data vector of user 1
    :param weight1: 1d vector with the weight of each element for user 1
    :param user2: 1d raw data vector of user 2
    :param weight2: 1d vector with the weight of each element for user 2
    :return: similarity score represented as euclidean distance or cosine similarity
    """
    return match_score(weight_data(standardize(user1), weight1), weight_data(standardize(user2), weight2))


if __name__ == "__main__":
    user1 = np.array([1, 2, 3])
    user2 = np.array([4, 5, 6])
    print(match_score(user1, user2, metric="euclidean"))
    print(standardize(np.array([1, 3, 5, 7, 9])))
    print(normalize(user1))
