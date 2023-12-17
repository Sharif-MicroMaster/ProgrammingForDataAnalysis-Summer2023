import re
import numpy as np

n = int(input().strip())
strings = []
for _ in range(n):
    res = re.sub(r'[^\w\s]', '', input().strip())
    strings.append(res)

query = re.sub(r'[^\w\s]','',input().strip())
strings.append(query)

words = [string.split() for string in strings]

vocab = set(words[0])
for i in range(1, n + 1):
    vocab = vocab.union(set(words[i]))

vocab = list(vocab)

vectors = [np.zeros(len(vocab), dtype=float) for _ in range(n + 1)]

for i in range(n + 1):
    for word in words[i]:
        j = vocab.index(word)
        vectors[i][j] += 1

def cosine_similarity(va, vb):
    return np.dot(va,vb)

query = vectors[n]

similarities = []
for i in range(n):
    similarities.append(cosine_similarity(vectors[i], query))
    
similarities = np.array(similarities)

print(similarities.argmax() + 1)