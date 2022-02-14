import os
import platform
import getpass

print("\n -----------------user---------------------")
print("\n " + getpass.getuser() + "\n")
print("----------------------------------------------------")
print("\n python version [] " + platform.python_version())
print("\n--------------------------------------------------")
print("\n system [] " + platform.system())
print("\n--------------------------------------------------")
print("\n versione [] " + platform.version())
print("\n--------------------------------------------------")
print("\n rilascio [] " + platform.release())
print("\n--------------------------------------------------")
print("\n macchina [] " + platform.machine())
print("\n--------------------------------------------------")
print("\n processore [] " + platform.processor())
print("\n--------------------------------------------------")
print("\n nome desktop [] " + platform.node())
print("\n--------------------------------------------------")
print("\n piattaforma [] " + platform.platform())
print("\n--------------------------------------------------\n")

if(platform.system() == "Windows"):
    import subprocess
    proc = subprocess.check_output("ipconfig" ).decode('utf-8')
    print(proc)
if(platform.system() == "Linux"):
    import subprocess
    proc_1 = subprocess.check_output("ifconfig" ).decode('utf-8')
    print(proc_1)

scelta = input("\n vuoi più informazioni? (S/n): ")
if(scelta == "S"):
    os.system("dxdiag")
    os.system("python3 language/italiano/console.py")
else:
    os.system("python3 language/italiano/console.py")
