// Import the required API classes.
import java.util.Scanner;

public class ShowLong
{
		public static void main(String[] args)
		{
			// Create the scanner.
			Scanner GetLong = new Scanner (System.in);
			
			//Obtain the division (the first number in the division).
			System.out.print("Type a number for the division: ");
			long Dividend = GetLong.nextLong();
			
			// Obtain the divisor (the part used to divide the 
			// dividend).
			System.out.print("Type a number for the divisor: ");
			long Divisor = GetLong.nextLong();
			
			// Perform the division.
			System.out.print(Dividend + " divided by ");
			System.out.print(Divisor + " equals ");
			System.out.print(Dividend / Divisor);
			System.out.print(" with a remainder of ");
			System.out.println(Dividend % Divisor);
		}
}
