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
    hide_word = '-'
    list_word = []
    list_word = len(ahorcad)
    for i in range(list_word-1):
        hide_word = str(hide_word) + '-'

    list(hide_word)
    list(ahorcad)
    
    # Convirtiendo los strings en listas.
    hide_word_2 = []
    ahorcad_2 = []

    for i in hide_word:
        hide_word_2.append(i)
    for i in ahorcad:
        ahorcad_2.append(i)

    # Desarrollo del error
    #import os
    print('hide_word_2: ', hide_word_2)
    print('ahorcad_2: ', ahorcad_2)
    while hide_word_2 != ahorcad_2:

        try: 
            add = input("Ingresa una letra: ")
            add = add.lower()
            assert add.islower()
            paso = -1


            for i in ahorcad_2:
                #print(i)
                paso = paso + 1
                #print('paso', paso)
                if i == add:
                    #print(i)
                    #print(add)
                    hide_word_2.pop(paso)
                    hide_word_2.insert(paso, add)
                    #print(hide_word_2)              
        except AssertionError:
            print("Solo se aceptan letras")
        print(hide_word_2)
        print(ahorcad_2)
    print("¡Lo has logrado! La palabra era " + ahorcad)      
            
            #os.system('clear')
    
def run():
    read()

if __name__ == '__main__':
    run()