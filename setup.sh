checkroot() {

if [[ "$(id -u)" -ne 0 ]]; then
   printf "\e[1;77mPlease, run this program as root!\n\e[0m"
   exit 1
fi

}

checkroot

echo -e "\n [+] UPDATING SYSTEM!"

apt update

mkdir clone

clear

echo -e"\n [*]         searching python3..."

if command -v python3 >/dev/null 2>&1 ; then

echo -e "\n\n [+]             PYTHON3 FOUND!!!"

else
echo -e "\n [-]          python3 not found"
echo -e "\n\n [-]        INSTALLING python3..."

sudo apt install python3||sudo pacman -S python3

fi

echo -e "\n\n [/] installing requirements..."
pip3 install -r requirements.txt
