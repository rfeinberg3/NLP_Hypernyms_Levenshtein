# NLP_Hypernyms_Levenshtein
Python solutions for extracting hypernyms using Hearst patterns and calculating Levenshtein edit distance between strings.

## Problems Solved

### Problem 1: Extracting Hypernyms Using Hearst Patterns

**Function:** `problem1(NPs, S)`

**Description:**
- **Input:**
  - `NPs`: A list of noun phrases, where each string is a lowercase noun phrase.
  - `S`: A string containing arbitrary text and symbols.
- **Output:** 
  - A set of tuples representing hypernyms found in the string `S`. Each tuple is in the form `(hypernym, hyponym)`, where both elements are noun phrases from the list `NPs`.

**Details:**
- The function uses regular expressions to find hypernym-hyponym relationships in the text `S` based on predefined Hearst patterns.
- The noun phrases may appear capitalized in `S`, and the function will match them accordingly.
- Example: If "dog" and "mammal" are in `NPs` and the text `S` contains "a dog is a mammal", the function will extract `('mammal', 'dog')`.

### Problem 2: Calculating Levenshtein Edit Distance

**Function:** `problem2(s1, s2)`

**Description:**
- **Input:**
  - `s1`: The first string.
  - `s2`: The second string.
- **Output:**
  - An integer representing the Levenshtein edit distance between `s1` and `s2`.

**Details:**
- The function calculates the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one string into the other.
- This is implemented without using any libraries that directly provide the edit distance algorithm.

## Usage

To use the functions, simply import the `NLP_Hypernyms_Levenshtein.py` module and call the desired function with appropriate arguments. For example:

```python
from NLP_Hypernyms_Levenshtein import problem1, problem2

# Example usage of problem1
noun_phrases = ["dog", "mammal"]
text = "A dog is a mammal."
hypernyms = problem1(noun_phrases, text)
print(hypernyms)  # Output: {('mammal', 'dog')}

# Example usage of problem2
string1 = "kitten"
string2 = "sitting"
distance = problem2(string1, string2)
print(distance)  # Output: 3
