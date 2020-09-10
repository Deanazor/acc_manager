import os
from acc_func import Account

dir_path = ''
file_path = ''

def file_opener(name):
    global dir_path
    global file_path

    dir_path = './acc_list/' + name + "/"
    file_path = name + '.txt'

    if os.path.exists(dir_path):
        acc_file = open(dir_path + file_path, 'r')
        acc_list = acc_file.readlines()
        acc_file.close()
    else :
        os.mkdir(dir_path)
        acc_list = []
    
    return acc_list

def save_file(content_list, name):
    f = open(dir_path + file_path, 'w')
    for cont in content_list:
        f.write("%s" % cont)
    f.close()

def add_item(item, temp_list):
    temp_list.append(item + "\n")
    return temp_list

def read_file(name):
    f = open(dir_path + file_path, 'r')
    print(f.readlines())

def see_content(content):
    print("\nYour Account : ")
    for i, cont in enumerate(content):
        print(i+1, " : ", cont)

def create_acc():
    temp_acc = Account(input("Account name : "), input("Account username : "), input("Account password : "))

    return temp_acc

def locker(t_name, t_pass):
    bat_path = './acc_list/'
    bat_file = 'Sender.bat'
    ori_path = os.getcwd()

    os.chdir(bat_path)
    os.startfile(bat_file)
    os.chdir(ori_path)

def main():
    print("Karena tidak case-sensitive namanya jgn sama ya :v")
    cur_name = input("Enter your name : ")
    cur_list = file_opener(cur_name)

    while(True):
        try :
            opt = int(input("1. Add item\n2. Print File\n3. save\n4. Exit\n"))
        except ValueError :
            opt = 0
        if(opt == 1):
            in_item = create_acc()
            in_name = in_item.get_name()
            cur_list = add_item(in_name, cur_list)
            cur_list.sort()
        elif(opt == 2):
            see_content(cur_list)
        elif(opt == 3):
            save_file(cur_list, cur_name)
            in_item.save_acc(dir_path, in_name + ".txt")
            print("File saved successfully\n")
        elif(opt == 4):
            break

    # read_file(cur_name)

main()