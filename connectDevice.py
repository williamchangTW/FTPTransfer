from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()

authorizer.add_user("user", "12345", ".", perm = "elradfmwMT")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("192.168.0.6", 2121), handler)
server.serve_forever()
