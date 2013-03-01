import BaseHTTPServer as HTTPServer 
# read the hostname fromt the config file


class ServerHandler(HTTPSever.BaseHTTPRequestHandler):
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

if __name__="__main__":
	server_class=HTTPSever.HTTPServer
	httpd=server_class((HOSTNAME,PORT),SeverHandler)
	print "Server started at",HOSTNAME,PORT
	try:
		httpd.server_forever
	except KeyboarIntterupt:
		pass
	httpd.server_close()


