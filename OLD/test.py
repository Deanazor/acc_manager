import os
import subprocess

cur_path = os.getcwd()

dir_path = './acc_list/'

sender = 'Sender.bat'
receiver = 'Receiver.bat'

def create_acc():
    with open(dir_path + sender, 'r') as f:
        bat_code = f.readlines()
        f.close()

    folder_name = input("Enter your name : ")
    folder_pass = input("Enter your password : ")

    bat_code[1] = 'call Receive.bat {} {}'.format(folder_name, folder_pass)

    with open(dir_path + sender, 'w') as f:
        for code in bat_code:
            f.write(code)
        f.close()
    
    return folder_name

def lock_folder():
    os.chdir(dir_path)
    os.startfile(sender)
    os.chdir(cur_path)

def folder_status(name):
    if os.path.exists(dir_path + name):
        print("Folder locked")
    else:
        print("Folder unlocked")

def main():
    while True:
        opt = int(input("1. Create Account\n2. Lock/unlock account\n3. Exit\n"))
        if(opt == 1):
            cur_name = create_acc()
        elif(opt == 2):
            lock_folder()
            folder_status(cur_name)
        elif(opt == 3):
            break

main()
# subprocess.call([dir_path + sender])