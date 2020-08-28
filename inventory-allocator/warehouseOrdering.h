#pragma once
#include <unordered_map>
#include "warehouseInventory.h"
const std::unordered_map<std::string, WarehouseInventory> getWarehouseOrders(ItemList customerOrder,
				         const std::unordered_map<std::string, WarehouseInventory> & warehouses);
void PrintWarehouseList(const std::unordered_map<std::string, WarehouseInventory> & warehouseInventories);