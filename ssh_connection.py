import os
import sys

user_file = input("\n# Enter user file path and name (e.g. D:\\MyApps\\myfile.txt): ")

if os.path.isfile(user_file) == True:
    print("\n* Username/password file is valid :)\n")

else:
    print("\n* File {} does not exist :( Please check and try again.\n".format(user_file))
    sys.exit()