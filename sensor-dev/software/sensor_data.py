import collections
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import serial
from serial.tools import list_ports
import threading
import numpy as np
import time


def find_ports():
    for p in list_ports.comports():
        if "CP2102" in p.description:
            return p.device
    return None

SERIAL_PORT = None 
if SERIAL_PORT is None:
    SERIAL_PORT = find_ports()
    print("Using port:", SERIAL_PORT)

if SERIAL_PORT is None:
    raise Exception("Serial Device not found")

BAUD = 115200

ser = serial.Serial(SERIAL_PORT, BAUD, timeout=0)

# 1. Configuration
MAX_POINTS = 50  # Keep only the last 50 data points on screen
UPDATE_INTERVAL = 50  # Update every 200 milliseconds (5Hz)

close_event = False

data_lock = threading.Lock()

x_data = collections.deque(maxlen=MAX_POINTS)
y_data = collections.deque(maxlen=MAX_POINTS)


fig, ax = plt.subplots()
line, = ax.plot([], [], label="Sensor Value", color="blue")
ax.set_ylabel("Reading")
ax.set_xlabel("Time (Ticks)")
ax.grid()
ax.legend()


ax.set_xlim(0, MAX_POINTS)
ax.set_ylim(0, 3.3)

counter = 0

def on_close(event):
    global close_event
    close_event = True


def update(frame):
    global counter

    latest_reading = None

    # Read all values currently waiting in the serial buffer
    while ser.in_waiting:
        raw = ser.readline()

        if not raw:
            break

        try:
            latest_reading = float(raw.decode("utf-8").strip())
        except ValueError:
            continue

    # Nothing new received
    if latest_reading is None:
        return line,

    # Add newest value
    with data_lock:
        x_data.append(counter)
        y_data.append(latest_reading)
        counter += 1

    # Update graph
    line.set_data(x_data, y_data)

    # Shift X-axis
    if counter > MAX_POINTS:
        ax.set_xlim(counter - MAX_POINTS, counter)

    return line,


# 4. Start the animation loop
ani = FuncAnimation(fig, update, interval=UPDATE_INTERVAL, cache_frame_data=False)
fig.canvas.mpl_connect('close_event', on_close)
plt.ion()
plt.show()


cont = True
touch_count = 0
isTouched = False
THRESHOLD = 1.75

overall_touch = 0

loopCount = 0

STABILITY_WINDOW = 10

y_curr = collections.deque(maxlen=STABILITY_WINDOW)
y_history = collections.deque(maxlen=30)

while cont:
    plt.pause(0.05)
    time.sleep(0.01)

    if close_event:
        print()
        print("Ending program")
        cont = False
        continue

    with data_lock:
        curr = len(y_data)
        if curr != -1 and curr > 10:
            y_curr.append(y_data[-1])
            y_history.append(y_data[-1])
        elif curr != -1 and curr == 10:
            y_curr.append(y_data[-1])
            y_history.append(y_data[-1])
            THRESHOLD = round(np.mean(list(y_curr)[-9:-1]) -0.03, 2)
            continue
        elif curr != -1:
            y_curr.append(y_data[-1])
            y_history.append(y_data[-1])
            continue

    if len(y_history) >= 30 and (np.std(y_history) <= 0.01) and not isTouched:
        THRESHOLD = round(np.median(y_history) - 0.03, 2)

    
    if y_curr[-1] < THRESHOLD:
        if isTouched:
            print(f"\r Sensor Value: {y_curr[-1]:.2f}".ljust(30), end="", flush=True)
            print("Pressed!".ljust(30), end="", flush=True)
            print(f"Threshold: {THRESHOLD}".ljust(30), end="", flush=True)
            print(f"Touch count: {overall_touch}".ljust(30), end="", flush=True)


        else: #Sensor is not marked as touched
            touch_count+=1
            if touch_count >= 3: #If the sensor stays under the threshold for 3 ticks, update state to touched
                isTouched = True
                touch_count = 0
                overall_touch += 1
                loopCount+=1
                continue

            print(f"\r Sensor Value: {y_curr[-1]:.2f}".ljust(30), end="", flush=True)
            print("Released!".ljust(30), end="", flush=True)
            print(f"Threshold: {THRESHOLD}".ljust(30), end="", flush=True)
            print(f"Touch count: {overall_touch}".ljust(30), end="", flush=True)
    else: #Current value >= THRESHOLD
        if isTouched:
            touch_count+=1
            if touch_count >= 6:
                isTouched = False
                touch_count=0
                loopCount +=1
                continue

            print(f"\r Sensor Value: {y_curr[-1]:.2f}".ljust(30), end="", flush=True)
            print("Released!".ljust(30), end="", flush=True)
            print(f"Threshold: {THRESHOLD}".ljust(30), end="", flush=True)
            print(f"Touch count: {overall_touch}".ljust(30), end="", flush=True)
            

        else: #Sensor is not marked as touched
            print(f"\r Sensor Value: {y_curr[-1]:.2f}".ljust(30), end="", flush=True)
            print("Released!".ljust(30), end="", flush=True)
            print(f"Threshold: {THRESHOLD}".ljust(30), end="", flush=True)
            print(f"Touch count: {overall_touch}".ljust(30), end="", flush=True)
    loopCount+=1



    