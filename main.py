import pandas as pd
import os

data_path = './Essential/'

def load_data():
    if os.path.exists('./Essential/main_info.csv'):
        try : 
            main_df = pd.read_csv('./Essential/main_info.csv')
        except UnicodeDecodeError:
            main_df = pd.DataFrame(columns=['acc_name', 'acc_uname', 'acc_pass'])
    else :
        main_df = pd.DataFrame(columns=['acc_name', 'acc_uname', 'acc_pass'])
    
    if os.path.exists('./Essential/misc_info.csv'):
        try :
            misc_df = pd.read_csv('./Essential/misc_info.csv')
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
    print(main_df)
    return main_df

def add_misc(df):
    name = input("Enter account name : ")
    uname = input("Enter username : ")
    info = input("Enter info title : ")
    desc = input("Enter info description : ")

    df = df.append({'acc_name' : name, 'acc_uname' : uname, 'info' : info, 'desc' : desc}, ignore_index=True)
    print(df)
    return df

def save_data(df, filename):
    df.to_csv(filename, index=False)

def main():
    main_df, misc_df = load_data()
    while True:
        opt = int(input("1. Add account\n2. Add other info\n3. Save data\n4. See tables\n5. Exit\n"))
        if opt==1:
            main_df = add_acc(main_df)
        elif opt==2:
            misc_df = add_misc(misc_df)
        elif opt==3:
            save_data(main_df, data_path+'main_info.csv')
            save_data(misc_df, data_path+'misc_info.csv')
        elif opt==4:
            print(main_df)
            print(misc_df)
        elif opt==5:
            break
main()