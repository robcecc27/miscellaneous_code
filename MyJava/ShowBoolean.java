// Import the required API classes.
import java.util.Scanner;

public class ShowBoolean
{
	public static void main (String[] args)
	{
		//Create the scanner
		Scanner GetBoolean = new Scanner(System.in);
		
		// Obtain input from the user.
		System.out.print("Do you like Oranges? ");
		boolean TheTruth = GetBoolean.nextBoolean();
		
		//Show the results
		System.out.print("It's " + TheTruth);
		System.out.println(" that you like oranges.");
	}
}
