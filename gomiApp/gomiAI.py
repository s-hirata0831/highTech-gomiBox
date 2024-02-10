from ultralytics import YOLO
from cam import getFrame
from cv2 import resize

# Load a model
model = YOLO('best.pt')

def getResultAI():
  img = getFrame();
  #img = resize(img,(600,600))
  result =  model.predict(source=img,
                conf=0.80,
                project="mypredict", # 出力先
                name="mypredict", #フォルダ名
                exist_ok=True, #上書きOKか
                save=True,
                max_det=1)

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