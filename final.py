import os 

def choose_word():
    word = ["programming"]
    return word[0]  

def show_hidden_word(word, guessed_letters):
    hidden = ""
    for letter in word:
        if letter in guessed_letters:
            hidden += letter
        else:
            hidden += "_"
    return hidden

def hangman_game():
    word = choose_word()
    remaining_attempts = 6
    guessed_letters = []
    
    print("¡Welcome to the 'hangman' game!")
    print("guess the word:")
    print (show_hidden_word(word, guessed_letters))
    
    while True:
        if remaining_attempts == 0:
            print("¡Oh no! you've run out of attempts. The word was:", word)
            break
        
        letter = input("Enter a letter: ").lower()
        os.system('cls')
        
        if letter in guessed_letters:
            print("You have already guessed that letter. Try another one.")
            continue
        
        guessed_letters.append(letter)
        
        if letter not in word:
            remaining_attempts -= 1
            print("Incorrect. You have", remaining_attempts, "attempts left.")
        else:
            print("¡Correct!")
        
        word_shown = show_hidden_word(word, guessed_letters)
        print(word_shown)
        
        if "_" not in word_shown:
            print("¡Congratulations!. You guessed the word correctly.")
            break
        
        continuar = input("Do you want to play again? (yes/no): ").lower()
        if continuar != "yes":
            print("¡Thanks for participating!")
            break

if __name__ == "__main__":
    hangman_game()