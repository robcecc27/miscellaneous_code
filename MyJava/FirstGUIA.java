
import java.awt.*;
import javax.swing.*;
	
	public class FirstGUIA extends JFrame {
	
		private JLabel label; 
		private JButton button;
		private JTextField textfield;
			
		public FirstGUIA () {
			setLayout(new FlowLayout());
			
			label = new JLabel("This is a label");
			add(label);
			
			textfield = new JTextField(15);
			add(textfield);
			
			button = new JButton("Click Me");
			add(button);
		}
		
		public static void main(String[] args) {
			FirstGUIA gui = new FirstGUIA();
			gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			gui.setSize(500, 500);
			gui.setVisible(true);
			gui.setTitle("Second GUI");
		}
	
}