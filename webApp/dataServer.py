from http.server import BaseHTTPRequestHandler
from socketserver import TCPServer
import asyncio
import tracemalloc
import json
import os
import cgi
from socketserver import ThreadingMixIn

class MyHandler(BaseHTTPRequestHandler):
    my_variable="Loading"
    pet="Loading"
    upload_dir='./templates/images'
    
    def do_POST(self):
        content_type, _ = cgi.parse_header(self.headers['Content-Type'])

        if content_type == 'application/json':
            content_length=int(self.headers['Content-Length'])
            post_data=self.rfile.read(content_length)
            data=json.loads(post_data.decode('utf-8'))
        
            if self.path == '/get_variable':
                MyHandler.my_variable=data.get('value')
            elif self.path == '/get_pet':
                MyHandler.pet = data.get('value')
        
            self.send_response(200)
            self.end_headers()

        elif content_type == 'multipart/form-data':
            form_data = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD':'POST'})
            
            if 'image' in form_data:
                file_item = form_data['image']
                if file_item.filename:
                    file_path = os.path.join(MyHandler.upload_dir, file_item.filename)
                    with open(file_path, 'wb') as file:
                        file.write(file_item.file.read())
                    
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write("画像のアップロードが成功しました".encode())
                    return
    
    def do_GET(self):
        #loop = asyncio.new_event_loop()
        #asyncio.set_event_loop(loop)
        #loop.run_until_complete(self.handle_request())
    
    #def handle_request(self):
        #tracemalloc.start()
        
        if self.path == '/get_variable':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            #MyHandler.my_variable = "50%"
            
            self.wfile.write(MyHandler.my_variable.encode())
            
        elif self.path == '/get_pet':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(MyHandler.pet.encode())
        elif self.path == '/get_image':
            image_path = './templates/images/predict.jpeg'
            try:
                with open('./templates/images/predict.jpeg', 'rb') as image_file:
                    image_date = image_file.read()
                    
                self.send_response(200)
                self.send_header('Conyeny-type', 'image/jpeg')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                self.wfile.write(image_data)
            except FileNotFoundError:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                self.wfile.write("File not found".encode())
        else:
            super().do_GET()
            
if __name__ == '__main__':
    if not os.path.exists(MyHandler.upload_dir):
        os.makedirs(MyHandler.upload_dir)

    server_adress = ('', 5000)
    httpd = TCPServer(server_adress, MyHandler)
    print('Starting server on port 5000...')
    httpd.serve_forever()
