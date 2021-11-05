def read():
    read_data = []
    with open("./data.txt", "r", encoding="utf-8") as r:
        for reading in r:
            read_data.append(reading)  
    
    choose_word = []
    number_data = []
    ahorcado = []

    from random import randint as ran
    number_data = len(read_data)
    choose_word = ran(0, number_data-1)
    ahorcado = read_data[choose_word]
    ahorcad = ahorcado[:-1]
        
    print("\n¡Adivina la palabra!\n")

    # Desarrollo de la list anónima con la palabra
    hide_word = '- '
    list_word = []
    list_word = len(ahorcad)
    for i in range(list_word-1):
        hide_word = str(hide_word) + '- '

    list(hide_word)
    list(ahorcad)
    caracteres_validos = ['a', 'á', 'b', 'c', 'd', 'e', 'é', 
                          'f', 'g', 'h', 'i', 'í', 'j', 'k',
                          'l', 'm', 'n', 'ñ', 'o', 'ó', 'p',
                          'q', 'r', 's', 't', 'u', 'ú', 'v',
                          'w', 'x', 'y', 'z']
    # Desarrollo del error
    # while hide_word != ahorcad:
    
    try: 
        add = input("Ingresa una letra: ")
        add = add.lower()
        assert add.islower()
    except AssertionError:
        print("Solo se aceptan letras")
    
    # import os
    # os.system('clear')

def run():
    read()

if __name__ == '__main__':
    run()