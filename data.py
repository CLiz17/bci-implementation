from pyOpenBCI import OpenBCICyton
import time
from collections import deque
import numpy as np
import cv2
from hanging_threads import start_monitoring
start_monitoring(seconds_frozen=10, test_interval =100)
global counter, l
counter = -1
l = []
l .append(['Fp1','F3','C3','P3','O1','F7','T3','T5','Fp2','F4','C4','P4','O2','F8','T4','T6'])
def print_raw(sample):
    global counter, l
    counter += 1
    l.append(sample.channels_data)
    if counter>=25:
        board.stop_stream()
        print("done","L:",len(l))
        np.savetxt("test_data2.csv", l, delimiter =",",fmt ='% s')
        print("Saved file")

board = OpenBCICyton(port='COM7',daisy=True) #takes COM port on its own.
board.start_stream(print_raw)
