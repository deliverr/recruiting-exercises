import java.util.HashMap;
import java.util.Map;

public class WareHouse {
    private String name;
    private Map<String, Integer> inventory;
    public WareHouse(String _name, Map<String, Integer> _inventory) {
        name = _name;
        inventory = _inventory;
    }
    public String getName() {
        return this.name;
    }
    public Map<String, Integer> getInventory() {
        return this.inventory;
    }
}
