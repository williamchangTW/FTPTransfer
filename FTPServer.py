from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer

import os

class MyHandler(FTPHandler):
	def on_connect(self):
		print("%s:%s connected" % (self.remote_ip, self.remote_port))

	def on_disconnect(self):
		pass

	def on_login(self, username):
		pass

	def on_logout(self, username):
		pass

	def on_file_sent(self, file):
		print(self.username, file)

	def on_file_received(self, file):
		print(self.username, file)
		pass
	
	def on_incomplete_file_sent(self, file):
		print(self.username, file)
		pass

	def on_imcomplete_file_received(self, file):
		os.remove(file)

def CreateFTP(user, passwd, ftpIP):
	authorizer = DummyAuthorizer()
	authorizer.add_user(user, passwd, homedir = ".", perm = "elradfmwMT")
	# authorizer.add_anonymous(homedir = ".")

	hadler = MyHandler
	hadler.authorizer = authorizer
	server = FTPServer((ftpIP, 2222), hadler)
	server.serve_forever()


if __name__ == "__main__":
	temp1 = os.popen("hostname").read().strip()
	temp2 = os.popen("hostname").read().strip()
	temp3 = os.popen("hostname -I").read().strip()
	CreateFTP(temp1, temp2, temp3)


	
