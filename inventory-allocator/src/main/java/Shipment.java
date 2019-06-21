import java.util.HashMap;
import java.util.Map;

public class Shipment {
    private Map<String, Integer> products = new HashMap<>();
    private String warehouseName;

    public Shipment(String warehouseName) {
        this.warehouseName = warehouseName;
    }

    /**
     * Adds product to Shipment
     * @param name
     * @param quantity
     */
    public void addProduct(String name, int quantity) throws BadInputException {
        if(quantity <= 0 || name.isEmpty()) {
            throw new BadInputException();
        }
        products.put(name, quantity);
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == this)
            return true;

        if (!(obj instanceof Shipment))
            return false;

        Shipment shipment = (Shipment) obj;
        return shipment.warehouseName == this.warehouseName
                && shipment.products.equals(this.products);

    }
}
