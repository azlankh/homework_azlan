try:
    num=int(input("Enter a Number:"))
    print("You Age is", num)
    
except ValueError:
    print("Invlid Input! Please enter Your Age.")
    print("Try Again")