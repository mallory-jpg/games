
from collections import Counter
import operator


class HighScoringWords:
    # the maximum number of items that can appear in the leaderboard
    MAX_LEADERBOARD_LENGTH = 100
    MIN_WORD_LENGTH = 3  # words must be at least this many characters long
    letter_values = {}
    valid_words = []

    def __init__(self, validwords='auticon/wordlist.txt', lettervalues='auticon/letterValues.txt'):
        """
        Initialise the class with complete set of valid words and letter values by parsing text files containing the data
        :param validwords: a text file containing the complete set of valid words, one word per line
        :param lettervalues: a text file containing the score for each letter in the format letter:score one per line
        :return:
        """
        with open(validwords) as f:
            self.valid_words = f.read().splitlines()

        with open(lettervalues) as f:
            for line in f:
                (key, val) = line.split(':')
                self.letter_values[str(key).strip().lower()] = int(val)

    def build_leaderboard_for_word_list(self):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOAD_LENGTH words from the complete set of valid words.
        :return: The list of top words.
        """
        # list of top-scoring words
        top_words = []

        # while length of list is less than or equal to 100 words
        while len(top_words) <= self.MAX_LEADERBOARD_LENGTH:
            all_words = {}
            for word in self.valid_words:
                # intialize counter
                word_score = 0
                # QA print(word)
                # minimum word length
                if len(word) >=3:
                    for letter in word:
                        points = self.letter_values[letter]
                        word_score += points
                    # adding word and score to all_words dictionary
                    all_words[word] = word_score

            # sorting words by word score
            sorted_by_value = dict(
                sorted(all_words.items(), key=operator.itemgetter(1), reverse=True))
            # adding the high scoring words to the top_words list
            for key, value in sorted_by_value.items():
                top_words.append(key)

        return top_words
    
    
    def build_leaderboard_for_letters(self, starting_letters):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words that can be built using only the letters contained in the starting_letters String.
        The number of occurrences of a letter in the startingLetters String IS significant. If the starting letters are bulx, the word "bull" is NOT valid.
        There is only one l in the starting string but bull contains two l characters.
        Words are ordered in the leaderboard by their score (with the highest score first) and then alphabetically for words which have the same score.
        :param starting_letters: a random string of letters from which to build words that are valid against the contents of the wordlist.txt file
        :return: The list of top buildable words.
        """
        # initialize empty words list 
        viable_words = []
        # creating a list of the letters from a given string
        letters = list(starting_letters)

        # ensure word list is within desired length
        while len(viable_words) <= self.MAX_LEADERBOARD_LENGTH:
            for word in self.valid_words:
                count = 1
                # create dictionary using Counter built-in library
                l_count = Counter(word)
                # QA print(l_count)
                # iterate through dictionary
                for key in l_count:
                    # only counting letters that are in the starting_letters list
                    if key not in letters:
                        count = 0
                    else:
                        # making sure to match the number of letters
                        if letters.count(key) != l_count[key]:
                            count = 0
                # add to list if count is correct
                if count == 1:
                    viable_words.append(word)

            return sorted(viable_words)

# w = HighScoringWords()
# w.build_leaderboard_for_word_list()
# w.build_leaderboard_for_letters('asdlkfjna')
