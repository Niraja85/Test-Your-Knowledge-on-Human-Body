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
                {
                    'type' : 'list',
                    'name' : 'mitochondria',
                    'message' : '1. Because its cells has mitochondria,which of your muscles never tires?',
                    'choices' : ['Tongue', 'Triceps', 'Heart', 'Gluteus Maximus']
                }
                {
                    'type' : 'list',
                    'name' : 'TM',
                    'message' : '2. The paper-thin tympanic membrane can be found in what body part?',
                    'choices' : ['Ear', 'Colon', 'Lungs', 'Throat']
                }
                {
                    'type' : 'list',
                    'name' : 'Bones',
                    'message' : '3. Which of these body parts has the most bones?',
                    'choices' : ['Rib-Cage', 'Foot', 'Skull', 'Hand']
                }
                {
                    'type' : 'list',
                    'name' : 'RBC',
                    'message' : '4. Where are red blood cells created?',
                    'choices' : ['Brain', 'Heart', 'Spleen', 'Bones']
                }
                {
                    'type' : 'list',
                    'name' : 'Big',
                    'message' : '5. Which of these body parts continue to get bigger with age?',
                    'choices' : ['Ear', 'Thumb', 'Spine', 'Femur']    
                }
                {
                    'type' : 'list',
                    'name' : 'Funny-bone',
                    'message' : '6. The funny bone is actually what type of body-part?',
                    'choices' : ['Nerve', 'Muscle', 'Bone', 'Organ']  
                }
                {
                    'type' : 'list',
                    'name' : 'Total-bones',
                    'message' : '7. How many bones are there in human body?',
                    'choices' : ['260', '206', '150', '200']  
                }
                {
                    'type' : 'list',
                    'name' : 'Mucus',
                    'message' : '8. What does mucus do?',
                    'choices' : ['Filters out harmful bacteria.', 'Helps in smell', 'Helps your lungs take in oxygen', 'Stops your nose from collapsing']          
                }
                {
                    'type' : 'list',
                    'name' : 'Eye-color',
                    'message' : '9. The most common eye color in the world is:',
                    'choices' : ['Brown', 'Blue', 'Green', 'Hazel']  
                }
                {
                    'type' : 'list',
                    'name' : 'Muscles-to-talk',
                    'message' : '10. How many muscles do you use when you talk?',
                    'choices' : ['45', '55', '72', '87']  
                }
            ]
def main():
    answers = prompt(questions,style=style)
    print(answers)

main()


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





