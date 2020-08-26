package com.tony.app;

import java.util.Collections;
import java.util.LinkedList;
import java.util.Map;
import java.util.TreeMap;

public class InventoryAllocator {

	/*
	 * Private attributes that will be used through the class.
	 */
	private TreeMap<String, LinkedList<Products>> mainMap = new TreeMap<String, LinkedList<Products>>(
			Collections.reverseOrder());
	private TreeMap<String, Products> outputMap = new TreeMap<String, Products>(Collections.reverseOrder());
	private LinkedList<Products> testProducts = new LinkedList<Products>();
	private Products tempProducts = new Products();


	/*
	 * The checkInventory method will accept a Products object with something like "orange, 10"
	 * and will check through the warehouses, and their respective inventories to get the cheapest
	 * shipping strategy.
	 */
	public TreeMap<String, Products> checkInventory(Products prod) {

		System.out.println("Test case: " + prod);

		boolean flag1 = false, flag2 = false;
		int marker = 0, totalSum = 0;

		totalSum = isBigger(prod, totalSum);

		/*
		 * These will be two preliminary checks.
		 * 1.) If requested item is greater than total stock in all warehouses, return empty map.
		 * 2.) If requested item doesn't exist, return empty map.
		 */
		if (prod.getAmount() > totalSum && totalSum != 0) {
			System.out.println("Not enough stock, returning empty map.");
			return new TreeMap<String, Products>();
		}
		if (totalSum == 0) {
			System.out.println("Item does not exist in any of the warehouses.");
			return new TreeMap<String, Products>();
		}

		
		/*
		 * Advance for loop to iterate over the warehouses.
		 */
		for (Map.Entry<String, LinkedList<Products>> iterable : mainMap.entrySet()) {

			testProducts = iterable.getValue();
			
			/*
			 * Checking to see if requested item is in that warehouse.
			 * 1.) if it does exist, set marker on location and break out.
			 * 2.) if not, continue to next iteration (or next warehouse)
			 */
			for (int i = 0; i < testProducts.size(); i++) {
				if (testProducts.get(i).getName().equals(prod.getName())) {
					marker = i;
					flag1 = true;
					break;
				}
			}

			if (!flag1)
				continue;

			
			/*
			 * Checking 3 cases in this block.
			 * 1.) If requested amount is the same.
			 * 2.) If requested amount less.
			 * 3.) If requested amount is greater
			 */
			if (prod.getAmount() == testProducts.get(marker).getAmount()) {
				outputMap.put(iterable.getKey(),
						new Products(testProducts.get(marker).getName(), testProducts.get(marker).getAmount()));
				prod.setAmount(prod.getAmount() - testProducts.get(marker).getAmount());
				flag2 = true;
				break;
			} else if (prod.getAmount() < testProducts.get(marker).getAmount()) {
				outputMap.put(iterable.getKey(), new Products(prod.getName(), testProducts.get(marker).getAmount()));
				flag2 = true;
				break;
			} else {
				
				if(prod.getAmount() == 0)
					break;

				tempProducts.setName(testProducts.get(marker).getName());
				tempProducts.setAmount(testProducts.get(marker).getAmount());
				outputMap.put(iterable.getKey(), tempProducts);

				prod.setAmount(prod.getAmount() - testProducts.get(marker).getAmount());
			}

			if (flag2) {
				flag2 = false;
				break;
			}

		}
		return outputMap;
	}

	/*
	 * This will gather the total number of stock for one particular item and store it in
	 * the integer "totalSum"
	 */
	public int isBigger(Products prod, int totalSum) {
		for (Map.Entry<String, LinkedList<Products>> iterable : mainMap.entrySet()) {
			testProducts = iterable.getValue();

			for (int i = 0; i < testProducts.size(); i++) {
				if (testProducts.get(i).getName().equals(prod.getName())) {
					totalSum += testProducts.get(i).getAmount();
				}
			}
		}
		return totalSum;
	}

	
	/*
	 * This will fill the Main warehouse map with default values so we can have something to work with.
	 * For a more dynamic entry, the user could be asked to provide warehouse names, items and their amounts
	 * at runtime in the console window.
	 */
	public void fillMap() {

		LinkedList<Products> tempProducts = new LinkedList<Products>();
		tempProducts.add(new Products("apple", 5));
		tempProducts.add(new Products("orange", 10));
		mainMap.put("owd", tempProducts);
		tempProducts = new LinkedList<Products>();

		tempProducts.add(new Products("apple", 5));
		tempProducts.add(new Products("blueberry", 10));
		tempProducts.add(new Products("orange", 10));

		mainMap.put("dm", tempProducts);

		tempProducts = new LinkedList<Products>();
		tempProducts.add(new Products("watermelon", 10));
		tempProducts.add(new Products("strawberry", 25));
		tempProducts.add(new Products("blueberry", 10));

		mainMap.put("ca", tempProducts);
	}

}
