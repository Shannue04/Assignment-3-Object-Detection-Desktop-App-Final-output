import cv2
import numpy as np

#encapsulation
class Formater:
    count = 1
    @classmethod
    def get_a_coppied_path(cls, path='', height=512, width=512):
        temp_image = cv2.imread(path)
        temp_image = cv2.resize(temp_image, (height, width))
        # path = 'temp/temp_image'+str(cls.count)+'.jpg'
        path = 'temp/temp_image.jpg'
        cv2.imwrite(path, temp_image)
        cls.count += 1

        return path
    
    @classmethod
    def resize_image(cls, image_path, height=300, width=300):
        image = cv2.imread(image_path)
        original_image = image.copy()
        _height, _width, _ = image.shape

        # Preprocess the image: resize and normalize
        input_data = cv2.resize(image, (height, width))
        print(f'b s : {input_data.shape}')
        input_data = np.expand_dims(input_data, axis=0)
        print(f'a s : {input_data.shape}')

        return (original_image, input_data, _height, _width)
    
    @classmethod
    def mark_image(cls,original_image, coordinates, height, width, label, score):
        ymin, xmin, ymax, xmax = coordinates
        (startX, startY, endX, endY) = (int(xmin * width), int(ymin * height), int(xmax * width), int(ymax * height))

        # Draw the bounding box
        label = f"{label}: {score * 100:.2f}%"
        cv2.rectangle(original_image, (startX, startY), (endX, endY), (0, 255, 0), 2)
        cv2.putText(original_image, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        return original_image
    
    @classmethod
    def save_image(cls, image, path):
        cv2.imwrite(path, image)
