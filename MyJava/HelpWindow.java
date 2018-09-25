import java.awt.*;

import javax.swing.*;

@SuppressWarnings("serial")
public class HelpWindow extends JDialog {
	JLabel label;
	
	public HelpWindow(JFrame frame)  {
		super(frame, "Help Window", true);
		setLayout(new FlowLayout());
		
		label = new JLabel ("This a string of information");
		add(label);
	}
}
