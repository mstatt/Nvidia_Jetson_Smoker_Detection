# Smoker Detection for Jetson Nano

<div id="top"></div>
<div align="center">
  
![](https://img.shields.io/badge/Language-Python-blue)
![](https://img.shields.io/badge/BASH-LINUX-brightgreen)
![](https://img.shields.io/badge/License-MIT-blue)

  
</div>



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/mstatt/Nvidia_Jetson_Smoker_Detection">
    <img src="assets/logo.png" alt="Logo" >
  </a>
</div>

## Smoker Detection for Jetson Nano

  <p align="center">
    A basic project to deploy a smoker detection application on a Jetson Nano (4GB), using the Jetson-Interface libraries as well as the Roboflow Docker container with a model that I trained, but all running locally. The basics are as follows:
    The USB camera streams to the initial model to detect a person which then captures the image and sends to the pre-trained model running on the roboflow docker image and checks for the appearence of a cigarette. If a cigarette is detected the model writes "Potential Smoker" to the image and saves it in the Smoking folder for later viewing. If the person is not smoking, the image is deleted from the capture directory.
    <br />

  </p>
  <p align="center">
    I am aware that this could be furthjer optimized from every Nth frame check to further training the model on Roboflow. My intention was not for perfection but rather for demonstration that this and other CV projects can be developed and deployed on the Jetson architecture. Feel free to fork and build on making this even faster and more accurate.
    <br />

  </p>

<!-- GETTING STARTED -->
## Getting Started

In order to get this project up and running it is assumed that you have already flashed and set up the Ubuntu desktop enviorment.



<!-- USAGE EXAMPLES -->
## Set Up
```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```
  <p align="center">
    All you need to do is the following:
    <br />
    <ol>
Get an account on roboflow.com, you will need this to use the inference call.
Once you set up an account locate your API key.
<li> Get an API key from roboflow.com</li>

<li> Replace the <API KEY> in the smoking_detection.py file with your API Key</li>
<li> Do not forget to save the file after editing.</li>
<li> Now you need to give the scripts the correct permissions to be able to run on the Jetson Nano.</li>
<li> Navigate to the directory containing the (max.sh and the start_smoking_container.sh) files.</li>
<li> Open a terminal in that directoy and run the following commands.</li>
```
>> sudo chmod u+x installs.sh
```
<br/>
```sh
>> sudo chmod u+x max.sh
```
  <br/>
```sh
>> sudo chmod u+x start_smoking_container.sh
```
<li> Now that your scripts can be ran start all of the required installs by running the following:</li>
```sh
>> sudo ./start_Smoking_container.sh
```
<li> You may get asked inf you want to install certain libraries etc, type Y and let run.</li>
<li> When you get to the Models options window, please be sure to select (ssd-mobilenet-v2).</li>
<li> Upon completion your Nano should reboot.</li>
  </p>
</ol>



<!-- OUTPUT -->
## Start Up

  <p align="center">
    Once the install finish and the Nano reboots you can test the application as follows:
    <br />
    <ol>
<li> Log back into the device.</li>
<li> Navigate to the root folder of the project.</li>
<li> First we will boost the performance of the Nano.</li>
<li> Open a terminal and enter the following:</li>
```sh
>> boost clocks
```
<br/>
```sh
>> sudo ./max.sh
```
  <li> Now we will start the Smoking detection Docker Container:</li>
```sh
>> sudo ./start_Smoking_container.sh
  ```
<li> Now open another terminal in the same directory and enter the following:</li>
```sh
>> python3 smoking_detection.py
```
  <li>The initial run may take a few minutes to load and start inferencing based on the Docker container as well as the 2 models the stream runs through. Remember initially we need to detect that a person is there, then we detect if that person has a cigarette.</li>
</ol>


Your display should resemble the images below. Be sure to check the "Smoking" directory for any captured images of smokers.

No Detection           |  Smoker Detected
:-------------------------:|:-------------------------:
![A1] |  ![B2]  


No Detection           |  Smoker Detected
:-------------------------:|:-------------------------:
![C3] |  ![D4]  



</p>


<!-- CONTACT -->
## Contact

Project Link: [https://github.com/mstatt/Nvidia_Jetson_Smoker_Detection]



<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

![](https://img.shields.io/badge/License-MIT-blue)



<!-- MARKDOWN LINKS & IMAGES -->
[license-shield]: assets/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6f74686e65696c647265772f426573742d524541444d452d54656d706c6174652e7376673f7374796c653d666f722d7468652d6261646765.svg?style=for-the-badge
[license-url]: https://github.com/mstatt/Emotion_Detection/blob/main/LICENSE.txt
[demo-url]: https://www.youtube.com/watch?v=AWB2cEKcME0

[A1]: assets/1.png
[B2]: assets/2.png
[C3]: assets/3.png
[D4]: assets/4.png
