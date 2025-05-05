print("Welcome to Hangman Game")
import random
words=["REALMADRID","BARCELONA","LIVERPOOL","CHELSEA"]
word=random.choice(words)
total_chances=7
guessed_word="_"*len(word)
while total_chances!=0:
 print(guessed_word)
 letter=input("Enter the letter : ").upper()
 if letter in word:
   for a in range (len(word)):
    if word[a]==letter:
     guessed_word=guessed_word[:a]+letter+guessed_word[a+1:]
   if guessed_word==word:
    print("Congratulations")
    print("You got it")
    print("The word is : ",word)
    break
  
 else:
   total_chances=total_chances-1
   print("Incorrect")
   print("Remaining chances are : ",total_chances)
else:
 print("Game over")
 print("All chances are finished")
 print("The word was : ",word)