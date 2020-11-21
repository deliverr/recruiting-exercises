import java.util.*;

public class InventoryAllocator {

    /**
     * HashMap of orders to be inputted. Maps each item being ordered to
     * the number ordered.
     */
    private HashMap<String, Integer> _order;

    /**
     * LinkedList of warehouses. Assumed to be pre-sorted based
     * on cost (first warehouse is the least expensive to ship from).
     */
    private LinkedList<Warehouse> _warehouses;

    /** Tracks the total number of orders left to be allocated. */
    private int _total;

    /**
     * Contructor for an InventoryAllocator object that takes a HashMap of
     * orders ORDER and a LinkedList of warehouses WAREHOUSES. Initializes _order,
     * _warehouses, and _total instance variables.
     */
    public InventoryAllocator(HashMap<String, Integer> order, LinkedList<Warehouse> warehouses) {
        _order = order;
        _warehouses = warehouses;
        for (String item : _order.keySet()) {
            _total += _order.get(item);
        }
    }

    /**
     * Computes the best way an order can be shipped, given the inventory across
     * the warehouses. Destructively modifies _orders to reflect inventory allocations.
     */
    public LinkedList<Warehouse> ship() {
        LinkedList<Warehouse> result = new LinkedList<Warehouse>();
        for (Warehouse wh : _warehouses) {
            //Create new warehouse wh_ship to append to result.
            Warehouse wh_ship = new Warehouse(wh.getName(), new HashMap<String, Integer>());
            //
            for (String item : wh.getInventory().keySet()) {
                //Return result if there are no more orders to allocate.
                if (_total == 0) {
                    return result;
                }
                //Iterate to next item if there are no orders for this item or
                //if this warehouse doesn't have the item in its inventory.
                else if (_order.getOrDefault(item, 0) == 0 || wh.getItemCount(item) == 0) {
                    continue;
                }
                else {
                    //Allocate as much of this warehouse's inventory of the item needed
                    // to fill the order.
                    int min_inv = Math.min(_order.get(item), wh.getItemCount(item));
                    wh_ship.setItemCount(item, min_inv);
                    //Decrement _total by number of items allocated.
                    _total -= min_inv;
                    //Number of this item left in orders after allocating to this warehouse.
                    //Negative value implies excess inventory in this warehouse.
                    int fill = _order.get(item) - wh.getItemCount(item);
                    //Set the order for this item to fill or 0 if fill < 0.
                    int max_inv = Math.max(0, fill);
                    _order.put(item, max_inv);
                    //Append wh_ship to result if it doesn't already contain it.
                    if (!result.contains(wh_ship)) {
                        result.add(wh_ship);
                    }
                }
            }
        }
        return result;
    }
}