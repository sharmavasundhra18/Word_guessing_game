#importing required packages
import random
from nltk.corpus import wordnet as wn

import nltk                        # ]
#------------------------------------------------------> DELETE THESE LINES AFTER FIRST RUN
nltk.download('wordnet') # ]

all_nouns = []
for synset in wn.all_synsets('n'):
    all_nouns.extend(synset.lemma_names())

#random word selecor
chosen_word= random.choices(all_nouns)

#extracting the word
final_word= chosen_word.pop(0)

#converting the word in a list
list1= []
for i in final_word:
    list1.append(i)

#seperate list for blanks
list2=[]
for i in range(len(final_word)):
    list2.append("_")
print(', '.join(map(str, list2)))

#main program
while True:
    guess= input("Enter your guess : ")
    if guess==final_word:
        print("You won! The word is ",final_word)
        break
    elif guess=="quit":
        print("The word was",final_word)
        break
    else:
        if len(guess) == len(final_word):
            for x in guess:
                if x in list1:
                    letter = list1.index(x)
                    list2.pop(letter)
                    list2.insert(letter, x)
        else:
            print("Word length not matched. Try again")
                
    print(', '.join(map(str, list2)))

#Thankyou!
