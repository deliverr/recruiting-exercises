import java.util.HashMap;

//Warehouse object contains name and its inventory
public class Warehouse {

    private String name;
    private HashMap<String, Integer> inventory;

    public Warehouse(String name, HashMap<String, Integer>inventory) {

        this.name = name;
        this.inventory = inventory;
    }

    public String getName() {
        return this.name;
    }

    public HashMap<String, Integer> getInventory() {
        return this.inventory;
    }
}
