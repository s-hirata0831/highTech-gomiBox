import cv2
capture = cv2.VideoCapture(0)
def getFrame():
  ret = False
  while(ret == False):
    ret, frame = capture.read()
  frame = cv2.resize(frame, (300, 300))
  return frame