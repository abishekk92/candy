import BaseHTTPServer as HTTPServer 
import config as config_parser
HOSTNAME=config_parser.get_hostname()
PORT=config_parser.get_port()
class ServerHandler(HTTPServer.BaseHTTPRequestHandler):
	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type","text/html")
		s.end_headers()
	def do_GET(s):
		s.send_response(200)
		s.send_header("Content-type","text/html")
		s.end_headers()
		for line in open(s.path,'r').read():
			s.wfile.write(line)

if __name__=="__main__":
	server_class=HTTPServer.HTTPServer
	httpd=server_class((HOSTNAME,PORT),ServerHandler)
	print "Server started at",HOSTNAME,PORT
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()


