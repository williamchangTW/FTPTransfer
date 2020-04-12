from ftplib import FTP
import os
import sys

def uploadFile(ftpIP, username, passwd, filename):
	"""
	print("Upload File " + filename + " begin...")
	session = ftplib.FTP(ftpIP, username, passwd)
	file = open(filename, "rb")
	session.storbinary("store" + filename, file)
	print("Upload File Success!")	
	file.close()
	session.quit()
	"""
	ftp = FTP()
	ftp.connect(ftpIP, 2222)
	ftp.login(username, passwd)
	ftp.retrlines("LIST")
	# ftp.cwd("a")
	ftp.retrlines("LIST")
	# f = open(filename, "rb")
	ftp.storbinary("STOR " + "new" + filename , open(filename, "rb"))

if __name__ == "__main__":
	temp1 = os.popen("hostname -I").read().strip()
	temp2 = os.popen("hostname").read().strip()
	temp3 = os.popen("hostname").read().strip()
	temp4 = sys.argv[1]
	uploadFile(temp1, temp2, temp3, temp4)
