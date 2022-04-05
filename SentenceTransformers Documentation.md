# SentenceTransformers Documentation

[SentenceTransformers Documentation — Sentence-Transformers documentation (sbert.net)](https://www.sbert.net/#:~:text=SentenceTransformers is a Python framework for state-of-the-art sentence%2C,%2F text embeddings for more than 100 languages.)

## Installation

You can install it using pip:

```
pip install -U sentence-transformers
```

We recommend **Python 3.6** or higher, and at least **PyTorch 1.6.0**. See [installation](https://www.sbert.net/docs/installation.html) for further installation options, especially if you want to use a GPU.

## Usage

The usage is as simple as:

```
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

#Our sentences we like to encode
sentences = ['This framework generates embeddings for each input sentence',
    'Sentences are passed as a list of string.',
    'The quick brown fox jumps over the lazy dog.']

#Sentences are encoded by calling model.encode()
embeddings = model.encode(sentences)

#Print the embeddings
for sentence, embedding in zip(sentences, embeddings):
    print("Sentence:", sentence)
    print("Embedding:", embedding)
    print("")
```