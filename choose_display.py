'''
This script is used for getting needed parameters for moving shown image to different display
'''

import screeninfo as si


monitors = si.get_monitors()

def get_display(display_id):
    return monitors[display_id].x, monitors[display_id].y
