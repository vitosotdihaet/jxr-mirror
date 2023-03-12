import cv2


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

def safe_exit(cam, exit_code=0):
    cam.release()
    cv2.destroyAllWindows()
    exit(exit_code)