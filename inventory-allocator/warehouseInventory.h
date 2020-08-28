#pragma once
#include <string>
#include <iostream>
#include "itemList.h"

class WarehouseInventory
{
	public:
		//Constructors
		WarehouseInventory(const ItemList & items = {});

		//Operators
		WarehouseInventory& operator=(const WarehouseInventory& rhs);
		bool operator== (const WarehouseInventory & rhs) const;
		int& operator[](const std::string & itemName) { return m_warehouseInventory[itemName]; }
		friend std::ostream & operator<<(std::ostream & os, const WarehouseInventory & warehouse);

		//Getters
		bool hasAllItems(const ItemList & customerOrder) const;
	private:
		ItemList m_warehouseInventory;
};