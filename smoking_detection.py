"""
2023 Jan Smoking Detection Project
Michael Stattelman
Deployed on Nvidia Jetson Nano
"""

import os
import cv2
import math
import uuid
import json
import shutil
import subprocess
import jetson_inference
import jetson.utils

# from nanocamera.NanoCam import Camera
import nanocamera as nano



def smokingDetection(initImg):
    """
    Function to take in image as a param and run against detection model
    """
    # Run initImage across the trained Model for classification.
    try:
        CurlUrl = (
            "base64 "
            + initImg
            + ' | curl -d @- "http://localhost:9001/cigarette_detection-g9e6e/7?api_key=<API KEY>"'
        )
        status, stroutput = subprocess.getstatusoutput(CurlUrl)
        y = json.dumps(stroutput)
        #vb = json.loads(stroutput)
        x = str(y).find("confidence")
        # Strip extra chars
        confidence = str(y[x + 14 : x + 19]).strip()
        confidence.replace('/', '')
        fconf = float("".join(c for c in confidence if (c.isdigit() or c == ".")))
        with open("score.txt", "a") as outfileA:
            outfileA.write(str(float(fconf))+'\n')
        #print(str(confidence))
        #Set the level of Confidence we want to trigger the save
        if float(fconf) >= float(0.70):
            return True
        else:
            return False

    except:
        return False


def moveImage(path1, path2,x1, y1):
    # Function to move images from Capture to Smoking directories
    img3 = cv2.imread(path1)

    # Add text
    cv2.putText(img3,"**Detected**",(x1, y1),cv2.FONT_HERSHEY_DUPLEX,1,(0, 0, 255), 2,)

    cv2.imwrite(str(path2),img3)
    os.remove(path1)



# a location for the camera stream. Stream location without "http://"
#camera_stream = "rtsp://admin:password@192.168.70.142:554"
# Create the Camera instance
#camera = nano.Camera(camera_type=3, source=camera_stream, width=640, height=480, fps=30)
net = jetson_inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
cap = cv2.VideoCapture(0)
#Uncomment below if you want a specific size for the display window.
cap.set(3, 640)
cap.set(4, 480)

# Set up Directories for image storage.
strDir = os.getcwd()
capturesdir = str(strDir) + "/Captures/"
smokingDir = str(strDir) + "/Smoking/"

frameRate = cap.get(5) #frame rate every second
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, img = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        imgCuda = jetson.utils.cudaFromNumpy(img)
        detections = net.Detect(imgCuda)
        # Get dimensions for bounding box.
        for d in detections:
            x1, y1, x2, y2, = (
                int(d.Left),
                int(d.Top),
                int(d.Right),
                int(d.Bottom),
            )
            className = net.GetClassDesc(d.ClassID)
            # 0) Initially we detect if its a person.
            if className == "person":
                #print("Person Detected")
                # Render bounding box
                cv2.rectangle(img, (x1, y1), (x2, y2), (0,0,255), 2)
                # 1) Capture image and send to classification model.
                # Assign a UUID to image name as to avoid collisions
                imgName = str(uuid.uuid1()) + ".jpg"
                path1 = capturesdir + imgName
                path2 = smokingDir + imgName
                # Write image to Capture Directory
                cv2.imwrite(path1, img)
                # 2) Return result of Detection.
                # 2A) Set smoking variable to true if smoking was detected
                ## Uncomment Below ////////////
                smoking = smokingDetection(path1)
                #///////////////////////////
                if smoking == True:
                    # 3) Move image to Smoking directory.
                    moveImage(path1, path2,x1, y1)
                    # 4) Add label to bounding box.
                    cv2.putText(
                    img,
                    "**Detected**",
                    (x1, y1),
                    cv2.FONT_HERSHEY_DUPLEX,
                    1,
                    (0, 0, 255),
                    2,
                )
                    # 4) reset smokinng variable to false
                    smoking == False
                else:
                    # 5) Delete initial image
                    os.remove(path1)
                    # 6) reset smokinng variable to false
                    smoking == False


    cv2.imshow("Image", img)
    cv2.waitKey(1)
