#!/usr/bin/env python
import time
import subprocess
subprocess.call('ifconfig', shell=True)
time.sleep(1)
interface=str(input('SELECT THE INTERFACE : '))
subprocess.call(f'ifconfig {interface} down',shell=True)
mac_adress=str(input("enter the mac adress  : "))
try:
	subprocess.call(f'ifconfig {interface} hw ether {mac_adress}',shell=True)
	subprocess.call(f'ifconfig {interface} up' ,shell=True)
	print(f"OPERATION SUCCESSFULL MAC ADRESS IS CHANGED TO {mac_adress}")
except Exception as e:
	print(f"operation failed due to {e}")
	subprocess.call(f'ifconfig {interface} up' ,shell=True)







