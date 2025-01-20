print("Welcome to Rollercoaster!")
height = float(input("Enter your height in cm? "))
bill=0

if height >= 120:
    print("you can ride on rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        bill=5
        print(" child ticket are $5.")
    elif age <= 18:
        bill = 7
        print(" youth ticket are $7.")
    elif 45 <= age <= 55:
        print("Every thing is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print(" Adult ticket are $12.")

    wants_photo = input("if you will take photo enter y or Enter n for No ")
    if wants_photo == "y" :
        bill += 3
    print(f"your total fare is : {bill}")

else:
    print("Sorry you have to  grow before you ride on rollercoaster")