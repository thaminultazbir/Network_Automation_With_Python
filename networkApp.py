import sys

from ip_file_valid import ip_file_valid
from ip_addr_valid import ip_addr_valid

ip_list = ip_file_valid()
# print(ip_list)
ip = ip_addr_valid(ip_list)
print(ip)