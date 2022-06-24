# -*- coding: utf-8 -*-

from itertools import permutations
from math import factorial
from pyrae import dle
import sys
import json

PROGRESS_MSG = 'Permutations assessed so far:'
FINAL_MSG = 'permutations reviewed in total.'
RAE_LINK = 'https://dle.rae.es/?id={id}'


# We don't need any logs.
dle.set_log_level('NOTSET')

def meanings(permutations):
    """
    Generator to yield the any matches.
    """

    i = 0
    for permutation in permutations:

        i += 1

        word = ''.join(permutation)

        # itertools.permutations returns each
        # permutation as an array of characters.
        # We need to join them
        meaning = dle.search_by_word(word=word)

        if not meaning: # can be None
            meaning = {}
        else:
            meaning = meaning.to_dict()

        articles = meaning.get('articles', [])

        for article in articles:

            definitions = article.get('definitions', [])

            yield {
                '_permutation_number': i,
                'permutation': word,
                'keyword_rae': meaning.get('title').split('|')[0], # yikes. RAE's fault.
                'definitions': [definition.get('sentence', {}).get('text',
                                            'Woops, something went wrong')
                                            for definition in definitions],
                'link': RAE_LINK.format(id=article.get('id'))}

        # I wanted to create something like a 'progress bar'.
        # Calculating percentage based on the number of the permutation
        # is more complicated than just printing the number of the permutation.
        # I chose to use carriage return to avoid spamming the terminal.
        sys.stdout.write(PROGRESS_MSG + str(i) + '\r')
        sys.stdout.flush()

    print(i, FINAL_MSG)

def anagrams(word):
    _permutations = permutations(word)

    print('Calculating', factorial(len(word)), 'permutations')

    for meaning in meanings(_permutations):

        # yikes, it's easier than using log10 to get the number of digits in the number.
        characters_to_clean = len(PROGRESS_MSG) + len(str(meaning.get('_permutation_number', 0)))

        # HACK: RAE sometimes returns words without any meaning, or just
        # short definitions.
        # (e.g. https://dle.rae.es/-oma?m=form).
        # In this case, the meaning is shorter than the 29 + len(# of permutation)
        # characters I print for the 'progress bar'. Causing funny output.
        # Just to be sure I 'clean' the line.
        sys.stdout.write((' ' * characters_to_clean) + '\r')
        sys.stdout.flush()

        print(json.dumps(meaning, indent=2))
