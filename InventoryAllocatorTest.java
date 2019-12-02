import static org.junit.Assert.*;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.junit.Before;
import org.junit.Test;

public class InventoryAllocatorTest {
	InventoryAllocator inventoryAllocation;
	AllocationComparator allocationComparator;

	@Before
	public void init() {
		inventoryAllocation = new InventoryAllocator();
		allocationComparator = new AllocationComparator();
	}

	// Happy Case, exact inventory match!
	@Test
	public void test0() {
		List<Allocation> expected = Arrays.asList(new Allocation[] { new Allocation("owd", "apple", 1) });
		Map<String, Integer> order = new HashMap<String, Integer>() {
			{
				put("apple", 1);
			}
		};
		List<WareHouse> wareHouses = Arrays
				.asList(new WareHouse[] { new WareHouse("owd", new HashMap<String, Integer>() {
					{
						put("apple", 1);
					}
				}) });
		List<Allocation> output = inventoryAllocation.invetoryAllocator(order, wareHouses);
		Collections.sort(expected, allocationComparator);
		Collections.sort(output, allocationComparator);
		assertEquals(expected, output);
	}

	// Not enough inventory -> no allocations!
	@Test
	public void test1() {
		List<Allocation> expected = Arrays.asList(new Allocation[] {});
		Map<String, Integer> order = new HashMap<String, Integer>() {
			{
				put("apple", 1);
			}
		};
		List<WareHouse> wareHouses = Arrays
				.asList(new WareHouse[] { new WareHouse("owd", new HashMap<String, Integer>() {
					{
						put("apple", 0);
					}
				}) });
		List<Allocation> output = inventoryAllocation.invetoryAllocator(order, wareHouses);
		Collections.sort(expected, allocationComparator);
		Collections.sort(output, allocationComparator);
		assertEquals(expected, output);
	}

	// Should split an item across warehouses if that is the only way to completely
	// ship an item:
	@Test
	public void test2() {
		List<Allocation> expected = Arrays
				.asList(new Allocation[] { new Allocation("dm", "apple", 5), new Allocation("owd", "apple", 5) });
		Map<String, Integer> order = new HashMap<String, Integer>() {
			{
				put("apple", 10);
			}
		};
		List<WareHouse> wareHouses = Arrays
				.asList(new WareHouse[] { new WareHouse("owd", new HashMap<String, Integer>() {
					{
						put("apple", 5);
					}
				}), new WareHouse("dm", new HashMap<String, Integer>() {
					{
						put("apple", 5);
					}
				}) });
		List<Allocation> output = inventoryAllocation.invetoryAllocator(order, wareHouses);
		Collections.sort(expected, allocationComparator);
		Collections.sort(output, allocationComparator);
		assertEquals(expected, output);
	}

	// Choose the least expensive approach when there are multiple possible
	// assignments
	@Test
	public void test3() {
		List<Allocation> expected = Arrays.asList(new Allocation[] { new Allocation("owd", "apple", 5) });
		Map<String, Integer> order = new HashMap<String, Integer>() {
			{
				put("apple", 5);
			}
		};
		List<WareHouse> wareHouses = Arrays
				.asList(new WareHouse[] { new WareHouse("owd", new HashMap<String, Integer>() {
					{
						put("apple", 5);
					}
				}), new WareHouse("dm", new HashMap<String, Integer>() {
					{
						put("apple", 5);
					}
				}) });
		List<Allocation> output = inventoryAllocation.invetoryAllocator(order, wareHouses);
		Collections.sort(expected, allocationComparator);
		Collections.sort(output, allocationComparator);
		assertEquals(expected, output);
	}

	// Make no selection when order is empty
	@Test
	public void test4() {
		List<Allocation> expected = Arrays.asList(new Allocation[] {});
		Map<String, Integer> order = new HashMap<String, Integer>();
		List<WareHouse> wareHouses = Arrays
				.asList(new WareHouse[] { new WareHouse("owd", new HashMap<String, Integer>() {
					{
						put("apple", 5);
					}
				}), new WareHouse("dm", new HashMap<String, Integer>() {
					{
						put("apple", 5);
					}
				}) });
		List<Allocation> output = inventoryAllocation.invetoryAllocator(order, wareHouses);
		Collections.sort(expected, allocationComparator);
		Collections.sort(output, allocationComparator);
		assertEquals(expected, output);
	}

	// Make no selection when order and inventory are both empty
	@Test
	public void test5() {
		List<Allocation> expected = Arrays.asList(new Allocation[] {});
		Map<String, Integer> order = new HashMap<String, Integer>();
		List<WareHouse> wareHouses = Arrays.asList(new WareHouse[] {});
		List<Allocation> output = inventoryAllocation.invetoryAllocator(order, wareHouses);
		Collections.sort(expected, allocationComparator);
		Collections.sort(output, allocationComparator);
		assertEquals(expected, output);
	}

	// A general case
	@Test
	public void test6() {
		List<Allocation> expected = Arrays
				.asList(new Allocation[] { new Allocation("owd", "apple", 1), new Allocation("dm", "apple", 4),
						new Allocation("owd", "orange", 4), new Allocation("dm", "orange", 1) });
		Map<String, Integer> order = new HashMap<String, Integer>() {
			{
				put("apple", 5);
				put("orange", 5);
			}
		};
		List<WareHouse> wareHouses = Arrays
				.asList(new WareHouse[] { new WareHouse("owd", new HashMap<String, Integer>() {
					{
						put("apple", 1);
						put("orange", 4);
					}
				}), new WareHouse("dm", new HashMap<String, Integer>() {
					{
						put("apple", 5);
						put("orange", 5);
					}
				}) });
		List<Allocation> output = inventoryAllocation.invetoryAllocator(order, wareHouses);
		Collections.sort(expected, allocationComparator);
		Collections.sort(output, allocationComparator);
		assertEquals(expected, output);
	}
}
