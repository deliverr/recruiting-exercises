import java.util.*;

public class InventoryAllocator {
    private List<Warehouse> warehouses;

    public InventoryAllocator() {
        warehouses = new ArrayList<>();
    }

    public InventoryAllocator(List<Warehouse> warehouses) {
        this.warehouses = warehouses;
    }

    /**
     * computes the lowest-cost fulfillment solution
     * @param o the order to fulfill
     * @return the fulfillment solution at the lowest cost
     */
    public Fulfillment fulfillOrder(Order o) {
        Order order = o.copyOrder();
        Fulfillment fulfillment = new Fulfillment();
        for (Warehouse warehouse : warehouses) {
            warehouse.processOrder(order, fulfillment);
            if (order.isCompleted()) return fulfillment;
        }
        splitOrder(order, fulfillment);
        return fulfillment;
    }

    /**
     * fulfills the item(s) that can be fulfilled
     * by combining stock of multiple warehouses
     * @param order the order to be fulfilled
     * @param fulfillment the fulfillment solution
     */
    public void splitOrder(Order order, Fulfillment fulfillment) {
        Set<String> items = order.getItems();
        Set<String> fulfilledItems = new HashSet<>();
        for (String item : items) {
            if (!isFulfillable(item, order)) continue;
            processOrderSplitting(item, order, fulfillment);
            fulfilledItems.add(item);
        }
        fulfilledItems.forEach(order::deleteItem);
    }

    /**
     * @param item item name
     * @param order the order to be fulfilled
     * @return true if the item can be fulfilled
     * by combining stock of multiple warehouses
     */
    public boolean isFulfillable(String item, Order order) {
        int quantityToFulfill = order.getItemQuantity(item);
        int totalStock = warehouses.stream().mapToInt(w -> w.getItemStock(item)).sum();
        return totalStock >= quantityToFulfill;
    }

    /**
     * fulfills the given item
     * @param item item name
     * @param order the order to be fulfilled
     * @param fulfillment the fulfillment solution
     */
    public void processOrderSplitting(String item, Order order, Fulfillment fulfillment) {
        int quantityToFulfill = order.getItemQuantity(item);
        for (Warehouse warehouse : warehouses) {
            int stock = warehouse.getItemStock(item);
            if (stock == 0) continue;
            int quantityFulfilled = Math.min(stock, quantityToFulfill);
            fulfillment.addFulfillment(warehouse.getName(), item, quantityFulfilled);
            warehouse.updateInventory(item, stock - quantityFulfilled);
            quantityToFulfill -= quantityFulfilled;
            if (quantityToFulfill == 0) {
                break;
            }
        }
    }
}
