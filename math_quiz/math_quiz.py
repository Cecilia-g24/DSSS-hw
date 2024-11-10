import random


def get_random_integer(min, max): #generate a random integer
    return random.randint(min, max)


def get_operator(): #Generate a numerical operator (addition, subtraction or multiplication)
    return random.choice(['+', '-', '*'])


def result(n1, n2, o): #Create a math problem string and calculate the expected answer.
    """
    n1 is the 1st integer generated,  
    n2 is the 2nd integer generated,  
    o is the numerical operator"""

    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a


def math_quiz():
    s = 0 #A player's initial score is 0
    t_q = 3 #total number of questions (needs to be an integer)

    print("Welcome to the Math Quiz Game!") #readable line 1
    print("You will be presented with math problems, and you need to provide the correct answers.")#readable line 2

    for _ in range(t_q): #generate random numbers and numerical operator for the quiz question 
        n1 = get_random_integer(1, 10); #pick a first random integer from 1 to 10
        n2 = get_random_integer(1, 6); #pick a second random integer from 1 to 6
        o = get_operator() #pick a numerical operator

        PROBLEM, ANSWER = result(n1, n2, o) #generate a random quiz problem
        print(f"\nQuestion: {PROBLEM}")
        
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER: #the player's answer is correct
            print("Correct! You earned a point.") #print a line
            s += 1  #add 1 to the player's score
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.") #if incorrect, show the correct answer

    print(f"\nGame over! Your score is: {s}/{t_q}") #end the game and show final score

if __name__ == "__main__":
    math_quiz()
