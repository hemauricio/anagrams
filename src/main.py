from anagram import anagrams

def main(word):
    return anagrams(word)

if __name__ == '__main__':
    word = input('Feed me a word: ')
    main(word.lower())
