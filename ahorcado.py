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
    print(hide_word)

    # Desarrollo del error
    # add = input("Ingresa una letra: ")
    # print(add)



def run():
    read()

if __name__ == '__main__':
    run()