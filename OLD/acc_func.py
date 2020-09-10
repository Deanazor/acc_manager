import os

class Account():
    def __init__(self, acc_name=None, acc_id=None, acc_pass=None):
        super().__init__()
        self.acc_name = acc_name + "\n" #Nama akun / jenis akun
        self.acc_id = acc_id + "\n" #username akun
        self.acc_pass = acc_pass + "\n" #password akun
        self.misc_info = []
    
    def other_info(self, info, desc):
        """
        Add any misc info
        """
        self.misc_info.append('[{}, {}]\n'.format(info, desc))
    
    def acc_info(self):
        """
        Display all info about your account
        """
        print("App name : ", self.acc_name)
        print("username : ", self.acc_id)
        print("password : ", self.acc_pass)

        for content in self.misc_info:
            info, desc = content
            print(info, " : ", desc)
    
    def update_main(self, acc_name=None, acc_id=None, acc_pass=None):
        """
        Update your account main info
        """
        if acc_name is not None:
            self.acc_name = acc_name + "\n"
        
        if acc_id is not None:
            self.acc_id = acc_id + "\n"
        
        if acc_pass is not None:
            self.acc_pass = acc_pass + "\n"
    
    def get_info(self):
        """
        Get full info
        """
        zenbu = [self.acc_name, self.acc_id, self.acc_pass, self.misc_info]
        return zenbu
    
    def get_name(self):
        """
        Only return account type
        """
        return self.acc_name[:-1]
    
    def save_acc(self, dir_path, file_name):
        full_path = dir_path + file_name
        full_info = self.get_info()

        acc_file = open(full_path, 'w')

        for content in full_info:
            acc_file.write('{}'.format(content))
