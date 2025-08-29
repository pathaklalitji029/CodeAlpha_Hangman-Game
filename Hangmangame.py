import random
#categories with words
categories={
    "Fruits":["apple","orange","grapes","banana","pineapple"],
    "Animals":["tiger","lion","elephant","monkey","dog"],
    "Cars":["toyota","bmw","audi","tata","mahindra"]
}

#hangman stages
stages=[
    """
       ------
       |    |
       |    o
       |   /|\\
       |   / \\
       |
    """,
        """
       ------
       |    |
       |    o
       |   /|\\
       |   / 
       |
    """,
        """
       ------
       |    |
       |    o
       |   /|\\
       |   
       |
    """,
        """
       ------
       |    |
       |    o
       |   /|
       |   
       |
    """,
        """
       ------
       |    |
       |    o
       |    |
       |   
       |
    """,
        """
       ------
       |    |
       |    o
       |   
       |  
       |
    """,
        """
       ------
       |    |
       |    
       |  
       |   
       |
    """

]
def play_round(username,lives):
    "play single round of hangman.Returns True if wins,False if lose."
    category=random.choice(list(categories.keys()))
    word=random.choice(categories[category]).lower()
    word_display=["_"]*len(word)
    guessed=set()
    

    print("\nNew Round Strated")
    print(f"Hint:It's a {category}!")
        
    while lives>0 and "_"in word_display:
        print("\n"+" ".join(word_display))
        print(stages[lives if lives < len(stages) else -1])
        print(f"Wrong Guesses Left:{lives}")
        print(f"Guessed letters: {','.join(sorted(guessed)) if guessed else 'none'}")
        
        guess=input("Enter a letter: ").lower()
        if not guess.isalpha() or len(guess)!=1:
            print("please enter a single valid letter!")
            continue

        if guess in guessed:
            print("You already guessed that letter!")
            continue

        guessed.add(guess)

        if guess in word:
            for i,ch in enumerate(word):
                if ch==guess:
                    word_display[i]=guess
            print("good guess!")
        else:
            lives-=1
            print("wrong guess!")
    if "_" not in word_display:
        print("\ncongratulations! You guessed the word:",word.upper())
        return True
    else:
        print(stages[0])
        print("\nGame Over! The word was:",word.upper() )
        return False
def hangman_game():
    wins=0
    losses=0
    print("Welcome To Multi Round Hangman Game :")
    username=input("Enter Your Name: ")
    #create difficulty mode
    print("\nChoose difficulty mode:")
    print("1.Easy(8 lives)")
    print("2.Meduim(6 lives)")
    print("3.Hard( 4 lives)")
    
    while True:
        choice=input("Enter 1, 2, or 3: ")
        if choice=="1":
            lives=8
            break
        elif choice=="2":
            lives=6
            break
        elif choice=="3":
            lives=4
            break
        else:
            print("Invalid choice.Please enter 1, 2, or 3.")
    while True:
        result=play_round(username,lives)
        if result:
            wins+=1
        else:
            losses+=1
        print(f"\nScoreboard: wins={wins},losses={losses}")
        again=input("\nDo you want to play again?(y/n):").lower()
        if again != "y":
            print(f"\nThanks for playing! {username}\n Your Final Score:")
            print(f"wins:{wins},losses:{losses}")
            break

#run the game 
hangman_game()
