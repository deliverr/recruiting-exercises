package main;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import test.InventoryAllocatorTest;

public class Main {
    public static void main(String[] args) {
        Result result = JUnitCore.runClasses(InventoryAllocatorTest.class);
        for( Failure failure: result.getFailures()){
            System.out.println(failure.toString());
        }


    }
}
