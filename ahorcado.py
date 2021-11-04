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
    print(ahorcado)

def run():
    read()

if __name__ == '__main__':
    run()