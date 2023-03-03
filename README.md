# AI-Virtual-Mouse
A virtual mouse used throughout the movement of hands in front of laptop's camera in order to minimize the usage of physical materials, it has all the features of the normal mouse in addition to screenshot feature.

## Project Lifecycle 

- accessing the camera 
- recognizing the hand landmarks 
- controling the mouse according to certain hand landmarks

## Tech Stack

Programming Languages : Python 3.8.16 ( updated versions won't work with Autopy library )

Libraries : autopy , cv2 , math , mediapipe , numpy , pyscreenshot , time

NB : all required libraries setup can be found in the libraries_setup notebook attached ( just run the cells :D ) 

if you faced any problem in installing the libraries please make sure that you are using python version 3.8 or less 

if you have a higher version you can simply create another enviroment with a suitable version in anaconda ( shown in the fig) then install numpy and the required libraries 

![image](https://user-images.githubusercontent.com/61950036/222779052-f79472f1-75c8-4290-85de-62686234c3b0.png)

## Libraries Details 

autopy : used to control the mouse with python 

cv2 : used to access the camera 

mediapipe : used to recognize the hand landmarks 

pyscreenshot : used to take a screenshot by python 

## Hand Poses

### Movement Pose : 

![image](https://user-images.githubusercontent.com/61950036/222793693-4be796ad-13d4-4b26-b9b0-8b25c6b7041d.png)

### Hold Pose : 

![Hold Pose](https://user-images.githubusercontent.com/61950036/222793994-1c0e2870-b7e9-4f41-b78f-eae2438a235e.png)


### Left Click with move : 

![Left Click while moving](https://user-images.githubusercontent.com/61950036/222793873-57855cda-bb0e-45d6-b18e-dffd6b2aad00.png)

### Left Click with hold : 

![Left Click with Hold pose](https://user-images.githubusercontent.com/61950036/222794140-44695716-3daf-4003-9ee8-ac318ea52ed8.png)

### Right Click : 

![Right Click ](https://user-images.githubusercontent.com/61950036/222794227-fe5ea404-553f-4b04-9ed7-c3a24cefa6c2.png)

### Screenshot Pose : 

![Screenshot Pose](https://user-images.githubusercontent.com/61950036/222794279-7a6c7bc1-eb79-479d-94d4-f762e0b3802c.png)

## Demo

![ezgif com-video-to-gif (2)](https://user-images.githubusercontent.com/126875631/222809470-fdb00930-e145-4245-83ba-b05f4e6f016f.gif)
