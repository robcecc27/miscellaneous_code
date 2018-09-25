package javagame;

import javax.swing.JFrame;
import javax.*;

public class JavaGame extends JFrame {
	
	public JavaGame(){
		setTitle("Java Game"); 
		setSize(250, 250);
		setResizable(false);
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		}
			
		public static void main(String[] args) {
			new JavaGame();
			
		}
}