""" Import Python modules """
import pyfiglet 
import colorama
from colorama import Fore, Back, Style, init
init()


"""
Game_start function to give a welcome message for starting the quiz.
"""

def game_start():
    welcome = pyfiglet.figlet_format("Welcome To The Quiz World !")
    print(welcome)
    
    ans = input(Fore.GREEN + "Are you ready to play? (yes/no)\n").lower()
    print(Style.RESET_ALL)
    if ans != "yes":
        quit()
       
game_start()


""" Creating Quiz questions and quiz choices """

quiz_questions: {
    "Because its cells has mitochondria,which of your muscles never tires?" : "c",
    "The paper-thin tympanic membrane can be found in what body part?" : "a",
    "Which of these body parts has the most bones?" : "d",
    "Where are red blood cells created?" : "d",
    "Which of these body parts continue to get bigger with age?" : "a",
    "The funny bone is actually what type of body-part?" : "a",
    "How many bones are there in human body?" : "b",
    "What does mucus do?" : "a",
    "The most common eye color in the world is:" : "a",
    "How many muscles do you use when you talk?" : "c"
} # type: ignore


quiz_choices = [
    [
        'a. Tongue', 'b. Triceps', 'c. Heart', 'd. Gluteus Maximus'
    ],
    [
        'a. Ear', 'b. Colon', 'c. Lungs', 'd. Throat'
    ],
    [
        'a. Rib-cage', 'b. Foot', 'c. Skull', 'd. Hand'
    ],
    [
        'a. Brain', 'b. Heart', 'c. Spleen', 'd. Bones'
    ],
    [
        'a. Ear', 'b. Thumb', 'c. Spine', 'd. Femur'
    ],
    [
        'a. Nerve', 'b. Muscle', 'c. Bone', 'd. Organ'
    ],
    [
        'a. 260', 'b. 206', 'c. 150', 'd. 200'
    ],
    [
        'a. Filters out harmful bacteria.', 'b. Helps in smell ', 'c. Helps your lungs take in oxygen ', 'd. Stops your nose from collapsing'   
    ],
    [
        'a. Brown', 'b. Blue', 'c. Green', 'd. Hazel'
    ],
    [
        'a. Brown', 'b. Blue', 'c. Green', 'd. Hazel'
    ],
    [
        'a.45', 'b. 55', 'c. 72', 'd. 87'
    ]
]
"""
q10 = """ 
a. 45
b. 55
c. 72
d. 87
"""

questions = {
    q1: "c",
    q2: "a",
    q3: "d",
    q4: "d",
    q5: "a",
    q6: "a",
    q7: "b",
    q8: "a",
    q9: "a",
    q10: "c"
}

def play_game():
    return questions


def get_score():
valid_answers = ['a', 'b', 'c', 'd']
correct_answer = list(questions.values())
score = 0 

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
                print(Fore.GREEN + "Correct Answer. You get 10 points!")
                print(Style.RESET_ALL)
                score = score + 10
                print("Your current score is:", score)
                break
            else:
                print(Fore.RED + "Incorrect Answer!")
                print(Style.RESET_ALL)
                break
        else:
            print("INVALID ANSWER!")
            continue  

    """
    The quit variable when chosen, stops the game and final score is displayed.
    """
    quit = input("Do you want to quit the quiz? (yes/no):\n").lower()
    if quit == "yes":
        print("Quitting Game!")
        break
 
print("The Final Score is:", score)  





