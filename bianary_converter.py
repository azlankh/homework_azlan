print("Welcome TO the Bianary Converter!!")
num = int(input("Enter A Number:"))

i = 1
ans = ("")
while num > 0:
    reminder = num % 2
    ans = str(reminder) + ans
    num = int(num/2)
print("The Binary Number is:", ans)
