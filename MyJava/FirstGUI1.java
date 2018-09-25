
import javax.swing.JFrame;

public class FirstGUI1 extends JFrame {
	public static void main (String[] args) {
		FirstGUI1 gui = new FirstGUI1();
		gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		gui.setSize(500, 500);
		gui.setVisible(true);
		gui.setTitle("First GUI");
	}
}