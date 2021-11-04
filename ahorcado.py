def read():
    read_data = []
    with open("./data.txt", "r", encoding="utf-8") as r:
        for reading in r:
            read_data.append(reading)
    print(read_data)


def run():
    read()

if __name__ == '__main__':
    run()