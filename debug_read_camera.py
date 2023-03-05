'''
This script is used for debugging ML model
It creates a window with a stream from chosen camera
Later this script will show you not only the stream, but also an output of ML model

With this script you can change between different cameras with keys, listed in keycodes.py
For example you can use DroidCam to use your Android device as a camera
'''

import cv2

from keycodes import Keycode
from cam_funcs import change_cam_id


WINDOW_NAME = 'debug'

cam_id = 0

cam = cv2.VideoCapture(cam_id)

_, frame = cam.read()
if not cam.isOpened():
    print(f"Port {cam_id} is not working.")
    cam_id += 1

cv2.imshow(WINDOW_NAME, frame)

print(f'Current id of camera is {cam_id}, name of window is \'{WINDOW_NAME}\'')

while cv2.getWindowProperty(WINDOW_NAME, 0) >= 0:
    _, frame = cam.read()

    # this will be changed to show ml-processed image + original image
    cv2.imshow(WINDOW_NAME, frame)

    key = cv2.waitKey(1)

    match key:
        case Keycode.QUIT:
            break
        case Keycode.PREV_CAM:
            cam_id, cam = change_cam_id(cam_id, cam, negative=True)
        case Keycode.NEXT_CAM:
            cam_id, cam = change_cam_id(cam_id, cam)

cam.release()
cv2.destroyAllWindows()
