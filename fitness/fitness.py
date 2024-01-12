def ask_fruit():
    number_of_fruit = input("How many pieces of fruit have you eaten today this today? \n")

    print("You  have eaten " + number_of_fruit + " pieces of fruit today. Well done.")

def ask_excercise():
    amount_of_excercise = input("How many hours of excercise have you done today?")

    print("You have done " + amount_of_excercise + " hours of excercise today. Nice.")

print("Remember, your weekly goal is to achieve eating 3 pieces of fruit and 3 excercise sessions that are an hour long.\n\n")

ask_fruit()

ask_excercise()