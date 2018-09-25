import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class mousemover extends JFrame {
	
	JLabel label1, label2, label3, label4, errorlabel;
	JTextField tf1, tf2, tf3, tf4;
	JButton button;
	
	public mousemover() {
		setLayout(new GridLayout(5, 2, 5, 5));
		
		label1 = new JLabel("Enter number of movements: ");
		add(label1);
		
		tf1 = new JTextField();
		add(tf1);
		
		label2 = new JLabel("Enter delay between movements");
		add(label2); 
		
		tf2 = new JTextField();
		add(tf2); 
		
		label3 = new JLabel("Enter screen width in pixwls"); 
		add(label3);
		
		tf3 = new JTextField();
		add(tf3);
		
		label4 = new JLabel("Enter screen height in pixels");
		add(label4);
		
		tf4 = new JTextField();
		add(tf4);
		
		button = new JButton("Start");
		add(button);
		
		errorlabel = new JLabel("");
		add(errorlabel);
		
		event e = new event();
		button.addActionListener(e);
	}
	
	public class event implements ActionListener{
		public void actionPerformed (ActionEvent e) {
			try {
				int num = (int) (Double.parseDouble(tf1.getText()));
				int delay = (int)(Double.parseDouble(tf2.getText()));
				int width = (int)(Double.parseDouble(tf3.getText()));
				int height = (int)(Double.parseDouble(tf4.getText()));
				
				if(num <= 0 || delay <= 0 || width <= 0 || height <= 0) {
					errorlabel.setText("Please enter positive valuses");
				} else {
					errorlabel.setText("");
					
					try {
						Robot rob = new Robot();
						for(int x=0; x<=num; x++){
							rob.mouseMove((int)(Math.random()*width), (int)(Math.random()*height));
							
							rob.delay(delay);
						}
					} catch (AWTException ex) {
						System.exit(0);
					}
				}
			} catch (Exception exx) {
				errorlabel.setText("Numbers Only");
			}
		}
	}
	
	public static void main (String [] args ) {
		mousemover gui = new mousemover();
		gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		gui.setVisible(true);
		gui.pack();
		gui.setTitle("Mice Game");
	}
}
