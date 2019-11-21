import java.util.*;

/** Each warehouse has a unique name and inventory distribution. */
public class Warehouse {

    /** Name for this warehouse. */
    private String _name;

    /** HashMap for this warehouse's inventory distribution. Maps each item
     *  to the amount in its inventory. */
    private HashMap<String, Integer> _inventory;

    /** Constructor for a warehouse object. */
    public Warehouse(String name, HashMap<String, Integer> inventory) {
        _name = name;
        _inventory = inventory;
    }

    /** Returns the number of a specific item in this warehouse's inventory. */
    public int getItemCount(String item) {
        return _inventory.getOrDefault(item, 0);
    }

    /** Sets the number of a specific item in this warehouse's inventory. */
    public void setItemCount(String item, int count) {
        _inventory.put(item, count);
    }

    /** Returns the name of this warehouse. */
    public String getName() {
        return _name;
    }

    /** Returns the HashMap of this warehouse's inventory. */
    public HashMap<String, Integer> getInventory() {
        return _inventory;
    }

    /** Returns this warehouse's name and inventory in a readable format. */
    public String toString() {
        return "{ name: " +  _name + ", inventory: " + _inventory + " }";
    }
}
