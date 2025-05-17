import cv2
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
import screen_brightness_control as abc

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Initialize pycaw for volume control
##23BCG10009
##23BCG10016
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
##23BCG10009
##23BCG10016
volume.GetMasterVolumeLevelScalar()
volbar = 400
volper = 0
volMin, volMax = volume.GetVolumeRange()[:2]

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Hand gesture for volume control
    results = hands.process(imgRGB)
    lmList = []
    
    if results.multi_hand_landmarks:
        for handlandmark in results.multi_hand_landmarks:
            ##23BCG10009
            ##23BCG10016
            for id, lm in enumerate(handlandmark.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
            mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)

        if lmList != []:
            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]
            cv2.circle(img, (x1, y1), 13, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 13, (255, 0, 0), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

            length = hypot(x2 - x1, y2 - y1)
            vol = np.interp(length, [30, 350], [volMin, volMax])
            volbar = np.interp(length, [30, 350], [400, 110])
            volper = np.interp(length, [30, 350], [0, 50])
            print(f"Volume: {vol}, Length: {int(length)}")
           ##23BCG10009
           ##23BCG10016
            volume.SetMasterVolumeLevel(vol, None)
            cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 255), 4)
            cv2.rectangle(img, (50, int(volbar)), (85, 400), (0, 0, 255), cv2.FILLED)
    
    # Hand gesture for brightness control
    results = hands.process(imgRGB)
    lmList = []

    if results.multi_hand_landmarks:
        for handLandmark in results.multi_hand_landmarks:
            for lmId, lm in enumerate(handLandmark.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([lmId, cx, cy])
                ##23BCG10009
                ##23BCG10016
                mpDraw.draw_landmarks(img, handLandmark, mpHands.HAND_CONNECTIONS)

        if lmList != []:
            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[12][1], lmList[12][2]
            cv2.circle(img, (x1, y1), 4, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 4, (255, 0, 0), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

            length = hypot(x2 - x1, y2 - y1)
            bright = np.interp(length, [15, 220], [0, 100])
            print(f"Brightness: {bright}, Length: {length}")
            abc.set_brightness(int(bright))
    
    cv2.imshow('Hand Gesture Control', img)

   
    if cv2.waitKey(1) & 0xFF == ord('k'):
        ##23BCG10009
        ##23BCG10016
        break

cap.release()
cv2.destroyAllWindows()