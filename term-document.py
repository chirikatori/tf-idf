import pandas as pd
from collections import Counter
from tools import list_docs, preprocess_article, get_article, extract_terms


def td_matrix(terms, docs):
    documents = [preprocess_article(get_article(file)) for file in docs]  # noqa
    term_doc_matrix = {term: [0] * len(documents) for term in terms}

    for doc_idx, article in enumerate(documents):
        word_count = Counter(article)
        for term in terms:
            term_doc_matrix[term][doc_idx] = word_count.get(term, 0)

    term_doc_matrix_list = [term_doc_matrix[term] for term in terms]
    return term_doc_matrix_list


if __name__ == "__main__":
    df = pd.DataFrame(data=td_matrix(extract_terms(50), list_docs(50)[1]),
                      index=extract_terms(50),
                      columns=list_docs(50)[0])
    df.to_csv("output/term-document.csv")
