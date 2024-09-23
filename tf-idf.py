import math
import numpy as np
from tools import (
    list_docs,
    preprocess_article,
    extract_terms,
    get_article
)
from collections import Counter
import pandas as pd


def tf(df, documents):
    doc_lengths = np.array([len(doc) for doc in documents])
    return df/doc_lengths


def idf(terms, docs):
    num_docs = len(docs)
    doc_frequency = Counter()

    for doc in docs:
        unique_words = set(doc)
        for term in terms:
            if term in unique_words:
                doc_frequency[term] += 1

    idf_values = []
    for term in terms:
        df = doc_frequency[term]
        if df == 0:
            idf_values.append(0)
        else:
            idf_values.append(math.log(num_docs / df, math.e))

    return idf_values


def tf_idf(df, terms, docs):
    term_freq = tf(df, docs)
    return term_freq.apply(lambda row: row * idf(terms, docs), axis=0)


if __name__ == "__main__":
    df = pd.read_csv("output/term-document.csv", index_col=0)
    docs = [preprocess_article(get_article(doc)) for doc in list_docs(50)[1]]
    tf_idf(df, extract_terms(50), docs).to_csv("output/tf-idf.csv")
