def shutdown(ans):
    if ans == "yes" or ans == "YES":
        print()
        print("Shutting Down...")
    elif ans == "no" or ans == "NO":
        print()
        print("Shutdown Is Aborted")
    else:
        print()
        print("Sorry")
        print("I Didn't Understand That")

print("Do You want the Computer To ShutDown?")
print("Type 'yes' or 'no'")
answer = input()
shutdown(answer)

