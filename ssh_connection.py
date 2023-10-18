import os
import sys

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