package controller;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;

import Type.AbstractItem;
import Type.AbstractOrder;
import Type.AbstractOrderItem;
import Type.AbstractWarehouse;
import model.Item;
import model.Order;
import model.OrderItem;
import model.Warehouse;

/**
 * Class-InventoryAllocator, Contains methods to compute the best way an order can be shipped 
 * given inventory across a set of warehouses
 * 
 * @author Arundathi Patil
 */
public class InventoryAllocator {
	
	/**
	 * 
	 * @param order
	 * @param warehouseList
	 * @return API- called by user to fetch the cheapest shipment list
	 */
	public static HashMap<String, HashMap<String, Integer>> getCheapestShipment(AbstractOrder order, List<AbstractWarehouse> warehouseList) {
		
		HashMap<String,Integer> itemsHashmap = buildHasmapOfOrder(order);
		HashMap<String, HashMap<String, Integer>> cheapestShipmentList = getWarehouseList(itemsHashmap, warehouseList);
		return cheapestShipmentList;
	}
	
	/**
	 * Builds HashMap of order items from given order
	 * @param order
	 * @return HashMap with key="order item name" and value="order item quantity"
	 */
	private static HashMap<String,Integer> buildHasmapOfOrder(AbstractOrder order) {
		List<AbstractOrderItem> itemList = order.getOrderItems();
		
		HashMap<String,Integer> itemsHashmap = new HashMap<String, Integer>();
		if(itemList !=null) {
			for(AbstractOrderItem item: itemList) {
				itemsHashmap.put(item.getItem().getName(), item.getQuantity());
			}
		}		
		return itemsHashmap;
	}
	
	/**
	 * 
	 * @param order
	 * @param warehouseList
	 * @return Returns cheapestShippmentList of warehouses
	 */
	private static HashMap<String, HashMap<String, Integer>> getWarehouseList(HashMap<String,Integer> order, List<AbstractWarehouse> warehouseList) {
		
		HashMap<String, HashMap<String, Integer>> cheapestShipmentList = new HashMap<>();
		
		for(Map.Entry element: order.entrySet()) {
			String key = (String) element.getKey();
			int quantity = (int) element.getValue();			
			cheapestShipmentList = findWareHouse(key, quantity, warehouseList, cheapestShipmentList);			
		}		
		return cheapestShipmentList;		
	}
	
	/**
	 * Function to find warehouse whose inventory contains the required item from the order 
	 * @param item
	 * @param quantity
	 * @param warehouseList
	 * @return Returns Modified cheapestShippmentList of warehouses
	 */
	private static HashMap<String, HashMap<String, Integer>> findWareHouse(String item, int quantity, List<AbstractWarehouse> warehouseList, HashMap<String, HashMap<String, Integer>> cheapestShipmentList) {		
		int requiredQuantity = quantity;		
		for(int i=0; i< warehouseList.size();i++) {
			HashMap<String,Integer> inventoryDistribution = warehouseList.get(i).getInventoryDistributionMap();
			if(requiredQuantity <= 0) {
				break;
			} else {
				if(inventoryDistribution.containsKey(item)) {
					if(inventoryDistribution.get(item) >= requiredQuantity) {
						HashMap<String, Integer> items = cheapestShipmentList.get(warehouseList.get(i).getName());
						if(items == null) {
							HashMap<String, Integer> newitems = new HashMap<>();
							newitems.put(item, requiredQuantity);
							cheapestShipmentList.put(warehouseList.get(i).getName(), newitems);
						} else {
							items.put(item, requiredQuantity);
							cheapestShipmentList.put(warehouseList.get(i).getName(), items);
						}
						break;
					} else if(inventoryDistribution.get(item) == 0) {
						continue;
					} else {
						requiredQuantity = requiredQuantity - inventoryDistribution.get(item);
						HashMap<String, Integer> items = cheapestShipmentList.get(warehouseList.get(i).getName());
						if(items == null) {
							HashMap<String, Integer> newitems = new HashMap<>();
							newitems.put(item, inventoryDistribution.get(item));
							cheapestShipmentList.put(warehouseList.get(i).getName(), newitems);
						} else {
							items.put(item, inventoryDistribution.get(item));
							cheapestShipmentList.put(warehouseList.get(i).getName(), items);
						}
						
					}
					
				}
			}
		}
		return cheapestShipmentList;
	}
}
