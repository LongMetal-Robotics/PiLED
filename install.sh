echo "Checking for and updating packages..."
sudo apt-get update
sudo apt-get upgrade

echo "Updating setuptools"
sudo pip3 install --upgrade setuptools

echo "Installing pynetworktables"
pip3 install pynetworktables

echo "Installing rgbmatrix"
curl https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/rgb-matrix.sh >rgb-matrix.sh
sudo bash rgb-matrix.sh

echo "Installing RPi GPIO library"
pip3 install RPI.GPIO

echo "Installing the Adafruit Blinka library"
pip3 install adafruit-blinka

echo "Installing Neopixel libraries"
pip3 install rpi_ws281x adafruit-circuitpython-neopixel

echo "Add this line to /etc/rc.local:"
echo "sudo -E python /home/pi/PiLED/matrix/main.py &"
echo "sudo -E python /home/pi/PiLED/string/main.py &"