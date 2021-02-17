package Code;

import org.junit.internal.TextListener;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;

 

public class ProjectTestSuiteRunner {
    // code relevant to test suite goes here
	public static void main(String [] args)
	{	JUnitCore junit = new JUnitCore();
		Result result = junit.run(TestInventoryAllocator.class);
		JUnitCore junitCore = new JUnitCore(); 
		junit.addListener(new TextListener(System.out)); 
		junit.run(TestInventoryAllocator.class);
	}
	
}


