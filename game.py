import shutil
import random
name=input("Enter your name:")
print("I hope",name, "you will playing well")
counter=0
count=0
 
width = shutil.get_terminal_size().columns

print('=' * width)
print("Play Stone, Paper, Scissors".center(width))
print('=' * width)

procedure = input("If you want rules (press 1): ")

if procedure == '1':
    print("\nRules of Game!")
    print("Stone beats scissor")
    print("Paper beats stone")
    print("Scissor beats paper")
    print("Choose stone, paper or scissor\n")

play = 'yes'

while play == 'yes':
    
    choice = input("Enter your choice: ").lower()

    chlist = ['stone', 'paper', 'scissor']
    cchoice = random.choice(chlist)

    print("\nYour choice =", choice)
    print("Computer choice =", cchoice)

    if choice == cchoice:
        print("Match Draw!")
        
    elif (choice == 'stone' and cchoice == 'scissor') or (choice == 'paper' and cchoice == 'stone') or (choice == 'scissor' and cchoice == 'paper'):
        print("Congratulations! You Win 🎉")
        counter +=1
    elif choice in chlist:
        
        print("Computer Wins!")
        count +=1

    else:
        print("Invalid choice! Please enter stone, paper or scissor.")

    play = input("\nDo you want to play more? (yes/no): ").lower()

score=("\nThanks for playing!  see your score card")
print("Your score =",counter)
print("Computer score =",count)