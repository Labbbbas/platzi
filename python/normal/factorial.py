def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)


if __name__ == "__main__":
    print("")
    number = int(input("Write a number of which you want to obtain its factorial: "))

    result = factorial(number)

    print("")
    print("Its factorial is: " + str(result))
    print("")