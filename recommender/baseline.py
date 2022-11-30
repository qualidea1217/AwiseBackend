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


def get_match_score(user1: ndarray, weight1: ndarray, user2: ndarray, weight2: ndarray,
                    preprocess: str = "normalize") -> float:
    """
    An all-in-one function that accepts two raw user data and give similarity between them
    :param preprocess: specify the type of data preprocessing, can be either normalize or standardize
    :param user1: 1d raw data vector of user 1
    :param weight1: 1d vector with the weight of each element for user 1
    :param user2: 1d raw data vector of user 2
    :param weight2: 1d vector with the weight of each element for user 2
    :return: similarity score represented as euclidean distance or cosine similarity
    """
    processed_user1 = None
    processed_user2 = None
    weighted_data1 = weight_data(user1, weight1)
    weighted_data2 = weight_data(user2, weight2)
    if preprocess == "normalize":
        processed_user1 = normalize(weighted_data1)
        processed_user2 = normalize(weighted_data2)
    elif preprocess == "standardize":
        processed_user1 = standardize(weighted_data1)
        processed_user2 = standardize(weighted_data2)
    output = match_score(processed_user1, processed_user2)
    return output


def get_num_similarity(num1: int | float, num2: int | float) -> float:
    """
    Calculate similarity between two numbers
    :param num1: number
    :param num2: umber
    :return: similarity range between 0 and 1
    """
    if num1 == num2:
        return 1
    else:
        return min(num1, num2) / max(num1, num2)


def get_top_3_field(user1: ndarray, user2: ndarray) -> list[list[str, float]]:
    """
    Calculate the similarity of each individual field without weight and return the top three field
    :param user1: data without weight
    :param user2: data without weight
    :return: list of top 3 field, each element is a list that the 1st element is the name of the field, the 2nd element
    is the similarity
    """
    lookup_table = {
        0: "getup_time",
        1: "bed_time",
        2: "social",
        3: "academic",
        4: "bring_people",
        5: "animal",
        6: "instrument",
        7: "cleaning",
        8: "cook",
        9: "share",
        10: "smoke",
        11: "alcohol"
    }
    similarity_array = [[lookup_table[i], get_num_similarity(user1[i], user2[i])] for i in range(len(user1))]
    similarity_array.sort(key=lambda x: x[1], reverse=True)
    return similarity_array[:3]
