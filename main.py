import pandas as pd
import os
from login import Account

data_path = './Essential/'
personal_path = './acc_list/'

def create_acc():
    while True:
        temp_name = input("Enter your name : ")
        opt = input("Generate random password? (Y/N) ")
        if opt =='y' or opt=='Y':
            temp_acc = Account(temp_name)
            temp_pass = temp_acc.generate_password()
        elif opt == 'n' or opt == 'N': 
            temp_pass = input("Enter password : ")
            temp_acc = Account(temp_name, temp_pass)

        reg_pass = temp_acc.register()

        if reg_pass:
            if opt =='y' or opt=='Y':
                print("Your password is : {}".format(temp_pass))
            break
        else :
            opt = input("Create another account? (Y/N) ")
            if opt == 'y' or opt == 'Y':
                pass
            elif opt == 'n' or opt == 'N':
                temp_acc = None
                break

    return temp_acc

def login_acc():
    while True:
        temp_name = input("Enter your name : ")
        temp_pass = input("Enter password : ")

        temp_acc = Account(temp_name, temp_pass)

        log_pass = temp_acc.login()

        if log_pass:
            print("Okaerinasaimasen")
            break
        else:
            print("Wrong password.... Dareduska?")
            temp_acc = None
            break
    
    return temp_acc

def load_data(full_path):
    if not os.path.exists(full_path):
        os.mkdir(full_path)
    if os.path.exists(full_path + '/main_info.csv'):
        try : 
            main_df = pd.read_csv(full_path + '/main_info.csv')
        except UnicodeDecodeError:
            main_df = pd.DataFrame(columns=['acc_name', 'acc_uname', 'acc_pass'])
    else :
        main_df = pd.DataFrame(columns=['acc_name', 'acc_uname', 'acc_pass'])
    
    if os.path.exists(full_path + '/misc_info.csv'):
        try :
            misc_df = pd.read_csv(full_path + '/misc_info.csv')
        except UnicodeDecodeError:
            misc_df = pd.DataFrame(columns=['acc_name', 'acc_uname', 'info', 'desc'])
    else :
        misc_df = pd.DataFrame(columns=['acc_name', 'acc_uname', 'info', 'desc'])
    
    return main_df, misc_df

def add_acc(main_df):
    name = input("Enter account name : ")
    uname = input("Enter username : ")
    password = input("Enter password : ")

    main_df = main_df.append({'acc_name' : name, 'acc_uname' : uname, 'acc_pass' : password}, ignore_index=True)
    # print(main_df)
    return main_df

def add_misc(df):
    name = input("Enter account name : ")
    uname = input("Enter username : ")
    info = input("Enter info title : ")
    desc = input("Enter info description : ")

    df = df.append({'acc_name' : name, 'acc_uname' : uname, 'info' : info, 'desc' : desc}, ignore_index=True)
    # print(df)
    return df

def save_data(df, filename):
    df.to_csv(filename, index=False)

def main():
    while True:
        opt = int(input("1. Create Account\n2. Login\n3. Exit\n"))
        if opt == 1:
            user_acc = create_acc()
            if user_acc is not None:
                break
        elif opt == 2:
            user_acc = login_acc()
            if user_acc is not None:
                break
        elif opt==3:
            raise SystemExit

    user_now = user_acc.get_name()
    full_path = personal_path + user_now
    main_df, misc_df = load_data(full_path)

    while True:
        opt = int(input("1. Add account\n2. Add other info\n3. Save data\n4. See tables\n5. Exit\n"))
        if opt==1:
            main_df = add_acc(main_df)
        elif opt==2:
            misc_df = add_misc(misc_df)
        elif opt==3:
            save_data(main_df, full_path+'/main_info.csv')
            save_data(misc_df, full_path+'/misc_info.csv')
        elif opt==4:
            print(main_df)
            print("\n")
            print(misc_df)
        elif opt==5:
            break

main()