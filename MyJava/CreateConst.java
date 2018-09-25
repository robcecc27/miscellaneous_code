// Import the required API classes.
import java.util.Scanner;

public class CreateConst
{
	public static void main(String[] args)
	{
		// Create a constant.
		final int MyConst = 345;
		
		//Display the constant on screen.
		System.out.println("The current value of MyConst is: " + MyConst);
		
		//Create the scanner.
		Scanner GetConst = new Scanner(System.in); 
		
		// Try to change the value.
		System.out.print("Enter a new value for MyConst: ");
		//MyConst = GetConst.nextInt();
	}
}