#Start Smoke detection container:
# Bump system performance
sh ./max.sh
sudo docker run --net=host --gpus all roboflow/inference-server:jetson