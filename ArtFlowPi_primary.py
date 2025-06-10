import cv2
import mediapipe as mp
import numpy as np
import time as t
import sys

mssg1 = ("Welcome to the **Virtual Painter INTERFACE**\n"
         "HERE YOU WILL ENJOY THE __MAGIC OF AI UTILISATION YOUR INDEX POINTERS__ FOR A CANVAS! ")
c, sec = 0, 0.04
for i in mssg1:
    print(i, end="")
    if c % 2 == 0:
        t.sleep(sec)
    else:
        t.sleep(sec + 0.09)
    c += 1

message = "Pls ENTER YOUR NAME"
sys.stdout.write('\n\r' + message + ': ')
sys.stdout.flush()
t.sleep(0.5)
sys.stdout.write('\r' + message + '  ')
sys.stdout.flush()
t.sleep(0.5)
user_name = input()

mssg3 = f"CURATING VIRTUAL GUI....\nUnpacking imported modules..\n\nGetCall() _*APACHE LICENSE 2.0 Vision Lib...\n"
mssg4 = f"MediaPipe Tasks (low-code API): deploy advanced on-device ML solutions..\n{user_name}'s canvas_en-route/taskPATH:\n\nLAUNCH !"
for j in mssg3:
    print(j, end="")
    if c % 2 == 0:
        t.sleep(sec - 0.05)
    else:
        t.sleep(sec)
    c += 1
for j in mssg4:
    print(j, end="")
    if j == user_name:
        sec = 0.01
    elif c % 2 == 0:
        t.sleep(sec)
    else:
        t.sleep(sec + 0.05)
    c += 1

# Call the function to start the blinking cursor effect

# Call the function to start the blinking cursor effect


# Initialize Mediapipe hand model
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)

# Define the color options
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]  # Red, Green, Blue
color_names = ['Red', 'Green', 'Blue']

# Initialize variables
cursor_pos = (0, 0)
prev_pos = None
selected_color = (0, 0, 0)  # Default drawing color (black)
is_eraser_active = False

# Initialize OpenCV video capture
cap = cv2.VideoCapture(0)

# Create an empty canvas
canvas = None

# Create a window for the canvas


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            cursor_pos = (int(index_tip.x * frame.shape[1]), int(index_tip.y * frame.shape[0]))
            break  # Consider only the first detected hand

        # Detect color selection or eraser activation
        for i, color in enumerate(colors + [(255, 255, 255)]):  # Adding white for eraser
            top_left = (10, 50 + i * 50)
            bottom_right = (100, 100 + i * 50)
            if top_left[0] <= cursor_pos[0] <= bottom_right[0] and top_left[1] <= cursor_pos[1] <= bottom_right[1]:
                if i < len(colors):  # Color selection
                    selected_color = colors[i]
                    is_eraser_active = False
                else:  # Eraser selected
                    is_eraser_active = True
                break

    # Draw color options
    for i, color in enumerate(colors + [(255, 255, 255)]):  # Adding white for eraser visually
        top_left = (10, 50 + i * 50)
        bottom_right = (100, 100 + i * 50)
        cv2.rectangle(frame, top_left, bottom_right, color, -1)
        text = color_names[i] if i < len(color_names) else 'Eraser'
        cv2.putText(frame, text, (20, 75 + i * 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    # Drawing operation
    if prev_pos and cursor_pos:
        if is_eraser_active:
            cv2.line(canvas, prev_pos, cursor_pos, (0, 0, 0), 20)  # Use black color for eraser
        else:
            cv2.line(canvas, prev_pos, cursor_pos, selected_color, 5)  # Draw with selected color

    prev_pos = cursor_pos if results.multi_hand_landmarks else None

    # Draw circular pointer at the index finger-tip
    if results.multi_hand_landmarks:
        index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        cv2.circle(frame, (int(index_tip.x * frame.shape[1]), int(index_tip.y * frame.shape[0])), 15, (128, 128, 128),
                   -1)

    # Composite the canvas and the frame (without displaying art in the Virtual Painter window)pan

    # Display the composite in the 'Virtual Painter' window (without art)
    cv2.imshow('Virtual Painter', frame)

    # Display the canvas in the 'Canvas' window
    cv2.imshow(f"{user_name}'s Canvas", canvas)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        canvas = np.zeros_like(frame)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
mssg5 = "\n\n***** Thank you for using our SERVICE!!! *****\nGROUP PI3\ncore Dev : ADITYA R SAHOO"
for k in mssg5:
    print(k, end="")
    if k == "1":
        sec = 0.001
    elif c % 2 == 0:
        t.sleep(sec)
    else:
        t.sleep(sec + 0.07)
    c += 1
