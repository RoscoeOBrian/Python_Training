import random

def get_guess():
    return list(input("What is your guess"))

def generate_code():
    digits=[str(num) for num in range(10)] #create list of strings with numbers 0 to 9

    random.shuffle(digits)

    return digits[:3]

#Generat clues
def generate_clues(code,user_guess):
    if user_guess==code:
        return "Code Cracked"

    clues = []

    for ind,num in enumerate(user_guess): #enumerate geht durch die Liste user_guess und gibt ind (=Index) und num (=eigentliche Nummer) aus
        if num == code[ind]: #wenn nummer aus user_guess gleich code an der gleichen stelle ist, dann ...
            clues.append("match") #"match" wird der Liste aus clues hinzugefügt
        elif num in code: #wenn nummer aus user_guess IRGENDWO im code ist, dann ...
            clues.append("close") #"close" word der clue liste hinzugefügt

    if clues == []:
        return ["Nope"]
    else:
        return clues


#RUN GAME LOGIC
print("Welcome Code Breaker!")

secret_code = generate_code()

clue_report = []

while clue_report != "Code Cracked":#!= not equal

    guess = get_guess()

    clue_report = generate_clues(guess, secret_code)
    print("Here is the result of your guess: ")
    for clue in clue_report:
        print(clue)
