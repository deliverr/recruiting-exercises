import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Inventory {
    public Inventory() {}

    // allocate invetory to different wareHouses
    public List<Map<String, Map<String, Integer>>> InventoryAllocate(Map<String, Integer> order, List<WareHouse> wareHouses) {
        // result
        List<Map<String, Map<String, Integer>>> ship = new ArrayList<Map<String, Map<String, Integer>>>();
        if (order.isEmpty() || wareHouses.size() == 0) return ship;
        for (int i = 0; i < wareHouses.size(); i++) {
            WareHouse cur = wareHouses.get(i);
            String name = cur.getName();
            Map<String, Integer> inventory = cur.getInventory();
            Map<String, Map<String, Integer>> temp = new HashMap<String, Map<String, Integer>>();
            // check every item in the order to see if there is a match in current wareHouse
            for (String item : order.keySet()) {
                if (inventory.containsKey(item) && order.get(item) != 0) {
                    if (!temp.containsKey(name)) {
                        temp.put(name, new HashMap<String, Integer>());
                    }
                    temp.get(name).put(item, Math.min(inventory.get(item), order.get(item)));
                    order.put(item, Math.max(0, order.get(item) - inventory.get(item)));
                }
            }
            if (!temp.isEmpty()) ship.add(temp);
        }
        // check if any item in the order is not enough in the wareHouse
        for (String item : order.keySet()) {
            if (order.get(item) > 0) return new ArrayList<Map<String, Map<String, Integer>>>();
        }
        return ship;
    }
}
