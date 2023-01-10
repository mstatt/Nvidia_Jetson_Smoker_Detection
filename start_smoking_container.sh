#Start Smoke detection container:
sh ./max.sh
sudo docker run --net=host --gpus all roboflow/inference-server:jetson