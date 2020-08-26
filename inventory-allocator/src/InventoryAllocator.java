package com.tony.app;

import java.util.Collections;
import java.util.LinkedList;
import java.util.Map;
import java.util.TreeMap;

public class InventoryAllocator {

	private TreeMap<String, LinkedList<Products>> mainMap = new TreeMap<String, LinkedList<Products>>(
			Collections.reverseOrder());
	private TreeMap<String, Products> outputMap = new TreeMap<String, Products>(Collections.reverseOrder());
	private LinkedList<Products> testProducts = new LinkedList<Products>();
	private Products tempProducts = new Products();


	public TreeMap<String, Products> checkInventory(Products prod) {

		System.out.println("Test case: " + prod);

		boolean flag1 = false, flag2 = false;
		int marker = 0, totalSum = 0;

		totalSum = isBigger(prod, totalSum);

		if (prod.getAmount() > totalSum && totalSum != 0) {
			System.out.println("Not enough stock, returning empty map.");
			return new TreeMap<String, Products>();
		}
		if (totalSum == 0) {
			System.out.println("Item does not exist in any of the warehouses.");
			return new TreeMap<String, Products>();
		}

		for (Map.Entry<String, LinkedList<Products>> iterable : mainMap.entrySet()) {

			testProducts = iterable.getValue();

			for (int i = 0; i < testProducts.size(); i++) {
				if (testProducts.get(i).getName().equals(prod.getName())) {
					marker = i;
					flag1 = true;
					break;
				}
			}

			if (!flag1)
				continue;

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
