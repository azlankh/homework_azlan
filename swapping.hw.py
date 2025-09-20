# Entering the number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print("The Order in which you entered the numbers is: ", num1, ",", num2, ",", num3)
#Swapping choice
swap = int(input("Do You Want to Swap? (1 for Yes, 0 for No): "))
if swap == 1:
    print("The swapping schemes are:")
    print("(1)." ,num1, ",", num3, ",", num2)
    print("(2)." ,num2, ",", num1, ",", num3)
    print("(3)." ,num2, ",", num3, ",", num1)
    print("(4)." ,num3, ",", num1, ",", num2)
    print("(5)." ,num3, ",", num2, ",", num1)
    swap_choice = float(input("Choose Swapping scheme; print 1,2,3,4 or 5? "))
    if swap_choice == 1:
        temp1 = num1
        temp2 = num3
        temp3 = num2
    elif swap_choice == 2:
        temp1 = num2
        temp2 = num1
        temp3 = num3
    elif swap_choice == 3:
        temp1 = num2
        temp2 = num3
        temp3 = num1
    elif swap_choice == 4:
        temp1 = num3
        temp2 = num1
        temp3 = num2
    elif swap_choice == 5:
        temp1 = num3
        temp2 = num2
        temp3 = num1
    else:
        print("Invalid Choice")
    num1 = temp1
    num2 = temp2
    num3 = temp3
else:
    print("No Swapping Done")
print("The Final Order of the numbers is: ", num1, ",", num2, ",", num3)