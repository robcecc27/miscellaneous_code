// Import the required API classes.
import java.util.Scanner;

//Import the required API packages.
import java.lang.*;

class SayHello2
{
		public static void main(String args[])
		{
			// Create an instance of the Scanner class to
			// use for keyboard access.
			Scanner getName = new Scanner (System.in);
			
			//Create a variable to hold the user's name.
			// This variable is designed to hold text.
			String userName;
			
			// Ask the user's name and place name in 
			// "userName" variable
			System.out.print("What is your name? ");
			userName = getName.nextLine();
			
			// Create a variable to hold the number of letters 
			// in the user's name.
			Integer letterCount;
			
			//Get the number of letters in the user's name.
			letterCount = userName.length();
			
			//Display a message to the user with the user's
			//name in view.
			System.out.println("Hello " + userName + " your name has " + letterCount + " letters in it!" + "\n");
		}
		
}