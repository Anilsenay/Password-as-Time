from time import gmtime, strftime

username = "admin"
password = str(int(strftime("%d%m%H%M", gmtime()))+300) ## +300 for GMT+3 which is my timezone

signed = False
attempts = 3;
while(signed == False):

	username = input("User name: ")
	passwd = input("Password: ")

	if(username == "admin" and passwd == password):
		print("You signed in")
		signed = True
	else:
		attempts = attempts - 1
		if(attempts == 0):
			print("Logging failed.")
			break;
		print("Wrong user name or password! ",attempts," attempts remaining.  Try again:")

