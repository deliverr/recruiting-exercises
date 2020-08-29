package Type;

import java.util.HashMap;
import java.util.List;

/**
 * Abstract class used to declare/implement Warehouse class 
 * @author Arundathi Patil
 *
 */
public abstract class AbstractWarehouse {
	private int id;
	private String name;
	private List<AbstractInventoryItem> inventoryDistribution;
	private HashMap<String, Integer> inventoryDistributionMap;
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public List<AbstractInventoryItem> getInventoryDistribution() {
		return inventoryDistribution;
	}
	public void setInventoryDistribution(List<AbstractInventoryItem> inventoryDistribution) {
		this.inventoryDistribution = inventoryDistribution;
	}
	public HashMap<String, Integer> getInventoryDistributionMap() {
		return inventoryDistributionMap;
	}
	public void setInventoryDistributionMap(HashMap<String, Integer> inventoryDistributionMap) {
		this.inventoryDistributionMap = inventoryDistributionMap;
	}
	
	
	

}
