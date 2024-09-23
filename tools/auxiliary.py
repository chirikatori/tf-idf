import nltk
import os
from nltk.corpus import stopwords
import string


def list_docs(num_of_docs: int):
    file_list = os.listdir("data")
    file_id = [int(file_list[i].split('-')[0].strip()) for i in range(len(file_list))]  # noqa
    file_list = [file for id, file in sorted(zip(file_id, file_list))]
    if num_of_docs > len(file_list) or num_of_docs <= 0:
        print(f"num_of_docs must be >= 0 and < {len(file_list)}")
        pass
    res = []
    for i in range(num_of_docs):
        res.append(file_list[i].split('-')[1].strip().split('.txt')[0].strip())
    return [res, file_list[:num_of_docs]]


def get_article(file):
    try:
        with open(f"data/{file}", mode="r") as f:
            article = f.read()
        return article
    except Exception:
        print("Oops!!! Something went wrong")


def preprocess_article(article):
    res = []
    tokens = nltk.word_tokenize(article)
    punctuation = string.punctuation
    stopwords_list = stopwords.words("english")

    for token in tokens:
        if (token not in stopwords_list and token not in punctuation):
            res.append(token)

    return res


def extract_terms(num_of_docs: int):
    terms = []
    for file in list_docs(num_of_docs)[1]:
        article = get_article(file)
        tokens = preprocess_article(article)
        terms.extend(tokens)
    terms = list(dict.fromkeys(terms))
    return terms
