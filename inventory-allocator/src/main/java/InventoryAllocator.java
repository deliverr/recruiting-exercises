import java.util.ArrayList;
import java.util.List;

public class InventoryAllocator {

    private static InventoryAllocator inventoryAllocator;

    private InventoryAllocator() {}

    public static InventoryAllocator getInstance() {
        if(inventoryAllocator == null) {
            inventoryAllocator = new InventoryAllocator();
        }
        return inventoryAllocator;
    }

    /**
     * @param order
     * @param warehouses
     * @return list of shipments
     */
    public List<Shipment> allocateOrder(Order order, List<Warehouse> warehouses) {
        List<Shipment> shipments = new ArrayList<>();

        for(Warehouse warehouse: warehouses) {
            Shipment shipment = warehouse.processOrder(order);
            if(shipment != null) {
                shipments.add(shipment);
            }

            if(order.isOrderFulfilled()) {
                return shipments;
            }
        }

        return new ArrayList<>();
    }
}
