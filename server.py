# - **********************************************************
# - Author: Suchin T
# - Date: 2024-09-26 (YYYY-MM-DD)
# - Version: 0.1
# - Function: Server CMD Application 
# - **********************************************************

from http.server import HTTPServer, BaseHTTPRequestHandler
from jinja2 import Template
from threading import Thread
from urllib.parse import urlparse
import json
import mylib

Version = "0.1"
Server_address = "127.0.0.1"
Server_port = 8000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        url_parse = urlparse(self.path)
        path = url_parse.path
        match path:
           case '/':        
             file_name = 'index.html' 
             try:
               data = {}
               data['server_address'] = Server_address
               data['server_port'] = Server_port
               data['version'] = Version
               data['client_address'],data['client_port'] = self.client_address
               file_html = open(file_name).read()
               template = Template(file_html)
               self.send_response(200)
               self.send_header('Content-type', 'text/html')
               self.end_headers()
               self.wfile.write(bytes(template.render(data),'utf-8'))
             except Exception as err:
              print(err)
              self.send_response(404)
              self.send_header('Content-type', 'text/html')
              self.end_headers()
              self.wfile.write(b'This page is not available')
           case '/t':
             file_name = 'temp.html'
             try:
               data = {}
               data["name"] = "sukiyaki"
               data["age"] = 39
               data["gender"] = "male"
               template = Template(open(file_name).read())
               self.send_response(200)
               self.send_header('Content-type', 'text/html')
               self.end_headers()
               self.wfile.write(bytes(template.render(data),'utf-8'))
             except:
               self.send_response(4040)
               self.send_header('Content-type', 'text/html')
               self.end_headers()
               self.wfile.write(b'4040 - error')
           case '/api/get':
             try:
               data = {}
               data["Server_address"] = Server_address
               data["Server_port"] = Server_port
               data["version"] = Version
               data_j = json.dumps(data)
               self.send_response(200)
               self.send_header('Content-type', 'application/json')
               self.end_headers()
               self.wfile.write(data_j.encode('utf-8'))
             except:
               self.send_response(5040)
               self.send_header('Content-type', 'text/html')
               self.end_headers()
               self.wfile.write(b'5040 -error')
           case '/form':
             print(f'self.path = {self.path}')
             url_parse = urlparse(self.path)
             print(f'url_parse.path = {url_parse.path}')
             print(f'url_parse.query = {url_parse.query}')
             try:
                temp = mylib.Change_form_data_2_json_format(url_parse.query)
                print(f'temp = {temp}')
                if temp != 'none':
                  obj = json.loads(temp)
                  print(f'obj = {obj}')
                file_html = open("form.html").read()
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                template = Template(file_html)
                self.wfile.write(bytes(template.render(obj),'utf-8'))
             except Exception as err:
               print(f'*** Error -> {err}')
               self.send_response(404)
               self.send_header('Content-type','text/html')
               self.end_headers()
               self.wfile.write(b'Error 404')

    def do_POST(self):
        url_parse = urlparse(self.path)
        path = url_parse.path
        match path:
          case '/api/post':
            try:
              content_length = int(self.headers['Content-Length'])
              data_in = self.rfile.read(content_length)
              print(f'data_in = {data_in}')
              data_in_dic = json.loads(data_in)
              print(f'type(data_in_dic) = {type(data_in_dic)}')
              print(f'data_in_dic = {data_in_dic}')
              self.send_response(200)
              self.send_header('Content-type','application/json')
              self.end_headers()
              self.wfile.write(data_in)
            except Exception as err:
              print(f'err = {err}')
              self.send_response(6040)
              self.send_header('Content-type','text/html')
              self.end_headers()
              self.wfile.write(b'6040 - error')
          case '/form/post':
            try:
              path = urlparse(self.path).path
              print(f'self.path = {self.path}')
              print(f'path = {path}')
              content_length = int(self.headers['Content-Length'])
              client_post = self.rfile.read(content_length)
              json_format = mylib.Change_form_data_2_json_format(client_post)
              print(f'json_format = {json_format}')
              if json_format != 'none':
                 obj = json.loads(json_format)
                 print(f'obj = {obj}')
                 tempp = Template(open("result.html").read())
                 self.send_response(200)
                 self.send_header('Content-type','text/html')
                 self.end_headers()
                 self.wfile.write(bytes(tempp.render(obj),"utf-8"))
            except Exception as err:
              print(f'Error = {err}')
              self.send_response(404)
              self.send_header('Content-type', 'html/text')
              self.end_headers()
              self.wfile.write(b'Error 404') 
              
httpd = HTTPServer((Server_address, Server_port), SimpleHTTPRequestHandler)
print(f'server_address : {httpd.server_address}, port : {httpd.server_port}')
print(f"version {Version}")
httpd.serve_forever()