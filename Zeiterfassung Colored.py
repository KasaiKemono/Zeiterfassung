import time
import sys
from time import strftime
from colorama import init
init()

iterate = 1

while True:
    if iterate == 1:
        color = '\033[31m'
    elif iterate == 2:
        color = '\033[32m'
    elif iterate == 3:
        color = '\033[34m'
        iterate = 0


    def time_convert(sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        print(color + "Time lapsed: {0}:{1}:{2}".format(int(hours), int(mins), sec))


    print(color)
    input("Press Enter to start")
    print(color + strftime('%H:%M:%S'))
    start_time = time.time()
    input("Press Enter to stop")
    print(color + strftime('%H:%M:%S'))
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    iterate = iterate + 1
