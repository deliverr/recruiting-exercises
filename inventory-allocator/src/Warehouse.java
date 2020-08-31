import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

public class Warehouse {
    private String warehouseName;
    private Map<String, Integer> inventory;

    public Warehouse(String name) {
        this.warehouseName = name;
        inventory = new HashMap<>();
    }

    /**
     * @return warehouse name
     */
    public String getName() {
        return warehouseName;
    }

    /**
     * adds an item and stock quantity to the inventory
     * @param item item name
     * @param quantity stock quantity
     */
    public void addToInventory(String item, Integer quantity) {
        inventory.put(item, inventory.getOrDefault(item, 0) + quantity);
    }

    /**
     * updates stock quantity of the given item
     * has no effect if the item is not found
     * @param item item name
     * @param quantity updated quantity of the item
     */
    public void updateInventory(String item, Integer quantity) {
        if(!inventory.containsKey(item)) return;
        inventory.put(item, quantity);
    }

    /**
     * @param item item name
     * @return stock quantity of the given item
     */
    public Integer getItemStock(String item) {
        return inventory.getOrDefault(item, 0);
    }

    /**
     * updates fulfillment solution
     * and stock quantity if stock is sufficient for the item(s)
     * deletes the item(s) fulfilled from the order
     * @param order the order to process
     * @param fulfillment the fulfillment solution
     */
    public void processOrder(Order order, Fulfillment fulfillment) {
        Set<String> items = order.getItems();
        Set<String> fulfilledItems = new HashSet<>();
        for(String item : items) {
            int quantityToFulfill = order.getItemQuantity(item);
            int stock = getItemStock(item);
            if(stock < quantityToFulfill) continue;
            fulfillment.addFulfillment(warehouseName, item, quantityToFulfill);
            fulfilledItems.add(item);
            updateInventory(item, stock - quantityToFulfill);
        }
        fulfilledItems.forEach(order::deleteItem);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("{ name: ").append(warehouseName)
                .append(", inventory: { ")
                .append(inventory.entrySet().stream()
                .map(e -> e.getKey() + ": " + e.getValue())
                .collect(Collectors.joining(", ")))
                .append(" } }");
        return sb.toString();
    }
}
