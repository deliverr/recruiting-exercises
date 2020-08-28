#include <algorithm> //std::min
#include "warehouseOrdering.h"

const std::unordered_map<std::string, WarehouseInventory> getWarehouseOrders(ItemList customerOrder,
	                     const std::unordered_map<std::string, WarehouseInventory> & warehouses)
{
	std::unordered_map<std::string, WarehouseInventory> result;

	//Check if any single warehouse can fulfill all the orders
	for (auto currentWarehouse : warehouses)
	{
		if (currentWarehouse.second.hasAllItems(customerOrder))
		{
			result[currentWarehouse.first] = currentWarehouse.second;
			return result;
		}
	}

	//Go through the item list of each warehouse, buying as many items as possible as we go
	for (auto currentWarehouse : warehouses)
	{
		for (auto item = customerOrder.begin(); item != customerOrder.end(); /*No Increment*/)
		{
			//The number bought from that warehouse will be the number desired if there are enough, or the maximum available otherwise
			int numOfItemBought = std::min(item->second, currentWarehouse.second[item->first]);
			if (numOfItemBought == 0)
			{
				++item;
				continue;
			}

			customerOrder[item->first] -= numOfItemBought;
			result[currentWarehouse.first][item->first] += numOfItemBought;

			//If the customer order for this item is satisfied, remove it from the shopping list
			if (item->second == 0)
			{
				item = customerOrder.erase(item);
			}
			else
			{
				++item;
			}
		}
		if (customerOrder.size() == 0)
			break;
	}
	//If we can't buy everything, buy nothing according to specs
	if (!customerOrder.empty())
		result.clear();

	return result;
}

void PrintWarehouseList(const std::unordered_map<std::string, WarehouseInventory> & warehouseInventories)
{
	std::cout << "[";
	for (auto it = warehouseInventories.begin(); it != warehouseInventories.end(); ++it)
	{
		if (it != warehouseInventories.begin())
			std::cout << ", ";
		std::cout << "{ " << it->first << ":";
		std::cout << it->second;
		std::cout << " }";
	}
	std::cout << "]" << std::endl;
}
