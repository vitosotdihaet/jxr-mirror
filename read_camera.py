import cv2

from enum import IntEnum


WINDOW_NAME = 'debug'


class Keycode(IntEnum):
    PREV_CAM = ord('w')
    NEXT_CAM = ord('e')

    QUIT = ord('q')


def list_ports(): # taken from https://stackoverflow.com/questions/57577445/list-available-cameras-opencv-python
    is_working = True
    curr_id = 0
    working_ports = []
    while is_working:
        cam = cv2.VideoCapture(curr_id)

        if not cam.isOpened():
            is_working = False
            print(f"Port {curr_id} is not working.")
        else:
            is_reading, _ = cam.read()

            w = cam.get(3)
            h = cam.get(4)

            if is_reading:
                print(f"Port {curr_id} is working ({w} x {h})")
                working_ports.append(curr_id)

        curr_id += 1
    return working_ports


def change_cam_id(cam_id, cam, negative=False):
    if negative:
        new_cam_id = max(0, cam_id - 1)
    else:
        new_cam_id = min(255, cam_id + 1) # you don't have 256 cameras, get real

    if new_cam_id == cam_id:
        print(f'Can\'t go to new camera id. Going to previous one: {cam_id}...')
        return cam_id, cam

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

_, frame = cam.read()
if not cam.isOpened():
    print(f"Port {cam_id} is not working.")
    cam_id += 1


cv2.imshow(WINDOW_NAME, frame)

print(f'Current id of camera is {cam_id}, name of window is \'{WINDOW_NAME}\'')

while cv2.getWindowProperty(WINDOW_NAME, 0) >= 0:
    _, frame = cam.read()

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
