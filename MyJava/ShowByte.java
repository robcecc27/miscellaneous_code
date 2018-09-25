// import the required API classes.
import java.util.Scanner;

public class ShowByte 
{
	public static void main(String[] args)
	{
		//Create the scanner.
		Scanner GetByte = new Scanner(System.in);
		
		// Obtain a byte value.
		System.out.print("Type any number: ");
		byte MyByte = GetByte.nextByte();
		
		//Display the value on screen.
		System.out.println("The value of MyByte is: " + MyByte);
	}
}