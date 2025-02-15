import cv2
import os
import string

# Correct the path by specifying the image file name and extension
img_path = r"C:\Users\Admin\Desktop\APP\IBM\mypic.jpg"  # Update with the actual image file name and extension

# Read the image
img = cv2.imread(img_path)  # Correct image path with extension

# Ensure image is in color (RGB format)
if img is None:
    print("Error: Image not found!")
    exit()

# Get image dimensions
height, width, channels = img.shape

# Take user input for secret message and passcode
msg = input("Enter secret message:")
password = input("Enter a passcode:")

# Check if the image can hold the message
message_length = len(msg)
pixels_needed = message_length * 3  # 3 channels per pixel (RGB)
if pixels_needed > height * width:
    print("Error: Image is too small to hold the entire message.")
    exit()

# Create the dictionaries
d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Initialize the indices for pixel manipulation
m, n, z = 0, 0, 0

# Embed the message into the image
for i in range(message_length):
    img[n, m, z] = d[msg[i]]  # Encode message character into the image pixel
    n = n + 1
    m = m + 1
    z = (z + 1) % 3  # Loop through the RGB channels

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

# Decrypt the message
message = ""
n, m, z = 0, 0, 0

# Ask for the passcode to decrypt
pas = input("Enter passcode for Decryption")
if password == pas:
    for i in range(message_length):
        message = message + c[img[n, m, z]]  # Decode the pixel value to get the message
        n = n + 1
        m = m + 1
        z = (z + 1) % 3  # Loop through the RGB channels
    print("Decryption message:", message)
else:
    print("YOU ARE NOT authorized")
