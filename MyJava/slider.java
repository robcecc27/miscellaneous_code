import java.awt.*;
import javax.swing.*;
import javax.swing.event.*;
 
public class slider extends JFrame {
	
	JSlider slider;
	JLabel label;
	
	public slider() {
			setLayout(new FlowLayout());
			
			slider = new JSlider(JSlider.HORIZONTAL, 0, 20, 0);
			slider.setMajorTickSpacing(5);
			slider.setPaintTicks(true);
			add(slider);
			
			label = new JLabel("Current value: 0");
			add(label);
			
			event e = new event();
			slider.addChangeListener(e);
	}
	
	public class event implements ChangeListener {
		public void stateChanged(ChangeEvent e) {
			int value = slider.getValue();
			
			label.setText("Current value: " + value);
		}
	}
	
	public static void main (String [] args ) {
			slider gui = new slider();
			gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			gui.setVisible(true);
			gui.setSize(300, 200);
			gui.setTitle("Sliders");
	}
}
