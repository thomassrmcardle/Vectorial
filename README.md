# Vectorial
This is Vectorial, a word vectorisation algorithm, which can generate vectors for words based on training data.

**How it works**
---
The algorithm is fairly simple by design. When a new word is appended to the dataset, the following steps are taken:
- A random vector is generated for the word (this acts as a placeholder and helps spread out the data)
- When trained with data, the vector adapts, shifting closer to or further from other words accordingly.
- Later, this data can be accessed at any time.
