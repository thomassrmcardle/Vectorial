# Vectorial
This is Vectorial, a word vectorisation algorithm, which can generate vectors for words based on training data.

Within this repository, there is also a fun, simple demonstration of the applications of such an algorithm, with a simple word-guessing game, using sine difference to guide the user into guessing the write word, telling them which guess had the "closest meaning", according to the algorithm.

*How it works*
The algorithm is fairly simple by design. When a new word is appended to the dataset, the following steps are taken:
- A random vector is generated for the word (this acts as a placeholder and helps spread out the data)
- When trained with data, the vector adapts, shifting closer to or further from other words accordingly.
- Later, this data can be accessed at any time.
