'''
Computer Chooses a Word
15.0/15.0 points (graded)
**Part B is dependent on your functions from ps4a.py, so be sure to complete ps4a.py before working on ps4b.py**

Now that you have completed your word game code, you decide that you would like to enable your computer (SkyNet) to play the game (your hidden agenda is to prove once and for all that computers are inferior to human intellect!) In Part B you will make a modification to the playHand function from part A that will enable this to happen. The idea is that you will be able to compare how you as a user succeed in the game compared to the computer's performance.

It is your responsibility to create the function compChooseWord(hand, wordList, n). Pseudocode is provided in the file ps4b.py.

If you follow the pseudocode, you'll create a computer player that is legal, but not always the best. Once you've implemented it following our approach, feel free to try your own approach! As much as we'd love to give you credit for making an improved compChooseWord function, we hope you can understand our automatic grading facilities are limited in their ability to accept differing solutions.
'''

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
     # Create a new variable to store the maximum score seen so far (initially 0)
    best_score = 0

    # Create a new variable to store the best word seen so far (initially None)
    best_word = None  

    # For each word in the wordList
    for word in wordList:

        if isValidWord(word,hand,wordList):
            # Find out how much making that word is worth
            this_score = getWordScore(word,n)
            # If the score for that word is higher than your best score
            if this_score > best_score:
                # Update your best score, and best word accordingly
                best_score = this_score
                best_word = word

    # return the best word you found.
    return best_word
