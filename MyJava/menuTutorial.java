import java.awt.event.*;
import java.awt.*;
import javax.swing.*;

public class menuTutorial extends JFrame {
	JMenuBar menubar;
	JMenu file;
	JMenuItem exit;
	
	public menuTutorial(){
		setLayout(new FlowLayout());
		
		menubar = new JMenuBar();
		setJMenuBar(menubar);
		
		file = new JMenu("File");
		menubar.add(file);
		
		exit = new JMenuItem("Exit");
		file.add(exit);
		
		event e = new event();
		exit.addActionListener(e);
	}
	
	public class event implements ActionListener {
		public void actionPerformed(ActionEvent e) {
			System.exit(0);
		}
	}
	
	public static void main (String [] args) {
		menuTutorial gui = new menuTutorial();
		gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		gui.setSize(400, 400);
		gui.setVisible(true);
	}
}