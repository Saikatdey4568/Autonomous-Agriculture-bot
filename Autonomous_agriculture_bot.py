import cv2
# import requests
import numpy as np
import urllib.request



# Define the coordinates for the three flower pots' ROI
flower_pots = [
    [(50, 140), (150, 240)],  # ROI for Flower Pot 1 (top-left to bottom-right)
    [(250, 20), (350, 120)],  # ROI for Flower Pot 2
    [(450, 140), (550, 240)],  # ROI for Flower Pot 3
    [(250, 280), (350, 380)]  # ROI for Return Rectangle
]

# Define the URLs for different actions on the ESP8266
esp8266_base_url = 'http://esp8266_ip_address'  # Replace with your ESP8266's IP address
forward_url = esp8266_base_url + '/forward'
return_url = esp8266_base_url + '/return'

# Define a function to handle mouse clicks
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        for i, (start, end) in enumerate(flower_pots):
            if start[0] <= x <= end[0] and start[1] <= y <= end[1]:
                if i < 3:
                    print(f"Clicked on Flower Pot {i+1}")
                    resp = urllib.request.urlopen(url + 'FORWARD')
                    # Send a POST request to move the smart car forward
                    # response = requests.post(forward_url)
                    # print(response.text)
                elif i == 3:
                    print(f"Clicked on Return")
                    resp = urllib.request.urlopen(url + 'FORWARD')
                    # Send a POST request to return the smart car
                    # response = requests.post(return_url)
                    # print(response.text)

# Create a blank image
image = np.zeros((400, 600, 3), dtype=np.uint8)

# Display the flower pots on the image
for (start, end) in flower_pots:
    cv2.rectangle(image, start, end, (0, 255, 0), 2)

# Display the image
cv2.imshow('Flower Pots', image)

# Set the mouse callback function
cv2.setMouseCallback('Flower Pots', click_event)

# Wait for a key press and close the window on pressing 'q'
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# Release all OpenCV windows
cv2.destroyAllWindows()