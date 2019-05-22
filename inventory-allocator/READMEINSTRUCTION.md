# INSTRUCTION

## Requirements and System Specification
* Java 1.7+
* Junit-4.12+
* hamcrest-core-1.3

# Project structure
``` 
Inventory-allocator
    lib
    src
        main
          InventoryAllocator.java
          Main.java
          Product.java
          Shipment.java
          Warehouse.java  
        test
          InventoryAllocatorTest.java
          ProductTest.java
          ShipmentTest.java
          WarehouseTest.java
        META-INF
          MANIFEST.MF    
     README.md
     READMEINSTRUCTION.md
     arquillian-junit-container-1.4.1.Final.jar
     hamcrest-core-1.3.jar
     inventory-allocator.jar
     junit-4.12.jar
External Libraries       

   ````
   All the source files are inside main folder and the unit test are inside test
   
   * To run the project, you can either use an IDE( i used Intelli IDEA) or you can directly execute the jar files i generated.
   * To run the project on commandline, make sure that there are 4 jar files( junit-4.12 jar, inventor-allocator.jar, arquililian-junit-container-1.4.1.Final.jar and hamcrest-core-1.3.jar)
   * On commandline type ``` java -jar inventory-allocator.jar```
   
   #Note: 
   * The commandline will run the class ```InventoryAllocatorTest.java```. It doesn't run every single class provided. To get coverage, use Intellij IDEA 
   and ```run with coverage``` of the test folder. 
   
  
   
   
 
