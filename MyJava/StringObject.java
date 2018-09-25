// Import the required API classes.
import java.util.Scanner;
import java.lang.String;

public class StringObject
{
	public static void main(String[] args)
	{
		//Create the scanner.
		Scanner GetString = new Scanner(System.in); 
		
		// Obtain a byte value.
		System.out.print("Type any string: ");
		String MyString = GetString.nextLine();
		
		//Display the value on screen.
		System.out.println("The value of the MyString is: " + MyString);		
	}
}