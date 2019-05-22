package test;

import main.InventoryAllocator;
import main.Product;
import main.Shipment;
import main.Warehouse;
import org.junit.Before;
import org.junit.Test;

import java.util.*;

import static org.junit.Assert.*;

public class InventoryAllocatorTest {
    private InventoryAllocator inventoryAllocator;
    private List<Product> listProducts;
    private Warehouse warehouse;
    private Product product;
    private HashMap<String, Integer> order;
    private List<Warehouse> inventoryDistribution;
    private Shipment shipment;
    private List<Shipment> expectedShipment;

    @Before
    public void setUp() throws Exception {
        inventoryAllocator = new InventoryAllocator();
        listProducts = new ArrayList<>();
        warehouse = new Warehouse();
        product = new Product();
        order = new HashMap<>();
        inventoryDistribution = new ArrayList<>();
        shipment = new Shipment();
        expectedShipment = new ArrayList<>();
    }

    @Test
    public void getProductByPriority() {

    }
    public void displayOrderExpectedAndProposedShipment(HashMap<String, Integer> order, List<Warehouse> inventoryDistribution,List<Shipment> expectedShipment,List<Shipment> proposedShipmentList){
        System.out.println("Order\t\t\t  :" + order + "\nDistribution List :" + inventoryDistribution);
        System.out.println("Proposed Shipment :" + proposedShipmentList);
        System.out.println("Expected Shipment :" + expectedShipment);
    }

    @Test
    public void getCheapestShipments() {
        System.out.println("->Happy Case, Exact Inventory Match");
        order.put("apple", 1);
        Warehouse warehouse = new Warehouse("owc",1);
        warehouse.addToInventory("apple",1);
        inventoryDistribution.add(warehouse);

        Shipment shipment = new Shipment("owc", new HashSet<>());
        shipment.addToShipmentList(new Product("apple",1,"owc",1));
        expectedShipment.add(shipment);
        List<Shipment> proposedShipmentList = inventoryAllocator.getCheapestShipments(inventoryDistribution, order);
        displayOrderExpectedAndProposedShipment(order,inventoryDistribution,expectedShipment,proposedShipmentList);
        assertEquals(expectedShipment.toString(), proposedShipmentList.toString());
        shipment.getShipmentList().add(product);
        expectedShipment.clear();

        System.out.println("\n->Inventory is more than needed order, so it should create one shipment");
        warehouse.getInventory().get(0).setQuantity(10);
        shipment = new Shipment("owc", new HashSet<>());
        shipment.getShipmentList().add(new Product("apple", 1, "owc", 1));
        expectedShipment.add(shipment);
        proposedShipmentList = inventoryAllocator.getCheapestShipments(inventoryDistribution, order);
        displayOrderExpectedAndProposedShipment(order,inventoryDistribution,expectedShipment,proposedShipmentList);
        assertEquals(expectedShipment.toString(), proposedShipmentList.toString());

        System.out.println("\n->Not enough inventory, so don't create any shipment");
        order.put("apple", 120);
        expectedShipment.clear();
        proposedShipmentList = inventoryAllocator.getCheapestShipments(inventoryDistribution, order);
        displayOrderExpectedAndProposedShipment(order,inventoryDistribution,expectedShipment,proposedShipmentList);
        assertEquals(expectedShipment.toString(), proposedShipmentList.toString());

        System.out.println("\n->Single order is in multiple warehouses, so split the item V_1");
        inventoryDistribution.clear();
        order.clear();
        expectedShipment.clear();
        order.put("apple",120);
        Warehouse dm = new Warehouse("dm", 0);
        Warehouse ocw = new Warehouse("ocw",1);
        dm.addToInventory("apple",119);
        inventoryDistribution.add(dm);
        ocw.addToInventory("apple",9);
        inventoryDistribution.add(ocw);
        Shipment multShipment = new Shipment("ocw", new HashSet<>());
        multShipment.addToShipmentList(new Product("apple", 1, "ocw", 1));
        expectedShipment.add(multShipment);
        multShipment = new Shipment("dm", new HashSet<>());
        multShipment.addToShipmentList(new Product("apple", 0, "dm", 119));

        expectedShipment.add(multShipment);

        proposedShipmentList = inventoryAllocator.getCheapestShipments(inventoryDistribution, order);
        displayOrderExpectedAndProposedShipment(order, inventoryDistribution, expectedShipment,proposedShipmentList);
        assertEquals(expectedShipment.toString(), proposedShipmentList.toString());

        System.out.println("\n->Single order is in multiple warehouses, so split the item V_2");
        //System.out.println("laksdjflakjsdflakdjf: " + inventoryDistribution);

        inventoryDistribution.clear();
        expectedShipment.clear();
        Warehouse warehouse1 = new Warehouse("owc",0);
        warehouse1.addToInventory(new Product("apple",8));

        inventoryDistribution.add(warehouse1);
        //add a second warehouse to the inventory distribution
        Warehouse warehouse2 = new Warehouse("dm",1);

        warehouse2.addToInventory(new Product("apple",119));
       // System.out.println("sss"+warehouse2.getInventory());
        inventoryDistribution.add(warehouse2);
        Shipment owcShipment = new Shipment("owc");
        Shipment dmShipment = new Shipment("dm");
        owcShipment.addToShipmentList(new Product("apple",0,"owc",8));
        dmShipment.addToShipmentList(new Product("apple",1,"dm",112));
        expectedShipment.add(dmShipment);
        expectedShipment.add(owcShipment);
        System.out.println("expected: " + expectedShipment);
        proposedShipmentList = inventoryAllocator.getCheapestShipments(inventoryDistribution, order);
        //System.out.println("Proposed Shipment: " + proposedShipmentList);
        displayOrderExpectedAndProposedShipment(order, inventoryDistribution, expectedShipment,proposedShipmentList);
        assertEquals(expectedShipment.toString(), proposedShipmentList.toString());

        System.out.println("\n->Multiple Orders are in multiple warehouses, so get them across");
        order.clear();
        order.put("Apple", 10);
        order.put("Orange", 17);
        order.put("Banana", 45);
        order.put("Kiwi", 19);

        Product apple = new Product("Apple", 100);
        Product kiwi = new Product("Kiwi", 100);
        Product oranges = new Product("Orange", 1);
        Product pears = new Product("Pears", 124);
        Product banana = new Product("Banana", 200);
        Product mango = new Product("Mango", 300);

        Warehouse warehouseSouth = new Warehouse("SouthCorner", 0);
        Warehouse warehouseNorth = new Warehouse("NorthCorner", 1);
        Warehouse wareHouseEast = new Warehouse("EastCorner", 2);
        Warehouse warehouseWest = new Warehouse("WestCorner", 3);

        warehouseSouth.addToInventory(apple, 100);
        warehouseSouth.addToInventory("Kiwi", 8);
        warehouseSouth.addToInventory(oranges, 34);
        warehouseSouth.addToInventory("Chicken", 18);

        warehouseNorth.addToInventory(banana);
        warehouseNorth.addToInventory(mango);
        wareHouseEast.addToInventory("Sprite", 200);
        wareHouseEast.addToInventory("Jordan Air", 17);
        warehouseWest.addToInventory("GummyBear", 1700);
        warehouseWest.addToInventory("Pears", 117);
        warehouseWest.addToInventory(kiwi);

        inventoryDistribution.clear();
        inventoryDistribution.addAll(Arrays.asList(warehouseNorth, warehouseSouth, wareHouseEast, warehouseWest));

        System.out.println(order);
        proposedShipmentList = inventoryAllocator.getCheapestShipments(inventoryDistribution, order);

        Shipment WestShipment = new Shipment("WestCorner");
        Shipment EastShipment = new Shipment("EastCorner");
        Shipment NorthShipment = new Shipment("NorthCorner");
        Shipment SouthShipment = new Shipment("SouthCorner");

        SouthShipment.addToShipmentList(new Product("Apple", 0, "SouthCorner", 10));
        SouthShipment.addToShipmentList(new Product("Kiwi", 0, "SouthCorner", 8));
        SouthShipment.addToShipmentList(new Product("Orange", 0, "SouthCorner", 17));
        NorthShipment.addToShipmentList(new Product("Banana", 1, "NorthCorner", 45));
        WestShipment.addToShipmentList(new Product("Kiwi", 3, "WestCorner", 11));

        expectedShipment.clear();
        expectedShipment.addAll(Arrays.asList(WestShipment, SouthShipment, NorthShipment));

        System.out.println("Order:              " + order + "\nDistribution List: " + inventoryDistribution);
        System.out.println("Expected:           " + expectedShipment);
        proposedShipmentList = inventoryAllocator.getCheapestShipments(inventoryDistribution, order);
        System.out.println("Proposed Shipment:  " + proposedShipmentList);
        assertEquals(expectedShipment.toString(), proposedShipmentList.toString());

        System.out.println("\n-> Multiple orders, multiple inventories, but one is missing, can't ship it");
        System.out.println(order);
        order.put("chicken",20);
        System.out.println(inventoryDistribution);
        expectedShipment = inventoryAllocator.getCheapestShipments(inventoryDistribution,order);
        System.out.println( "Order            : " + order + "\nDistribution List: " + inventoryDistribution);
        System.out.println( "Expected:          " + expectedShipment);
        proposedShipmentList = inventoryAllocator.getCheapestShipments(inventoryDistribution, order);
        System.out.println("Proposed Shipment: " + proposedShipmentList);
        assertEquals(expectedShipment.toString(), proposedShipmentList.toString());

    }
}