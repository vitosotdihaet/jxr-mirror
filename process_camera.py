import cv2

# camera related imports
from keycodes import Keycode
from cam_funcs import change_cam_id

# ml related imports
from ml import process_img


cam_id = 0 # choosing from which camera port to read

cam = cv2.VideoCapture(cam_id)

while True:
    _, frame = cam.read()


    processed_img = process_img(frame) # here all the processing happens


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
