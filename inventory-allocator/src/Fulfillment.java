import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class Fulfillment {
    private Map<String, Map<String, Integer>> fulfillment;

    public Fulfillment() {
        fulfillment = new HashMap<>();
    }

    /**
     * adds an item and its quantity to fulfillment
     * @param warehouseName the warehouse fulfilling the item
     * @param item item name
     * @param quantity quantity fulfilled
     */
    public void addFulfillment(String warehouseName, String item, Integer quantity) {
        fulfillment.putIfAbsent(warehouseName, new HashMap<>());
        Map<String, Integer> shipment = fulfillment.get(warehouseName);
        shipment.put(item, shipment.getOrDefault(item, 0) + quantity);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[ ")
                .append(fulfillment.keySet().stream()
                .map(k -> k + ": " + shipmentString(k))
                .collect(Collectors.joining(", ")))
                .append(" ]");
        return sb.toString();
    }

    private String shipmentString(String warehouseName) {
        Map<String, Integer> shipment = fulfillment.get(warehouseName);
        StringBuilder sb = new StringBuilder();
        sb.append("{ ")
                .append(shipment.entrySet().stream()
                .map(e -> e.getKey() + ": " + e.getValue())
                .collect(Collectors.joining(", ")))
                .append(" }");
        return sb.toString();
    }

    @Override
    public boolean equals(Object o) {
        if(this == o) return true;
        if(o == null || o.getClass()!= this.getClass()) return false;
        Fulfillment other = (Fulfillment) o;
        if(this.fulfillment.size() != other.fulfillment.size()) return false;
        for(String warehouseName : fulfillment.keySet()) {
            Map<String, Integer> thisShipment = fulfillment.get(warehouseName);
            Map<String, Integer> otherShipment = other.fulfillment.getOrDefault(warehouseName, null);
            if(!thisShipment.equals(otherShipment)) return false;
        }
        return true;
    }

    @Override
    public int hashCode() {
        return this.toString().hashCode();
    }
}
