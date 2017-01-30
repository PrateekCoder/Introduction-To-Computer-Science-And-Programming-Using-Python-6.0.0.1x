'''
Valid Words
10.0/10.0 points (graded)
At this point, we have written code to generate a random hand and display that hand to the user. We can also ask the user for a word (Python's raw_input) and score the word (using your getWordScore). However, at this point we have not written any code to verify that a word given by a player obeys the rules of the game. A valid word is in the word list; and it is composed entirely of letters from the current hand. Implement the isValidWord function.

Testing: Make sure the test_isValidWord tests pass. In addition, you will want to test your implementation by calling it multiple times on the same hand - what should the correct behavior be? Additionally, the empty string ('') is not a valid word - if you code this function correctly, you shouldn't need an additional check for this condition.

Fill in the code for isValidWord in ps4a.py and be sure you've passed the appropriate tests in test_ps4a.py before pasting your function definition here.

Canopy specific instructions: If you modify code in ps4a.py go to

Run -> Restart Kernel (or hit the CTRL with the dot on your keyboard)

before running test_ps4a.py. You have to do this every time you modify the file ps4a.py and want to run the file test_ps4a.py, otherwise changes to the former will not be incorporated in the latter.
'''

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    letters = getFrequencyDict(word)

    for i in letters:
        if letters[i] > hand.get(i, 0):
            return False

    return word in wordList