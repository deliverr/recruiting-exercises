import java.util.LinkedHashMap;
import java.util.Map;

public class Shipments {
	public static void main(String[] args) {
		Shipments shipments = new Shipments();
		System.out.println(shipments.processShipment(getOrderedItems(), getInventoryMap()));
	}

	public Map<String, Map<String, Integer>> processShipment(Map<String, Integer> orderedItems,
			Map<String, Map<String, Integer>> inventoryMap) {
		Map<String, Map<String, Integer>> shipment = new LinkedHashMap<>();
		// int companyCount = 0;// Variable to count the iteration of companies
		for (String orderedItem : orderedItems.keySet()) {
			boolean isOrderComplete = false;
			int companyCount = 0;// Variable to count the iteration of companies
			for (String company : inventoryMap.keySet()) {
				companyCount++;
				if (isOrderComplete)// If the Order item is completed do not search in more companies
					continue;

				if (inventoryMap.get(company).get(orderedItem) != null) {

					Map<String, Integer> shipmentOrderItemCurrent = new LinkedHashMap<>();
					Map<String, Integer> shipmentTotal = new LinkedHashMap<>();
					shipmentOrderItemCurrent.put(orderedItem,
							inventoryMap.get(company).get(orderedItem) > orderedItems.get(orderedItem)
									? orderedItems.get(orderedItem)
									: inventoryMap.get(company).get(orderedItem));

					if (shipment.containsKey(company)) {
						shipmentTotal.putAll(shipment.get(company));
					}

					shipmentTotal.putAll(shipmentOrderItemCurrent);
					shipment.put(company, shipmentTotal);
					if (inventoryMap.get(company).get(orderedItem) < orderedItems.get(orderedItem)) {

						orderedItems.put(orderedItem,
								orderedItems.get(orderedItem) - shipmentOrderItemCurrent.get(orderedItem));
						// If its the last company and order is still not met then remove all the
						// previous items
						if (companyCount == inventoryMap.keySet().size() && orderedItems.get(orderedItem) > 0) {
							for (String company1 : inventoryMap.keySet()) {
								if (shipment.get(company1) != null)
									shipment.get(company1).remove(orderedItem);
							}

						}
					} else if (inventoryMap.get(company).get(orderedItem) >= orderedItems.get(orderedItem)) {
						isOrderComplete = true;
					}

				}
			}

		}

		for (String shipMent : shipment.keySet()) {
			if (shipment.get(shipMent).isEmpty()) {
				shipment.remove(shipMent);
			}
		}

		return shipment;
	}

	public static Map<String, Integer> getOrderedItems() {
		Map<String, Integer> orderedItems = new LinkedHashMap<>();
		orderedItems.put("Apple", 5);
		orderedItems.put("Banana", 12); // remove if quantity not met
		orderedItems.put("Orange", 30);

		return orderedItems;
	}

	public static Map<String, Map<String, Integer>> getInventoryMap() {
		Map<String, Map<String, Integer>> inventoryMap = new LinkedHashMap<>();

		Map<String, Integer> owdInventoryItem = new LinkedHashMap<>();
		owdInventoryItem.put("Apple", 5);
		owdInventoryItem.put("Orange", 10);
		inventoryMap.put("Owd", owdInventoryItem);

		Map<String, Integer> dmInventoryItem = new LinkedHashMap<>();
		dmInventoryItem.put("Banana", 5);
		dmInventoryItem.put("Orange", 10);
		inventoryMap.put("dm", dmInventoryItem);

		Map<String, Integer> daInventoryItem = new LinkedHashMap<>();
		daInventoryItem.put("Banana", 5);
		daInventoryItem.put("Orange", 10);
		inventoryMap.put("da", daInventoryItem);
		return inventoryMap;
	}
}
