package allocator;

import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

public class Shipment {
    private final String warehouse;
    private final Map<String, Integer> items;

    public Shipment(String warehouseName) {
        warehouse = warehouseName;
        items = new HashMap<>();
    }

    public Shipment(String warehouseName, Map<String, Integer> items) {
        warehouse = warehouseName;
        this.items = items;
    }

    public void addItem(String itemName, int quantity) {
        items.put(itemName, quantity);
    }

    public boolean isEmpty() {
        return items.isEmpty();
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) return true;
        if (other == null || getClass() != other.getClass()) return false;
        Shipment shipment = (Shipment) other;
        return warehouse.equals(shipment.warehouse) &&
                items.equals(shipment.items);
    }

    @Override
    public int hashCode() {
        return Objects.hash(warehouse, items);
    }

    @Override
    public String toString() {
        return String.format("{ %s: %s }", warehouse, items.toString());
    }
}
