package allocator;

import java.util.Map;

public class Warehouse {
    private final String name;
    private final Map<String, Integer> inventory;

    public Warehouse(String name, Map<String, Integer> inventory) {
        this.name = name;
        this.inventory = inventory;
    }

    public String getName() {
        return name;
    }

    public Map<String, Integer> getInventory() {
        return inventory;
    }
}
