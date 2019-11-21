import static org.junit.Assert.*;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.Test;
import java.util.*;


public class InventoryAllocatorTest {

    @Test
    /** Exact inventory match. */
    public void testHappyCase() {
        HashMap<String, Integer> order = new HashMap<String, Integer>();
        order.put("apple", 1);

        LinkedList<Warehouse> warehouses = new LinkedList<Warehouse>();
        HashMap<String, Integer> inventory = new HashMap<String, Integer>();
        inventory.put("apple", 1);
        Warehouse wh = new Warehouse("owd", inventory);
        warehouses.add(wh);

        System.out.println("Input: " + order + ", " + warehouses);

        LinkedList<Warehouse> result = new LinkedList<Warehouse>();
        result.add(wh);

        InventoryAllocator allocator = new InventoryAllocator(order, warehouses);
        LinkedList<Warehouse> output = allocator.ship();

        System.out.println("Output: " + output);
        System.out.println();

        assertEquals(result.toString(), output.toString());
    }

    @Test
    /** Not enough inventory  -> No allocations. */
    public void testNotEnough() {
        HashMap<String, Integer> order = new HashMap<String, Integer>();
        order.put("apple", 1);

        LinkedList<Warehouse> warehouses = new LinkedList<Warehouse>();
        HashMap<String, Integer> inventory = new HashMap<String, Integer>();
        inventory.put("apple", 0);
        Warehouse wh = new Warehouse("owd", inventory);
        warehouses.add(wh);

        System.out.println("Input: " + order + ", " + warehouses);

        InventoryAllocator allocator = new InventoryAllocator(order, warehouses);
        LinkedList<Warehouse> output = allocator.ship();

        System.out.println("Output: " + output);
        System.out.println();

        assertEquals(new LinkedList<>(), output);
    }

    @Test
    /** Split an item across warehouses if that is the only way to completely ship an
     * item. */
    public void testSplit() {
        HashMap<String, Integer> order = new HashMap<String, Integer>();
        order.put("apple", 10);

        LinkedList<Warehouse> warehouses = new LinkedList<Warehouse>();

        HashMap<String, Integer> inventory1 = new HashMap<String, Integer>();
        inventory1.put("apple", 5);
        Warehouse wh1 = new Warehouse("owd", inventory1);
        warehouses.add(wh1);

        HashMap<String, Integer> inventory2 = new HashMap<String, Integer>();
        inventory2.put("apple", 5);
        Warehouse wh2 = new Warehouse("dm", inventory2);
        warehouses.add(wh2);

        System.out.println("Input: " + order + ", " + warehouses);

        LinkedList<Warehouse> result = new LinkedList<Warehouse>();
        result.add(wh1);
        result.add(wh2);

        InventoryAllocator allocator = new InventoryAllocator(order, warehouses);
        LinkedList<Warehouse> output = allocator.ship();

        System.out.println("Output: " + output);
        System.out.println();

        assertEquals(result.toString(), output.toString());
    }

    @Test
    /** Excess inventory from both warehouses. */
    public void testExample() {
        HashMap<String, Integer> order = new HashMap<String, Integer>();
        order.put("apple", 5);
        order.put("banana", 5);
        order.put("orange", 5);

        LinkedList<Warehouse> warehouses = new LinkedList<Warehouse>();

        HashMap<String, Integer> inventory1 = new HashMap<String, Integer>();
        inventory1.put("apple", 5);
        inventory1.put("orange", 10);
        Warehouse wh1 = new Warehouse("owd", inventory1);
        warehouses.add(wh1);

        HashMap<String, Integer> inventory2 = new HashMap<String, Integer>();
        inventory2.put("banana", 5);
        inventory2.put("orange", 10);
        Warehouse wh2 = new Warehouse("dm", inventory2);
        warehouses.add(wh2);

        System.out.println("Input: " + order + ", " + warehouses);

        InventoryAllocator allocator = new InventoryAllocator(order, warehouses);
        LinkedList<Warehouse> output = allocator.ship();

        LinkedList<Warehouse> result = new LinkedList<Warehouse>();

        HashMap<String, Integer> result_inv1 = new HashMap<String, Integer>();
        result_inv1.put("apple", 5);
        result_inv1.put("orange", 5);
        Warehouse result_wh1 = new Warehouse("owd", result_inv1);
        result.add(result_wh1);

        HashMap<String, Integer> result_inv2 = new HashMap<String, Integer>();
        result_inv2.put("banana", 5);
        Warehouse result_wh2 = new Warehouse("dm", result_inv2);
        result.add(result_wh2);

        System.out.println("Output: " + output);
        System.out.println();

        assertEquals(result.toString(), output.toString());
    }

    @Test
    /** Five items allocated from 4 warehouses. */
    public void test5Fruits() {
        HashMap<String, Integer> order = new HashMap<String, Integer>();
        order.put("apple", 5);
        order.put("banana", 5);
        order.put("orange", 20);
        order.put("mango", 5);
        order.put("watermelon", 15);

        LinkedList<Warehouse> warehouses = new LinkedList<Warehouse>();

        HashMap<String, Integer> inventory1 = new HashMap<String, Integer>();
        inventory1.put("apple", 10);
        inventory1.put("orange", 7);
        inventory1.put("watermelon", 7);
        Warehouse wh1 = new Warehouse("sf", inventory1);
        warehouses.add(wh1);

        HashMap<String, Integer> inventory2 = new HashMap<String, Integer>();
        inventory2.put("banana", 5);
        inventory2.put("orange", 10);
        inventory2.put("mango", 5);
        Warehouse wh2 = new Warehouse("ny", inventory2);
        warehouses.add(wh2);

        HashMap<String, Integer> inventory3 = new HashMap<String, Integer>();
        inventory3.put("banana", 5);
        inventory3.put("orange", 15);
        inventory3.put("mango", 5);
        Warehouse wh3 = new Warehouse("la", inventory3);
        warehouses.add(wh3);

        HashMap<String, Integer> inventory4 = new HashMap<String, Integer>();
        inventory4.put("watermelon", 9);
        Warehouse wh4 = new Warehouse("dc", inventory4);
        warehouses.add(wh4);

        System.out.println("Input: " + order + ", " + warehouses);

        InventoryAllocator allocator = new InventoryAllocator(order, warehouses);
        LinkedList<Warehouse> output = allocator.ship();

        LinkedList<Warehouse> result = new LinkedList<Warehouse>();

        HashMap<String, Integer> result_inv1 = new HashMap<String, Integer>();
        result_inv1.put("apple", 5);
        result_inv1.put("orange", 7);
        result_inv1.put("watermelon", 7);
        Warehouse result_wh1 = new Warehouse("sf", result_inv1);
        result.add(result_wh1);

        HashMap<String, Integer> result_inv2 = new HashMap<String, Integer>();
        result_inv2.put("banana", 5);
        result_inv2.put("orange", 10);
        result_inv2.put("mango", 5);
        Warehouse result_wh2 = new Warehouse("ny", result_inv2);
        result.add(result_wh2);

        HashMap<String, Integer> result_inv3 = new HashMap<String, Integer>();
        result_inv3.put("orange", 3);
        Warehouse result_wh3 = new Warehouse("la", result_inv3);
        result.add(result_wh3);

        HashMap<String, Integer> result_inv4 = new HashMap<String, Integer>();
        result_inv4.put("watermelon", 8);
        Warehouse result_wh4 = new Warehouse("dc", result_inv4);
        result.add(result_wh4);

        System.out.println("Output: " + output);
        System.out.println();

        assertEquals(result.toString(), output.toString());
    }

    @Test
    /** Order completed before all warehouses iterated over. */
    public void testFinishedOrder() {
        HashMap<String, Integer> order = new HashMap<String, Integer>();
        order.put("apple", 10);

        LinkedList<Warehouse> warehouses = new LinkedList<Warehouse>();

        HashMap<String, Integer> inventory1 = new HashMap<String, Integer>();
        inventory1.put("apple", 5);
        Warehouse wh1 = new Warehouse("owd", inventory1);
        warehouses.add(wh1);

        HashMap<String, Integer> inventory2 = new HashMap<String, Integer>();
        inventory2.put("apple", 5);
        Warehouse wh2 = new Warehouse("dm", inventory2);
        warehouses.add(wh2);

        HashMap<String, Integer> inventory3 = new HashMap<String, Integer>();
        inventory3.put("apple", 5);
        Warehouse wh3 = new Warehouse("ny", inventory3);
        warehouses.add(wh3);

        System.out.println("Input: " + order + ", " + warehouses);

        LinkedList<Warehouse> result = new LinkedList<Warehouse>();
        result.add(wh1);
        result.add(wh2);

        InventoryAllocator allocator = new InventoryAllocator(order, warehouses);
        LinkedList<Warehouse> output = allocator.ship();

        System.out.println("Output: " + output);
        System.out.println();

        assertEquals(result.toString(), output.toString());
    }

    @Test
    /** Only the last warehouse should have items allocated. */
    public void testLastWarehouse() {
        HashMap<String, Integer> order = new HashMap<String, Integer>();
        order.put("apple", 5);
        order.put("banana", 30);
        order.put("orange", 6);

        LinkedList<Warehouse> warehouses = new LinkedList<Warehouse>();

        HashMap<String, Integer> inventory1 = new HashMap<String, Integer>();
        inventory1.put("apple", 0);
        Warehouse wh1 = new Warehouse("sf", inventory1);
        warehouses.add(wh1);

        HashMap<String, Integer> inventory2 = new HashMap<String, Integer>();
        inventory2.put("orange", 0);
        Warehouse wh2 = new Warehouse("ny", inventory2);
        warehouses.add(wh2);

        HashMap<String, Integer> inventory3 = new HashMap<String, Integer>();
        inventory3.put("apple", 5);
        inventory3.put("banana", 31);
        inventory3.put("orange", 6);
        Warehouse wh3 = new Warehouse("la", inventory3);
        warehouses.add(wh3);

        System.out.println("Input: " + order + ", " + warehouses);

        InventoryAllocator allocator = new InventoryAllocator(order, warehouses);
        LinkedList<Warehouse> output = allocator.ship();

        LinkedList<Warehouse> result = new LinkedList<Warehouse>();

        HashMap<String, Integer> result_inv1 = new HashMap<String, Integer>();
        result_inv1.put("apple", 5);
        result_inv1.put("banana", 30);
        result_inv1.put("orange", 6);
        Warehouse result_wh1 = new Warehouse("la", result_inv1);
        result.add(result_wh1);

        System.out.println("Output: " + output);
        System.out.println();

        assertEquals(result.toString(), output.toString());
    }

    @Test
    /** Warehouses contain items not in the order. */
    public void testItemsNotInOrder() {
        HashMap<String, Integer> order = new HashMap<String, Integer>();
        order.put("apple", 5);
        order.put("banana", 5);
        order.put("orange", 5);

        LinkedList<Warehouse> warehouses = new LinkedList<Warehouse>();

        HashMap<String, Integer> inventory1 = new HashMap<String, Integer>();
        inventory1.put("apple", 5);
        inventory1.put("orange", 10);
        inventory1.put("cabbage", 10);
        Warehouse wh1 = new Warehouse("ny", inventory1);
        warehouses.add(wh1);

        HashMap<String, Integer> inventory2 = new HashMap<String, Integer>();
        inventory2.put("banana", 5);
        inventory2.put("orange", 10);
        inventory2.put("sweet potato", 10);
        Warehouse wh2 = new Warehouse("sf", inventory2);
        warehouses.add(wh2);

        System.out.println("Input: " + order + ", " + warehouses);

        InventoryAllocator allocator = new InventoryAllocator(order, warehouses);
        LinkedList<Warehouse> output = allocator.ship();

        LinkedList<Warehouse> result = new LinkedList<Warehouse>();

        HashMap<String, Integer> result_inv1 = new HashMap<String, Integer>();
        result_inv1.put("apple", 5);
        result_inv1.put("orange", 5);
        Warehouse result_wh1 = new Warehouse("ny", result_inv1);
        result.add(result_wh1);

        HashMap<String, Integer> result_inv2 = new HashMap<String, Integer>();
        result_inv2.put("banana", 5);
        Warehouse result_wh2 = new Warehouse("sf", result_inv2);
        result.add(result_wh2);

        System.out.println("Output: " + output);
        System.out.println();

        assertEquals(result.toString(), output.toString());
    }

    /* Run the unit tests in this file. */
    public static void main(String[] args) {
        Result result = JUnitCore.runClasses(InventoryAllocatorTest.class);
    }
}
