def palidrome_2(word):
    reversed_word = word[::-1]
    
    if reversed_word == word:
        return True
    return False

def palidrome(word):
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0,letter)

    reversed_word=''.join(reversed_letters)

    if reversed_word == word:
        return True
    return False

if __name__ == '__main__':
    word =input("Escribe una palabra: ").lower()
    
    result = palidrome_2(word)

    word = word.capitalize()
    
    if result is True:
        print("{} si es un palindromo".format(word))
    else:
        print(("{} no es un palindromo".format(word)))