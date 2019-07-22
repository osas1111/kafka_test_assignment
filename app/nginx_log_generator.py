from random import randint, choice
import os


def log_generator():
	ip = '.'.join([str(randint(0,255)) for x in range(4)])
	status_code = choice(list(set(["200", "401", "404", "503"])))
	request = choice(list(set(["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT"])))
	string = ' '.join([ip, "HTTP/1.1", status_code, request])
	return(string)

if not os.path.exists("log"):
    os.makedirs("log")

with open("log/access.log", 'w+') as logfile:
	while True:
		print((log_generator()))
		logfile.write((log_generator())+"\n")
