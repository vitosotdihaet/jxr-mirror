import cv2

# camera related imports
from keycodes import Keycode
from cam_funcs import change_cam_id

# ml related imports
import process_image as pi

WINDOW_NAME = 'JXR'

cam_id = 0 # choosing from which camera port to read

cam = cv2.VideoCapture(cam_id)

_, frame = cam.read()

cv2.namedWindow(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow(WINDOW_NAME, frame)

while True:
    _, frame = cam.read()


    cv2.imshow(WINDOW_NAME, pi.blank(frame))


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
