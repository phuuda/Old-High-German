import os

path = "/Users/Valeriya/Desktop/workshop/texts/"


def getTexts(path):
    texts = []
    for filename in os.listdir(path):
        if 'idea' not in filename and '.txt' in filename:
            with open(path + filename, "r", encoding="utf-8") as f:
                texts.append(f.read())
    return texts


def removeLatineLines(texts):  # тут надо доработать или поменять на удаление по тегу, если теги будут
    new_texts = []
    stop_words = [" lat.", " p."]  # можно римские цифры ещё регуляркой находить
    for text in texts:
        new_lines = []
        for line in text.split("\n"):
            if not any(stop_word in line for stop_word in stop_words):
                new_lines.append(line)
        new_texts.append("\n".join(new_lines))
    return (new_texts)


def tokenizeTexts(texts):
    tokenized_texts = []

    stop_sybols = [u'№', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9', u'0']

    chars_to_remove = [u'«', u'»', u'!', u'<', u'>', u'?', u',', u'.', u'(', u')', u'[', u']', u'"', u';', u':', u'/',
                       u'\\']
    dd = {ord(c): "" for c in chars_to_remove}
    dd[ord(u"_")] = " "

    stop_words = ["page", "sentence", "verse"]

    for text in texts:
        tokens = []
        for word in text.split():
            if not any(st in word for st in stop_sybols):
                word = word.translate(dd).lower()
                if len(word) > 0 and word not in stop_words:
                    tokens.append(word)
        tokenized_texts.append(tokens)

    return tokenized_texts


texts = getTexts(path)

texts = removeLatineLines(texts)

tokenized_texts = tokenizeTexts(texts)

import numpy as np
import sklearn.cluster
from Levenshtein import distance

tokenized_texts_flat = [item for sublist in tokenized_texts for item in sublist]
words = list(set(tokenized_texts_flat))
words = np.asarray(words) #So that indexing with a list will work
lev_similarity = -1*np.array([[distance(w1, w2) for w1 in words] for w2 in words])

affprop = sklearn.cluster.AffinityPropagation(affinity="precomputed", damping=0.5)
affprop.fit(lev_similarity)
for cluster_id in np.unique(affprop.labels_):
    exemplar = words[affprop.cluster_centers_indices_[cluster_id]]
    cluster = np.unique(words[np.nonzero(affprop.labels_==cluster_id)])
    cluster_str = ", ".join(cluster)
    print(" - *%s:* %s" % (exemplar, cluster_str))
