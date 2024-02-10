from ultralytics import YOLO
from cam import getFrame
from cv2 import resize
from time import sleep

# Load a model
onnx_model = YOLO('best.onnx')

def getResultAI():
  img = getFrame();
  
  result = onnx_model.predict(img,
                              save=True,
                              imgsz=640,
                              conf=0.91,
                              iou=0.0001,
                              device='cpu',
                              max_det=1,
                              project="mypredict",
                              name="mypredict",
                              exist_ok=True)
  
  for single_result in result:
    if len(single_result.boxes) > 0:
      result_label_num = single_result.boxes.cls.item()
      if(result_label_num == 0):
        result_label = 'CAN'
      else:
        result_label = 'PET'
    else:
      result_label = None
  print(result_label)
  return result_label