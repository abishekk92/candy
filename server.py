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
		#read from the file from s.path and write back as the response

if __name__="__main__":
	server_class=HTTPSever.HTTPServer
	httpd=server_class((HOSTNAME,PORT),SeverHandler)
	print "Server started at",HOSTNAME,PORT
	try:
		httpd.server_forever
	except KeyboarIntterupt:
		pass
	httpd.server_close()


