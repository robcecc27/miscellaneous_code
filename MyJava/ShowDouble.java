// Import the required API classes.
import java.util.Scanner;
import java.lang.Math;

public class ShowDouble
{
	public static void main(String[] args)
	{
		// Create the scanner.
		Scanner GetADouble = new Scanner(System.in);
		
		// Obtain a number to manipulate.
		System.out.print("Type any number: ");
		double Calc = GetADouble.nextDouble();
		
		// Output the square and the square root
		// of this number.
		System.out.print("The square of " + Calc + " is:");
		System.out.println(Calc * Calc);
		System.out.print("The square root of " + Calc + " is: ");
		System.out.println(Math.sqrt(Calc));
	}
}