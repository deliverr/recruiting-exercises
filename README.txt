# Please run following commands to compile and run the whole project
javac InventoryAllocator.java
javac -cp junit.jar:. InventoryAllocatorTest.java
java -cp junit.jar:org.hamcrest.core_1.3.0.v201303031735.jar:. org.junit.runner.JUnitCore InventoryAllocatorTest
