package driver;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import Type.AbstractItem;
import Type.AbstractOrder;
import Type.AbstractOrderItem;
import Type.AbstractWarehouse;
import controller.InventoryAllocator;
import model.Item;
import model.Order;
import model.OrderItem;
import model.Warehouse;

/**
 * Driver class containing main() method from where application execution begins.
 * @author Arundathi Patil
 *
 */
public class Driver {

	public static void main(String[] args) {
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
		
		
		System.out.println("Input: { apple: 5, banana: 10 }, [{ name: owd, inventory: { apple: 4, banana:10 } }, { name: dm, inventory: { apple: 5, banana:10 }}]");
		HashMap<String, HashMap<String, Integer>> cheapestShipmentList = InventoryAllocator.getCheapestShipment(order, warehouseList);
		System.out.println("Output: " +cheapestShipmentList.toString());

	}

}
