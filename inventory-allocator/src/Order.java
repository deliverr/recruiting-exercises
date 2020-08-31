import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

public class Order {
    private Map<String, Integer> orderDetails;

    public Order() {
        orderDetails = new HashMap<>();
    }

    /**
     * deep copies the original order
     * @return a deep copy of the original order
     */
    public Order copyOrder() {
        Order copyOrder = new Order();
        orderDetails.forEach((k, v) -> copyOrder.orderDetails.put(k, v));
        return copyOrder;
    }

    /**
     * adds an item and quantity to an order
     * @param item item name
     * @param quantity item quantity
     */
    public void addItem(String item, Integer quantity) {
        orderDetails.put(item, orderDetails.getOrDefault(item, 0) + quantity);
    }

    /**
     * deletes an item from the order after fulfilled
     * has no effect if the item is not found
     * @param item item name
     */
    public void deleteItem(String item) {
        if(!orderDetails.containsKey(item)) return;
        orderDetails.remove(item);
    }

    /**
     * @param item item name
     * @return the quantity to fulfill
     */
    public Integer getItemQuantity(String item) {
        return orderDetails.getOrDefault(item, 0);
    }

    /**
     * @return a set of items in the order
     */
    public Set<String> getItems() {
        return orderDetails.keySet();
    }

    /**
     * @return true if all the items are fulfilled
     */
    public boolean isCompleted() {
        return orderDetails.isEmpty();
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("{ ").
                append(orderDetails.entrySet().stream()
                .map(e -> e.getKey() + ": " + e.getValue())
                .collect(Collectors.joining(", ")))
                .append(" }");
        return sb.toString();
    }
}
