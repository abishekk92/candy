import eventlet
from eventlet.green import BaseHTTPServer as HTTPServer 
import config as config_parser
import os
HOSTNAME=config_parser.get_hostname()
PORT=config_parser.get_port()
number=0
class ServerHandler(HTTPServer.BaseHTTPRequestHandler):
	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type","text/html")
		s.end_headers()
	def do_GET(s):
		try:
			to_write=open(os.getcwd()+s.path,'r').read()
			s.send_response(200)
		except:
			s.send_response(404)
			to_write="Page not found"
		s.send_header("Content-type","text/html")
		s.end_headers()
		s.wfile.write(to_write)
if __name__=="__main__":
	server=HTTPServer.HTTPServer
	httpd=server((HOSTNAME,PORT),ServerHandler)
	print "Server started at",HOSTNAME,PORT
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		httpd.server_close()


