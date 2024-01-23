import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

def find_max_len_in_line(path):
    biggest_str = ""
    with open(path) as file:
        lines = file.read().splitlines()

        # max_len takes the biggest value (len) from the lines
        max_len = max(len(x) for x in lines)

        for line in lines:
            if len(line) > len(biggest_str):
                biggest_str = line
        print(max_len, biggest_str)

# find_max_len_in_line("text.txt")

def conver_to_csv():
    with open("text.txt") as file:
        data_file = file.readlines()
        # a nest-list with tuple [(English, Meaning)] indance
    data = [(data_file[i].strip(), data_file[i+1].strip()) for i in range(0, len(data_file), 2)]
    # print(data)
    df = pd.DataFrame(data=data, columns=["English", "Meaning"])
    print(df)
    df.to_csv("5k most used.csv")

conver_to_csv()