#library

import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy 
import pyscreenshot

######################

#varibles

wCam, hCam = 640, 480 # dimensions of the window 

frameR = 100     #Frame Reduction

smoothening = 7  #random value

pTime = 0 # prev time for the frames

plocX, plocY = 0, 0 # previous location

clocX, clocY = 0, 0 # current location

cap = cv2.VideoCapture(0)

cap.set(3, wCam)

cap.set(4, hCam)

detector = htm.handDetector(maxHands=1)

wScr, hScr = autopy.screen.size() # dimentions of the monitor

######################

while True:
    #Find the landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # Get the tip of the index and middle finger
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]

        # Check which fingers are up
        fingers = detector.fingersUp()
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                      (255, 0, 255), 2)

        # controling the mouse at (Moving Mode) if middle finger, ring finger and little finger are close
        if fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0 :
            

            # Convert the coordinates
            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

            # Smooth Values to make the mouse move easly
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # Move mouse 
            autopy.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY
            length, img, lineInfo = detector.findDistance(4, 10, img)
            
            
            
            #controling the click right like select all or drawing by closing and opening the thumb using distance
            #if distance smaller than 35 pixel it will click it the color of the ball will change to green 
            if length < 50:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.toggle(autopy.mouse.Button.LEFT,True)
                
                
            #if distance greater than 35 pixel it will relese the click
            else :
                autopy.mouse.toggle(autopy.mouse.Button.LEFT,False)

        
        # Clicking Mode(stop moving) if middle finger, ring finger and little finger are open
        if fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
              
            # Click left mouse detect if thumb equal zero
            if fingers[0] == 0 :
                autopy.mouse.click(autopy.mouse.Button.LEFT)
                
            # Click right mouse detect if index equal zero
            if fingers[1] == 0 :
                autopy.mouse.click(autopy.mouse.Button.RIGHT)
          
                
                
        
        #when you close yur hand it will take a screenshot by using pyscreenshot library
        elif  fingers[4] == 1 and fingers[0]==1 and fingers[2] == 0 and fingers[3] == 0 and fingers[1] == 0:
            print('screenshot')
            scrName = str(np.random.randint(0,999999))
            im = pyscreenshot.grab()
            im.save("%s.png"%(scrName))
            
            
             

    # Step11: Frame rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (28, 58), cv2.FONT_HERSHEY_PLAIN, 3, (255, 8, 8), 3)

    # Step12: Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)