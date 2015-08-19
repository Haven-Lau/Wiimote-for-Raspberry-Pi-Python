# Wiimote for Raspberry Pi Python
This is a sample python code to control Raspberry Pi's with Wiimotes.
You will need a bluetooth dongle for this.

To get started, you will need to install these libraries through console.

First, upgrade to the latest version of raspbian:
```
  -sudo apt-get update
  -sudo apt-get upgrade
```
Install all the bluetooth drivers:
```
sudo apt-get install –-no-install-recommends bluetooth
```
Cwiid library:
```
sudo apt-get install python cwiid
```
Uinput library:
```
sudo apt-get install python-pip
sudo pip install python-uinput
```

To allow uinput library to be automatically loaded on every reboot:
```
sudo tee –a /etc/modules <<< “uinput”
sudo update-initramfs -u
```
Lastly, open python 2, and copy and paste the code in python, then save it under home/pi/ in any name. 
To run the script, replace *filename* with the actual file name the code is saved as.
sudo python filename.py
