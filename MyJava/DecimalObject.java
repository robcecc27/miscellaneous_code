// Import the required API classes.
import java.math.BigDecimal;

public class DecimalObject
{
	public static void main(String[] args)
	{
		//Create a decimal type from a float.
		BigDecimal Value1 = new BigDecimal(4.395f);
		
		//Because float relies on a base 2 
		//repesentaion of the number,
		// the output isn't what you'd expect.
		System.out.println("Using a float is inaccurate: ");
		System.out.println(Value1);
		
		//Create a decimal type form a double.
		BigDecimal Value2 = new BigDecimal(4.395);
		
		// Using a double is slightly more accurate.
		System.out.println("Using a double is inaccurate: ");
		System.out.println(Value2);
		
		// Create a decimal using a String instead.
		BigDecimal Value3 = new BigDecimal("4.395");
		
		// The output is waht you'd expect this time.
		System.out.print("Using a String is accurate: ");
		System.out.println(Value3);
		
		// Create the difference between Value1 and 2
		BigDecimal Value4 = new BigDecimal(4.395f - 4.395);
		
		// The difference between Value 1 and 2.
		System.out.print("The difference between 1 & 2: ");
		System.out.println(Value4);
	}
}