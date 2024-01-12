def ask_fruit():
    number_of_fruit = input("How many pieces of fruit have you eaten today today? \n")

    #print("You  have eaten " + number_of_fruit + " pieces of fruit today. Well done.")

def ask_excercise():
    amount_of_excercise = input("How many hours of excercise have you done today? \n")

    #print("You have done " + amount_of_excercise + " hours of excercise today. Nice.")

print("Remember, your weekly goal is to achieve eating 3 pieces of fruit and 3 excercise sessions that are an hour long.\n\n")

number_of_fruit = 0
amount_of_excercise = 0

ask_fruit()

ask_excercise()

if (number_of_fruit < 2):
    fruit_weight = 0
    fruit_phrase = (number_of_fruit + " is not great, but it's ok")

if (number_of_fruit == 2):
    fruit_weight = 1
    fruit_phrase = (number_of_fruit + " is good, keep it up")

if (number_of_fruit > 2):
    fruit_weight = 2
    fruit_phrase = (number_of_fruit + " is great, nicely done")

if (amount_of_excercise == 0):
    excercise_weight = 0
    excercise_phrase = (amount_of_excercise + " hours of excercise isn't good, let's try and get better")

if (amount_of_excercise < 0.75 and amount_of_excercise > 0):
    excercise_weight = 1
    excercise_phrase = (amount_of_excercise + " hours of excercise isn't fantastic, but it's better than none, keep trying")

if (amount_of_excercise >= 0.75 and amount_of_excercise < 1.5):
    excercise_weight = 2
    excercise_phrase = (amount_of_excercise + " hours of excercise is good, but I know you can do better, keep it up")

if (amount_of_excercise >= 1.5 and amount_of_excercise < 3):
    excercise_weight = 3
    excercise_phrase = (amount_of_excercise + " hours of excercise is great, keep up the great work")

if (amount_of_excercise >= 3 and amount_of_excercise < 4.5):
    excercise_weight = 4
    excercise_phrase = (amount_of_excercise + " hours of excercise is brilliant, keep going")

if (amount_of_excercise >= 4.5 and amount_of_excercise < 6):
    excercise_weight = 5
    excercise_phrase = (amount_of_excercise + " hours of excercise is amazing, consider taking a rest day")

