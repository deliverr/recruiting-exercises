import java.util.HashMap;
import java.util.Map;

public class Warehouse {
    private String name;
    private Map<String, Integer> inventory = new HashMap<>();

    public Warehouse(String name) {
        this.name = name;
    }

    /**
     * Adds new product to warehouse
     *
     * @param productName
     * @param quantity
     */
    public void addProduct(String productName, int quantity) {
        inventory.put(productName, quantity);
    }

    /**
     *
     * @param order
     * @return Shipment object or null if warehouse has no product to ship
     */
    public Shipment processOrder(Order order) {
        Map<String, Integer> shippingProducts = new HashMap<>();
        for (String productName : order.getProductNames()) {
            if (inventory.containsKey(productName)){
                int productQuantity = Math.min(order.getProductQuantity(productName), inventory.get(productName));
                shippingProducts.put(productName, productQuantity);
            }
        }

        // If no product is shipped from warehouse return null
        if(shippingProducts.size() == 0) {
            return null;
        }

        Shipment shipment = new Shipment(this.name);

        try {
            for (Map.Entry<String, Integer> product : shippingProducts.entrySet()) {
                String productName = product.getKey();
                int quantity = product.getValue();

                shipment.addProduct(productName, quantity);

                if (quantity >= order.getProductQuantity(productName)) {
                    order.removeProduct(productName);
                } else {
                    order.setProduct(productName, order.getProductQuantity(productName) - quantity);
                }

                if (quantity >= inventory.get(productName)) {
                    inventory.remove(productName);
                } else {
                    inventory.put(productName, inventory.get(productName) - quantity);
                }
            }
        } catch (BadInputException e) {
            System.err.println("Bad input: " + e);
        }

        return shipment;
    }
}
