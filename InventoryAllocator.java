import java.util.*;

public class InventoryAllocator {
	public List<Allocation> invetoryAllocator(Map<String, Integer> order, List<WareHouse> wareHouses) {
		Map<String, Integer> orderCopy = new HashMap<>();
		for(Map.Entry<String, Integer> entry: order.entrySet()) {
			orderCopy.put(entry.getKey(), entry.getValue());
		}
		List<Allocation> allocations = new ArrayList<>();
		for(WareHouse warehouse: wareHouses) {
			for(Map.Entry<String, Integer> entry: warehouse.inventory.entrySet()) {
				if(orderCopy.containsKey(entry.getKey())) {
					if(orderCopy.get(entry.getKey()) <= entry.getValue()) {
						allocations.add(new Allocation(warehouse.wareHouse, entry.getKey(), orderCopy.get(entry.getKey())));
						orderCopy.remove(entry.getKey());
						if(orderCopy.size() == 0) {
							return allocations;
						}
					} else {
						allocations.add(new Allocation(warehouse.wareHouse, entry.getKey(), entry.getValue()));
						orderCopy.put(entry.getKey(), orderCopy.get(entry.getKey()) - entry.getValue());
					}
				}
			}
		}
		return new ArrayList<>();
	}
}
class Allocation {
	String wareHouse;
	String item;
	int quantity;
	public Allocation(String wareHouse, String item, int quantity) {
		this.wareHouse = wareHouse;
		this.item = item;
		this.quantity = quantity;
	}
	@Override
	public String toString() {
		return "wareHouse: " + wareHouse + ": [" + item + ": " + quantity + "]";
	}
	@Override
	public boolean equals(Object obj) {
		if(obj == null || !(obj instanceof Allocation)) {
			return false;
		}
		Allocation another = (Allocation) obj;
		return wareHouse.equals(another.wareHouse) && item.equals(another.item) && quantity == another.quantity;
	}
	@Override
	public int hashCode() {
		return wareHouse.hashCode() + 13 * item.hashCode() + quantity * 17;
	}
}
class WareHouse {
	String wareHouse;
	Map<String, Integer> inventory;
	public WareHouse(String wareHouse, Map<String, Integer> inventory) {
		this.wareHouse = wareHouse;
		this.inventory = inventory;
	}
}
class AllocationComparator implements Comparator<Allocation> {

	@Override
	public int compare(Allocation a1, Allocation a2) {
		if(a1.wareHouse != a2.wareHouse) {
			return a1.wareHouse.compareTo(a2.wareHouse);
		}
		if(a1.item != a2.item) {
			return a1.item.compareTo(a2.item);
		}
		return a1.quantity < a2.quantity ? -1 : 1;
	}
	
}
