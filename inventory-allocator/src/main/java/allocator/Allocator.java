package allocator;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Allocator {
    public static void main(String[] args) {
    }

    public List<Shipment> produceCheapestShipment(Map<String, Integer> order, List<Warehouse> warehouses) {
        List<Shipment> shipments = new ArrayList<>();
        Map<Integer, Shipment> shipmentMap = new HashMap<>();

        // First check if there are items that can be completely shipped from one warehouse
        for (int i = 0; i < warehouses.size(); i++) {
            Warehouse warehouse = warehouses.get(i);
            Shipment shipment = new Shipment(warehouse.getName());
            Map<String, Integer> inventory = warehouse.getInventory();
            for (Map.Entry<String, Integer> item : order.entrySet()) {
                String itemName = item.getKey();
                int orderQuantity = item.getValue();
                int inventoryQuantity = inventory.getOrDefault(itemName, -1);
                if (orderQuantity > 0 && orderQuantity <= inventoryQuantity) {
                    // Item can be completely shipped from the warehouse
                    shipment.addItem(itemName, orderQuantity);
                    // Update the order
                    item.setValue(0);
                }
            }
            shipmentMap.put(i, shipment);
        }

        for (int i = 0; i < warehouses.size(); i++) {
            Warehouse warehouse = warehouses.get(i);
            Shipment shipment = shipmentMap.get(i);
            Map<String, Integer> inventory = warehouse.getInventory();
            for (Map.Entry<String, Integer> item : order.entrySet()) {
                String itemName = item.getKey();
                int orderQuantity = item.getValue();
                if (orderQuantity > 0 && inventory.containsKey(itemName)) {
                    // Ship as much as the inventory can supply
                    int shippedQuantity = Math.min(orderQuantity, inventory.get(itemName));
                    shipment.addItem(itemName, shippedQuantity);
                    // Update the order
                    item.setValue(orderQuantity - shippedQuantity);

                }
            }
            if (!shipment.isEmpty()) {
                // There is shipment from the warehouse
                shipments.add(shipment);
            }
        }

        for (int quantity : order.values()) {
            if (quantity > 0) {
                // There are unshipped items, so the order cannot be shipped
                shipments.clear();
                return shipments;
            }
        }
        return shipments;
    }
}
