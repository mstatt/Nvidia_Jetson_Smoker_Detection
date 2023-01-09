#!/bin/sh
sudo apt-get upgrade
sudo apt-get update
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update 
sudo apt-get install -y sublime-tex
sudo apt-get install -y python3-setuptools
sudo apt-get install -y git wget cmake curl
sudo apt-get install -y python3-numpy python3-pip
sudo apt-get install -y libpython3-dev libpng-dev libtiff-dev
sudo apt-get install -y qtbase5-dev libjpeg-dev
sudo apt-get install -y build-essential unzip pkg-config
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install -y libgtk2.0-dev libcanberra-gtk*
sudo apt-get install -y libxvidcore-dev libx264-dev libgtk-3-dev
sudo apt-get install -y libtbb2 libtbb-dev libdc1394-22-dev
sudo apt-get install -y libv4l-dev v4l-utils telegraf
sudo apt-get install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
sudo apt-get install -y libavresample-dev libvorbis-dev libxine2-dev
sudo apt-get install -y libfaac-dev libmp3lame-dev libtheora-dev libopencore-amrnb-dev
sudo apt-get install -y libopenblas-dev libatlas-base-dev libblas-dev
sudo apt-get install -y liblapack-dev libeigen3-dev gfortran
sudo apt-get install -y libhdf5-dev protobuf-compiler python3-venv
sudo apt-get install -y libprotobuf-dev libgoogle-glog-dev libgflags-dev
sudo apt-get install -y libcanberra-gtk-module
sudo apt-get install -y v4l-utils jtop
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update 
sudo apt-get install -y sublime-tex

sudo -H pip3 install -U jetson-stats
sudo -H pip3 install Jetson.GPIO
sudo -H pip3 install roboflow
sudo -H pip3 install uuid

# Download the correct Jetson Interface repo and build it with cmake
git clone --recursive https://github.com/dusty-nv/jetson-inference
cd jetson-inference
git submodule update --init
mkdir build
cd build
cmake ../
make -j$(nproc)
sudo make install

sudo iw dev wlan0 set power_save off
sudo apt-get update
sudo apt-get upgrade

sudo sh -c "echo '/usr/local/cuda/lib64' >> /etc/ld.so.conf.d/nvidia-tegra.conf"
sudo ldconfig

sudo pip3 install -U pip
sudo pip3 install -U numpy grpcio absl-py py-cpuinfo psutil portpicker six mock requests gast h5py astor termcolor protobuf keras-applications keras-preprocessing wrapt google-pasta setuptools testresources

- Installing TensorFlow
sudo pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v42 tensorflow-gpu

- Upgrade TensorFlow
sudo pip3 install --upgrade --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v42 tensorflow-gpu

sudo pip3 install keras jupyter pillow matplotlib

python3 -c 'import numpy; print(numpy.__version__)'
python3 -c 'import tensorflow; print(tensorflow.__version__)'
python3 -c 'import keras; print(keras.__version__)'
python3 -c 'import jupyter; print(jupyter.__version__)'
python3 -c 'import PIL; print(PIL.__version__)'
python3 -c 'import matplotlib; print(matplotlib.__version__)'

git clone https://github.com/NVIDIA-AI-IOT/jetcam
cd jetcam
pip3 install ./ --user

sudo apt autoremove -y
sudo apt clean
sudo apt remove thunderbird libreoffice-* -y

#Install and run Yolo5 Docker and Model
sudo docker pull roboflow/inference-server:jetson

# Update again and reboot
sudo apt-get update
sudo shutdown -r now
