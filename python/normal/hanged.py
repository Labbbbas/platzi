import random
import os


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
    =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
    =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
    =========''', '''
''']


WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'videojuegos',
    'democracia',
    'computadora',
    'teclado',
    'perro',
    'gato',
    'abuela',
    'ricardo',
    'fernando',
    'curso',
    'audifonos',
    'comida',
    'manzana',
    'gorra',
    'diego',
    'agua',
    'television',
    'espejo',
    'jessica',
    'pizza',
    'hamburguesa',
    'celular',
    'regla',
    'papel',
    'casa',
    'carro',
    'primo',
    'numero',
    'estufa',
    'colchon',
    'plato',
    'impresora',
    'camisa',
    'escritorio',
    'caja',
    'refrigerador',
    'ferrocarril',
    'ornitorrinco',
    'parangaricutirimicuaro',
    'murcielago',
    'gis',
    'chamarra'
]


def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]


def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('')


def run():
    word = random_word()
    hidden_word = ['_'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: '))

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                os.system('clear')
                display_board(hidden_word, tries)
                print('')
                print('¡Perdiste! La palabra correcta era {}'.format(word))
                print('')
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []

        try:
            hidden_word.index('_')
        except ValueError:
            os.system('clear')
            display_board(hidden_word, tries)
            print('')
            print('¡Felicidades! Ganaste. La palabra es: {}'.format(word))
            print('')
            break

        os.system('clear')


if __name__ == '__main__':
    os.system('clear')
    print('')
    print('                  B I E N V E N I D O S  A  A H O R C A D O S')
    run()