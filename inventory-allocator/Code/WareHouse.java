package Code;



import java.util.LinkedHashMap;
import java.util.Map;

/*
 * warehouse POJO class for dummy data
 */
public class WareHouse {

	private String warehouseName;
	private Map<String, Long> inventory;

	public WareHouse(String warehouseName) 
	{

		this.warehouseName = warehouseName;
		this.inventory = new LinkedHashMap<>();
	}
	
	//returns warehouse name
	public String getWarehouseName() 
	{
		return warehouseName;
	}

	//returns item count in warehouse
	public long getItemQuantity(String itemName) 
	{
		if (this.inventory.containsKey(itemName)) 
		{
			return (long) this.inventory.get(itemName);
		} 
		else 
		{
			return 0;
		}
	}
	
	//set warehouse name
	public void setWarehouseName(String warehouseName) 
	{
		this.warehouseName = warehouseName;
	}

	//set inventory
	public void setInventory(String name, long quantity) 
	{
		this.inventory.put(name, quantity);
	}
	
	//get inventory for warehouse
	public Map<String, Long> getInventory() 
	{
		return inventory;
	}

	@Override
	public String toString() 
	{
		return "WareHouse [warehouseName=" + warehouseName + ", inventory=" + inventory + "]";
	}

}
