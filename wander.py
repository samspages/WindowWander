import os
import pygetwindow as gw
import threading
from screeninfo import get_monitors
import keyboard
import time
import random
import pyrect

monitor_display = 1

def get_main(monitor_index):
    monitors = get_monitors()
    if monitors:
        return monitors[monitor_index]
    else:
        return None

def window_walk(id, stop):
    visited = set()

    # self-avoidance variation
    def drunk_step(pos):
        while True:
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            random.shuffle(directions)
            for dx, dy in directions:
                new_pos = (pos.x + dx, pos.y + dy)
                if new_pos not in visited:
                    return dx, dy
            return 1, 1

    os.system("start chrome --new-window --app=https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJtdDNtZ2hndHExaDk0Z3B4NDRhdjh6OTliZGw5N3drZDE5MnhvZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/AwNGX4XvvODO8/giphy.webp")
    time.sleep(0.4) # yup
    
    main_display = get_main(monitor_display)
    main_x = main_display.x
    main_y = main_display.y
    windows = gw.getWindowsWithTitle("Big Cat LOL GIF")
    
    if windows:
        window = windows[0]
        window.resizeTo(600, 525)
        main_x += 760
        main_y += 300
        window.moveTo(main_x, main_y) 

        while True:
            pos = window.topleft
            dx, dy = drunk_step(pos)
            window.moveTo(pos.x + dx, pos.y + dy)
            visited.add((pos.x, pos.y))
            time.sleep(0.075)

            if stop():
                break
    else:
        raise RuntimeError("none windows")

def main(): 
    stop_threads = False
    tmp = threading.Thread(target=window_walk, args=(id, lambda: stop_threads))
    tmp.start()

    while not stop_threads:
        if keyboard.is_pressed("]"):
            stop_threads = True
            tmp.join()
            print('exiting')

    windows = gw.getWindowsWithTitle("Big Cat LOL GIF")
    if windows:
        for window in windows:
            window.close()

if __name__ == '__main__':
    main()