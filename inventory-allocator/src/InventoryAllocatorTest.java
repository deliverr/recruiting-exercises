import static org.junit.Assert.*;
import org.junit.Test;
import java.util.*;


public class InventoryAllocatorTest {

    /** Tolerance for comparison of doubles. */
    static final double DELTA = 1e-15;

    @Test
    public void testProduct() {
        /* assertEquals for comparison of doubles takes three arguments:
         *      assertEquals(expected, actual, DELTA).
         *  + if Math.abs(expected - actual) < DELTA, then the test succeeds.
         *  + Otherwise, the test fails.
         *
         *  See http://junit.sourceforge.net/javadoc/org/junit/ \
         *             Assert.html#assertEquals(double, double, double)
         *  for more. */

        assertEquals(30, Arithmetic.product(5, 6), DELTA);
        assertEquals(-30, Arithmetic.product(5, -6), DELTA);
        assertEquals(0, Arithmetic.product(0, -6), DELTA);
    }

    @Test
    /** Exact inventory match. */
    public void testHappyCase() {
        HashMap<String, int> order = new HashMap<String, int>();
        order.put("apple", 1);

        HashMap<String, int> owd = new HashMap<String, int>();
        owd.put("apple", 1);

        LinkedList<HashMap<String, int>> warehouse = new LinkedList<HashMap<String, int>>();
        warehouse.add(owd);

        InventoryAllocator allocator = new InventoryAllocator(order, warehouse);

        assertEquals(warehouse, allocator.ship(order, warehouse));
    }

    @Test
    /** Not enough inventory  -> No allocations. */
    public void testNotEnough() {
        HashMap<String, int> order = new HashMap<String, int>();
        order.put("apple", 1);

        HashMap<String, int> owd = new HashMap<String, int>();
        owd.put("apple", 0);

        LinkedList<HashMap<String, int>> warehouse = new LinkedList<HashMap<String, int>>();
        warehouse.add(owd);

        InventoryAllocator allocator = new InventoryAllocator(order, warehouse);

        assertNull(allocator.ship(order, warehouse));
    }

    @Test
    /** Split an item across warehouses if that is the only way to completely ship an
     * item. */
    public void testSplit() {
        HashMap<String, int> order = new HashMap<String, int>();
        order.put("apple", 10);

        HashMap<String, int> owd = new HashMap<String, int>();
        owd.put("apple", 5);

        HashMap<String, int> dm = new HashMap<String, int>();
        owd.put("apple", 5);

        LinkedList<HashMap<String, int>> warehouse = new LinkedList<HashMap<String, int>>();
        warehouse.add(owd);
        warehouse.add(dm);

        InventoryAllocator allocator = new InventoryAllocator(order, warehouse);

        assertEquals(warehouse, allocator.ship(order, warehouse));
    }

    @Test
    /** Excess inventory from both warehouses. */
    public void testExample() {
        HashMap<String, int> order = new HashMap<String, int>();
        order.put("apple", 5);
        order.put("banana", 5);
        order.put("orange", 5);

        HashMap<String, int> owd = new HashMap<String, int>();
        owd.put("apple", 5);
        owd.put("orange", 10);

        HashMap<String, int> dm = new HashMap<String, int>();
        owd.put("banana", 5);
        owd.put("orange", 10);

        LinkedList<HashMap<String, int>> warehouse = new LinkedList<HashMap<String, int>>();
        warehouse.add(owd);
        warehouse.add(dm);

        InventoryAllocator allocator = new InventoryAllocator(order, warehouse);

        LinkedList<HashMap<String, int>> result = new LinkedList<HashMap<String, int>>();
        HashMap<String, int> owd1 = new HashMap<String, int>();
        owd1.put("apple", 5);
        owd1.put("orange", 5);
        HashMap<String, int> dm1 = new HashMap<String, int>();
        dm1.put("banana", 5);
        result.add(owd1);
        result.add(dm1);

        assertEquals(result, allocator.ship(order, warehouse));
    }

    /* Run the unit tests in this file. */
    public static void main(String... args) {
        System.exit(junit.textui.runClasses(ArithmeticJUnitTest.class));
    }
}
