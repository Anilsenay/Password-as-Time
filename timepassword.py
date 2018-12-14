from datetime import datetime

username = "admin"
password = str(int(datetime.now().strftime("%d%m%H%M")))

signed = False
attempts = 3;
while(signed == False):

	username = input("User name: ")
	passwd = input("Password: ")
	print(password)
	if(username == "admin" and passwd == password):
		print("You signed in")
		signed = True
	else:
		attempts = attempts - 1
		if(attempts == 0):
			print("Logging failed.")
			break;
		print("Wrong user name or password! ",attempts," attempts remaining.  Try again:")

