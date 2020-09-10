import os
import hashlib
import pandas as pd
import numpy as np

cur_path = os.getcwd()

data_path = './Essential/'
personal_path = './acc_list/'

sender = 'Sender.bat'
receiver = 'Receiver.bat'

class Account():
    def __init__(self, acc_name, acc_pass):
        super().__init__()
        self.acc_name = acc_name
        self.acc_pass = acc_pass
        self.df = None
    
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
            'sha256', # The hash digest algorithm for HMAC
            passcode.encode('utf-8'), # Convert the password to bytes
            salt_2, # Provide the salt
            100000, # It is recommended to use at least 100,000 iterations of SHA-256
        )

        return salt, key

    def get_name(self):
        return self.acc_name

    def register(self):
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

        return reg_pass
    
    def login(self):
        self.load_data()
        log_info = self.df.loc[(self.df['main_name'] == self.acc_name)]
        log_info['salt'] = log_info['salt'].astype(bytes)
        salt = log_info['salt'][0]
        key = log_info['key'][0]
        log_pass = False

        res_key = hashlib.pbkdf2_hmac(
            'sha256', # The hash digest algorithm for HMAC
            self.acc_pass.encode('utf-8'), # Convert the password to bytes
            salt, # Provide the salt
            100000, # It is recommended to use at least 100,000 iterations of SHA-256
        )

        if str(key) == str(res_key):
            log_pass = True

        return log_pass