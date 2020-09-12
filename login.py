import os
import hashlib
import pandas as pd
import random
import string

cur_path = os.getcwd()

data_path = './Essential/'
personal_path = './acc_list/'

sender = 'Sender.bat'
receiver = 'Receiver.bat'

class Account():
    def __init__(self, acc_name, acc_pass = None):
        super().__init__()
        self.acc_name = acc_name
        self.acc_pass = acc_pass
        self.df = None
        self.bat_code = None
        self.log_status = False
        self.folder_status = False
    
    def load_data(self):
        if os.path.exists(data_path + "users.csv"):
            try : 
                self.df = pd.read_csv(data_path + "users.csv")
            except UnicodeDecodeError:
                self.df = pd.DataFrame(columns=['main_name', 'salt', 'key'])
        else :
            self.df = pd.DataFrame(columns=['main_name', 'salt', 'key'])
        
    def hash_pass(self, passcode):
        salt = os.urandom(32)
        salt_2 = str(salt)
        salt_2 = salt_2[2:-1]
        salt_2 = bytes(salt_2, 'utf-8')
        key = hashlib.pbkdf2_hmac(
            'sha256',
            passcode.encode('utf-8'),
            salt_2,
            100000,
        )

        return salt, key

    def get_name(self):
        return self.acc_name

    def register(self):
        if self.acc_pass is None:
            _ = self.generate_password()
        self.load_data()
        salt, key = self.hash_pass(self.acc_pass)

        salt = str(salt)
        salt = salt[2:-1]

        self.df = self.df.append({'main_name' : self.acc_name, 'salt' : salt, 'key' : key}, ignore_index=True)

        duplicate_row = self.df.duplicated(subset=['main_name'])

        reg_pass = True

        for i in duplicate_row.index:
            if duplicate_row[i] == True:
                self.df.drop(i, axis = 0, inplace=True)
                print("Username already exist.")
                print("Register failed....")
                reg_pass = False
                break
        
        if reg_pass:
            self.df.to_csv(data_path + 'users.csv', index = False)
            self.log_status = True

        return reg_pass
    
    def login(self):
        self.load_data()

        # if not self.check_folder():
        #     self.lock_folder()

        log_info = pd.DataFrame().append(self.df.loc[(self.df['main_name'] == self.acc_name)], ignore_index=True)
        salt = bytes(log_info['salt'][0], 'utf-8')
        key = log_info['key'][0]
        log_pass = False

        res_key = hashlib.pbkdf2_hmac(
            'sha256',
            self.acc_pass.encode('utf-8'),
            salt,
            100000,
        )

        if str(key) == str(res_key):
            log_pass = True

        self.log_status = log_pass
        return log_pass
    
    def read_bat(self):
        bat_path = './acc_list/Sender.bat'

        with open(bat_path, 'r') as f:
            self.bat_code = f.readlines()
            f.close()
    
    def write_bat(self):
        bat_path = './acc_list/Sender.bat'

        with open(bat_path, 'w') as f:
            for code in self.bat_code:
                f.write(code)
            f.close()

    def exec_bat(self, bat_file):
        cur_dir = os.getcwd()
        print(cur_dir)

        os.chdir('./acc_list/')
        os.startfile(bat_file)
        os.chdir(cur_dir)

    def lock_folder(self):
        if self.df is None:
            self.load_data()
        
        if self.bat_code is None:
            self.read_bat()

        # bat_path = './acc_list/Sender.bat'
        log_info = pd.DataFrame().append(self.df.loc[(self.df['main_name'] == self.acc_name)], ignore_index=True)
        folder_name = log_info['main_name'][0]
        folder_pass = log_info['key'][0]
        folder_salt = bytes(log_info['salt'][0], 'utf-8')
        folder_hide = '\"' + folder_name +'.{21EC2020-3AEA-1069-A2DD-08002B30309D}\"'

        res_key = hashlib.pbkdf2_hmac(
            'sha256',
            self.acc_pass.encode('utf-8'),
            folder_salt,
            100000,
        )

        res_key = str(res_key)

        self.bat_code[1] = 'call Receive.bat {} {} {} {}'.format(folder_name, folder_pass, folder_hide, res_key)

        self.write_bat()

        self.exec_bat('Sender.bat')
    
    def check_folder(self, name=None):
        if name is None:
            self.folder_status = os.path.exists(personal_path + self.acc_name)
        else :
            self.folder_status = os.path.exists(personal_path+name)

        return self.folder_status

    def generate_password(self):
        length = random.randint(16, 25)
        words = string.ascii_letters + string.digits
        result = ''.join((random.choice(words) for i in range(length)))
        self.acc_pass = result

        return result

    def check_status(self):
        print("Logged-in : {}".format(self.log_status))
        print("Table status : {}".format(self.check_folder()))
    
    def logout(self):
        self.lock_folder()
    
    def Remember(self):
        data_exist = os.path.exists(data_path + 'remember.csv')

        if data_exist:
            try : 
                df = pd.read_csv(data_path + "remember.csv")
            except UnicodeDecodeError:
                df = pd.DataFrame(columns=['acc_name', 'acc_pass'])
        else :
            df = pd.DataFrame(columns=['acc_name', 'acc_pass'])
        
        if df.empty:
            df = df.append({'acc_name' : self.acc_name, 'acc_pass' : self.acc_pass}, ignore_index=True)
        else:
            df.drop(df.index, axis = 0, inplace=True)
            df = df.append({'acc_name' : self.acc_name, 'acc_pass' : self.acc_pass}, ignore_index=True)
        
        df.to_csv(data_path + 'remember.csv', index=False)
    
    def log_remember(self):
        df = pd.read_csv(data_path + "remember.csv")

        if self.acc_name == df['acc_name'][0]:
            self.acc_name = df['acc_name'][0]
            self.acc_pass = df['acc_pass'][0]

        is_log = self.login()
        return is_log