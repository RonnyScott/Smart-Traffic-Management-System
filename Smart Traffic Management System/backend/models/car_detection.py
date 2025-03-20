import cv2
import torch

# Load the YOLO model (pre-trained)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def detect_cars(image_path):
    image = cv2.imread(image_path)
    results = model(image)
    results.show()  # Show image with detected cars
    return results.pandas().xyxy[0]  # Bounding box results

if __name__ == "__main__":
    detect_cars('test.jpg')  # Test with a sample image
