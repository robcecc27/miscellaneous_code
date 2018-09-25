// Import the required API classes.
import java.math.BigInteger;

public class BigIntegerObject
{
	public static void main(String[] args)
	{
		// Create a long that contains the maximum value.
		long Overflow = 9223372036854775807l;
		
		// Display the value so you can see
		// it works fine.
		System.out.println("Initial Overflow value: " + Overflow);
		
		// Create an overflow condition and display it.
		Overflow = Overflow + 1;
		System.out.println("Overflow + 1 value: " + Overflow);
		
		// Create a BigInteger that contains a maximum
		// long value.
		BigInteger NoOverflow = BigInteger.valueOf(9223372036854775807l);
		
		// Display the value so you can see
		// it works fine.
		System.out.println("Initial NoOverflow value: " + NoOverflow);
		
		// Add 1 and see what happens.
		NoOverflow = NoOverflow.add(BigInteger.ONE);
		System.out.println("NoOverflow + 1 value: " + NoOverflow);
		
		// Multiply the result by 3 to see what happens.
		NoOverflow = NoOverflow.multiply(BigInteger.valueOf(3));
		System.out.println("NoOverflow * 3 value: " + NoOverflow);
	}
}