#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random 
from colorama import Fore
import sys

i=1
j=1
k=1
count=0

def repeat_game():
    f=str(input("Do you wnat to Play again (Yes or No ):"))
    if (f.lower() == "yes"):
        first_stage(count)
    else:
        sys.exit()
            
def first_stage(count):
    ncount=0
    for i in range (14+1) :
        random_question=random.choice(list(gkquestion_1.keys()))
        print(Fore.BLUE, f"\nYour {i} Question is...\n{random_question}")
        a=str(input("Enter the Answer for the Question (Yes or No):"))
        answer=gkquestion_1.get(random_question, "Question not found in dictionary")
        del gkquestion_1[random_question]
        if (a.lower()==answer.lower()) :
            print(Fore.RED+"congrats you get one point")
            count+=1
            if(count==4):
                 print("Your are close to the second stage")
            elif (count==5):
                print(Fore.RED+"\nCongrats you reach the Second stage of the GAME")
                print("Congrats you got a MAP in the MAP there is way to find the KEY and TREASURE")
                second_stage(count)
        else :
            print(Fore.BLACK+"Your answer is wrong")
            print(Fore.BLACK+"Come on you definately got the map try it")
            ncount+=1
            if (ncount>10):
                print("Sorry you loss the game")
                repeat_game()
                
def second_stage(count):
    for j in range (14+1) :
        ncount=0
        random_question=random.choice(list(gkquestion_2.keys()))
        print(Fore.BLUE, f"\nYour {j} Question is...\n{random_question}")
        b=str(input("Enter the Answer for the Question (Yes or No):"))
        answer=gkquestion_2.get(random_question,"Question not found in dictionary")
        del gkquestion_2[random_question]
        if (b.lower()==answer.lower()) :
            print(Fore.RED+"congrats your get one point")
            count+=1
            if(count==10):
                print("Come on two stpes ahead of success")
            elif(count==12):
                print(Fore.RED+"\nCongrats you reach the Third stage of the GAME")
                print("Congarts you got a key")
                third_stage(count)

        else :
            print(Fore.BLACK+"Your answer is Wrong")
            ncount+=1
            print("Come on don't loose your hope try again, read the question clearly and answer correctly")
            if ( ncount >7):
                print("Sorry you lose in the game")
                repeat_game()
            

def third_stage(count):
    for k in range (15):
        ncount=0
        random_question=random.choice(list(gkquestion_3.keys()))
        print(Fore.BLUE, f"\nYour {k} Question is...\n{random_question}")
        c=str(input("Enter the Answer for the Question (Yes or No):"))
        answer=gkquestion_3.get(random_question,"Question not found in dictionary")
        del gkquestion_3[random_question]
        if (c.lower()==answer.lower()) :
            print(Fore.RED+"congrats your get one point")
            count+=1
            if (count==21):
                print(Fore.RED+"congrats You found Treasure")
                repeat_game()
          
        else:
            print(Fore.BLACK+"Your answer is wrong")
            print("Come on actually you complete 2 stages this stage also you will complete. Read the question clearly and answwer it")
            ncount+=1
            if(ncount>5):
                print("Sorry you lose in the game")
                repeat_game()
                
print(Fore.RED+"ENIGMA-Text based Game")


print(Fore.RED +'''             ENIGMA- A TEXT BASED GAME
        Rules and Regulations of the Game :
        1. Totally there are three stages in the game\n
        2. The goal is to find the Treasure\n
        3. There are 3 levels based on difficulty\n
        4. For level ONE you have to answer 5 question correctly out of 10\n
        5. For level TWO you have to answer 7 question correctly out of 10\n
        6. For level THREE you have to answer 9 question correctly out of 10\n
        7. If you finish Level ONE you will get a map and a key which will lead you to the treasure\n
        8. If you finish Level TWO you get a KEY\n
        9. IF you finish Level THREE you get a TREASURE\n
        10. ALL QUESTIONS ARE YES OR NO TYPE\n''')



gkquestion_1 = {
    "Is the Earth round?": "Yes",
    "Is water composed of hydrogen and oxygen?": "Yes",
    "Is the Great Wall of China visible from space?": "No",
    "Is the Eiffel Tower located in London?": "No",
    "Is the sun a star?": "Yes",
    "Is the currency of Japan called the Yen?": "Yes",
    "Is Mount Everest the tallest mountain in the world?": "Yes",
    "Is Antarctica the driest continent on Earth?": "Yes",
    "Is a tomato a fruit?": "Yes",
    "Is the Statue of Liberty located in Paris?": "No",
    "Is the Earth flat?": "No",
    "Do humans breathe oxygen?": "Yes",
    "Is water wet?": "No",
    "Is the sun a planet?": "No"
}

gkquestion_2 =  {
    "Is photosynthesis the process by which plants convert sunlight into energy?": "Yes",
    "Is the Andromeda Galaxy the closest spiral galaxy to our Milky Way?": "Yes",
    "Is the concept of Schrödinger's cat related to quantum mechanics?": "Yes",
    "Is the Taj Mahal built entirely of marble?": "Yes",
    "Is the Hubble Space Telescope primarily used to observe planets in our solar system?": "No",
    "Is the Louvre Museum located in Barcelona?": "No",
    "Is the C programming language developed by Dennis Ritchie?": "Yes",
    "Is the Caspian Sea the world's largest saltwater lake?": "Yes",
    "Is Marie Curie the only person to have won Nobel Prizes in two different scientific fields?": "Yes",
    "Is Antarctica the coldest continent on Earth?": "Yes",
    "Is the moon larger than Earth?": "No",
    "Is a computer an example of a mechanical machine?": "No",
    "Is English the most widely spoken language in the world?": "No",
    "Is the concept of 'Habeas Corpus' related to the right to a fair trial?": "Yes"
}

gkquestion_3 = {
    "Is the Riemann Hypothesis the only unsolved problem from Hilbert's list of 23 mathematical problems?": "No",
    "Is the Planck constant used to define the kilogram in the International System of Units (SI)?": "Yes",
    "Is the Double Slit Experiment a key demonstration of quantum physics wave-particle duality?": "Yes",
    "Is Gödel's Incompleteness Theorem a fundamental result in the philosophy of mathematics?": "Yes",
    "Is the Poincaré Conjecture a famous problem in the field of topology?": "Yes",
    "Is the Drake Equation used to estimate the number of active, communicative extraterrestrial civilizations in the Milky Way galaxy?": "Yes",
    "Is the concept of the Fermi Paradox related to the apparent contradiction between the high probability of extraterrestrial life and the lack of evidence for, or contact with, such civilizations?": "Yes",
    "Is the Casimir Effect a physical phenomenon where closely spaced parallel plates experience an attractive force due to quantum fluctuations in vacuum energy?": "Yes",
    "Is the concept of 'non-Euclidean geometry' a departure from the geometry developed by Euclid in his Elements?": "Yes",
    "Is the Monty Hall Problem a probability puzzle involving choosing doors with hidden prizes?": "Yes",
    "Is a light-year a unit of time?": "No",
    "Is the human brain the largest brain in the animal kingdom?": "No",
    "Is aluminum the most abundant metal in the Earth's crust?": "Yes",
    "Is the process of photosynthesis carried out by animals?": "No",
    "Is a light wave a transverse wave?": "Yes",
}

first_stage(count)



# In[ ]:





# In[ ]:





# In[ ]:




