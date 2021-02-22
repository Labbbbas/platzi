import random

def run():
    number_found = False
    random_number = random.randint(0, 20)

    while number_found == False:
        number = int(input("Intenta un numero: "))
        if number == random_number:
            print("Felicidades! Encontraste el numero!")
            number_found = True
        elif number > random_number:
            print("El numero es mas chico")
        else:
            print("El numero es mas grande")


if __name__ == "__main__":
    run()