# Anagrams [RAE](https://www.rae.es/).

Get the anagrams in Spanish of any word.


### Requirements
```
pip install -r requirements.txt
```

### Usage
```
$ python3 src/main.py
Feed me a word: <YOUR WORD HERE>
```

After entering the word you'll get a summary of how many permutations of the word will be calculated and searched by  meaning.
```
Calculating N permutations
```

You'll see a progress message saying how many permutations have been assessed.

```
Permutations assessed so far: m
```

In case of a match, a json will be printed with the following format.

```
{
  '_permutation_number': <PERMUTATION NUMBER>,
  'permutation': <PERMUTATION>,
  'keyword_rae': <RAE's KEYWORD>,
  'definitions': <LIST OF DEFINITIONS>,
  'link': <DIRECT LINK TO DEFINITION>
}
```

Once it finishes, an ending message will be displayed.
```
N permutations reviewed in total.
```

Please be mindful of the complexity of the algorithm.

#### NOTE: The Spanish Royal Academy's dictionary (RAE) is used for this.

Note to future self: This can be improved, as multiple instances of any letter will
generate *n* repeated permutations with *n* being the number of duplicate letters
in the word.
