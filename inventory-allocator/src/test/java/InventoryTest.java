import org.junit.Test;

import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class InventoryTest {

    // one item in the order and one wareHouse
    @Test
    public void basicTest() {
        // build order iput
        Map<String, Integer> order = new HashMap<String, Integer>();
        order.put("apple", 1);

        // build wareHouse input
        List<WareHouse> list = new ArrayList<WareHouse>();
        Map<String, Integer> _inventory = new HashMap<String, Integer>();
        _inventory.put("apple", 1);
        WareHouse w1 = new WareHouse("owd", _inventory);
        list.add(w1);

        // build result
        List<Map<String, Map<String, Integer>>> res = new ArrayList<Map<String, Map<String, Integer>>>();
        Map<String, Map<String, Integer>> temp = new HashMap<String, Map<String, Integer>>();
        temp.put("owd", new HashMap<String, Integer>());
        temp.get("owd").put("apple", 1);
        res.add(temp);

        Inventory inventory = new Inventory();
        assertEquals(res, inventory.InventoryAllocate(order, list));
    }

    //one item in the order and one wareHouse but wareHouse has not enough item for order
    @Test
    public void emptyTest() {
        // build order iput
        Map<String, Integer> order = new HashMap<String, Integer>();
        order.put("apple", 1);

        // build wareHouse input
        List<WareHouse> list = new ArrayList<WareHouse>();
        Map<String, Integer> _inventory = new HashMap<String, Integer>();
        _inventory.put("apple", 0);
        WareHouse w1 = new WareHouse("owd", _inventory);
        list.add(w1);

        // build result
        List<Map<String, Map<String, Integer>>> res = new ArrayList<Map<String, Map<String, Integer>>>();

        Inventory inventory = new Inventory();
        assertEquals(res, inventory.InventoryAllocate(order, list));
    }

    //multi items in order and multi wareHouses but wareHouses do not have enough item
    @Test
    public void multiItemEmptyTest() {
        // build order iput
        Map<String, Integer> order = new HashMap<String, Integer>();
        order.put("apple", 5);
        order.put("banana", 10);
        order.put("orange", 5);

        // build wareHouse input
        List<WareHouse> list = new ArrayList<WareHouse>();
        Map<String, Integer> _inventory1 = new HashMap<String, Integer>();
        _inventory1.put("apple", 5);
        _inventory1.put("orange", 10);
        WareHouse w1 = new WareHouse("owd", _inventory1);
        Map<String, Integer> _inventory2 = new HashMap<String, Integer>();
        _inventory2.put("banana", 5);
        _inventory2.put("orange", 10);
        WareHouse w2 = new WareHouse("dm", _inventory2);
        list.add(w1);
        list.add(w2);

        // build result
        List<Map<String, Map<String, Integer>>> res = new ArrayList<Map<String, Map<String, Integer>>>();

        Inventory inventory = new Inventory();
        assertEquals(res, inventory.InventoryAllocate(order, list));
    }

    //one item in order and multi wareHouses
    @Test
    public void basicTest2() {
        // build order iput
        Map<String, Integer> order = new HashMap<String, Integer>();
        order.put("apple", 10);

        // build wareHouse input
        List<WareHouse> list = new ArrayList<WareHouse>();
        Map<String, Integer> _inventory1 = new HashMap<String, Integer>();
        _inventory1.put("apple", 5);
        WareHouse w1 = new WareHouse("owd", _inventory1);
        WareHouse w2 = new WareHouse("dm", _inventory1);
        list.add(w1);
        list.add(w2);

        // build result
        List<Map<String, Map<String, Integer>>> res = new ArrayList<Map<String, Map<String, Integer>>>();
        Map<String, Map<String, Integer>> temp1 = new HashMap<String, Map<String, Integer>>();
        temp1.put("owd", new HashMap<String, Integer>());
        temp1.get("owd").put("apple", 5);
        Map<String, Map<String, Integer>> temp2 = new HashMap<String, Map<String, Integer>>();
        temp2.put("dm", new HashMap<String, Integer>());
        temp2.get("dm").put("apple", 5);
        res.add(temp1);
        res.add(temp2);

        Inventory inventory = new Inventory();
        assertEquals(res, inventory.InventoryAllocate(order, list));
    }

    //multi items in order and multi wareHouses
    @Test
    public void multiItems() {
        // build order iput
        Map<String, Integer> order = new HashMap<String, Integer>();
        order.put("apple", 5);
        order.put("banana", 5);
        order.put("orange", 5);

        // build wareHouse input
        List<WareHouse> list = new ArrayList<WareHouse>();
        Map<String, Integer> _inventory1 = new HashMap<String, Integer>();
        _inventory1.put("apple", 5);
        _inventory1.put("orange", 10);
        WareHouse w1 = new WareHouse("owd", _inventory1);
        Map<String, Integer> _inventory2 = new HashMap<String, Integer>();
        _inventory2.put("banana", 5);
        _inventory2.put("orange", 10);
        WareHouse w2 = new WareHouse("dm", _inventory2);
        list.add(w1);
        list.add(w2);

        // build result
        List<Map<String, Map<String, Integer>>> res = new ArrayList<Map<String, Map<String, Integer>>>();
        Map<String, Map<String, Integer>> temp1 = new HashMap<String, Map<String, Integer>>();
        temp1.put("owd", new HashMap<String, Integer>());
        temp1.get("owd").put("apple", 5);
        temp1.get("owd").put("orange", 5);
        Map<String, Map<String, Integer>> temp2 = new HashMap<String, Map<String, Integer>>();
        temp2.put("dm", new HashMap<String, Integer>());
        temp2.get("dm").put("banana", 5);
        res.add(temp1);
        res.add(temp2);

        Inventory inventory = new Inventory();
        assertEquals(res, inventory.InventoryAllocate(order, list));
    }

    //multi items in order and multi wareHouses (some wareHouses have no items in the order and all items in one wareHouse)
    @Test
    public void multiItems2() {
        // build order iput
        Map<String, Integer> order = new HashMap<String, Integer>();
        order.put("pineapple", 10);
        order.put("cherry", 5);
        order.put("grape", 7);

        // build wareHouse input
        List<WareHouse> list = new ArrayList<WareHouse>();
        Map<String, Integer> _inventory1 = new HashMap<String, Integer>();
        _inventory1.put("apple", 5);
        _inventory1.put("orange", 10);
        WareHouse w1 = new WareHouse("owd", _inventory1);
        Map<String, Integer> _inventory2 = new HashMap<String, Integer>();
        _inventory2.put("banana", 5);
        _inventory2.put("orange", 10);
        WareHouse w2 = new WareHouse("dm", _inventory2);
        Map<String, Integer> _inventory3 = new HashMap<String, Integer>();
        _inventory3.put("pineapple", 15);
        _inventory3.put("cherry", 5);
        _inventory3.put("grape", 10);
        WareHouse w3 = new WareHouse("hos", _inventory3);
        list.add(w1);
        list.add(w2);
        list.add(w3);

        // build result
        List<Map<String, Map<String, Integer>>> res = new ArrayList<Map<String, Map<String, Integer>>>();
        Map<String, Map<String, Integer>> temp1 = new HashMap<String, Map<String, Integer>>();
        temp1.put("hos", new HashMap<String, Integer>());
        temp1.get("hos").put("pineapple", 10);
        temp1.get("hos").put("cherry", 5);
        temp1.get("hos").put("grape", 7);
        res.add(temp1);

        Inventory inventory = new Inventory();
        assertEquals(res, inventory.InventoryAllocate(order, list));
    }

    //multi items in order and multi wareHouses (some wareHouses have no items in the order and all items in different wareHouses)
    @Test
    public void multiItems3() {
        // build order iput
        Map<String, Integer> order = new HashMap<String, Integer>();
        order.put("pineapple", 10);
        order.put("cherry", 5);
        order.put("grape", 7);
        order.put("apple", 6);

        // build wareHouse input
        List<WareHouse> list = new ArrayList<WareHouse>();
        Map<String, Integer> _inventory1 = new HashMap<String, Integer>();
        _inventory1.put("apple", 5);
        _inventory1.put("orange", 10);
        WareHouse w1 = new WareHouse("owd", _inventory1);
        Map<String, Integer> _inventory2 = new HashMap<String, Integer>();
        _inventory2.put("banana", 5);
        _inventory2.put("orange", 10);
        WareHouse w2 = new WareHouse("dm", _inventory2);
        Map<String, Integer> _inventory3 = new HashMap<String, Integer>();
        _inventory3.put("pineapple", 15);
        _inventory3.put("cherry", 5);
        _inventory3.put("grape", 10);
        _inventory3.put("apple", 4);
        WareHouse w3 = new WareHouse("hos", _inventory3);
        list.add(w1);
        list.add(w2);
        list.add(w3);

        // build result
        List<Map<String, Map<String, Integer>>> res = new ArrayList<Map<String, Map<String, Integer>>>();
        Map<String, Map<String, Integer>> temp1 = new HashMap<String, Map<String, Integer>>();
        temp1.put("owd", new HashMap<String, Integer>());
        temp1.get("owd").put("apple", 5);
        Map<String, Map<String, Integer>> temp2 = new HashMap<String, Map<String, Integer>>();
        temp2.put("hos", new HashMap<String, Integer>());
        temp2.get("hos").put("apple", 1);
        temp2.get("hos").put("pineapple", 10);
        temp2.get("hos").put("cherry", 5);
        temp2.get("hos").put("grape", 7);
        res.add(temp1);
        res.add(temp2);

        Inventory inventory = new Inventory();
        assertEquals(res, inventory.InventoryAllocate(order, list));
    }

    //empty order and multi wareHouses
    @Test
    public void emptyOrder() {
        // build order iput
        Map<String, Integer> order = new HashMap<String, Integer>();

        // build wareHouse input
        List<WareHouse> list = new ArrayList<WareHouse>();
        Map<String, Integer> _inventory1 = new HashMap<String, Integer>();
        _inventory1.put("apple", 5);
        _inventory1.put("orange", 10);
        WareHouse w1 = new WareHouse("owd", _inventory1);
        Map<String, Integer> _inventory2 = new HashMap<String, Integer>();
        _inventory2.put("banana", 5);
        _inventory2.put("orange", 10);
        WareHouse w2 = new WareHouse("dm", _inventory2);
        list.add(w1);
        list.add(w2);

        // build result
        List<Map<String, Map<String, Integer>>> res = new ArrayList<Map<String, Map<String, Integer>>>();

        Inventory inventory = new Inventory();
        assertEquals(res, inventory.InventoryAllocate(order, list));
    }

    //multi items in the order and empty wareHouse
    @Test
    public void emptyWareHouse() {
        // build order iput
        Map<String, Integer> order = new HashMap<String, Integer>();
        order.put("apple", 5);
        order.put("banana", 5);
        order.put("orange", 5);

        // build wareHouse input
        List<WareHouse> list = new ArrayList<WareHouse>();

        // build result
        List<Map<String, Map<String, Integer>>> res = new ArrayList<Map<String, Map<String, Integer>>>();

        Inventory inventory = new Inventory();
        assertEquals(res, inventory.InventoryAllocate(order, list));
    }

}
