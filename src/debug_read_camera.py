'''
This script is used for debugging ML model
It creates a window with a stream of frames from chosen camera
Later this script will show not only the stream, but also a processed output of ML model

With this script you can change between different cameras with keys, listed in keycodes.py
For example you can use DroidCam to use your Android device as a camera
'''

import cv2

from keycodes import Keycode
from cam_funcs import change_cam_id, safe_exit
from choose_display import get_display

import process_image as pi


WINDOW_NAME = 'debug'
DISPLAY_ID = 0


cam_id = 0
cam = cv2.VideoCapture(cam_id)

_, frame = cam.read()
for cam_id in range(10 + 1):
    if cam.isOpened():
        break
    else:
        cam = cv2.VideoCapture(cam_id)
        print(f"Port {cam_id} is not working. Trying {cam_id + 1}")

    if cam_id == 10:
        print("No working cameras found. Bailing...")
        safe_exit(cam, 1)


move_display = get_display(DISPLAY_ID)

# create a window
cv2.namedWindow(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN)
cv2.moveWindow(WINDOW_NAME, move_display[0], move_display[1])
cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow(WINDOW_NAME, frame)

print(f'Created a window on display {DISPLAY_ID}.\nCurrent id of camera is {cam_id}.\nName of window is \'{WINDOW_NAME}\'')

while cv2.getWindowProperty(WINDOW_NAME, 0) >= 0:
    _, frame = cam.read()

    cv2.imshow(WINDOW_NAME, pi.reverse_color_bytes(frame))

    key = cv2.waitKey(1)

    match key:
        case Keycode.QUIT:
            break
        case Keycode.PREV_CAM:
            cam_id, cam = change_cam_id(cam_id, cam, negative=True)
        case Keycode.NEXT_CAM:
            cam_id, cam = change_cam_id(cam_id, cam)

safe_exit(cam)