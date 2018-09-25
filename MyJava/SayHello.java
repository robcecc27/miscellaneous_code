// Import the required API classes.
import java.util.Scanner;
import java.lang.String;

class SayHello
{
		public static void main(String args[]) 
		{
			//Creat an instance of the Scanner class to 
			//use for keyboard access.
			Scanner getName = new Scanner(System.in);
			
			//Create a variable to hold the user's name.
			//This variable is designed to hold text.
			String userName;
			
			//Ask the user's name and place this name in
			// "String userName"
			System.out.print("What is your name? ");
			userName = getName.nextLine();
			
			//Display a Message to the user with the
			//user's name in view.
			// "\n" was to add a new line won't work without quotes			
			System.out.println("Hello " + userName + "!" + "\n");
		}
}
