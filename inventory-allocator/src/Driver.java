package com.tony.app;

public class Driver {

	public static void main(String[] args) {
		
		InventoryAllocator inventory = new InventoryAllocator();
		
		inventory.fillMap();
		
		/*
		 * Here are the test cases for our warehouses.
		 * The checkInventory method will check by cheapest warehouse first if it can
		 * fulfill an order.
		 */
//		System.out.println(inventory.checkInventory(new Products("apple", 1)));
//		System.out.println(inventory.checkInventory(new Products("apple", 11)));
//		System.out.println(inventory.checkInventory(new Products("apple", 10)));
//		System.out.println(inventory.checkInventory(new Products("blueberry", 10)));
//		System.out.println(inventory.checkInventory(new Products("watermelon", 5)));
		System.out.println(inventory.checkInventory(new Products("blueberry", 20)));
	}

}
