package Code;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class InventoryAllocator {
	
	/*
	 * function which returns cheapest shipment in terms of list of hashmaps.
	 */
	public List<Map> cheapestShipment(Map<String, Long> order, List<WareHouse> available) 
	{	
		
		List<Map> result = new ArrayList<>();  //list to store result
		Map<String, HashMap<String, Long>> currentMap = new LinkedHashMap<String, HashMap<String, Long>>();  //map for storing available data
		long numberOfWareHouse=available.size();  
		
		
		//returns empty list if no warehouse present or no order present 
		if(numberOfWareHouse==0 || order.size()==0)
		{			
			return result;
		}
		
		
		//looping for checking order items
		for (String itemName : order.keySet())
		{
			String currentItem = itemName;			
			long currentCount = order.get(itemName);	
			if(currentCount<=0)
			{	
				return result;
			}
				//loop for checking available items for order items in warehouse
				for (int i = 0; i < numberOfWareHouse; i++) 
				{	
					WareHouse currentWareHouse = available.get(i);
					
					//no items are available in warehouse 
					if(currentWareHouse.getInventory().size()==0)
					{
						continue;
					}
					String currentWareHouseName = currentWareHouse.getWarehouseName();
					long currentWareHouseItemQuantity = currentWareHouse.getItemQuantity(currentItem);
					
					
					//edge case for item count
					if (currentWareHouseItemQuantity <= 0) 
					{
						continue;
					}
					
					//if desired count of item is satisfied then break
					if(currentCount<=0)
					{
						break;
					}
					
					//available count in warehouse is let than desired count then update new desired count by subtracting available count
					else if (currentCount > currentWareHouseItemQuantity) 
					{
							currentCount = currentCount - currentWareHouseItemQuantity;							
							HashMap<String, Long> temp = currentMap.getOrDefault(currentWareHouseName, new LinkedHashMap<>());
							temp.put(currentItem, currentWareHouseItemQuantity);
							currentMap.put(currentWareHouseName, temp);
							
					} 
					//available count is more or equal then fulfill particular item. 
					else 
					{	
							currentCount = 0;
							HashMap<String, Long> temp = currentMap.getOrDefault(currentWareHouseName, new LinkedHashMap<>());
							temp.put(currentItem, currentWareHouseItemQuantity);
							currentMap.put(currentWareHouseName, temp);							
							break;
					}
				}
			
			//if order item is not satisfied then return empty list
			if (currentCount != 0) 
			{
				result.clear();
				return result;
			} 
			
		}
		
		
		//all items are satisfied and store in list of cheapest Shipment warehouse maps
		for(String itemName : currentMap.keySet())
		{
			HashMap<String, HashMap<String, Long>> current = new LinkedHashMap<String, HashMap<String, Long>>();
			current.put(itemName, currentMap.get(itemName));
			result.add(current);			
		}
		
		//return list of cheapest Shipment warehouse maps
		return result;		
		
	}
}
