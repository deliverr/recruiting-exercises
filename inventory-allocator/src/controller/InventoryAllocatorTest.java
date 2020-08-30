package controller;

import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import org.junit.Test;

import Type.AbstractItem;
import Type.AbstractOrder;
import Type.AbstractOrderItem;
import Type.AbstractWarehouse;
import model.Item;
import model.Order;
import model.OrderItem;
import model.Warehouse;

public class InventoryAllocatorTest {

	/**
	 * Input: { apple: 5, banana: 10 }, [{ name: owd, inventory: { apple: 4, banana:10 } }, { name: dm, inventory: { apple: 5, banana:10 }}]
	 * Output: [{ dm: { apple: 1 }}, { owd: { apple: 4, banana: 10 } }]
	 * 
	 */
	@Test
	public void testShippingUsingMultipleWarehouse() {
		AbstractOrder order = new Order();
		
		AbstractItem item1 = new Item();
		item1.setId(1);
		item1.setName("apple");
		AbstractOrderItem orderItem1 = new OrderItem();
		orderItem1.setItem(item1);
		orderItem1.setQuantity(5);
		AbstractItem item2 = new Item();
		item2.setId(1);
		item2.setName("banana");
		AbstractOrderItem orderItem2 = new OrderItem();
		orderItem2.setItem(item2);
		orderItem2.setQuantity(10);
		
		List<AbstractOrderItem> orderItemList = new ArrayList<>();
		orderItemList.add(orderItem1);
		orderItemList.add(orderItem2);
		
		order.setOrderItems(orderItemList);
		order.setAccountId(1234);
		
		
		
		Warehouse wh1 = new Warehouse();
		HashMap<String, Integer> inventoryForwh1 = new HashMap<>();
		inventoryForwh1.put("apple", 4);
		inventoryForwh1.put("banana", 10);
		wh1.setName("owd");
		wh1.setInventoryDistributionMap(inventoryForwh1);
		
		Warehouse wh2 = new Warehouse();
		HashMap<String, Integer> inventoryForwh2 = new HashMap<>();
		inventoryForwh2.put("apple", 5);
		inventoryForwh2.put("bannana", 10);		
		wh2.setName("dm");
		wh2.setInventoryDistributionMap(inventoryForwh2);
		
		List<AbstractWarehouse> warehouseList = new ArrayList<AbstractWarehouse>();
		
		warehouseList.add(wh1);
		warehouseList.add(wh2);
		HashMap<String, HashMap<String, Integer>> cheapestShipmentList = InventoryAllocator.getCheapestShipment(order, warehouseList);
		
		int appleCountFordm = cheapestShipmentList.get("dm").get("apple");
		boolean bananaFordm = cheapestShipmentList.get("dm").containsKey("banana");
		int appleCountForowd = cheapestShipmentList.get("owd").get("apple");
		int bananaCountForowd = cheapestShipmentList.get("owd").get("banana");
		
		assertFalse(cheapestShipmentList.isEmpty());
		assertNotNull(cheapestShipmentList.get("owd"));
		assertNotNull(cheapestShipmentList.get("dm"));		
		assertEquals(1, appleCountFordm);
		assertEquals(false, bananaFordm);
		assertEquals(4, appleCountForowd);
		assertEquals(10, bananaCountForowd);
	}
	
	/**
	 * Input: { apple: 1 }, [{ name: owd, inventory: { apple: 0 } }]
	 * Output: []
	 */
	@Test
	public void testIfOrderCannotBeShipped() {
		AbstractOrder order = new Order();
		
		AbstractItem item1 = new Item();
		item1.setId(1);
		item1.setName("apple");
		AbstractOrderItem orderItem1 = new OrderItem();
		orderItem1.setItem(item1);
		orderItem1.setQuantity(1);
		List<AbstractOrderItem> orderItemList = new ArrayList<>();
		orderItemList.add(orderItem1);		
		order.setOrderItems(orderItemList);
		
		Warehouse wh1 = new Warehouse();
		HashMap<String, Integer> inventoryForwh1 = new HashMap<>();
		inventoryForwh1.put("apple", 0);
		wh1.setName("owd");
		wh1.setInventoryDistributionMap(inventoryForwh1);
		
		List<AbstractWarehouse> warehouseList = new ArrayList<AbstractWarehouse>();
		
		warehouseList.add(wh1);
		
		HashMap<String, HashMap<String, Integer>> cheapestShipmentList = InventoryAllocator.getCheapestShipment(order, warehouseList);
		
		assertTrue(cheapestShipmentList.isEmpty());
	}
	
	/**
	 * Input: { apple: 1 }, [{ name: owd, inventory: { apple: 1 } }]
	 * Output: [{ owd: { apple: 1 } }]
	 */
	@Test
	public void testShippingUsingSingleWarehouse() {
		AbstractOrder order = new Order();
		AbstractItem item1 = new Item();
		item1.setId(1);
		item1.setName("apple");
		AbstractOrderItem orderItem1 = new OrderItem();
		orderItem1.setItem(item1);
		orderItem1.setQuantity(1);
		List<AbstractOrderItem> orderItemList = new ArrayList<>();
		orderItemList.add(orderItem1);		
		order.setOrderItems(orderItemList);
		
		Warehouse wh1 = new Warehouse();
		HashMap<String, Integer> inventoryForwh1 = new HashMap<>();
		inventoryForwh1.put("apple", 1);
		wh1.setName("owd");
		wh1.setInventoryDistributionMap(inventoryForwh1);
		
		List<AbstractWarehouse> warehouseList = new ArrayList<AbstractWarehouse>();
		
		warehouseList.add(wh1);
		
		HashMap<String, HashMap<String, Integer>> cheapestShipmentList = InventoryAllocator.getCheapestShipment(order, warehouseList);
		
		int appleCountForowd = cheapestShipmentList.get("owd").get("apple");
		boolean bananaForowd = cheapestShipmentList.get("owd").containsKey("banana");
		
		assertFalse(cheapestShipmentList.isEmpty());
		assertNotNull(cheapestShipmentList.get("owd"));
		assertEquals(1, appleCountForowd);
		assertEquals(false, bananaForowd);
	}
	
	/**
	 * Input: { pear: 2, orange:1 }, [{ name: owd, inventory: { pear: 1 } }]
	 * Output: [{ owd: { pear: 1 } }]
	 */
	@Test
	public void testIfPartialOrderCanBeShipped() {
		AbstractOrder order = new Order();
		AbstractItem item1 = new Item();
		item1.setId(1);
		item1.setName("pear");
		AbstractOrderItem orderItem1 = new OrderItem();
		orderItem1.setItem(item1);
		orderItem1.setQuantity(2);
		
		AbstractItem item2 = new Item();
		item2.setId(1);
		item2.setName("orange");
		AbstractOrderItem orderItem2 = new OrderItem();
		orderItem2.setItem(item2);
		orderItem2.setQuantity(1);
		
		List<AbstractOrderItem> orderItemList = new ArrayList<>();
		orderItemList.add(orderItem1);		
		order.setOrderItems(orderItemList);
		
		Warehouse wh1 = new Warehouse();
		HashMap<String, Integer> inventoryForwh1 = new HashMap<>();
		inventoryForwh1.put("pear", 1);
		wh1.setName("owd");
		wh1.setInventoryDistributionMap(inventoryForwh1);
		
		List<AbstractWarehouse> warehouseList = new ArrayList<AbstractWarehouse>();
		
		warehouseList.add(wh1);
		HashMap<String, HashMap<String, Integer>> cheapestShipmentList = InventoryAllocator.getCheapestShipment(order, warehouseList);
		
		
		int PearCountForowd = cheapestShipmentList.get("owd").get("pear");
		boolean orangeForowd = cheapestShipmentList.get("owd").containsKey("orange");
		
		assertFalse(cheapestShipmentList.isEmpty());
		assertNotNull(cheapestShipmentList.get("owd"));
		assertEquals(1, PearCountForowd);
		assertEquals(false, orangeForowd);
	}
	
	/**
	 * Input: { pear: 10, orange:5 }, [{ name: owd, inventory: { pear: 5 } }, { name: dm, inventory: { pear: 5 } }]
	 * Output: [{ owd: { pear: 5 } }, { dm: { pear: 5 } }]
	 */
	@Test
	public void testIfPartialOrderCanBeShippedFromMultipleWarehous() {
		AbstractOrder order = new Order();
		AbstractItem item1 = new Item();
		item1.setId(1);
		item1.setName("pear");
		AbstractOrderItem orderItem1 = new OrderItem();
		orderItem1.setItem(item1);
		orderItem1.setQuantity(10);
		
		AbstractItem item2 = new Item();
		item2.setId(1);
		item2.setName("orange");
		AbstractOrderItem orderItem2 = new OrderItem();
		orderItem2.setItem(item2);
		orderItem2.setQuantity(5);
		
		List<AbstractOrderItem> orderItemList = new ArrayList<>();
		orderItemList.add(orderItem1);		
		order.setOrderItems(orderItemList);
		
		Warehouse wh1 = new Warehouse();
		HashMap<String, Integer> inventoryForwh1 = new HashMap<>();
		inventoryForwh1.put("pear", 5);
		wh1.setName("owd");
		wh1.setInventoryDistributionMap(inventoryForwh1);
		
		Warehouse wh2 = new Warehouse();
		HashMap<String, Integer> inventoryForwh2 = new HashMap<>();
		inventoryForwh2.put("pear", 5);
		wh2.setName("dm");
		wh2.setInventoryDistributionMap(inventoryForwh2);
		
		List<AbstractWarehouse> warehouseList = new ArrayList<AbstractWarehouse>();
		
		warehouseList.add(wh1);
		warehouseList.add(wh2);
		HashMap<String, HashMap<String, Integer>> cheapestShipmentList = InventoryAllocator.getCheapestShipment(order, warehouseList);
		
		int PearCountForowd = cheapestShipmentList.get("owd").get("pear");
		int PearCountFordm = cheapestShipmentList.get("dm").get("pear");
		boolean orangeForowd = cheapestShipmentList.get("owd").containsKey("orange");
		boolean orangeFordm = cheapestShipmentList.get("owd").containsKey("orange");
		
		assertFalse(cheapestShipmentList.isEmpty());
		assertNotNull(cheapestShipmentList.get("owd"));
		assertNotNull(cheapestShipmentList.get("dm"));
		assertEquals(5, PearCountForowd);
		assertEquals(5, PearCountFordm);
		assertEquals(false, orangeForowd);
		assertEquals(false, orangeFordm);
	}
	
	/**
	 * Input: {}, [{ name: owd, inventory: { pear: 5 } }, { name: dm, inventory: { pear: 5 } }]
	 * Output: []
	 */
	@Test
	public void testShipmentListIsNullIfOrderIsNull()
	{
		AbstractOrder order = new Order();
		
		Warehouse wh1 = new Warehouse();
		HashMap<String, Integer> inventoryForwh1 = new HashMap<>();
		inventoryForwh1.put("pear", 5);
		wh1.setName("owd");
		wh1.setInventoryDistributionMap(inventoryForwh1);
		
		Warehouse wh2 = new Warehouse();
		HashMap<String, Integer> inventoryForwh2 = new HashMap<>();
		inventoryForwh2.put("pear", 5);
		wh2.setName("dm");
		wh2.setInventoryDistributionMap(inventoryForwh2);
		
		List<AbstractWarehouse> warehouseList = new ArrayList<AbstractWarehouse>();
		
		warehouseList.add(wh1);
		warehouseList.add(wh2);
		
		HashMap<String, HashMap<String, Integer>> cheapestShipmentList = InventoryAllocator.getCheapestShipment(order, warehouseList);
		
		assertTrue(cheapestShipmentList.isEmpty());
	}	

}
