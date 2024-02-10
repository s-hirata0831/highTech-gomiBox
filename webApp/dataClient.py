import requests
import json
import time

def send_post_request(value):
	url='http://172.20.10.2:5000/get_variable'
	data={'value': value}
	headers={'Content-type': 'application/json'}
	
	response=requests.post(url, data=json.dumps(data), headers=headers)
	
	if response.status_code == 200:
		print('POST request successfull -CAN-')
	else:
		print(f'POST request faiiled with status code: {response.status_code}')

def send_pet(value):
	url='http://172.20.10.2:5000/get_pet'
	data={'value': value}
	headers={'Content-type': 'application/json'}
	
	response=requests.post(url, data=json.dumps(data), headers=headers)
	
	if response.status_code == 200:
		print('POST request successfull -PET-')
	else:
		print(f'POST request faiiled with status code: {response.status_code}')

def send_image(file_path):
    url = 'http://172.20.10.2:5000/get_image'

    with open(file_path, 'rb') as file:
        files = {'image': (file.name, file, 'image/jpeg')}
        response = requests.post(url, files=files)

        if response.status_code == 200:
            print('画像のアップロードが成功しました')
        else:
            print(f'ステータスコード {response.status_code} で画像のアップロードに失敗しました')

		
if __name__ == '__main__':
	can=52
	pet=22
	image_path='C:\Users\hirat\Pictures\壁紙\411091332-New_York_USA_4752x3168_r-NkR8-1536x864-MM-100.jpeg'
	while True:
		send_post_request(str(can)+'本')
		send_pet(str(pet)+'本')
		can+=1
		pet+=1
		send_image(image_path)
		time.sleep(5)
	ser.close()
