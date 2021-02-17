package Code;
import Code.InventoryAllocator;
import Code.WareHouse;



import static org.junit.Assert.assertEquals;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import org.junit.Test;
import org.junit.internal.TextListener;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;


/*
 * test class for InventoryAllocator
 */
public class TestInventoryAllocator {

	private Map<String, Long> order;  //order input
	private List<Map> testOutputList; //test result for cheapest shipment

	public TestInventoryAllocator()
	{
		order = new LinkedHashMap<>();
		testOutputList = new ArrayList<>();
	}	
	
	
	

	/*
	 * this test is for ordering single items from single warehouse Happy Case,
	 * exact inventory match!*
	 *
	input is :
		order is : {apple=1}
		data is : [WareHouse [warehouseName=owd, inventory={apple=1}]]
	output is :
		available is:[{owd={apple=1}}]
	 *
	 */
	@Test
	public void testWithOneItem() 
	{
		//adding warehouse data
		WareHouse owd = new WareHouse("owd");
		owd.setInventory("apple", 1);
		List<WareHouse> warehouseList = new ArrayList<>();
		warehouseList.add(owd);		
		
		//adding values for order
		order.put("apple", (long) 1);		
		
		InventoryAllocator object = new InventoryAllocator();
			
		//dummy result data 
		Map<String, HashMap<String, Long>> outputMap = new LinkedHashMap<String, HashMap<String, Long>>();
		HashMap<String, Long> innerMap=new LinkedHashMap<>();
		innerMap.put("apple", (long) 1);
		outputMap.put("owd", innerMap);
		testOutputList.add(outputMap);
		
		
		
		assertEquals(testOutputList,object.cheapestShipment(order, warehouseList));
	}
	
	
	

	/*
	 * this test is for Not enough inventory -> no allocations!
	 * 
	 * 
	 * input is :
			order is : {apple=1}
			data is : [WareHouse [warehouseName=owd, inventory={}]]
		output is :
			available is:[]
	 */
	@Test
	public	void testWithNoItemInWareHouse() 
	{
		//adding warehouse data
		WareHouse owd = new WareHouse("owd");
		List<WareHouse> warehouseList = new ArrayList<>();
		warehouseList.add(owd);
		
		//adding values for order
		order.put("apple", (long) 1);
		
		InventoryAllocator object = new InventoryAllocator();	
		
		assertEquals(testOutputList,object.cheapestShipment(order, warehouseList));
	}
	
	
	

	/*
	 * this test is for ordering one item in multiple warehouse
	 * 
	 * input is :
			order is : {apple=10}
			data is : [WareHouse [warehouseName=owd, inventory={apple=5}], WareHouse [warehouseName=dm, inventory={apple=5}]]
	   output is :
			available is:[{owd={apple=5}}, {dm={apple=5}}]
	 */
	@Test
	public void testWithSplitItems() 
	{
		//adding warehouse data
		WareHouse owd = new WareHouse("owd");
		owd.setInventory("apple", 5);
		WareHouse dm = new WareHouse("dm");
		dm.setInventory("apple", 5);
		List<WareHouse> warehouseList = new ArrayList<>();
		warehouseList.add(owd);
		warehouseList.add(dm);		
		
		//adding values for order
		order.put("apple", (long) 10);

		InventoryAllocator object = new InventoryAllocator();		
		
		//dummy result data 
		Map<String, HashMap<String, Long>> outputMapOWD = new LinkedHashMap<String, HashMap<String, Long>>();
		HashMap<String, Long> innerMapOWD=new LinkedHashMap<>();
		innerMapOWD.put("apple", (long) 5);
		outputMapOWD.put("owd", innerMapOWD);
		testOutputList.add(outputMapOWD);		
		Map<String, HashMap<String, Long>> outputMapDM = new LinkedHashMap<String, HashMap<String, Long>>();
		HashMap<String, Long> innerMapDM=new LinkedHashMap<>();
		innerMapDM.put("apple", (long) 5);
		outputMapDM.put("dm", innerMapDM);
		testOutputList.add(outputMapDM);	
		
		assertEquals(testOutputList,object.cheapestShipment(order, warehouseList));

		
	}

	/*
	 * this test is for ordering multiple items in multiple warehouses
		input is :
			order is : {apple=10, banana=5, orange=20}
			data is : [WareHouse [warehouseName=owd, inventory={apple=5, orange=10, banana=5}], WareHouse [warehouseName=dm, inventory={apple=5, banana=5, orange=100}]]
		output is :
			available is:[{owd={apple=5, banana=5, orange=10}}, {dm={apple=5, orange=100}}]
	 */
	@Test
	public void testWithMultipleItems() 
	{
		
		//adding warehouse data
		WareHouse owd = new WareHouse("owd");
		owd.setInventory("apple", 5);
		owd.setInventory("orange", 10);
		owd.setInventory("banana", 5);
		WareHouse dm = new WareHouse("dm");
		dm.setInventory("apple", 5);
		dm.setInventory("banana", 5);
		dm.setInventory("orange", 100);
		List<WareHouse> warehouseList = new ArrayList<>();
		warehouseList.add(owd);
		warehouseList.add(dm);		
		
		//adding values for order
		order.put("apple", (long) 10);
		order.put("banana", (long) 5);
		order.put("orange", (long) 20);
		
		InventoryAllocator object = new InventoryAllocator();
		
		//dummy result data 	
		Map<String, HashMap<String, Long>> outputMapOWD = new LinkedHashMap<String, HashMap<String, Long>>();
		HashMap<String, Long> innerMapOWD=new LinkedHashMap<>();
		innerMapOWD.put("apple", (long) 5);
		innerMapOWD.put("banana", (long) 5);
		innerMapOWD.put("orange", (long) 10);
		outputMapOWD.put("owd", innerMapOWD);
		testOutputList.add(outputMapOWD);
		
		Map<String, HashMap<String, Long>> outputMapDM = new LinkedHashMap<String, HashMap<String, Long>>();
		HashMap<String, Long> innerMapDM=new LinkedHashMap<>();
		innerMapDM.put("apple", (long) 5);
		innerMapDM.put("orange", (long) 100);
		outputMapDM.put("dm", innerMapDM);
		testOutputList.add(outputMapDM);
		
		assertEquals(testOutputList,object.cheapestShipment(order, warehouseList));
	}
	
	
	
	
	
	
	/*
	 * this test is with warehouse having negative value
	 * 
	   input is :
			order is : {apple=5}
			data is : [WareHouse [warehouseName=owd, inventory={apple=-4}], WareHouse [warehouseName=dm, inventory={apple=5}]]
	   output is :
			available is:[{dm={apple=5}}]
	 */
	@Test
	public void testWithNegativeWarehouseItem() 
	{
		
		//adding warehouse data
		WareHouse owd = new WareHouse("owd");
		owd.setInventory("apple", -4);
		WareHouse dm = new WareHouse("dm");
		dm.setInventory("apple", 5);
		List<WareHouse> warehouseList = new ArrayList<>();
		warehouseList.add(owd);
		warehouseList.add(dm);		
		
		//adding values for order
		order.put("apple", (long) 5);

		InventoryAllocator object = new InventoryAllocator();
				
		//dummy result data 
		Map<String, HashMap<String, Long>> outputMapDM = new LinkedHashMap<String, HashMap<String, Long>>();
		HashMap<String, Long> innerMapDM=new LinkedHashMap<>();
		innerMapDM.put("apple", (long) 5);
		outputMapDM.put("dm", innerMapDM);
		testOutputList.add(outputMapDM);		
		
		assertEquals(testOutputList,object.cheapestShipment(order, warehouseList));
	}
	
	
	
	
	
	
	/*
	 * this test is for ordering zero or negative items,
	 * 
	 * input is :
			order is : {apple=-1}
			data is : [WareHouse [warehouseName=owd, inventory={apple=1}]]
	output is :
			available is:[]
	 * 
	 * 
	 * 
	 */
	@Test
	public void testWithNegativeOrderItem() 
	{
		//adding warehouse data
		WareHouse owd = new WareHouse("owd");
		owd.setInventory("apple", 1);
		List<WareHouse> warehouseList = new ArrayList<>();
		warehouseList.add(owd);
		
		//adding values for order
		order.put("apple", (long) -1);
		
		InventoryAllocator object = new InventoryAllocator();
		
		assertEquals(testOutputList,object.cheapestShipment(order, warehouseList));
	}
	
	

	/*
	 * this test is for testing no warehouse or no order available,
		input is :
			order is : {}
			data is : []
		output is :
			available is:[]
	 */
	@Test
	public void testForNoWareHousePresent() 
	{		
		InventoryAllocator object = new InventoryAllocator();
		
		assertEquals(testOutputList,object.cheapestShipment(order, new ArrayList<>()));
	}
	
	
	
	
	
	/*
	 * this test is for providing negative order value as same as warehouse
	 * 
	 * 
	 * input is :
			order is : {apple=-4, banana=0, orange=2}
			data is : [WareHouse [warehouseName=owd, inventory={apple=-4, banana=0, orange=2}]]
		output is :
			available is:[]
	 */
	@Test
	public void testWithNegativeWarehouseAndOrderItem() 
	{
		
		//adding warehouse data
		WareHouse owd = new WareHouse("owd");
		owd.setInventory("apple", -4);
		owd.setInventory("banana", 0);
		owd.setInventory("orange", 2);
		List<WareHouse> warehouseList = new ArrayList<>();
		warehouseList.add(owd);		
		
		//adding values for order
		order.put("apple", (long) -4);
		order.put("banana", (long) 0);
		order.put("orange", (long) 2);

		InventoryAllocator object = new InventoryAllocator();		
			
		assertEquals(testOutputList,object.cheapestShipment(order, warehouseList));
	}
}
