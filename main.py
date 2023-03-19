import cv2

import lib.cam_funcs as cf
import lib.ml.main as ml
import lib.process_file as pf
import lib.create_output_image as oi

from lib.process_text import create_file_name
from lib.keycodes import Keycode


cam_id = 0
WINDOW_NAME = 'JXR'
DISPLAY_ID = 0


cam = cf.create_fullscreen_window(WINDOW_NAME, cam_id, DISPLAY_ID)

while cv2.getWindowProperty(WINDOW_NAME, 0) >= 0:
    _, frame = cam.read()

    texts = ml.get_text_from_image(frame)
    for text in texts:
        filename = create_file_name(text)
        opened_file = pf.find_file(filename)
        frame = oi.text_to_img(opened_file)
    cv2.imshow(WINDOW_NAME, frame)

    key = cv2.waitKey(1)

    match key:
        case Keycode.QUIT:
            break
        case Keycode.PREV_CAM:
            cam_id, cam = cf.change_cam_id(cam_id, cam, negative=True)
        case Keycode.NEXT_CAM:
            cam_id, cam = cf.change_cam_id(cam_id, cam)

cf.safe_exit(cam)