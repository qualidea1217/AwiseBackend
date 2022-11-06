#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 9 14:31:00 2022

@author: chrisfeng
"""

import pandas as pd
import numpy as np
import sklearn.decomposition
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import minmax_scale
import sklearn.cluster
import sklearn.metrics

import sqlite3
import timeit
import django

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AwiseBackend.settings")


def get_cluster(userData: list, userWeight: list, userID: int):
    nparray = [np.multiply(userData[:,1:][i], userWeight[i]) for i in range(len(userData))]
    numDf = pd.DataFrame(nparray)

    # ******* PCA ***********
    normData = StandardScaler().fit_transform(numDf)
    pca = sklearn.decomposition.PCA()
    fit = pca.fit_transform(normData)

    explained = 0
    count = 0

    while explained < 0.7:
        explained += pca.explained_variance_ratio_[count]
        count += 1

    score = fit[:, 0:count]  # Keep dimensions

    calinskiScore = []

    for k in range(2, 6):
        KM = sklearn.cluster.KMeans(n_clusters=k, random_state=0).fit(score)
        labels = KM.fit_predict(score)
        calinskiScore.append(sklearn.metrics.calinski_harabasz_score(score, labels))

    KM = sklearn.cluster.KMeans(n_clusters=np.argmax(calinskiScore) + 2, random_state=0).fit(score)

    userIDX = numDf.loc[numDf[:0] == userID] 

    # Find the score
    eucDist = []
    for i in range(0, len(score) - 1):
        if i == userIDX:
            eucDist.append(None)
        eucDist.append(1 - np.linalg.norm(score[userIDX, :] - score[i, :]))

    matchScoreOut = minmax_scale(eucDist)

    # Find group
    userGroup = KM.labels_[userIDX]
    groupOut = [i for i, x in enumerate(KM.labels_) if x == userGroup]

    return matchScoreOut, groupOut

    





