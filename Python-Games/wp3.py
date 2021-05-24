# Word Puzzle V3
# Word Puzzle is a game in which the user must guess a random word
# by entering guesses for its letters

import uagame
import random

# creates a 500x600 graphical window
def create_window():
    window = uagame.Window('Word Puzzle', 500, 600)
    return window

# displays multi-line instructions line-by-line
def display_instructions(window, instructions, string_coords):
    for line in instructions:
        window.draw_string(line, 0, string_coords[1])
        string_coords[1] += window.get_font_height()

# displays the answer so far
def display_puzzle_string(window, puzzle, string_coords):
    blanks = ' '.join(puzzle)
    window.draw_string('The answer so far is '+blanks, 0, string_coords[1])
    string_coords[1] += window.get_font_height()

# displays the number of guesses left and takes a guess from the user
def get_guess(window, num_guesses, string_coords):
    num_string = str(num_guesses)
    guess = window.input_string('Guess a letter ('+num_string+' guesses remaining): ',0,string_coords[1])
    string_coords[1] += window.get_font_height()    
    return guess

# if the user's guess is correct and not already guessed, updates the puzzle
def update_puzzle_string(puzzle, answer, guess, answer_list):
    updated = False
    for i in range(len(answer_list)):
        if answer_list[i] == guess: 
            if puzzle[i] != guess:
                puzzle[i] = answer_list[i]
                updated = True           
    return (updated, puzzle)

# checks if the entire word has been guessed
def is_word_found(puzzle):
    is_win = False
    if '_' not in puzzle:
        is_win = True
    return is_win

def play_game(window, puzzle, answer, string_coords, answer_list):
    
    num_guesses = 4
    
    is_win = False
    updated = False    
    
    while (num_guesses > 0) and (is_win != True):
        guess = get_guess(window, num_guesses, string_coords)
        updated, puzzle = update_puzzle_string(puzzle, answer, guess, answer_list)
        display_puzzle_string(window, puzzle, string_coords)
        is_win = is_word_found(puzzle)
        if updated == False:
            num_guesses -= 1
    
    return is_win

def display_result(window, is_win, answer, string_coords):
    if is_win == True:
        window.draw_string('Good job! You found the word '+ answer+'!',0,string_coords[1])
    else:
        window.draw_string('Not quite, the correct word was '+answer+'. Better luck next time.',0,string_coords[1])  
    
def end_game(window, string_coords):
    window.input_string('Press enter to end the game',0,string_coords[1])
    window.close()    

def main():
    
    string_coords = [0,0]
    
    words = ['apple','banana','watermelon','kiwi','pineapple','mango']
    answer = random.choice(words)
    answer_list = list(answer)
           
    # create list of blanks
    puzzle = []
    for i in answer_list:
        puzzle.append('_')        

    window = create_window()
    
    # set font size and colour
    window.set_font_size(18)
    window.set_font_color('white')
    
    # instructions
    instructions = [
        "I'm thinking of a secret word.",
        "Try and guess the word. You can guess one letter",
        "at a time. Each time you guess I will show you",
        "which letters have been correctly guessed and which",
        "letters are still missing. You will have 4 guesses to",
        "guess all of the letters. Good luck!",
        ]    
    
    display_instructions(window, instructions, string_coords)
    
    # display random word
    display_puzzle_string(window, puzzle, string_coords)
    
    is_win = play_game(window, puzzle, answer, string_coords, answer_list)
    
    display_result(window, is_win, answer, string_coords)
    string_coords[1] += window.get_font_height()    
    end_game(window, string_coords)
    
main()