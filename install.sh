sudo apt update
sudo apt upgrade

sudo apt-get install -y python3-smbus i2c-tools

python -m venv --system-site-packages env_DIYDrone
source env_DIYDrone/bin/activate

pip install -r requirements.txt