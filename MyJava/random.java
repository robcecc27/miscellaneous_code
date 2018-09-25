import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class random extends JFrame {
	
	JPanel panel;
	
	public random() {
		panel = new JPanel();
		panel.setBackground(randomColor());
		add(panel);
		
		event e = new event();
		panel.addMouseListener(e);
		
	}
	
	public Color randomColor() {
		int r = (int)(Math.random()*256);
		int g = (int)(Math.random()*256);
		int b = (int)(Math.random()*256);
		return(new Color(r, g, b));
	}
	
	public class event implements MouseListener {
		
		public void mouseClicked(MouseEvent e) {
			panel.setBackground(randomColor());
		}
		
		public void mousePressed(MouseEvent e) {
		}
		
		public void mouseReleased(MouseEvent e) {
		}
		
		public void mouseEntered(MouseEvent e) {
		}
		
		public void mouseExited(MouseEvent e) {
		}
	}
		
		public static void main (String [] args ) {
			random gui = new random();
			gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			gui.setVisible(true);
			gui.setSize(500, 500);
			gui.setTitle("Random Color Panel");
		}
}
