// Import the required API classes.
import java.util.Scanner;
import java.util.Random;
import java.util.Calendar;

public class ShowInt
{
	public static void main(String args[])
	{
		// Create the scanner.
		Scanner GetInt = new Scanner(System.in);
		
		// Obtain an int value.
		System.out.print("Type a number between 1 and 10: ");
		int YourGuess = GetInt.nextInt();
		
		// Get the current time.
		Calendar MyCal = Calendar.getInstance();
		
		// Create a random number generator.
		Random MyRandom = new Random();
		
		// Set the seed value for the random number using
		// the current number of milliseconds in the time.
		MyRandom.setSeed(MyCal.getTimeInMillis());
		
		// Obtain a random number between 1 and 10.
		int MyGuess = MyRandom.nextInt(10) + 1;
		
		// Display the value on screen.
		System.out.print("Your guess was: " + YourGuess);
		System.out.println(" My guess was: " + MyGuess);
	}
}