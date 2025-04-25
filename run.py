""" Import Python modules """
import pyfiglet 
from PyInquirer import style_from_dict, prompt, Token, Separator

"""
Assigning color styles to the game's questions, answers and instructions.
"""
style = style_from_dict ({
    Token.Question : '#FFA500',   #Orange
    Token.Answer : '#008000',    #Green
    Token.Instruction : '#fff',  #White
})


"""
A welcome statement for starting the quiz and if the user
says no, the game quits, and if chooses yes to play the game, 
questions are displayed.
"""
welcome = pyfiglet.figlet_format("Welcome To The Quiz World !")
print(welcome)

ans = input("Are you ready to play? (yes/no)\n").lower()

if ans != "yes":
    quit()

score = 0

"""
Creating a dictionary of questions and the choices of answers in the form a list.
"""
questions = [
                {'type' : 'list',
                 'name' : 'mitochondria',
                 'message' : '1. Because its cells has mitochondria,which of your muscles never tires?',
                 'choices' : ['Tongue', 'Triceps', 'Heart', 'Gluteus Maximus']
                }
                {'type' : 'list',
                 'name' : 'TM',
                 'message' : '2. The paper-thin tympanic membrane can be found in what body part?',
                 'choices' : ['Ear', 'Colon', 'Lungs', 'Throat']
                }
                {'type' : 'list',
                 'name' : 'Bones',
                 'message' : '3. Which of these body parts has the most bones?',
                 'choices' : ['Rib-Cage', 'Foot', 'Skull', 'Hand']
                }
                {'type' : 'list',
                 'name' : 'RBC',
                 'message' : '4. Where are red blood cells created?',
                 'choices' : ['Brain', 'Heart', 'Spleen', 'Bones']
                }
                {'type' : 'list',
                 'name' : 'Big',
                 'message' : '5. Which of these body parts continue to get bigger with age?',
                 'choices' : ['Ear', 'Thumb', 'Spine', 'Femur']    
                }
                {'type' : 'list',
                 'name' : 'Funny-bone',
                 'message' : '6. The funny bone is actually what type of body-part?',
                 'choices' : ['Nerve', 'Muscle', 'Bone', 'Organ']  
                }
                {'type' : 'list',
                 'name' : 'Total-bones',
                 'message' : '7. How many bones are there in human body?',
                 'choices' : ['260', '206', '150', '200']  
                }
                {'type' : 'list',
                 'name' : 'Mucus',
                 'message' : '8. What does mucus do?',
                 'choices' : ['Filters out harmful bacteria.', 'Helps in smell', 'Helps your lungs take in oxygen', 'Stops your nose from collapsing']          
                }
                {'type' : 'list',
                 'name' : 'Eye-color',
                 'message' : '9. The most common eye color in the world is:',
                 'choices' : ['Brown', 'Blue', 'Green', 'Hazel']  
                }
                {'type' : 'list',
                 'name' : 'Muscles-to-talk',
                 'message' : '10. How many muscles do you use when you talk?',
                 'choices' : ['45', '55', '72', '87']  
                }
            ]



q1 = """ Because its cells has mitochondria,which of your muscles never tires?
a. Tongue
b. Triceps
c. Heart
d. Gluteus Maximus
"""
q2 = """ The paper-thin tympanic membrane can be found in what body part?
a. Ear
b. Colon
c. Lungs
d. Throat
"""
q3 = """ Which of these body parts has the most bones?
a. Rib-cage
b. Foot
c. Skull
d. Hand
"""
q4 = """ Where are red blood cells created?
a. Brain
b. Heart
c. Spleen
d. Bones
"""
q5 = """ Which of these body parts continue to get bigger with age?
a. Ear
b. Thumb
c. Spine
d. Femur
"""
q6 = """ The funny bone is actually what type of body-part?
a. Nerve
b. Muscle
c. Bone
d. Organ
"""
q7 = """ How many bones are there in human body?
a. 260
b. 206
c. 150
d. 200
"""
q8 = """ What does mucus do?
a. Filters out harmful bacteria.
b. Helps in smell
c. Helps your lungs take in oxygen
d. Stops your nose from collapsing
"""
q9 = """ The most common eye color in the world is:
a. Brown
b. Blue
c. Green
d. Hazel
"""
q10 = """ How many muscles do you use when you talk?
a. 45
b. 55
c. 72
d. 87
"""


#questions = {
    #q1: "c",
    #q2: "a",
    #q3: "d",
    #q4: "d",
    #q5: "a",
    #q6: "a",
    #q7: "b",
    #q8: "a",
    #q9: "a",
    #q10: "c"


"""
Creating a variable so that anything entered 
apart from the choices returns as invalid.
"""
valid_answers = ["a", "b", "c", "d"]
"""
Creating a for loop to iterate the question and its correct answers.
"""
for question in questions:
    print(question)
    print("------------------------")

    while True:
        answer = input("Enter the correct answer a/b/c/d: \n")
        if answer in valid_answers:
            if answer == questions[question]:
                print("Correct Answer. You get 10 points!")
                score = score + 10
                print("Your current score is:", score)
                break
            else:
                print("Incorrect Answer!")
                break
        else:
            print("INVALID ANSWER!")
            continue  

    """
    The quit variable when chosen, stops the game and final score is displayed.
    """
    quit = input("Do you want to quit the quiz? (yes/no):\n")
    if quit == "yes":
        print("Quitting Game!")
        break
 
print("The Final Score is:", score)  



