""" Import Python modules """
import pyfiglet 
import colorama
from colorama import Fore, Back, Style, init
init()


def game_start():
    """
    Game_start function to give a welcome message for starting the quiz.
    """
    welcome = pyfiglet.figlet_format("Welcome To The Quiz World !")
    print(welcome)

    ans = input(Fore.GREEN + "ARE YOU READY TO PLAY? (Y/N)\n")
    print(Style.RESET_ALL)
    if ans != "Y":
        quit()


game_start()


""" Creating variables from q1 to q10 which includes questions and choices,
that will act as key in dictionary named questions.
"""

q1 = """1. Because its cells has mitochondria,which of your muscles never tires?
a. Tongue
b. Triceps
c. Heart
d. Gluteus Maximus
"""
q2 = """2. The paper-thin tympanic membrane can be found in what body part?
a. Ear
b. Colon
c. Lungs
d. Throat
"""
q3 = """3. Which of these body parts has the most bones?
a. Rib-cage
b. Foot
c. Skull
d. Hand
"""
q4 = """4. Where are red blood cells created?
a. Brain
b. Heart
c. Spleen
d. Bones
"""
q5 = """5. Which of these body parts continue to get bigger with age?
a. Ear
b. Thumb
c. Spine
d. Femur
"""
q6 = """6. The funny bone is actually what type of body-part?
a. Nerve
b. Muscle
c. Bone
d. Organ
"""
q7 = """7. How many bones are there in human body?
a. 260
b. 206
c. 150
d. 200
"""
q8 = """8. What does mucus do?
a. Filters out harmful bacteria.
b. Helps in smell
c. Helps your lungs take in oxygen
d. Stops your nose from collapsing
"""
q9 = """9. The most common eye color in the world is:
a. Brown
b. Blue
c. Green
d. Hazel
"""
q10 = """10. How many muscles do you use when you talk?
a. 45
b. 55
c. 72
d. 87
"""

"""
Created a dictionary with q1 to q10 as 'key' and correct answer as 'value'
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
    """
    The play_game function displays the questions and user has to choose the correct answer.
    """
    print(Fore.GREEN + Style.BRIGHT + "There are 10 questions with 4 choices (a,b,c,d)\n")
    print(Fore.GREEN + Style.BRIGHT + "Please select one choice and enter your answer.\n")
    print(Fore.GREEN + Style.BRIGHT + "You get 10 points for each correct answer!\n")
    print(Style.RESET_ALL)

    start = pyfiglet.figlet_format("LET'S BEGIN!!!", font = "digital")
    print(start)

    valid_answers = ['a', 'b', 'c', 'd']
    """
    Creating a variable so that anything entered 
    apart from the choices returns as invalid.
    """

    for question in questions:
        print(question)
        print("-------------------------------")
        
        while True:
            answer = input(Fore.BLUE + "Enter the correct answer a/b/c/d:\n")
            print(Style.RESET_ALL)
            if answer in valid_answers:
                if answer == questions[question]:
                    print(Fore.GREEN + "CORRECT ANSWER. You get 10 points!")
                    print(Style.RESET_ALL)
                    break
                else:
                    print(Fore.RED + "INCORRECT ANSWER!!!!")
                    print(Style.RESET_ALL)
                    break
        else:
            print(Fore.RED + "INVALID ANSWER!")
            continue  

play_game()


def get_score():
    

