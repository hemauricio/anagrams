from itertools import permutations
from math import factorial
from pyrae import dle
import sys

# We don't need any logs.
dle.set_log_level('NOTSET')

def meanings(permutations):
    """
    Generator to yield the any matches.
    """

    i = 0
    for permutation in permutations:

        # itertools.permutations returns each
        # permutation as an array of characters.
        # We need to join them
        m = dle.search_by_word(word=''.join(permutation)).to_dict()

        articles = m.get('articles', [])

        for article in articles:

            definitions = article.get('definitions', [])

            yield (m.get('title').split('|')[0], # yikes. RAE's fault.
                    [definition.get('sentence', {}).get('text',
                        'Woops, something went wrong')
                            for definition in definitions])

        i += 1
        # I wanted to create something like a 'progress bar'.
        # Calculating percentage based on the number of the permutation
        # is more complicated than just printing the number of the permutation.
        # I chose to use carriage return to avoid spamming the terminal.
        sys.stdout.write('Permutations assessed so far:' + str(i) + '\r')
        sys.stdout.flush()

    print(i, 'permutations reviewed in total.')

def anagrams(word):
    _permutations = permutations(word)

    print('Calculating', factorial(len(word)), 'permutations')

    for meaning in meanings(_permutations):
        if meaning:
            # HACK: RAE sometimes returns words without any meaning.
            # They're in the dictionary but there's no meaning available.
            # (e.g. https://dle.rae.es/-oma?m=form).
            # In this case, the meaning is shorter than the 30 characters I
            # print for the 'progress bar'. Causing funny output.
            # Just to be sure I 'clean' the line.
            sys.stdout.write(' '*30 + '\r')
            sys.stdout.flush()
            print(meaning)
