sub1 = float(input("Enter marks for English: "))
sub2 = float(input("Enter marks for Maths: "))
sub3 = float(input("Enter marks for Science: "))
sub4 = float(input("Enter marks for Social Science: "))
sub5 = float(input("Enter marks for Hindi: "))
sum = sub1 + sub2 + sub3 + sub4 + sub5
print("Your total marks are:", sum)
average = sum / 5
print("Your average marks are:", average)
if average >= 90:
    print("Grade A")
elif average >= 80:
    print("Grade B")
elif average < 70:
    print("Grade C")
elif average < 60:
    print("Grade D")    
elif average < 40:
    print("Grade F")