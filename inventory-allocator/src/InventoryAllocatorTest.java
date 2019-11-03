import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashMap;

import org.junit.*;

public class InventoryAllocatorTest {

	private static InventoryAllocator allocator1;
	private static InventoryAllocator allocator2;
	private static InventoryAllocator allocator3;
	private static InventoryAllocator allocator4;
	private static InventoryAllocator allocator5;
	private static InventoryAllocator allocator6;
	private static InventoryAllocator allocator7;
	private static InventoryAllocator allocator8;
	private static InventoryAllocator allocator9;
	private static InventoryAllocator allocator10;
	private static InventoryAllocator allocator11;
	
	
	private ArrayList<LinkedHashMap<String, Object>> shipment;
	private LinkedHashMap<Object, Integer> invOwd;
	private LinkedHashMap<Object, Integer> invDm;
	private LinkedHashMap<Object, Integer> invWh;
	private LinkedHashMap<Object, Integer> mapAgainst;
	
	@BeforeClass
	public static void oneTimeSetUp()
	{	
		/*allocator 1 set up*/
		/*Every order has possible allocation*/
		ArrayList<Object> orderList = new ArrayList<>(Arrays.asList("apple", 5, "banana", 5, "orange", 5));
		LinkedHashMap<Object, Integer> order = initOrder(orderList);

		ArrayList<LinkedHashMap<Object, Object>> warehouse = new ArrayList<>();
		
		LinkedHashMap<Object, Object> description = new LinkedHashMap<>();		
		ArrayList<Object> inventoryList = new ArrayList<>(Arrays.asList("apple", 5, "orange", 5));
		initWarehouse("owd", inventoryList, description);
		
		warehouse.add(description);
		
		description = new LinkedHashMap<>();
		inventoryList = new ArrayList<>(Arrays.asList("banana", 5, "orange", 10));
		initWarehouse("dm", inventoryList, description);
		
		warehouse.add(description);
		
		allocator1 = new InventoryAllocator(order, warehouse);
		
		
		
		/*allocator 2 set up*/
		/*Exact Inventory Match*/
		orderList = new ArrayList<>(Arrays.asList("apple", 1));
		order = initOrder(orderList);

		warehouse = new ArrayList<>();
		
		description = new LinkedHashMap<>();		
		inventoryList = new ArrayList<>(Arrays.asList("apple", 1));
		initWarehouse("owd", inventoryList, description);
		
		warehouse.add(description);
		
		allocator2 = new InventoryAllocator(order, warehouse);
		
		
		
		/*allocator 3 set up*/
		/*Not enough Inventory in 1 warehouse*/
		orderList = new ArrayList<>(Arrays.asList("apple", 1));
		order = initOrder(orderList);

		warehouse = new ArrayList<>();
		
		description = new LinkedHashMap<>();		
		inventoryList = new ArrayList<>(Arrays.asList("apple", 0));
		initWarehouse("owd", inventoryList, description);
		
		warehouse.add(description);
		
		allocator3 = new InventoryAllocator(order, warehouse);
		
		
		
		/*allocator 4 set up*/
		/*Allocation of order is split up among warehouses*/
		orderList = new ArrayList<>(Arrays.asList("apple", 10));
		order = initOrder(orderList);

		warehouse = new ArrayList<>();
		
		description = new LinkedHashMap<>();		
		inventoryList = new ArrayList<>(Arrays.asList("apple", 5));
		initWarehouse("owd", inventoryList, description);
		
		warehouse.add(description);
		
		description = new LinkedHashMap<>();		
		inventoryList = new ArrayList<>(Arrays.asList("apple", 5));
		initWarehouse("dm", inventoryList, description);
		
		warehouse.add(description);
		
		allocator4 = new InventoryAllocator(order, warehouse);
		
		
		
		/*allocator 5 set up*/
		/*Allocation of order is split up among warehouses, but not enough allocation*/
		orderList = new ArrayList<>(Arrays.asList("apple", 10));
		order = initOrder(orderList);

		warehouse = new ArrayList<>();
		
		description = new LinkedHashMap<>();		
		inventoryList = new ArrayList<>(Arrays.asList("apple", 5));
		initWarehouse("dm", inventoryList, description);
		
		warehouse.add(description);
		
		description = new LinkedHashMap<>();		
		inventoryList = new ArrayList<>(Arrays.asList("apple", 2));
		initWarehouse("owd", inventoryList, description);
		
		warehouse.add(description);
		
		description = new LinkedHashMap<>();		
		inventoryList = new ArrayList<>(Arrays.asList("apple", 1));
		initWarehouse("wh", inventoryList, description);
		
		warehouse.add(description);
		
		allocator5 = new InventoryAllocator(order, warehouse);
		
		
		
		/*allocator 6 set up*/
		/*Multiple order with success allocations, but 1 order with no allocation*/
		orderList = new ArrayList<>(Arrays.asList("apple", 10, "banana", 3, "orange", 4));
		order = initOrder(orderList);

		warehouse = new ArrayList<>();
		
		description = new LinkedHashMap<>();		
		inventoryList = new ArrayList<>(Arrays.asList("apple", 5, "banana", 2, "orange", 3));
		initWarehouse("owd", inventoryList, description);
		
		warehouse.add(description);
		
		description = new LinkedHashMap<>();		
		inventoryList = new ArrayList<>(Arrays.asList("apple", 2));
		initWarehouse("dm", inventoryList, description);
		
		warehouse.add(description);
		
		description = new LinkedHashMap<>();		
		inventoryList = new ArrayList<>(Arrays.asList("apple", 3, "orange", 1));
		initWarehouse("wh", inventoryList, description);
		
		warehouse.add(description);
		
		allocator6 = new InventoryAllocator(order, warehouse);
		
		
		
		/*allocator 7 set up*/
		/*order is empty, warehouse is empty*/
		order= new LinkedHashMap<Object, Integer>();
		warehouse = new ArrayList<>();

		allocator7 = new InventoryAllocator(order, warehouse);
		
		
		
		/*allocator 8 set up*/
		/*warehouse is empty*/
		orderList = new ArrayList<>(Arrays.asList("apple", 10, "banana", 3, "orange", 4));
		order = initOrder(orderList);
		
		warehouse = new ArrayList<>();

		allocator8 = new InventoryAllocator(order, warehouse);
		
		
		
		/*allocator 9 set up*/
		/*order is empty*/
		order= new LinkedHashMap<Object, Integer>();
		warehouse = new ArrayList<>();
		
		description = new LinkedHashMap<>();		
		inventoryList = new ArrayList<>(Arrays.asList("apple", 5, "banana", 2, "orange", 3));
		initWarehouse("owd", inventoryList, description);
		
		warehouse.add(description);
		
		description = new LinkedHashMap<>();		
		inventoryList = new ArrayList<>(Arrays.asList("apple", 2, "orange", 1));
		initWarehouse("dm", inventoryList, description);
		
		warehouse.add(description);

		allocator9 = new InventoryAllocator(order, warehouse);
		
		
		
		/*allocator 10 set up*/
		/*Last warehouse available*/
		orderList = new ArrayList<>(Arrays.asList("apple", 5));
		order = initOrder(orderList);

		warehouse = new ArrayList<>();
		
		description = new LinkedHashMap<>();		
		inventoryList = new ArrayList<>(Arrays.asList("apple", 0));
		initWarehouse("owd", inventoryList, description);
		
		warehouse.add(description);
		
		description = new LinkedHashMap<>();		
		inventoryList = new ArrayList<>(Arrays.asList("apple", 0));
		initWarehouse("dm", inventoryList, description);
		
		warehouse.add(description);
		
		description = new LinkedHashMap<>();		
		inventoryList = new ArrayList<>(Arrays.asList("apple", 5));
		initWarehouse("wh", inventoryList, description);
		
		warehouse.add(description);
		
		allocator10 = new InventoryAllocator(order, warehouse);
		
		
		
		/*allocator 11 set up*/
		/*Last warehouse with extra allocation*/
		orderList = new ArrayList<>(Arrays.asList("apple", 5));
		order = initOrder(orderList);

		warehouse = new ArrayList<>();
		
		description = new LinkedHashMap<>();		
		inventoryList = new ArrayList<>(Arrays.asList("apple", 0));
		initWarehouse("owd", inventoryList, description);
		
		warehouse.add(description);
		
		description = new LinkedHashMap<>();		
		inventoryList = new ArrayList<>(Arrays.asList("apple", 1));
		initWarehouse("dm", inventoryList, description);
		
		warehouse.add(description);
		
		description = new LinkedHashMap<>();		
		inventoryList = new ArrayList<>(Arrays.asList("apple", 5));
		initWarehouse("wh", inventoryList, description);
		
		warehouse.add(description);
		
		allocator11 = new InventoryAllocator(order, warehouse);
			
		
	}

	private static LinkedHashMap<Object, Integer> initOrder(ArrayList<Object> order)
	{
		LinkedHashMap<Object, Integer> map = new LinkedHashMap<>();
		
		for(int i = 0 ; i < order.size()-1 ; i+=2)
		{
			map.put(order.get(i), (Integer) order.get(i+1));
		}
		
		return map;
	}
	
	private static void initWarehouse(String name, ArrayList<Object> inv, LinkedHashMap<Object, Object> description)
	{
		description.put("name", name);
		
		LinkedHashMap<Object, Integer> inventory = new LinkedHashMap<Object, Integer>();
		for(int i = 0 ; i < inv.size()-1 ; i+=2)
		{
			inventory.put(inv.get(i), (Integer) inv.get(i+1));
		}
				
		description.put("inventory", inventory);
		
	}
	
	@Before
	public void setUp()
	{
		shipment = new ArrayList<LinkedHashMap<String, Object>>();
		invOwd = new LinkedHashMap<Object, Integer>();
		invDm = new LinkedHashMap<Object, Integer>();
		invWh = new LinkedHashMap<Object, Integer>();
		mapAgainst = new LinkedHashMap<Object, Integer>();
				
	}
	@SuppressWarnings("unchecked")
	@Test
	public void testGetCheapestShipmentAllocator1()
	{
		
		/*Allocator1 Test*/
		/*Every order has possible allocation*/
		shipment = allocator1.getCheapestShipment();
		
		invOwd = (LinkedHashMap<Object, Integer>) shipment.get(0).get("owd");
		mapAgainst = new LinkedHashMap<>();
	    mapAgainst.put("apple", new Integer(5));
	    mapAgainst.put("orange", new Integer(5));
	    
		assertEquals(invOwd, mapAgainst);
		
		LinkedHashMap<Object, Integer> invDm = (LinkedHashMap<Object, Integer>) shipment.get(1).get("dm");
		mapAgainst = new LinkedHashMap<>();
	    mapAgainst.put("banana", new Integer(5));
	    
	    assertEquals(invDm, mapAgainst);
	    
	    printOut(1, shipment);
		
	}
	@SuppressWarnings("unchecked")
	@Test
	public void testGetCheapestShipmentAllocator2()
	{
		
		/*Allocator2 Test*/
	    /*Exact Inventory Match*/
		shipment = allocator2.getCheapestShipment();
		
		invOwd = (LinkedHashMap<Object, Integer>) shipment.get(0).get("owd");
		mapAgainst = new LinkedHashMap<>();
	    mapAgainst.put("apple", new Integer(1));
	    
	    assertEquals(invOwd, mapAgainst);
		
	    printOut(2, shipment);
	    
	} 
	
	@SuppressWarnings("unchecked")
	@Test
	public void testGetCheapestShipmentAllocator3()
	{
	    
	    /*Allocator3 Test*/
	    /*Not enough Inventory in 1 warehouse*/
		shipment = allocator3.getCheapestShipment();
		
		assertTrue(shipment.size() == 0);
		
		printOut(3, shipment);
	    
	}  
	
	@SuppressWarnings("unchecked")
	@Test
	public void testGetCheapestShipmentAllocator4()
	{
	    
		/*Allocator4 Test*/
		/*Allocation of order is split up among warehouses*/
		shipment = allocator4.getCheapestShipment();
		
		invOwd = (LinkedHashMap<Object, Integer>) shipment.get(0).get("owd");
		mapAgainst = new LinkedHashMap<>();
	    mapAgainst.put("apple", new Integer(5));
	    
	    assertEquals(invOwd, mapAgainst);
	    
	    invDm = (LinkedHashMap<Object, Integer>) shipment.get(1).get("dm");
		mapAgainst = new LinkedHashMap<>();
	    mapAgainst.put("apple", new Integer(5));
	    
	    assertEquals(invDm, mapAgainst);
		
	    printOut(4, shipment);
	    
	}  
	
	@SuppressWarnings("unchecked")
	@Test
	public void testGetCheapestShipmentAllocator5()
	{
		/*Allocator5 Test*/
	    /*Allocation of order is split up among warehouses, but not enough allocation*/
		shipment = allocator5.getCheapestShipment();
		
		assertTrue(shipment.size() == 0);
		
		printOut(5, shipment);
	}
	
	@SuppressWarnings("unchecked")
	@Test
	public void testGetCheapestShipmentAllocator6()
	{
		shipment = allocator6.getCheapestShipment();
		
		invOwd = (LinkedHashMap<Object, Integer>) shipment.get(0).get("owd");
		mapAgainst = new LinkedHashMap<>();
	    mapAgainst.put("apple", new Integer(5));
	    mapAgainst.put("orange", new Integer(3));
	    
	    assertEquals(invOwd, mapAgainst);
	    
	    invDm = (LinkedHashMap<Object, Integer>) shipment.get(1).get("dm");
		mapAgainst = new LinkedHashMap<>();
	    mapAgainst.put("apple", new Integer(2));
	    
	    assertEquals(invDm, mapAgainst);
	    
	    LinkedHashMap<Object, Integer> invWh = (LinkedHashMap<Object, Integer>) shipment.get(2).get("wh");
		mapAgainst = new LinkedHashMap<>();
	    mapAgainst.put("apple", new Integer(3));
	    mapAgainst.put("orange", new Integer(1));
	    
	    assertEquals(invWh, mapAgainst);
	    
	    printOut(6, shipment);
	}
		
	@SuppressWarnings("unchecked")
	@Test
	public void testGetCheapestShipmentAllocator7()
	{
		/*order is empty, warehouse is empty*/
		shipment = allocator7.getCheapestShipment();
		
		assertTrue(shipment.size() == 0);
		
		printOut(7, shipment);
	}
		
	@SuppressWarnings("unchecked")
	@Test
	public void testGetCheapestShipmentAllocator8()
	{
		/*Allocator8 Test*/
		/*warehouse is empty*/
		shipment = allocator8.getCheapestShipment();
		
		assertTrue(shipment.size() == 0);
		
		printOut(8, shipment);
	}
	    
	@SuppressWarnings("unchecked")
	@Test
	public void testGetCheapestShipmentAllocator9()
	{
		/*Allocator9 Test*/
		/*order is empty*/
		shipment = allocator9.getCheapestShipment();
		
		assertTrue(shipment.size() == 0);
		
		printOut(9, shipment);
	}
	    
	@SuppressWarnings("unchecked")
	@Test
	public void testGetCheapestShipmentAllocator10()
	{
		/*Allocator10 Test*/
		/*Last warehouse available*/
		shipment = allocator10.getCheapestShipment();

	    invWh = (LinkedHashMap<Object, Integer>) shipment.get(0).get("wh");
		mapAgainst = new LinkedHashMap<>();
	    mapAgainst.put("apple", new Integer(5));
	    
	    assertEquals(invWh, mapAgainst);
	    
	    printOut(10, shipment);
	}
		
	@SuppressWarnings("unchecked")
	@Test
	public void testGetCheapestShipmentAllocator11()
	{
		 /*Allocator11 Test*/
		/*Last warehouse with extra allocation*/
		shipment = allocator11.getCheapestShipment();

		invDm = (LinkedHashMap<Object, Integer>) shipment.get(0).get("dm");
		mapAgainst = new LinkedHashMap<>();
	    mapAgainst.put("apple", new Integer(1));
	    
	    assertEquals(invDm, mapAgainst);
	    
	    invWh = (LinkedHashMap<Object, Integer>) shipment.get(1).get("wh");
		mapAgainst = new LinkedHashMap<>();
	    mapAgainst.put("apple", new Integer(4));
	    
	    assertEquals(invWh, mapAgainst);
	    
	    printOut(11, shipment);
	}

	
	private void printOut(int nth, ArrayList<LinkedHashMap<String, Object>> shipment)
	{
		System.out.println("Test " + nth + " result:");
	    System.out.println(shipment);
	    System.out.println();
	}
	

}