import paramiko
import time
import os.path
import sys
import re

# -------------Checking User Credentials--------------------

user_file = input("\n# Enter user file path and name (e.g. D:\\MyApps\\myfile.txt): ")

if os.path.isfile(user_file) == True:
    print("\n* Username/password file is valid :)\n")

else:
    print("\n* File {} does not exist :( Please check and try again.\n".format(user_file))
    sys.exit()

#-------------------Checking Command File-------------------------

cmd_file = input("\n# Enter command file path and name (e.g. D:\\MyApps\\myfile.txt): ")

if os.path.isfile(cmd_file) == True:
    print("\n* Command file is valid :)\n")

else:
    print("\n* File {} does not exist :( Please check and try again.\n".format(cmd_file))


# ----------OPEN SSHV2 CONNECTION TO THE DEVICE----------
def ssh_connection(ip):
    global user_file
    global cmd_file
    try:
        selected_user_file = open(user_file, 'r')
        selected_user_file.seek(0)
        user_name = selected_user_file.readlines()[0].split(',')[0].rsplit("\n")
        selected_user_file.seek(0)
        password = selected_user_file.readlines()[0].split(',')[1].rsplit("\n")


        # -------login into the device----------
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy)