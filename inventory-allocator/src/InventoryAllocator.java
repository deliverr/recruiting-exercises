import java.util.*;

public class InventoryAllocator {

	private LinkedHashMap<Object, Integer> order;
	private ArrayList<LinkedHashMap<Object, Object>> warehouse;
	
	public InventoryAllocator(LinkedHashMap<Object, Integer> order, ArrayList<LinkedHashMap<Object, Object>> warehouse)
	{
		this.order = order;
		this.warehouse = warehouse;
	}
	
	@SuppressWarnings("unchecked")
	public ArrayList<LinkedHashMap<String, Object>> getCheapestShipment()
	{
		//record all the shipment from each warehouse for every possible order
		ArrayList<LinkedHashMap<String, Object>> shipment = new ArrayList<>();
		
		//record temporarily all the shipment from each warehouse
		LinkedHashMap<String, LinkedHashMap<Object, Integer>> tmp = new LinkedHashMap<>();
		for(Object k : order.keySet())
		{
			//record all the warehouse name and amount allocated with i = warehouse name & i+1 = allocated amount
			ArrayList<Object> shipping = new ArrayList<Object>();
			
			int remOrder = order.get(k);
			for(int i = 0 ; i < warehouse.size(); i++)
			{
				LinkedHashMap<Object, Object> description = warehouse.get(i);
				
				//get the name of the warehouse
				String name = (String) description.get("name");

				//get the inventory of the warehouse
				HashMap<Object, Integer> inventory = (HashMap<Object, Integer>) description.get("inventory");
				
				//shipment can be done from this particular warehouse
				if(inventory.containsKey(k) && inventory.get(k) > 0)
				{
					//allocated amount
					int allocatedAmount = Math.min(remOrder, inventory.get(k));
					
					//update order
					remOrder -= allocatedAmount;					
					
					//update inventory(this snippet is unnecessary due to 1-1 mapping)
					int remaining = inventory.get(k) - allocatedAmount;
					if(remaining == 0)
						inventory.remove(k);
					else
						inventory.put(k, remaining);
					
					//update shipping
					shipping.add(name);
					shipping.add(allocatedAmount);
					
					//cheapest found
					if(remOrder == 0)
						break;
					
				}
				
			}
			
			/*Update shipment if an order can be placed.
			  if an order cannot be placed, then the allocation would not be recorded in any
			  of these shipments*/ 
			if(remOrder == 0)
			{
				for(int i = 0 ; i < shipping.size()-1; i+=2)
				{
					if(!tmp.containsKey(shipping.get(i)))
						tmp.put((String) shipping.get(i), new LinkedHashMap<Object, Integer>());
					
					tmp.get(shipping.get(i)).put(k, (Integer) shipping.get(i+1));
				}
				
			}
			
			
		}
		
		//put data shipment into the arraylist
		for(String s : tmp.keySet())
		{
			LinkedHashMap<String, Object> m = new LinkedHashMap<>();
			m.put(s, tmp.get(s));
			
			shipment.add(m);
		}
		
		return shipment;
	}
	
	
	
	
}
