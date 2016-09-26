import os
def rename_files():
    file_list = os.listdir(r"/users/jay/jayb/fullstack_nano/alphabet")
    #saved_path = os.getcwd()
    #print("Current Working Directory is " + saved_path)
    os.chdir(r"/users/jay/jayb/fullstack_nano/alphabet")
    
    for file_name in file_list:
        print("Old Name = " + file_name)
        print("New Name = " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
        #os.chdir(saved_path)

rename_files()
