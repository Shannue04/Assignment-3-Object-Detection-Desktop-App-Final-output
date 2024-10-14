import tensorflow as tf
from formater import Formater

#Singletone Class
class ObjectDetector:
    model_path = "TFLite_model/detect.tflite"
    labels_path = "TFLite_model/labelmap.txt"

    object_detector = None
    
    @classmethod
    def get_instance(cls):
        if cls.object_detector is None:
            cls.object_detector = ObjectDetector()

        return cls.object_detector

    def __init__(self):
        self.interpreter = tf.lite.Interpreter(model_path=self.model_path)
        self.interpreter.allocate_tensors()

        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        self.labels = self._load_labels(label_file=self.labels_path)


    def _load_labels(self, label_file):
        with open(label_file, 'r') as f:
            return {i: label.strip() for i, label in enumerate(f.readlines())}
    
    def detect(self, image_path, threshold=0.5):
        orginal_image, input_data, height, width = Formater.resize_image(image_path=image_path)
        # Set the tensor to the input data
        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
        self.interpreter.invoke()
        print('Image setting to tensor done')

        # Get detection results
        boxes = self.interpreter.get_tensor(self.output_details[0]['index'])[0]  # Bounding box coordinates
        classes = self.interpreter.get_tensor(self.output_details[1]['index'])[0]  # Class index
        scores = self.interpreter.get_tensor(self.output_details[2]['index'])[0]  # Confidence score

        print(f'get score  : {scores}')
        print(f'classes : {classes}')
        print(f'boxes : {boxes}')

        # Process each detection
        for i in range(len(scores)):
            if scores[i] > threshold:
                orginal_image = Formater.mark_image(original_image=orginal_image, coordinates=boxes[i],height=height,width=width, label=self.labels[int(classes[i])],score=scores[i])
                
         
        print(f'final image shape : {orginal_image.shape}')
        output_path = 'temp/output.jpg'

        Formater.save_image( orginal_image, output_path)

        return output_path