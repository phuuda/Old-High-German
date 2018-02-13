import os
import re
import numpy as np
import sklearn.cluster
from Levenshtein import distance

path = "Old-High-German-master/ahd-texts/texts/"

def getTexts(path):
    texts = []
    for filename in os.listdir(path):
        if "idea" not in filename and ".txt" in filename:
            with open(path + filename, "r", encoding="utf-8") as f:
                texts.append(f.read())
    return texts

def removeTagged(texts):
    new_texts = []
    for text in texts:
        new_text = re.sub("<.+?>.+?</.+?>", "", text)
        new_texts.append(new_text)
    return (new_texts)

def tokenizeTexts(texts):
    tokenized_texts = []
    stop_sybols = "№1234567890"
    stop_words = ["page", "sentence", "verse"]
    for text in texts:
        tokens = []
        for word in text.split():
            if not any(st in word for st in stop_sybols):
                word = word.lower()
                word = re.sub("[\«\»\!<>\?,\.\(\)\[\]\";:\\/]", "", word)
                word = re.sub("_", " ", word)
                if len(word) > 0 and word not in stop_words:
                    tokens.append(word)
        tokenized_texts.append(tokens)
    return tokenized_texts

texts = getTexts(path)
texts = removeTagged(texts)

tokenized_texts = tokenizeTexts(texts)

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
