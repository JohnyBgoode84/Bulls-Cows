"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jan Černý
email: JohnyBgoode@seznam.cz
discord: JohnyBgoode84
"""

import random
import datetime

#POMOCNÉ PROMĚNNÉ
separator = "-" * 48
t_start = datetime.datetime.now()

#NÁHODNÉ ČÍSLO
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
mix_num = random.sample(numbers, 4)
if mix_num[0] == 0:
   mix_num = random.sample(numbers, 4)
random_numbers = ''.join([str(x) for x in mix_num])

#ÚVOD
def intro() -> None:
    print("Hi there!")
    print(separator)
    print("I've generated a random 4 digit number for you")
    print("Let's play a bulls and cows game.")
    print(separator)
    #print("tajné číslo je", random_numbers)
    print("Enter a number (non-repeating numbers):")
    print(separator)

#KONTROLA ZADÁNÍ
def entry(tip: str):
    result = False
    if not tip.isdecimal():
        print(f"Please input numbers only! \n{separator}")
    elif len(tip) != 4:
        print(f"Please input 4 numbers! \n{separator}")
    elif tip[0] == "0":
        print(f"Number cannot begin with 0! \n{separator}")
    elif len(set(tip)) != 4:
        print(f"All digits must be unique! \n{separator}")
    else:
        result = True
    return result


#VYHODNOCENÍ SHODY
def matches(tip: str, random_num: list):
    bulls, cows = 0, 0
    for i, number in enumerate(tip):
        if number == random_num[i]:
            bulls += 1
        elif number in random_num:
            cows += 1

    #stav, množné
    if bulls != 4:
        state = f"{bulls} bull"
        if bulls > 1:
            state = f"{bulls} bulls"
        state += f", {cows} cow"
        if cows > 1:
            state += "s"
        return state
      
def main():
    count_tips = 0
    intro()

    while True:
        tip = input(">>> ")
        
        if entry(tip):
            count_tips += 1
            message = matches(tip, random_numbers)
            if not message:
                result(count_tips)
                print(separator)
                break
            else:
                print(message)
                print(separator)
 

    if count_tips <= 10:
        print("That's amazing")
    elif count_tips < 25:
        print("That's average")
    else:
        print("That's not so good")

#VYSLEDEK
def result(count_tip_num: int):
    print("Correct, you've guessed the right number")
    print("in", count_tip_num, "guesses")

    t_end = datetime.datetime.now()
    t_overall = t_end - t_start
    print(f"\nTotal playing time in seconds: {t_overall.seconds}")

if __name__ == '__main__':
    main()