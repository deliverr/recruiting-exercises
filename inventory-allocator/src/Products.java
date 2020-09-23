package com.tony.app;

public class Products {

	private String name;
	private int amount;

	public Products(String name, int amount) {
		super();
		this.name = name;
		this.amount = amount;
	}

	public Products() {
		super();
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getAmount() {
		return amount;
	}

	public void setAmount(int amount) {
		this.amount = amount;
	}

	@Override
	public String toString() {
		return name + " : " + amount;
	}
	
	

}
