# This work is licensed under the MIT license.
# Copyright (c) 2013-2023 OpenMV LLC. All rights reserved.
# https://github.com/openmv/openmv/blob/master/LICENSE
#
# Hello World Example
#
# openmv_brick_detection.py

import sensor, image, time
import pyb
from pyb import UART

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(True)
sensor.set_auto_whitebal(True)

clock = time.clock()

COLOR_THRESHOLDS = [
    (20, 40, 30, 50, 25, 50), # Red threshold (RGB: R_min, R_max, G_min, G_max, B_min, B_max)
    (25, 45, -50, -20, 10, 32) # Green threshold (LAB: L_min, L_max, A_min, A_max, B_min, B_max)
]

RED_COLOR = (255, 0, 0)
GREEN_COLOR = (0, 255, 0)
TEXT_COLOR = (255, 255, 255) # White text for contrast, though not used for "Unknown" anymore
uart = UART(3, 9600)
blue_led = pyb.LED(3)

while(True):
    uart.write(bytearray([0]))
    #basically the code just sends '0' to the evn
    #this code is just to test whether the serial works
    #like if the connections and stuff are correct
    #it doesnt send the actual obstacle stuff yet

    blue_led.on() #easier debugging because can tell if the code is running from the blue led
#    time.sleep(1000)
    clock.tick()
    img = sensor.snapshot()

    screen_midpoint_x = img.width() // 2

    img.draw_line(screen_midpoint_x, 0, screen_midpoint_x, img.height(), color=(255, 255, 255), thickness=1)

    blobs = img.find_blobs(COLOR_THRESHOLDS, pixels_threshold=200, area_threshold=200, merge=True)

    if blobs:
        for blob in blobs:
            center_x = blob.cx()

            # Initialize color_name and draw_color based on the detected blob's code.
            # Since blobs are only found if they match a threshold, these will always be set.
            color_name = "" # Will be set to "Red" or "Green"
            draw_color = (0, 0, 0) # Will be set to RED_COLOR or GREEN_COLOR

            if blob.code() & 0b001: # Checks if the first threshold (Red) was matched
                color_name = "Red"
                draw_color = RED_COLOR
            if blob.code() & 0b010: # Checks if the second threshold (Green) was matched
                color_name = "Green"
                draw_color = GREEN_COLOR

            side_of_screen = ""
            if center_x < screen_midpoint_x:
                side_of_screen = "Left side"
            else:
                side_of_screen = "Right side"

            img.draw_rectangle(blob.rect(), color=draw_color, thickness=2)
            img.draw_cross(center_x, blob.cy(), color=draw_color, size=10)
            img.draw_string(blob.x(), blob.y() - 10, "%s (%s)" % (color_name, side_of_screen), color=draw_color, scale=1.5)
            print("%s brick detected on the %s" % (color_name, side_of_screen))

    else:
        print("No bricks detected.")

    print("FPS: %f" % clock.fps())
