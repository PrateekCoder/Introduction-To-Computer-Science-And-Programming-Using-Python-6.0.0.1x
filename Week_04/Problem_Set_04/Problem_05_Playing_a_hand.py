'''
Playing a Hand
15.0/15.0 points (graded)
In ps4a.py, note that in the function playHand, there is a bunch of pseudocode. This pseudocode is provided to help guide you in writing your function. Check out the Why Pseudocode? resource to learn more about the What and Why of Pseudocode before you start coding your solution.

Note: Do not assume that there will always be 7 letters in a hand! The parameter n represents the size of the hand.
'''

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # Keep track of the total score
    score = 0
    
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
    
        # Display the hand
        print "Current Hand: ",
        displayHand(hand)

        # Ask user for input
        word = raw_input('Enter word, or a "." to indicate that you are ' +
            'finished: ')
        
        # If the input is a single period:
        if word == ".":
            # End the game (break out of the loop)
            break

        # Otherwise (the input is not a single period):
        else:

            # If the word is not valid:
            if not isValidWord(word, hand, wordList):
            
                # Reject invalid word (print a message followed by blank line)
                print "Invalid word, please try again.\n"

            # Otherwise (the word is valid):
            else:
                word_score = getWordScore(word, n)
                score += word_score
                # Tell the user how many points the word earned, and the 
                # updated total score, in one line followed by a blank line
                print '"' + word + '" earned', word_score, "points. Total:", \
                    score, "points.\n"
                
                # Update the hand 
                hand = updateHand(hand, word)
                

    
    if word == ".":
        print "Goodbye! Total score:", score, "points.\n"
    else:
        print "Run out of letters. Total score:", score, "points.\n"

