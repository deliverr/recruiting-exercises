import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;

import static org.junit.jupiter.api.Assertions.*;

public class SolutionTest {

    @Test
    public void test_order_shipped_using_one_warehouse() throws Exception {

        /*
        * Test inputItems: { apple : 1 }
        * Test inputWarehouses: [{ name: owd, inventory: { apple: 1 }}]
        *
        * Expected output: [{ owd: { apple: 1}}]
        **/

        Solution solution = new Solution();

        //make input items
        HashMap<String, Integer> inputItems = new HashMap<>();
        inputItems.put("apple", 1);

        //create inventory for warehouse 1
        HashMap<String, Integer> inventory_1 = new HashMap<>();
        inventory_1.put("apple", 1);

        //create warehouse 1 and add it
        Warehouse warehouse_1 = new Warehouse("owd", inventory_1);
        ArrayList<Warehouse> warehouses = new ArrayList<>();
        warehouses.add(warehouse_1);

        //get the result
        ArrayList<Result> result = solution.answer(inputItems, warehouses);


        assertEquals("owd",result.get(0).getName(), "warehouse name should be owd");
        assertEquals(1, result.get(0).getItemList().get("apple"), "only expect 1 apple");



    }

    @Test
    public void test_no_order_shipped_when_nothing_in_inventory() throws Exception {

        /*
         * Test inputItems: { apple : 1 }
         * Test inputWarehouses: [{ name: owd, inventory: { apple: 0 }}]
         *
         * Expected output: []
         **/

        Solution solution = new Solution();

        //make input items
        HashMap<String, Integer> inputItems = new HashMap<>();
        inputItems.put("apple", 1);

        //create inventory for warehouse 1
        HashMap<String, Integer> inventory_1 = new HashMap<>();
        inventory_1.put("apple", 0);

        //create warehouse 1 and add it
        Warehouse warehouse_1 = new Warehouse("owd", inventory_1);
        ArrayList<Warehouse> warehouses = new ArrayList<>();
        warehouses.add(warehouse_1);

        //get the result
        ArrayList<Result> result = solution.answer(inputItems, warehouses);

        assertEquals(true, result.isEmpty(), "Expect result empty");
    }

    @Test
    public void test_no_order_shipped_when_not_enough_in_inventory() throws Exception {

        /*
         * Test inputItems: { apple : 1, banana: 2 }
         * Test inputWarehouses: [{ name: owd, inventory: { apple: 1 }}]
         *
         * Expected output: []
         **/

        Solution solution = new Solution();

        //make input items
        HashMap<String, Integer> inputItems = new HashMap<>();
        inputItems.put("apple", 1);
        inputItems.put("banana", 2);

        //create inventory for warehouse 1
        HashMap<String, Integer> inventory_1 = new HashMap<>();
        inventory_1.put("apple", 1);

        //create warehouse 1 and add it
        Warehouse warehouse_1 = new Warehouse("owd", inventory_1);
        ArrayList<Warehouse> warehouses = new ArrayList<>();
        warehouses.add(warehouse_1);

        //get the result
        ArrayList<Result> result = solution.answer(inputItems, warehouses);

        assertEquals(true, result.isEmpty(), "Expect result empty");
    }


    @Test
    public void test_order_shipped_using_multiple_warehouse() throws Exception {

        /*
         * Test inputItems: { apple : 10 }
         * Test inputWarehouses: [{ name: owd, inventory: { apple: 4 }}, { name: dm, inventory: { apple: 8 }}]
         *
         * Expected output: [{ owd: { apple: 4}}, { dm: { apple: 6}}]
         **/

        Solution solution = new Solution();

        //make input items
        HashMap<String, Integer> inputItems = new HashMap<>();
        inputItems.put("apple", 10);

        //create inventory for warehouse 1
        HashMap<String, Integer> inventory_1 = new HashMap<>();
        inventory_1.put("apple", 4);
        //create warehouse 1
        Warehouse warehouse_1 = new Warehouse("owd", inventory_1);

        //create inventory for warehouse 2
        HashMap<String, Integer> inventory_2 = new HashMap<>();
        inventory_2.put("apple", 8);
        //create warehouse 2
        Warehouse warehouse_2 = new Warehouse("dm", inventory_2);

        //create list of warehouses
        ArrayList<Warehouse> warehouses = new ArrayList<>();
        warehouses.add(warehouse_1);
        warehouses.add(warehouse_2);

        //get the result
        ArrayList<Result> result = solution.answer(inputItems, warehouses);


        assertEquals(2, result.size(), "We should ship order from 2 warehouses");
        assertEquals("owd",result.get(0).getName(), "warehouse name should be owd");
        assertEquals(4, result.get(0).getItemList().get("apple"), "only expect 4 apple from owd");
        assertEquals("dm",result.get(1).getName(), "warehouse name should be dm");
        assertEquals(6, result.get(1).getItemList().get("apple"), "only expect 6 apple from dm");

    }

    @Test
    public void test_order_shipped_using_one_warehouse_when_it_can_be_shipped_from_two_warehouses() throws Exception {
        /*
         * Test inputItems: { apple : 10 }
         * Test inputWarehouses: [{ name: owd, inventory: { apple: 10 }},
         *                        { name: dm, inventory: { apple: 6 }}]
         *
         * Expected output: [{ owd: { apple: 10}}]
         **/

        Solution solution = new Solution();

        //make input items
        HashMap<String, Integer> inputItems = new HashMap<>();
        inputItems.put("apple", 10);


        //create inventory for warehouse 1
        HashMap<String, Integer> inventory_1 = new HashMap<>();
        inventory_1.put("apple", 10);
        //create warehouse 1
        Warehouse warehouse_1 = new Warehouse("owd", inventory_1);

        //create inventory for warehouse 2
        HashMap<String, Integer> inventory_2 = new HashMap<>();
        inventory_2.put("apple", 6);
        //create warehouse 2
        Warehouse warehouse_2 = new Warehouse("dm", inventory_2);


        //create list of warehouses
        ArrayList<Warehouse> warehouses = new ArrayList<>();
        warehouses.add(warehouse_1);
        warehouses.add(warehouse_2);

        //get the result
        ArrayList<Result> result = solution.answer(inputItems, warehouses);


        assertEquals(1, result.size(), "Should only need one warehouse to ship order");
        assertEquals("owd",result.get(0).getName(), "warehouse name should be owd");
        assertEquals(10, result.get(0).getItemList().get("apple"), "expect 10 apple from owd");


    }

    @Test
    public void test_order_shipped_using_one_warehouse_when_it_can_be_shipped_from_multiple_warehouses() throws Exception {

        /*
         * Test inputItems: { banana : 5, apple: 4, orange: 3 }
         * Test inputWarehouses: [{ name: owd, inventory: { apple: 6, banana: 7, orange: 5 }},
         *                        { name: dm, inventory: { apple: 8, banana: 10 }},
         *                        { name: acr, inventory: { orange: 6 }}]
         *
         * Expected output: [{ owd: { apple: 4, banana: 5, orange: 3}}]
         **/

        Solution solution = new Solution();

        //make input items
        HashMap<String, Integer> inputItems = new HashMap<>();
        inputItems.put("banana", 5);
        inputItems.put("apple", 4);
        inputItems.put("orange", 3);

        //create inventory for warehouse 1
        HashMap<String, Integer> inventory_1 = new HashMap<>();
        inventory_1.put("apple", 6);
        inventory_1.put("banana", 7);
        inventory_1.put("orange", 5);
        //create warehouse 1
        Warehouse warehouse_1 = new Warehouse("owd", inventory_1);

        //create inventory for warehouse 2
        HashMap<String, Integer> inventory_2 = new HashMap<>();
        inventory_2.put("apple", 8);
        inventory_2.put("banana", 10);
        //create warehouse 2
        Warehouse warehouse_2 = new Warehouse("dm", inventory_2);

        //create inventory for warehouse 3
        HashMap<String, Integer> inventory_3 = new HashMap<>();
        inventory_3.put("orange", 6);
        //create warehouse 2
        Warehouse warehouse_3 = new Warehouse("acr", inventory_3);

        //create list of warehouses
        ArrayList<Warehouse> warehouses = new ArrayList<>();
        warehouses.add(warehouse_1);
        warehouses.add(warehouse_2);
        warehouses.add(warehouse_3);

        //get the result
        ArrayList<Result> result = solution.answer(inputItems, warehouses);


        assertEquals(1, result.size(), "Should only need one warehouse to ship order");
        assertEquals("owd",result.get(0).getName(), "warehouse name should be owd");
        assertEquals(4, result.get(0).getItemList().get("apple"), "expect 4 apple from owd");
        assertEquals(5, result.get(0).getItemList().get("banana"), "expect 5 banana from owd");
        assertEquals(3, result.get(0).getItemList().get("orange"), "expect 4 orange from owd");


    }


    @Test
    public void test_order_shipped_from_closest_two_when_can_be_shipped_from_more_warehouses() throws Exception {

        /*
         * Test inputItems: { apple: 8, banana: 12, orange: 5 }
         * Test inputWarehouses: [{ name: owd, inventory: { apple: 6, banana: 7, orange: 5 }},
         *                        { name: dm, inventory: { apple: 3, banana: 10, orange: 3 }},
         *                        { name: acr, inventory: { apple: 10, orange: 6 }}]
         *
         * Expected output: [{ owd: { apple: 6, banana: 7, orange: 5}},
         *                   { dm: { apple: 2, banana: 5}}]
         **/

        Solution solution = new Solution();

        //make input items
        HashMap<String, Integer> inputItems = new HashMap<>();
        inputItems.put("apple", 8);
        inputItems.put("banana", 12);
        inputItems.put("orange", 5);

        //create inventory for warehouse 1
        HashMap<String, Integer> inventory_1 = new HashMap<>();
        inventory_1.put("apple", 6);
        inventory_1.put("banana", 7);
        inventory_1.put("orange", 5);
        //create warehouse 1
        Warehouse warehouse_1 = new Warehouse("owd", inventory_1);

        //create inventory for warehouse 2
        HashMap<String, Integer> inventory_2 = new HashMap<>();
        inventory_2.put("apple", 3);
        inventory_2.put("banana", 10);
        inventory_2.put("orange", 3);
        //create warehouse 2
        Warehouse warehouse_2 = new Warehouse("dm", inventory_2);

        //create inventory for warehouse 3
        HashMap<String, Integer> inventory_3 = new HashMap<>();
        inventory_3.put("apple", 10);
        inventory_3.put("orange", 6);
        //create warehouse 2
        Warehouse warehouse_3 = new Warehouse("acr", inventory_3);

        //create list of warehouses
        ArrayList<Warehouse> warehouses = new ArrayList<>();
        warehouses.add(warehouse_1);
        warehouses.add(warehouse_2);
        warehouses.add(warehouse_3);

        //get the result
        ArrayList<Result> result = solution.answer(inputItems, warehouses);


        assertEquals(2, result.size(), "Should only need two warehouses to ship order");
        assertEquals("owd",result.get(0).getName(), "warehouse name should be owd");
        assertEquals(6, result.get(0).getItemList().get("apple"), "expect 6 apple from owd");
        assertEquals(7, result.get(0).getItemList().get("banana"), "expect 7 banana from owd");
        assertEquals(5, result.get(0).getItemList().get("orange"), "expect 5 orange from owd");
        assertEquals("dm",result.get(1).getName(), "warehouse name should be dm");
        assertEquals(2, result.get(1).getItemList().get("apple"), "expect 2 apple from dm");
        assertEquals(5, result.get(1).getItemList().get("banana"), "expect 5 banana from dm");


    }




}