import static org.junit.jupiter.api.Assertions.*;

import java.util.LinkedHashMap;
import java.util.Map;

import org.junit.jupiter.api.Test;

class ShipmentsTest {
	
	private static String APPLE = "apple";
	private static String BANANA = "banana";
	private static String ORANGE = "orange";
	private static String OWD = "owd";
	private static String DM = "dm";


	@Test
	void testProcessShipmentsCase1() {
		Shipments shipments = new Shipments();
		Map<String, Map<String, Integer>> shipmentMap = shipments.processShipment(getOrderedItemsCase1(),
				getInventoryMapCase1());
		System.out.println("Test Case 1 "+ shipmentMap);
		assertEquals(shipmentMap.size(), 1);
		assertEquals("{owd={apple=1}}", shipmentMap.toString());
	}
	
	@Test
	void testProcessShipmentsCase2() {
		Shipments shipments = new Shipments();
		Map<String, Map<String, Integer>> shipmentMap = shipments.processShipment(getOrderedItemsCase2(),
				getInventoryMapCase2());
                System.out.println("Test Case 2 "+ shipmentMap);
		assertEquals(shipmentMap.size(), 2);
		assertEquals("{owd={apple=5}, dm={apple=5}}", shipmentMap.toString());
	}
	
	@Test
	void testProcessShipmentsCase3() {
		Shipments shipments = new Shipments();
		Map<String, Map<String, Integer>> shipmentMap = shipments.processShipment(getOrderedItemsCase3(),
				getInventoryMapCase3());
	        System.out.println("Test Case 3 "+ shipmentMap);
		assertEquals(shipmentMap.size(), 0);
		assertEquals("{}", shipmentMap.toString());
	}
	
	@Test
	void testProcessShipmentsCase4() {
		Shipments shipments = new Shipments();
		Map<String, Map<String, Integer>> shipmentMap = shipments.processShipment(getOrderedItemsCase4(),
				getInventoryMapCase4());
		assertEquals(shipmentMap.size(), 2);
                System.out.println("Test Case 1 "+ shipmentMap);
		assertEquals("{owd={apple=5, orange=5}, dm={banana=5}}", shipmentMap.toString());
	}

	private Map<String, Integer> getOrderedItemsCase1() {
		Map<String, Integer> orderedItems = new LinkedHashMap<>();
		orderedItems.put(APPLE, 1);

		return orderedItems;
	}

	private Map<String, Map<String, Integer>> getInventoryMapCase1() {
		Map<String, Map<String, Integer>> inventoryMap = new LinkedHashMap<>();

		Map<String, Integer> owdInventoryItem = new LinkedHashMap<>();
		owdInventoryItem.put(APPLE, 1);
		inventoryMap.put(OWD, owdInventoryItem);

		return inventoryMap;
	}

	private Map<String, Integer> getOrderedItemsCase2() {
		Map<String, Integer> orderedItems = new LinkedHashMap<>();
		orderedItems.put(APPLE, 10);

		return orderedItems;
	}

	private Map<String, Map<String, Integer>> getInventoryMapCase2() {
		Map<String, Map<String, Integer>> inventoryMap = new LinkedHashMap<>();

		Map<String, Integer> owdInventoryItem = new LinkedHashMap<>();
		owdInventoryItem.put(APPLE, 5);
		inventoryMap.put(OWD, owdInventoryItem);

		Map<String, Integer> dmInventoryItem = new LinkedHashMap<>();
		dmInventoryItem.put(APPLE, 5);
		inventoryMap.put(DM, dmInventoryItem);

		return inventoryMap;
	}

	private Map<String, Integer> getOrderedItemsCase3() {
		Map<String, Integer> orderedItems = new LinkedHashMap<>();
		orderedItems.put(APPLE, 1);

		return orderedItems;
	}

	private Map<String, Map<String, Integer>> getInventoryMapCase3() {
		Map<String, Map<String, Integer>> inventoryMap = new LinkedHashMap<>();

		Map<String, Integer> owdInventoryItem = new LinkedHashMap<>();
		owdInventoryItem.put(APPLE, 0);
		inventoryMap.put(OWD, owdInventoryItem);

		return inventoryMap;
	}
	
	private Map<String, Integer> getOrderedItemsCase4() {
		Map<String, Integer> orderedItems = new LinkedHashMap<>();
		orderedItems.put(APPLE, 5);
		orderedItems.put(BANANA, 5);
		orderedItems.put(ORANGE, 5);

		return orderedItems;
	}

	private Map<String, Map<String, Integer>> getInventoryMapCase4() {
		Map<String, Map<String, Integer>> inventoryMap = new LinkedHashMap<>();

		Map<String, Integer> owdInventoryItem = new LinkedHashMap<>();
		owdInventoryItem.put(APPLE, 5);
		owdInventoryItem.put(ORANGE, 10);
		inventoryMap.put(OWD, owdInventoryItem);

		Map<String, Integer> dmInventoryItem = new LinkedHashMap<>();
		dmInventoryItem.put(BANANA, 5);
		dmInventoryItem.put(ORANGE, 10);
		inventoryMap.put(DM, dmInventoryItem);

		return inventoryMap;
	}

}
