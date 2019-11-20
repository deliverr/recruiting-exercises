import java.util.*;

public class InventoryAllocator {

    /**
     * HashMap of orders to be inputted. Maps each item being ordered to
     * the number ordered.
     */
    private HashMap<String, int> order;

    /**
     * LinkedList containing HashMaps for each warehouse. Each HashMap contains
     * the warehouses inventory distribution. Assumed to be pre-sorted based
     * on cost (first warehouse is the least expensive to ship from).
     */
    private LinkedList<HashMap<String, int>> warehouse

    /**
     * Contructor for an InventoryAllocator object that takes a HashMap of
     * orders ORD and a LinkedList of warehouses WH. Initializes the order and
     * warehouse instance variables.
     */
    public InventoryAllocator(HashMap<String, int> ord, LinkedList<HashMap<String, int>> wh) {
        this.order = ord;
        this.warehouse = wh;
    }

    /**
     * Computes the best way an order can be shipped, given the inventory across
     * the warehouses. Destructively modifies warehouse LinkedList.
     */
    public LinkedList<HashMap<String, int>> ship() {
        LinkedList<HashMap<String, int>> result = new LinkedList<HashMap<String, int>>;
        for (HashMap<String, int> wh : warehouse) {
            for (String item : wh.keySet()) {
                if (order.containsKey(item)) {
                    // Amount of item left in warehouse wh after shipping.
                    int fill = order.get(item) - wh.get(item);
                    // Order fulfilled for item, so remove from HashMap.
                    // Negative item -> excess inventory from warehouse.
                    if (fill <= 0) {
                        fill == 0;
                        // Update warehouse to send requested number of items.
                        wh.put(item, order.get(item));
                        order.remove(item);
                    }
                    // Ship all inventory from wh, but there are still orders
                    // for item.
                    else {
                        order.put(item, fill);
                    }
                    if (!result.contains(wh)) {
                        result.add(wh);
                    }
                }
                if (orders.isEmpty()) {
                    return result;
                }
            }
        }
        // Not enough inventory for any allocations. Returns empty LinkedList.
        return new LinkedList();
    }
}
