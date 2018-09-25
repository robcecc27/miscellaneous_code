import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class checkbox extends JFrame {
	
	JCheckBox show1, show2;
	JLabel label1, label2;
	
	public checkbox() {
		setLayout(new GridLayout(2, 2));
		
		label1 = new JLabel("");
		add(label1);
		
		label2 = new JLabel("");
		add(label2);
		
		show1 = new JCheckBox("Show first label");
		add(show1);
		
		show2 = new JCheckBox("Show second label");
		add(show2);
		
		event e = new event();
		show1.addItemListener(e);
		show2.addItemListener(e);
	}
	
	public class event implements ItemListener {
		public void itemStateChanged(ItemEvent e) {
			if(show1.isSelected()) {
				label1.setText("You pushed first CB");
			} else {
				label1.setText("");
			}
			
			if(show2.isSelected()) {
				label2.setText("You pushed second CB");
			} else {
				label2.setText("");
			}
		}
	}
	
	public static void main (String [] args ) {
			checkbox gui = new checkbox();
			gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			gui.setVisible(true);
			gui.setSize(300, 150);
			gui.setTitle("Check Box");
	}
}
