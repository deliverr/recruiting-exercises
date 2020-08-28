#include "warehouseInventory.h"

WarehouseInventory::WarehouseInventory(const ItemList & items) :
	m_warehouseInventory(items)
{
}

WarehouseInventory & WarehouseInventory::operator=(const WarehouseInventory & rhs)
{
	if (this == &rhs)
		return *this;

	m_warehouseInventory = rhs.m_warehouseInventory;
	return *this;
}

bool WarehouseInventory::hasAllItems(const ItemList & customerOrder) const
{
	//For each item in the customer's order
	for (auto it : customerOrder)
	{
		//If the inventory of the warehouse is insufficient, return false
		try {
			if (m_warehouseInventory.at(it.first) < it.second)
				return false;
		}
		catch (std::out_of_range exception)
		{
			return false;
		}
	}
	return true;
}

bool WarehouseInventory::operator==(const WarehouseInventory & rhs) const
{
	return m_warehouseInventory == rhs.m_warehouseInventory;
}

std::ostream & operator<<(std::ostream & os, const WarehouseInventory & warehouse)
{
	for (auto it = warehouse.m_warehouseInventory.begin(); it != warehouse.m_warehouseInventory.end(); ++it)
	{
		//If this isn't the first item we're printing
		if (it != warehouse.m_warehouseInventory.begin())
			os << ", ";
		os << " { " << it->first << ": " << it->second << " }";
	}
	return os;
}
