#!/bin/python

# Imports
import subprocess
import re
from subprocess import PIPE

# Collect output from grep /net/pnic esx.conf
p = subprocess.Popen(['grep','/net/pnic','esx.conf'],stdout=PIPE,stderr=PIPE)
mac_list = [x.decode() for x in p.stdout]
d = {}
mac_pattern = '([a-fA-F0-9]{2}[:|\-]?){6}'
for line in mac_list:
	if 'name' in line:
		vmnic = line[line.find('vmnic'):].strip().rstrip('"')
		d[vmnic] = {}
	if 'mac' in line:
		mac = re.compile(mac_pattern).search(line).group()
		d[vmnic]['mac'] = mac

# Collect output from 'lspci -n | grep vmnic'
p = subprocess.Popen(['lspci','-n','|','grep','vmnic'],stdout=PIPE,stderr=PIPE)
pci_list = [x.decode() for x in p.stdout if 'vmnic' in x.decode()]
for line in pci_list:
	vmnic = line[line.find('vmnic'):line.find('\]')-1]
	pci_id = line[:line.find(' ')]
	if vmnic in d:
		d[vmnic]['pci_id'] = pci_id

sorted_keys = sorted(d.keys(),key=lambda x: int(re.search('[0-9]+',x).group()))

print('VMNIC'.ljust(10),'MAC_ADDRESS'.ljust(20),'PCI_ID')
for key in sorted_keys:
	if 'mac' in d[key] and 'pci_id' in d[key]:
		print(key.ljust(10),d[key]["mac"].ljust(20),d[key]["pci_id"])

