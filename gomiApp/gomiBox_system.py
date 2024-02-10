from time import sleep, time

from playMp3 import playMp3 as p
from gomiAI import getResultAI as ai
from servo import openPetCover as oPET, openCanCover as oCAN, closePetCover as cPET, closeCanCover as cCAN
from irSignal import readIR, resultIsCAN, setOpenSignalPin, readResetNumSw
import json
import requests

def getUp():
  cCAN()
  cPET()
  #sleep(3)
  print("GOMI BOX GET UP NOW")
  p('WindowsXP.mp3')

def reset():
  global can_cnt
  global pet_cnt
  print("play_error!")
  p('error.mp3')
  can_cnt = 0
  pet_cnt = 0
  send_post_request(str(can_cnt)+'本')
  send_pet(str(pet_cnt)+'本')
  closeCover()

def pushedResetNumButton():
  return readResetNumSw()

def waitGomi():
  result = ai()
  while(result == None):
    print(pushedResetNumButton())
    if(pushedResetNumButton()):
      reset()
      return 'reset'
    #sleep(0.3)
    result = ai()
  p('WAON.mp3')
  return result

def closeCover():
  cCAN()
  cPET()
  setOpenSignalPin(False)

def setCanPinOutput(result):
  if(result == 'CAN'):
    resultIsCAN(True)
  else:
    resultIsCAN(False)

def openCover(result):
  if(result == 'CAN'):
    oCAN()
  else:
    oPET()
  sleep(0.7)
  setOpenSignalPin(True)

def waitSignal():
  start_time = time()
  while(readIR() == False):
    now_time = time()
    wait_time = now_time - start_time
    if(wait_time > 15.0 or pushedResetNumButton()):
      if(pushedResetNumButton()):
        reset()
      return False
  p('PayPay.mp3')
  return True

def countCANandPET(result):

  if(result == 'CAN'):
    global can_cnt
    can_cnt += 1
    send_post_request(str(can_cnt)+'本')
    
  else:
    global pet_cnt
    pet_cnt += 1
    send_pet(str(pet_cnt)+'本')

def cntCondition():
  global can_cnt
  global pet_cnt
  global max_can_cnt
  global max_pet_cnt

  if(can_cnt < max_can_cnt and pet_cnt < max_pet_cnt):
    return 0
  elif(can_cnt == max_can_cnt and pet_cnt < max_pet_cnt):
    return 1
  elif(can_cnt < max_can_cnt and pet_cnt == max_pet_cnt):
    return 2
  else:
    return 3

def send_post_request(value):
  url='http://172.20.10.2:5000/get_variable'#IPアドレスをウェブアプリ側のIPに変更
  data={'value': value}
  headers={'Content-type': 'application/json'}

  response=requests.post(url, data=json.dumps(data), headers=headers)

  if response.status_code == 200:
    print('POST request successfull -CAN-')
  else:
    print(f'POST request faiiled with status code: {response.status_code}')

def send_pet(value):
  url='http://172.20.10.2:5000/get_pet'#IPアドレスをウェブアプリ側のIPに変更
  data={'value': value}
  headers={'Content-type': 'application/json'}

  response=requests.post(url, data=json.dumps(data), headers=headers)

  if response.status_code == 200:
    print('POST request successfull -PET-')
  else:
    print(f'POST request faiiled with status code: {response.status_code}')

def send_image(file_path):
  url = 'http://172.20.10.2:5000/get_image'#IPアドレスをウェブアプリ側のIPに変更

  with open(file_path, 'rb') as file:
    files = {'image': (file.name, file, 'image/jpeg')}
    response = requests.post(url, files=files)

    if response.status_code == 200:
      print('画像のアップロードが成功しました')
    else:
      print(f'ステータスコード {response.status_code} で画像のアップロードに失敗しました')


def main():
  cnt_condition = cntCondition()
  all_ok = 0
  can_full = 1
  pet_full = 2
  all_full = 3

  if(cnt_condition != all_full):
    result = waitGomi()
    if(result == 'reset'):
      return 0 # reset
    if((cnt_condition == all_ok) or (cnt_condition == can_full and result != 'CAN') or (cnt_condition == pet_full and result != 'PET')):
      setCanPinOutput(result)
      openCover(result)
      if(waitSignal()):
        countCANandPET(result)
        sleep(2)
      closeCover()
  return 1

#------------------------------main--------------------------
can_cnt = 0
pet_cnt = 0
max_can_cnt = 14
max_pet_cnt = 14
send_post_request(str(can_cnt)+'本')
send_pet(str(pet_cnt)+'本')
  
getUp()
while(True):
  main()
  sleep(2)
