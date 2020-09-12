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

def del_data(main_df, misc_df):
    del_acc = input("Enter the account type to be deleted : ")
    del_uname = input("Enter the username of the account : ")

    for i in main_df.index:
        if main_df['acc_name'][i] == del_acc and main_df['acc_uname'][i] == del_uname:
            main_df.drop(i, axis=0, inplace=True)
    
    for i in misc_df.index:
        if misc_df['acc_name'][i] == del_acc and misc_df['acc_uname'][i] == del_uname:
            misc_df.drop(i, axis=0, inplace=True)
    
    return main_df, misc_df

def search_data(main_df, misc_df):
    src_acc = input("Enter Account type : ")
    src_uname = input("Enter account username : ")
    found = False

    for i in main_df.index:
        fnd_acc = main_df['acc_name'][i]
        fnd_uname = main_df['acc_uname'][i]
        if fnd_acc == src_acc and fnd_uname == src_uname:
            print("\nAccount : {} with username : {} is found!".format(fnd_acc, fnd_uname))
            found = True

    if found:
        print("Other info :")
        for i in misc_df.index:
            if misc_df['acc_name'][i] == src_acc and misc_df['acc_uname'][i] == src_uname:
                fnd_info = misc_df['info'][i]
                fnd_desc = misc_df['desc'][i]
                print("{} : {}".format(fnd_info, fnd_desc))
        print("\n")
    
    else : 
        print("\nSorry, account not found\n")

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
        opt = int(input("1. Add account\n2. Add other info\n3. Delete Account\n4. Save data\n5. Search Account\n6. See tables\n7. Check Status\n8. Exit\n"))
        if opt==1:
            main_df = add_acc(main_df)
        elif opt==2:
            misc_df = add_misc(misc_df)
        elif opt==3:
            main_df, misc_df = del_data(main_df, misc_df)
        elif opt==4:
            save_data(main_df, full_path+'/main_info.csv')
            save_data(misc_df, full_path+'/misc_info.csv')
        elif opt==5:
            search_data(main_df, misc_df)
        elif opt==6:
            print(main_df)
        elif opt==7:
            user_acc.check_status()
        elif opt==8:
            # user_acc.logout()
            break

main()