# 008
# price = int(input("Enter the amount on the bill: "))
# people = int(input("How many people did you eat with?: "))
# result = price // people
# print(result)

# 009 NO
# date = int(input("Enter the number of days: "))
# hours = date * 24
# m = hours * 60
# s = m * 60
# print("In", date, "days there are...")
# print(hours, "hours")
# print(m, "minutes")
# print(s, "secondes")

# 010
# weight = int(input("Enter your weight in kg: "))
# pound = weight * 2.204
# print("This is" , pound, "pounds")

# 011
# large = int(input("Enter Number over 100: "))
# small = int(input("Enter Number less than 10: "))
# result = large // small
# print("A small number goes into a large number", result, "times.")

# 012
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 > num2:
#     print(num2)
#     print(num1)
# else:
#     print(num1)
#     print(num2)

# 013
# num1 = int(input("Enter under 20 number: "))
# if num1 >= 20:
#     print("Too high")
# else:
#     print("Thank you")

# 014
# num = int(input("Enter numbers 10 and 20 or less: "))
# if num > 10 and num <= 20:
#     print("Thank you")
# else:
#     print("Incorrect answers")

# 015
# color = input("Enter your favorite color: ")
# if color == "red" or color == "RED" or color == "Red":
#     print("I like red too")
# else:
#     print("I don't lik that color, I prefer red")

# 016
# rain = input("Is it raining?: ")
# rain = str.lower(rain)
# if rain == "yes" :
#     windy = input("Is it windy?: ")
#     windy = str.lower(windy)
#     if windy == "yes":
#         print("It is too windy for an umbrella")
#     else:
#         print("Take an umbrella")
# else:
#     print("Enjoy your day")

# 017
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You can vote")
# elif age == 17:
#     print("You can learn to drive")
# elif age == 16:
#     print("You can buy a lottery ticket")
# else:
#     print("You can go Trick-or-Treating")

# 018
# num = int(input("Enter number: "))
# if num < 10:
#     print("Too low")
# elif num >= 10 and num <= 20:
#     print("Correct")
# else:
#     print("Too high")

# 019
# num = int(input("Enter 1 or 2 or 3: "))
# if num == 1:
#     print("Thank you")
# elif num == 2:
#     print("Well done")
# elif num == 3:
#     print("Correct")
# else:
#     print("Error message")

# 020
# name = input("Enter your name: ")
# namenum = len(name)
# print(namenum)

# 021
# name = input("Enter your name: ")
# lasttname = input("Enter your last name: ")
# fullname = name + " " + lastname
# num = len(fullname)
# print(fullname)
# print(num)

# 022
# firstname = input("Enter your first name: ")
# lastname = input("Enter your last name: ")
# firstname = firstname.title()
# lastname = lastname.title()
# name = firstname + " " + lastname
# print(name)

# 023
# lyrics = input("Enter the lyrics of a song: ")
# num = len(lyrics)
# print("This has", num, "letters in it")
# start = int(input("Enter a starting number: "))
# end = int(input("Enter an end number: "))
# part = (lyrics[start:end])
# print(part)

# 024
# word = input("Enter any word: ")
# word = word.upper()
# print(word)

# 025
# name = input("Enter your name: ")
# if len(name) < 5:
#     lastname = input("Enter your last name: ")
#     fullname = name + lastname
#     print(fullname.upper())
# else:
#     print(name.lower)

# 026 i don't know
# word = input("Enter any word: ")
# idk = word[0].lower()
# length = len(word)
# rest = word[1:length]
# if idk != "a" and idk != "e" and idk != "i" and idk != "o" and idk != "u":
#     lastword = rest + idk + "ay"
# else: 
#     lastword = word + "way"
# print(lastword.lower())

# 027
# import math
# num = float(input("Enter number: "))
# print(num * 2)

# 028
# import math
# num = float(input("Enter number: "))
# num = num*2
# print(round(num, 2))

# 029
# import math
# num = int(input("Enter over 500 number: "))
# num = round(math.sqrt(num), 2)
# # print(round(num, 2))
# print(num)

# 030
# import math
# print(round(math.pi, 5))

# 031
# import math
# radius = int(input("Please enter the radius of the circle: "))
# area = math.pi * (radius**2)
# print(area)

# 032
# import math
# radius = int(input("Please enter the radius of the column: "))
# height = int(input("Please enter the height of the column: "))
# volume = math.pi * (radius**2) * height
# print(round(volume, 3))

# 033
# import math
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = num1 // num2
# num4 = num1 % num2
# print(num1, "divided by", num2, "is", num3, "with", num4, "remaining")

# 034
# import math
# print("1) square\n2) Triangle\n")
# shape = int(input("Enter 1 or 2: "))
# if shape == 1:
#     side = int(input("Enter the length of the side: "))
#     area = side * side
#     print("It's", area, "in width")
# elif shape == 2:
#     height = int(input("Enter height: "))
#     base = int(input("Enter base: "))
#     area = (height * base) / 2
#     print("It's", area, "in width")
# else:
#     print("Please Enter 1 or 2")

# # 035
# name = input("Enter your name: ")
# for i in range(0,3):
#     print(name)

# # 035
# name = input("Enter your name: ")
# for i in range(0,3):
#     print(name)

# 036
# name = input("Enter your name: ")
# num = int(input("Enter number: "))
# for i in range(0,num):
#     print(name)
    
# 037
# name = input("Enter your name: ")
# for i in name:
#     print(i)

# 038
# name = input("Enter your name: ")
# num = int(input("Enter number: "))
# for o in range(0,num): 
#     for i in name:
#         print(i)

# 039
# num = int(input("Enter number of 1 ~ 12:  "))
# for i in range(1,13):
#     answer = i * num
#     print(i, "x", num, "=", answer)

# 040
# num = int(input("Enter number under 50: "))
# for number in range(50, num-1, -1):
#     print(number)

# 041
# name = input("Enter your name: ")
# num = int(input("Enter number: "))
# if num < 10:
#     for i in range(0, num):
#         print(name)
# elif num >= 10:
#     for i in range(0,3):
#         print("Too high")

# 042
# total = 0
# for i in range(0,5):
#     num = int(input("Enter a number: "))
#     ans = input("Do you want to this number included? (y/n) ")
#     if ans == "y":
#         total = total + num
# print(total)

# 043
# dir = input("Do you want count up or down? (u,d) ")
# if dir == "u":
#     num = int(input("What is the top number?: "))
#     for i in range(1, num+1):
#         print(i)
# elif dir == "d":
#     num = int(input("Enter under 20 number: "))
#     for i in range(num, 0, -1):
#         print(i)
# else:
#     print("I don't understand")

# 044
# num = int(input("How many friends do you want to invite to the party: "))
# if num < 10:
#     for i in range(0,num):
#         name = input("Enter a name: ")
#         print(name, "has been invited.")
# else:
#     print("Too many people")
