import random
import math

print("Welcome to my first python project")
color1 = input("Enter a color: ")
object = input("Enter a object: ")
gender = input("Choose your gender ( Type b/g ): ")
name1 = input("Enter a boy name: ")
name2 = input("Enter a girl name: ")
number = input("Enter a number: ")

if gender == "b" or gender == "B":
    print("Once upon a time there was a boy named " + name1 +
        ". He proposed to " + name2 + " with his " + object +
        ". The " + object + " was " + color1 + " in color. " +
        "As the boy was such a stupid, she didn't wanted to be in that relationship. " +
        "So she slapped him " + number + " times and left the place. " +
        "And that was a small little story for you stupid " + name1 + ".....")
else:
    print("Once upon a time there was a girl named " + name2 +
        ". He proposed to " + name1 + " with a " + object +
        ". The " + object + " was " + color1 + " in color. " +
        "As the boy was such a stupid, he didn't wanted to be in that relationship. " +
        "So he slapped him " + number + " times and left the place. " +
        "And that was a small little story for you stupid " + name2 + ".....")
