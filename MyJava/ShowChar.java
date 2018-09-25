// Import the required API classes.
import java.util.Scanner;

public class ShowChar
{
	public static void main(String[] args)
	{
		// Create the scanner
		Scanner GetChar = new Scanner(System.in);
		
		// Obtain input from the user.
		System.out.print("Type any singe letter or Number: ");
		char AChar = GetChar.findInLine(".").charAt (0);
		
		// Display the input.
		System.out.println ("You typed: " + AChar);
	}
}