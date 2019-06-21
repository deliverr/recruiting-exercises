import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Order {
    private Map<String, Integer> products = new HashMap<>();

    /**
     *
     * @param name
     * @param quantity
     */
    public void addProduct(String name, int quantity) throws BadInputException{
        if(quantity <= 0 || name.isEmpty()) {
            throw new BadInputException();
        }
        products.put(name, quantity);
    }

    /**
     *
     * @param name
     * @return
     */
    public int getProductQuantity(String name) {
        return products.getOrDefault(name, -1);
    }

    /**
     *
     * @return
     */
    public Set<String> getProductNames() {
        return products.keySet();
    }

    /**
     *
     * @param productName
     * @param quantity
     */
    public void setProduct(String productName, int quantity) throws BadInputException {
        if(quantity <= 0 || productName.isEmpty()) {
            throw new BadInputException();
        }
        products.put(productName, quantity);
    }

    /**
     *
     * @param productName
     */
    public void removeProduct(String productName) {
        products.remove(productName);
    }

    /**
     * Checks if order has been fulfilled by warehouses
     * @return
     */
    public boolean isOrderFulfilled() {
        return products.size() == 0;
    }

}
