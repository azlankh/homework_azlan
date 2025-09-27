name = input ("Enter Your Name: ")
age = int(input ("Enter The Your Age: "))
if age >= 10:
    if age >= 10 and age <= 19:
        print ("You Can Join This Class", name)
    elif age >= 20:
        print ("Join In A different Class", name)
elif age <= 10:
    print ("Your Too Young To Join this Class")
    print ("Join After Some Years", name)