import cv2

from ml import process_img

from enum import IntEnum


class Keycode(IntEnum):
    PREV_CAM = ord('w')
    NEXT_CAM = ord('e')

    QUIT = ord('q')


def change_cam_id(cam_id, cam, negative=False):
    if negative:
        new_cam_id = cam_id - 1
    else:
        new_cam_id = cam_id + 1

    new_cam = cv2.VideoCapture(new_cam_id)

    if new_cam.isOpened():
        print(f'New camera id is {new_cam_id}')
        cam.release()
        return new_cam_id, new_cam
    else:
        print(f'Port {new_cam_id} is not working. Going to previous id: {cam_id}...')
        new_cam.release()
        return cam_id, cam


cam_id = 0

cam = cv2.VideoCapture(cam_id)

while True:
    _, frame = cam.read()

    process_img(frame)

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
