
import javax.swing.JFrame;

public class FirstGUI extends JFrame {
	public static void main (String[] args) {
		FirstGUI gui = new FirstGUI();
		gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		gui.setSize(500, 500);
		gui.setVisible(true);
		gui.setTitle("First GUI");
	}
}