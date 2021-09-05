#importing aaltu faltu samaan
import random
import nltk
from nltk.corpus import wordnet as wn
all_nouns = []
for synset in wn.all_synsets('n'):
    all_nouns.extend(synset.lemma_names())

#ek random sa word
chosen_word= random.choices(all_nouns)

#word ko extract
final_word= chosen_word.pop(0)

#word ko converting in list
list1= []
for i in final_word:
    list1.append(i)

#seperate list for blanks
list2=[]
for i in range(len(final_word)):
    list2.append("_")
print(list2)

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
        for x in guess:
            if x in list1:
                letter = list1.index(x)
                list2.pop(letter)
                list2.insert(letter, x)
                print(list2)

            

                
            
