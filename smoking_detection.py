"""
2023 Jan Smoking Detection Project
Michael Stattelman
Deployed on Nvidia Jetson Nano
"""

import os
import cv2
import uuid
import json
import shutil
import subprocess
import jetson_inference
import jetson.utils


def smokingDetection(initImg):
    """
    Function to take in image as a param and run against detection model
    """
    # Run initImage across the trained Model for classification.
    try:
        CurlUrl = (
            "base64 "
            + initImg
            + ' | curl -d @- "http://localhost:9001/smoking-detection-08o4g/1?api_key=<API KEY>"'
        )
        status, stroutput = subprocess.getstatusoutput(CurlUrl)
        y = json.dumps(stroutput)
        x = str(y).find("confidence")
        # Strip extra chars
        confidence = str(y[x + 14 : x + 19]).strip()
        fconf = float("".join(c for c in confidence if (c.isdigit() or c == ".")))
        #print(str(confidence))
        if float(fconf) >= float(0.82):
            #print(str(fconf))
            return True
        else:
            return False

    except:
        return False


def moveImage(path1, path2):
    # FUnction to move images from Capture to Smoking directories
    shutil.move(path1, path2)




net = jetson_inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
cap = cv2.VideoCapture(0)
#Uncomment below if you want a specific size for the display window.
#cap.set(3, 640)
#cap.set(4, 480)

# Set up Directories for image storage.
strDir = os.getcwd()
capturesdir = str(strDir) + "/Captures/"
smokingDir = str(strDir) + "/Smoking/"

while True:
    success, img = cap.read()
    imgCuda = jetson.utils.cudaFromNumpy(img)
    detections = net.Detect(imgCuda)
    # GEt dimensions for bounding box.
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
            smoking = smokingDetection(path1)
            if smoking == True:
                # 3) Move image to Smoking directory.
                moveImage(path1, path2)
                # 4) Add label to bounding box.
                cv2.putText(
                img,
                "Potential Smoker",
                (x1 + 5, y1 + 15),
                cv2.FONT_HERSHEY_DUPLEX,
                0.75,
                (255, 0, 255),
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
