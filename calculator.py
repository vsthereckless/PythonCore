from time import sleep

delay = 2
longDelay = 5

print("HI! I am you primitive calculator. Let's do some math!!!")

sleep(delay)

firstNumber = int(input("Type in the first number: "))
print(f"The first number is {firstNumber}")

sleep(delay)

secondNumber = int(input("Type in the second number: "))
print(f"The second number is {secondNumber}")

sleep(delay)

print("Now let me calculate something for you...\nloading...\n")

sleep(longDelay)

print("I have the results!! Enjoj")
print(firstNumber, "+", secondNumber, "=", firstNumber + secondNumber)
print(firstNumber, "-", secondNumber, "=", firstNumber - secondNumber)
print(firstNumber, "*", secondNumber, "=", firstNumber * secondNumber)
print(firstNumber, "/", secondNumber, "=", int(firstNumber / secondNumber))
print(firstNumber, "**", secondNumber, "=", firstNumber ** secondNumber)

sleep(longDelay)

print("\nThank You for choosing me! Have a good one:)")
