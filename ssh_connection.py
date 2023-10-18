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
        username = selected_user_file.readlines()[0].split(',')[0].rsplit("\n")
        selected_user_file.seek(0)
        password = selected_user_file.readlines()[0].split(',')[1].rsplit("\n")


        # -------login into the device----------
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy)

        session.connect(ip.rstrip("\n"), username=username, password=password)
        connection = session.invoke_shell()
        connection.send("enable\n")
        connection.send("terminal length 0\n")  #disable pagination
        time.sleep(1)

        # --Entering Global Configure Mode--
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)

        selected_cmd_file = open(cmd_file, 'r')
        selected_cmd_file.seek(0)

        for each_line in selected_cmd_file.readlines():
            connection.send(each_line+'\n')
            time.sleep(2)
        
        selected_user_file.close()
        selected_cmd_file.close()

        router_output = connection.recv(65535)

        if re.search(b"% Invalid input", router_output):
            print("* There is at least One IOS syntax error on device {} : (".format(ip))
        else:
            print("\n Done for Device {} :)".format(ip))
        
        print(str(router_output)+"\n")
        session.close()

    except paramiko.AuthenticationException:
        print("Invalid Username/Password. Please check the credential file")
        print("Closing Program Bye...!")