import java.util.Date;
import java.text.*;
import java.util.Scanner;

public class timepassword {

	public static void main(String[] args) {

		String username = "admin";
		String password;
		boolean signed = false;
		int loginAttempts = 3;
		Scanner input = new Scanner(System.in);

		Date currentDate = new Date();
		SimpleDateFormat dateFormat = new SimpleDateFormat ("ddMMhhmm");

		password = dateFormat.format(currentDate);

		while(!signed) {

			System.out.print("User name: ");
			String inputUserName = input.next();
			System.out.print("Password: ");
			String inputPasswd = input.next();

			if( username.equals(inputUserName) && password.equals(inputPasswd) ) {
				System.out.println("You signed in.");
				signed = true;
			}

			else {
				loginAttempts--;

				if(loginAttempts == 0) {
					System.out.println("Logging failed.");
					break;
				}

				System.out.println("Wrong user name or password! " + loginAttempts + " attempt remaining." +
				"Try again: ");
			}

		}

	}

}
