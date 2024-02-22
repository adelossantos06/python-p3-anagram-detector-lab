# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        matches = []
        for word in possible_anagrams:
             if sorted(word.lower()) == sorted(self.word.lower()) and word.lower() != self.word.lower():
                matches.append(word)
        return matches