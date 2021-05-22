package deliverr;

import org.junit.Assert;
import org.junit.jupiter.api.Test;
import java.util.*;


class InventoryAllocatorTest {

    InventoryAllocator ia = new InventoryAllocator();

    Map<String, Integer> orders = new HashMap<>();

    List finalShipment = new ArrayList();

    List inputList;

    String expectedOutput;

    List<Warehouse> warehouseList = new ArrayList();

    Map<String, Integer> firstInventory = new HashMap<>();

    Map<String, Integer> secondInventory = new HashMap<>();

    Map<String, Integer> thirdInventory = new HashMap<>();


    @Test
    public void createShipmentsWithNoInput() {

        inputList = ia.createShipments(orders, warehouseList);

        Assert.assertEquals(finalShipment, inputList);

    }

    @Test
    public void shipmentsWithOneInventory(){

        orders.put("apple", 10);
        orders.put("mango", 10);

        firstInventory.put("apple",10);
        firstInventory.put("mango", 10);

        Warehouse warehouse1 = new Warehouse("xyz", firstInventory);

        warehouseList.add(warehouse1);

        inputList = ia.createShipments(orders, warehouseList);

        expectedOutput = "[{xyz: {apple=10, mango=10}}]";

        Assert.assertEquals(expectedOutput, inputList.toString());
    }

    @Test
    public void shipmentsWithDistributedInventory() {

        orders.put("apple", 5);
        orders.put("mango", 5);

        firstInventory.put("apple", 3);
        firstInventory.put("mango",2);

        secondInventory.put("apple",1);
        secondInventory.put("mango",2);

        thirdInventory.put("apple", 2);
        thirdInventory.put("mango", 2);


        Warehouse warehouse1 = new Warehouse("xyz", firstInventory);

        Warehouse warehouse2 = new Warehouse("abc", secondInventory);

        Warehouse warehouse3 = new Warehouse("owd", thirdInventory);

        warehouseList.add(warehouse1);
        warehouseList.add(warehouse2);
        warehouseList.add(warehouse3);

        finalShipment = ia.createShipments(orders, warehouseList);

        expectedOutput = "[{xyz: {apple=3, mango=2}}, {abc: {apple=1, mango=2}}, {owd: {apple=1, mango=1}}]";

        Assert.assertEquals(finalShipment.toString(), expectedOutput);

    }

    @Test
    public void shipmentsWithEmptyWarehouseList(){

        orders.put("apple", 10);
        orders.put("mango", 10);

        inputList = ia.createShipments(orders, warehouseList);

        Assert.assertEquals(finalShipment, inputList);

    }

    @Test
    public void shipmentsWithEmptyOrders(){

        firstInventory.put("apples", 10);

        secondInventory.put("mango", 10);

        Warehouse warehouse1 = new Warehouse("xyz", firstInventory);

        Warehouse warehouse2 = new Warehouse("abc", secondInventory);

        warehouseList.add(warehouse1);
        warehouseList.add(warehouse2);

        inputList = ia.createShipments(orders, warehouseList);

        Assert.assertEquals(finalShipment, inputList);

    }


}