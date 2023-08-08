File = open("assignment 13/movies.txt", "r")
data = File.readlines()

def read_data():
    dict_data = {}
    for each_data in data:
        ddata = each_data.rstrip()
        name, imdb = ddata.split("  ")
        dict_data[name] = imdb
    return dict_data

def Add(dictt):
    name = input("Please enter name of movie: ")
    IMDB = float(input("entre score IMDB: "))
    dictt.update({name : str(IMDB)})
    return dictt

def show_list(dictt):
    for i in sorted(dictt.keys()):
        print(i, dictt[i])
    
def show_imdb(dictt):
    s_dict = sorted(dictt.values(), reverse=True)  
    for i in range(5):
        for j in dictt.keys():
            if dictt[j] == s_dict[i]:
                print(s_dict[i], j)
def exit_(dictt):
    file = open("movies.txt", "w")
    for i in dictt.keys():
        string = i + "  " + dictt[i]+ "\n"
        file.write(string)

dic_data = read_data()

while True:
    operation = int(input("1=> add\n2=> show list\n3=> show IMDB\n4=> exit\nPlease enter your choice: "))
    if operation == 1:
        dic_data = Add(dic_data)
        exit(dic_data)
    elif operation == 2:
        show_list(dic_data)
    elif operation == 3:
        show_imdb(dic_data)
    elif operation == 4:
        exit_(dic_data)
        break
    else:
        print("The entered number is out of range(1 to 4)")