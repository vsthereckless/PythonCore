from time import sleep

delay = 4

print("Hi, let me introduce myself! My name is Volodia. I'm 25 and I live in Lviv, Ukraine\n\
Now tell me something about you: ")
sleep(2)

userName = input("What is your name? ")

while True:
    try: 
        userAge = int(input("How old are you? "))
        break
    except ValueError:
        print("You age should be a number, you silly :)")


userAddress = input("Where do you live? ")

print(f"Hello {userName}! Nice to meet you!")
print(f"Your age is {userAge}.")
print(f"You live in {userAddress}.")
