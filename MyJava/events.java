
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

	public class events extends JFrame {
		private JLabel label1;
		private JLabel label2;
		private JButton button1;
		private JButton button2;
		private int x = 0, y = 0;
		
		public events() {
			setLayout (new FlowLayout());
		
			button1 = new JButton("Click '1' Here");
			add(button1);
			
			label1 = new JLabel("");
			add(label1);
			
			button2 = new JButton("Click '2' Here");
			add(button2);
			
			label2 = new JLabel("");
			add(label2);
			
			
			event e = new event();
			button1.addActionListener(e);
			
			event2 ev = new event2();
			button2.addActionListener(ev);
			
		}
		
		public class event implements ActionListener {
			public void actionPerformed(ActionEvent e){
				if(x == 0) {
					label1.setText("This is from the button 1");
					x =1;
				} else if(x == 1) {
					label1.setText("");
					x = 0;
				}
			}
		}
		
		public class event2 implements ActionListener {
			public void actionPerformed(ActionEvent ev){
				if(y == 0) {
					label2.setText("This is from the button 2");
					y = 1;
				} else if(y == 1) {
					label2.setText("");
					y = 0;
				}					
			}
		}
		
		public static void main(String[] args) {
			events gui = new events();
			gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			gui.setSize(275, 300);
			gui.setVisible(true);
			gui.setTitle("Events Program");
		}
}