import subprocess
print(' [Status] Installing packages... [Status] ')
subprocess.call('sudo add-apt-repository multiverse && sudo apt-get install python3-pip -y && pip3 install requests bs4', shell=True)
print(' [Status] Packages installed! [Status] ')