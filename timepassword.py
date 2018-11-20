from time import gmtime, strftime

username = "admin"
password = str(int(strftime("%d%m%H%M", gmtime()))+300) ## +300 for GMT+3 which is my timezone

signed = False

while(signed == False):

	username = input("User name: ")
	passwd = input("Password: ")

	if(username == "admin" and passwd == password):
		print("You signed in")
		signed = True
	else:
		print("Wrong user name or password! Try again:")
