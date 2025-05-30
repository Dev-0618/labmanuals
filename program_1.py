# -*- coding: utf-8 -*-
"""Program 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1adWN_WTYZVKp3eue1USYiOynLOWngSOM

Explore pre-trained word vectors.

  
  

1.   Explore word relationships using vector arithmetic.
2.   Perform arithmetic operations and analyze results.
"""

import gensim.downloader as api
import numpy as np

word_vectors = api.load("word2vec-google-news-300")

def vector_arithmetic(word1, word2, word3):
    result_vector = word_vectors[word1] - word_vectors[word2] + word_vectors[word3]
    similar_words = word_vectors.most_similar([result_vector], topn=5)
    return similar_words

# Example: "King - Man + Woman"
print("Result of 'king - man + woman':")
print(vector_arithmetic("king", "man", "woman"))

def find_similar_words(word):
    return word_vectors.most_similar(word, topn=5)

print("\nWords similar to 'computer':")
print(find_similar_words("computer"))

"""This code demonstrates how to work with **pre-trained Word2Vec word embeddings** using the `gensim` library. Word2Vec is a model that represents words as numerical vectors in a high-dimensional space, allowing for various linguistic computations such as similarity checks and arithmetic operations.

### **Loading the Word2Vec Model**
The script starts by importing `gensim.downloader` and `numpy`. The `gensim` library provides an easy way to download and use pre-trained models. In this case, the **Google News 300-dimensional Word2Vec model** is loaded. This model has been trained on a massive corpus of text (Google News, containing about 100 billion words), and it represents each word as a **300-dimensional vector**.

### **Word Vector Arithmetic**
The core idea behind Word2Vec is that similar words have similar vector representations. Moreover, relationships between words can be represented mathematically. The function `vector_arithmetic(word1, word2, word3)` performs the following operation:

          word1−word2+word3

This means that the vector for `word1` is adjusted by subtracting `word2` and adding `word3`. The result is a new vector that is then compared to existing word vectors to find the most similar words.

For example, **"king - man + woman"** is expected to return **"queen"** because the difference between "king" and "man" is conceptually similar to the difference between "queen" and "woman."

### **Finding Similar Words**
The function `find_similar_words(word)` takes a word as input and retrieves the **top 5 most similar words** based on cosine similarity. Cosine similarity measures how close two word vectors are in the multi-dimensional space.

For example, when searching for words similar to **"computer"**, we might get results like:
- **"computers"**
- **"laptop"**
- **"PC"**
- **"workstation"**
- **"server"**

These results make sense because these words are commonly associated with "computer."

### **Key Observations**
1. **Semantic Meaning in Vector Space**: The model captures relationships between words, allowing for meaningful transformations such as "Paris - France + Italy = Rome."
2. **Pre-Trained Model Usage**: The Google News Word2Vec model is widely used for NLP tasks due to its large vocabulary and training on real-world data.
3. **Potential Biases**: Since the model is trained on news articles, it may inherit certain biases from the training data.
4. **Errors with Out-of-Vocabulary Words**: If a word is not present in the model’s vocabulary, an error will be raised.

### **Applications**
This approach is widely used in:
- **Chatbots**: To find contextually relevant responses.
- **Search Engines**: To retrieve related search terms.
- **Recommendation Systems**: To suggest similar items based on textual data.
- **Machine Translation**: To understand word relationships across languages.

"""



!python -m spacy download en_core_web_md

import spacy

# Load medium-sized word vector model
nlp = spacy.load("en_core_web_md")

# Function to get vector arithmetic
def vector_arithmetic_spacy(word1, word2, word3):
    vec = nlp(word1).vector - nlp(word2).vector + nlp(word3).vector
    most_similar = sorted(nlp.vocab, key=lambda w: w.vector @ vec, reverse=True)[:5]
    return [w.text for w in most_similar]

print("Result of 'king - man + woman' using spaCy:")
print(vector_arithmetic_spacy("king", "man", "woman"))

# Find similar words
def find_similar_spacy(word):
    token = nlp(word)
    return [w.text for w in sorted(nlp.vocab, key=lambda w: token.similarity(nlp(w.text)), reverse=True)[:5]]

print("\nWords similar to 'computer' using spaCy:")
print(find_similar_spacy("computer"))

"""This code demonstrates how to use **spaCy** to perform word vector arithmetic and find similar words using pre-trained word embeddings. Unlike `gensim`, which loads Word2Vec models, `spaCy` provides built-in word vector representations, making it a powerful alternative for NLP tasks.

### **Loading the spaCy Model**
The script begins by importing `spacy` and loading the **"en_core_web_md"** model. This is a medium-sized English model that includes **300-dimensional word vectors**, trained on a large corpus. Unlike `gensim`, which downloads external models, `spaCy` comes with its own pre-trained embeddings.

### **Word Vector Arithmetic**
The function `vector_arithmetic_spacy(word1, word2, word3)` performs the following operation:

                    word1−word2+word3

This means:
- The vector representation of `word2` is subtracted from `word1`, effectively removing its influence.
- The vector of `word3` is then added to adjust the meaning accordingly.
- The resulting vector is compared with all words in `spaCy`'s vocabulary to find the most similar matches.

For example, the expression **"king - man + woman"** should ideally return **"queen"**, as the difference between "king" and "man" is conceptually similar to the difference between "queen" and "woman."

To find the closest words, the function sorts all vocabulary words based on their **dot product similarity** with the computed vector. The top 5 most similar words are then returned.

### **Finding Similar Words**
The function `find_similar_spacy(word)` takes a single word and finds the **top 5 most similar words** based on **cosine similarity**.

- `token.similarity(nlp(w.text))` computes the similarity between the given word and each word in `spaCy`’s vocabulary.
- The results are sorted in descending order to return the most relevant words.

For example, if we search for words similar to **"computer"**, we might get:
- **"computers"**
- **"laptop"**
- **"PC"**
- **"workstation"**
- **"server"**

### **Key Observations**
1. **Built-in spaCy Word Embeddings**: Unlike `gensim`, which requires downloading external models, `spaCy` provides word vectors directly within its language models.
2. **Efficient Vector Arithmetic**: This method allows for meaningful transformations, similar to **Word2Vec**.
3. **Bias in Model Data**: Since embeddings are pre-trained on large corpora, they may inherit biases.
4. **Vocabulary Limitations**: If a word is **out-of-vocabulary (OOV)**, `spaCy` might not provide accurate vectors.

### **Applications**
- **Text Similarity**: Finding words related to a given term.
- **Recommendation Systems**: Suggesting similar items based on text.
- **Semantic Search**: Enhancing search engines with context-aware results.
- **Chatbots & NLP Assistants**: Understanding word relationships.
"""

from transformers import AutoTokenizer, AutoModel
import torch

# Load BERT model
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

# Get embeddings
def get_embedding(text):
    tokens = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**tokens)
    return outputs.last_hidden_state.mean(dim=1)  # Sentence embedding

# Cosine similarity
def cosine_similarity(vec1, vec2):
    return torch.nn.functional.cosine_similarity(vec1, vec2).item()

word1, word2 = "king", "queen"
sim = cosine_similarity(get_embedding(word1), get_embedding(word2))
print(f"Similarity between {word1} and {word2} using BERT: {sim:.4f}")

"""This code demonstrates how to use **BERT (Bidirectional Encoder Representations from Transformers)** to compute **word embeddings** and measure their similarity using **cosine similarity**. Unlike traditional word embedding models like Word2Vec and GloVe, BERT generates **contextualized embeddings**, meaning the vector representation of a word depends on its surrounding context.

---

### **Loading the BERT Model**
The script begins by importing necessary libraries from the **Hugging Face Transformers** library and **PyTorch**. Then, it loads the **BERT-base (uncased)** model and its corresponding tokenizer:

1. **AutoTokenizer**: Converts text into tokenized input suitable for BERT.
2. **AutoModel**: Loads the pre-trained BERT model, which will generate contextual word embeddings.

The model used here is `"bert-base-uncased"`, which is a 12-layer transformer trained on a large corpus of English text.

---

### **Generating Word Embeddings**
The function `get_embedding(text)` processes a given word or sentence through BERT to generate an embedding:

1. **Tokenization**: Converts the input text into tokenized format suitable for BERT (`return_tensors="pt"` produces PyTorch tensors).
2. **Model Processing**: The tokenized input is fed into the BERT model.
3. **Extracting Embeddings**: The model returns multiple embeddings (one per token in the sequence). Since BERT is designed to process sentences, the function computes the **mean** of all token embeddings to get a single **sentence-level representation**.

> 🔹 Unlike Word2Vec or spaCy embeddings, BERT **does not** provide static word embeddings. The same word can have different embeddings depending on its context.

---

### **Computing Cosine Similarity**
The function `cosine_similarity(vec1, vec2)` calculates the **cosine similarity** between two vectors. This measures how similar two word embeddings are:

cosine similarity=  A⋅B / ∣∣A∣∣×∣∣B∣∣


- A value **close to 1** indicates high similarity.
- A value **close to 0** suggests no similarity.
- A value **close to -1** suggests opposite meanings.

---

### **Example Execution**
The script then compares the similarity between `"king"` and `"queen"`:

1. The function `get_embedding("king")` retrieves the BERT-generated vector for `"king"`.
2. Similarly, `get_embedding("queen")` retrieves the vector for `"queen"`.
3. The cosine similarity between these two vectors is calculated and printed.

A high similarity score (e.g., **0.8 - 0.9**) would indicate that BERT understands **"king" and "queen"** as related words.

---

### **Key Observations**
1. **Contextualized Embeddings**: Unlike Word2Vec, where "bank" always has the same vector, BERT considers **context** (e.g., "river bank" vs. "money bank").
2. **Sentence-Level Meaning**: BERT’s embeddings represent **full sentences**, not just individual words.
3. **Transformer-Based Power**: Instead of predicting the next word (like Word2Vec), BERT is **bidirectional**, meaning it considers both left and right contexts when encoding a word.

---

### **Applications**
✅ **Semantic Search**: Finding documents that match a user query based on meaning rather than exact words.  
✅ **Chatbots & NLP Assistants**: Understanding the true intent behind user messages.  
✅ **Text Classification**: Grouping similar documents or emails based on content.  
✅ **Machine Translation**: Mapping words with contextual meaning rather than just dictionary-based translations.

---

### **Limitations**
- **Computational Cost**: BERT is much heavier than Word2Vec, requiring **more memory and processing power**.
- **Not a Traditional Word Embedding Model**: Unlike Word2Vec or GloVe, BERT embeddings change depending on the **sentence context**.

---

### **Conclusion**
This approach shows how BERT can be leveraged for **semantic similarity tasks** using transformer-based embeddings. It is **far more powerful than traditional word vectors** and can be used for **advanced NLP applications** like **question answering, text generation, and recommendation systems**. 🚀

---

### **Which One Should You Use?**
| Library     | Strengths | Best Use Case |
|------------|----------|---------------|
| **Gensim** | Fast, Large pretrained models | Word relationships |
| **spaCy** | Lightweight, easy API | General NLP tasks |
| **Transformers (BERT, GPT)** | Context-aware | Sentence similarity |
"""