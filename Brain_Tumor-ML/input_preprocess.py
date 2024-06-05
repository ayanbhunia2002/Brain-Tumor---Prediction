import numpy as np
import cv2

def preprocess_image_1(file_content):
    image = cv2.imdecode(np.frombuffer(file_content, np.uint8), cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("Could not read the image file.")
    image = cv2.resize(image, (128, 128))  # Resize to 128x128
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    img = image / 255.0
    img = np.expand_dims(img, axis=-1)  # Add a channel dimension
    return img

def preprocess_image_2(file_content):
    image = cv2.imdecode(np.frombuffer(file_content, np.uint8), cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("Could not read the image file.")
    image = cv2.resize(image, (32, 32))  # Resize to 128x128
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    print(image)
    return image.flatten()
     