import java.awt.*;
import javax.swing.*;

public class table extends JFrame {
	
	JTable table;
	
	public table() {
		setLayout(new FlowLayout());
		
		String[] columnNames = {"Name", "Eye-Color", "Gender"};
		
		Object[][] data = {
			{"Bill", "Hazel", "Male"},
				{"Mary", "Black", "Female"},
					{"Rick", "Red", "Male"},
						{" Janice", "Yellow", "Female"},
		};
		
		table = new JTable(data, columnNames);
		table.setPreferredScrollableViewportSize(new Dimension(500, 50));
		table.setFillsViewportHeight(true);
		
		JScrollPane scrollPane = new JScrollPane(table);
		add(scrollPane);
	}
	
	public static void main (String [] args ) {
			table gui = new table();
			gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			gui.setVisible(true);
			gui.setSize(700, 200);
			gui.setTitle("Java Tables");
	}
}
