import org.junit.Assert;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

class InventoryAllocatorTest {

    @Test
    void fulfillOrder() {
        Warehouse owd = new Warehouse("owd");
        owd.addToInventory("apple", 5);
        owd.addToInventory("banana", 6);
        owd.addToInventory("peach", 8);
        owd.addToInventory("guava", 5);
        System.out.println("\n----- owd warehouse -----\n");
        System.out.println(owd);

        Warehouse dm = new Warehouse("dm");
        dm.addToInventory("apple", 5);
        dm.addToInventory("peach", 2);
        dm.addToInventory("pineapple", 7);
        dm.addToInventory("banana", 6);
        dm.addToInventory("guava", 5);
        System.out.println("\n----- dm warehouse -----\n");
        System.out.println(dm);

        List<Warehouse> warehouses = new ArrayList<>();
        warehouses.add(owd);
        warehouses.add(dm);

        InventoryAllocator allocator = new InventoryAllocator(warehouses);

        //HAPPY CASE - fulfilled without splitting
        Order HAPPY_ORDER = new Order();
        HAPPY_ORDER.addItem("apple", 5);
        HAPPY_ORDER.addItem("pineapple", 3);
        System.out.println("\n----- HAPPY_ORDER -----\n");
        System.out.println(HAPPY_ORDER);

        Fulfillment HAPPY_CASE = new Fulfillment();
        HAPPY_CASE.addFulfillment("owd", "apple", 5);
        HAPPY_CASE.addFulfillment("dm", "pineapple", 3);
        System.out.println("\n----- HAPPY_CASE -----\n");
        System.out.println(HAPPY_CASE);

        Fulfillment actualHappyCase = allocator.fulfillOrder(HAPPY_ORDER);
        // HAPPY_CASE ASSERTION
        Assert.assertEquals(HAPPY_CASE, actualHappyCase);


        // SAD CASE - nothing fulfilled
        Order SAD_ORDER = new Order();
        SAD_ORDER.addItem("peach", 12);

        System.out.println("\n----- SAD_ORDER -----\n");
        System.out.println(SAD_ORDER);

        Fulfillment SAD_CASE = new Fulfillment();
        System.out.println("\n----- SAD_CASE -----\n");
        System.out.println(SAD_CASE);

        Fulfillment actualSadCase = allocator.fulfillOrder(SAD_ORDER);
        // SAD_CASE ASSERTION
        Assert.assertEquals(SAD_CASE, actualSadCase);


        // SPLIT CASE - fulfilled by splitting / combining
        Order SPLIT_ORDER = new Order();
        SPLIT_ORDER.addItem("banana", 7);
        SPLIT_ORDER.addItem("guava", 10);

        System.out.println("\n----- SPLIT_ORDER -----\n");
        System.out.println(SPLIT_ORDER);

        Fulfillment SPLIT_CASE = new Fulfillment();
        SPLIT_CASE.addFulfillment("owd", "banana", 6);
        SPLIT_CASE.addFulfillment("dm", "banana", 1);
        SPLIT_CASE.addFulfillment("owd", "guava", 5);
        SPLIT_CASE.addFulfillment("dm", "guava", 5);

        System.out.println("\n----- SPLIT_CASE -----\n");
        System.out.println(SPLIT_CASE);

        Fulfillment actualSplitCase = allocator.fulfillOrder(SPLIT_ORDER);
        // SPLIT_CASE ASSERTION
        Assert.assertEquals(SPLIT_CASE, actualSplitCase);
    }
}


/**
 * Run successfully, Junit test cases got passed.
 *
 * Console should print the following contents:
 *
 * ----- owd warehouse -----
 *
 * { name: owd, inventory: { banana: 6, apple: 5, peach: 8, guava: 5 } }
 *
 * ----- dm warehouse -----
 *
 * { name: dm, inventory: { banana: 6, apple: 5, pineapple: 7, peach: 2, guava: 5 } }
 *
 * ----- HAPPY_ORDER -----
 *
 * { apple: 5, pineapple: 3 }
 *
 * ----- HAPPY_CASE -----
 *
 * [ dm: { pineapple: 3 }, owd: { apple: 5 } ]
 *
 * ----- SAD_ORDER -----
 *
 * { peach: 12 }
 *
 * ----- SAD_CASE -----
 *
 * [  ]
 *
 * ----- SPLIT_ORDER -----
 *
 * { banana: 7, guava: 10 }
 *
 * ----- SPLIT_CASE -----
 *
 * [ dm: { banana: 1, guava: 5 }, owd: { banana: 6, guava: 5 } ]
 */
