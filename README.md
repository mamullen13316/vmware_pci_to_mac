# ESXi PCI ID to MAC address Mapping Discovery
## Overview
This script can be used to find the MAC address to PCI address mapping on an ESXi host. 


## Usage
Transfer the pcitomac.py file to the ESXi host using scp and run from the ESX shell:

```
chmod +x pcitomac.py
./pcitomac.py
```

## Example
```buildoutcfg
[root@esxi-host10:/etc/vmware] ./pcitomac.py
VMNIC      MAC_ADDRESS          PCI_ID
vmnic0     00:25:b5:00:a0:6f    0000:09:00.0
vmnic1     00:25:b5:00:b0:6f    0000:0a:00.0
vmnic2     00:25:b5:00:a0:1f    0000:0b:00.0
vmnic3     00:25:b5:00:b0:1f    0000:0c:00.0
vmnic4     00:25:b5:00:a0:5e    0000:0d:00.0
vmnic5     00:25:b5:00:b0:5e    0000:0e:00.0
vmnic6     00:25:b5:00:a0:7a    0000:0f:00.0
vmnic7     00:25:b5:00:a0:4a    0000:10:00.0
vmnic8     00:25:b5:00:a0:5a    0000:11:00.0
vmnic9     00:25:b5:00:a0:2a    0000:12:00.0
vmnic10    00:25:b5:00:a0:3a    0000:13:00.0
vmnic11    00:25:b5:00:a0:0a    0000:14:00.0
vmnic12    00:25:b5:00:a0:1a    0000:15:00.0
vmnic13    00:25:b5:00:a0:79    0000:16:00.0
vmnic14    00:25:b5:00:a0:69    0000:17:00.0
```
