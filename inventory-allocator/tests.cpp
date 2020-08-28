#include <unordered_map>
#include "tests.h"
#include "itemList.h"
#include "warehouseOrdering.h"

//All fruits can be ordered from a single warehouse at the beginning of the list
bool testExample1()
{
	ItemList order;
	order["apple"] = 1;

	std::unordered_map<std::string, WarehouseInventory> warehouseInventories;
	warehouseInventories["owd"]["apple"] = 1;

	std::unordered_map<std::string, WarehouseInventory> expectedOutput;
	expectedOutput["owd"]["apple"] = 1;

	std::unordered_map<std::string, WarehouseInventory> result = getWarehouseOrders(order, warehouseInventories);
	PrintTestOutput(expectedOutput, result);

	return result == expectedOutput;
}

//All fruits can be ordered from various warehouses
bool testExample2()
{
	ItemList order;
	order["apple"] = 10;

	std::unordered_map<std::string, WarehouseInventory> warehouseInventories;
	warehouseInventories["owd"]["apple"] = 5;
	warehouseInventories["dm"]["apple"] = 5;

	std::unordered_map<std::string, WarehouseInventory> expectedOutput;
	expectedOutput["owd"]["apple"] = 5;
	expectedOutput["dm"]["apple"] = 5;

	std::unordered_map<std::string, WarehouseInventory> result = getWarehouseOrders(order, warehouseInventories);
	PrintTestOutput(expectedOutput, result);

	return result == expectedOutput;
}

//Fruits are not all available
bool testExample3()
{
	ItemList order;
	order["apple"] = 1;

	std::unordered_map<std::string, WarehouseInventory> warehouseInventories;
	warehouseInventories["owd"]["apple"] = 0;

	std::unordered_map<std::string, WarehouseInventory> expectedOutput;

	std::unordered_map<std::string, WarehouseInventory> result = getWarehouseOrders(order, warehouseInventories);
	PrintTestOutput(expectedOutput, result);

	return result == expectedOutput;
}

//Some, but not all fruits are not all available
bool testExample4()
{
	ItemList order;
	order["apple"] = 2;

	std::unordered_map<std::string, WarehouseInventory> warehouseInventories;
	warehouseInventories["owd"]["apple"] = 1;

	std::unordered_map<std::string, WarehouseInventory> expectedOutput;

	std::unordered_map<std::string, WarehouseInventory> result = getWarehouseOrders(order, warehouseInventories);
	PrintTestOutput(expectedOutput, result);

	return result == expectedOutput;
}

//All fruits can be ordered from various warehouses
bool testExample5()
{
	ItemList order;
	order["apple"] = 10;
	order["orange"] = 1;
	order["pear"] = 30;

	std::unordered_map<std::string, WarehouseInventory> warehouseInventories;
	warehouseInventories["owd"]["apple"] = 50;
	warehouseInventories["owd"]["orange"] = 2;
	warehouseInventories["dm"]["apple"] = 50;
	warehouseInventories["dm"]["pear"] = 20;
	warehouseInventories["wam"]["apple"] = 15;
	warehouseInventories["wam"]["orange"] = 15;
	warehouseInventories["wam"]["pear"] = 15;

	std::unordered_map<std::string, WarehouseInventory> expectedOutput;
	expectedOutput["owd"]["apple"] = 10;
	expectedOutput["owd"]["orange"] = 1;
	expectedOutput["dm"]["pear"] = 20;
	expectedOutput["wam"]["pear"] = 10;

	std::unordered_map<std::string, WarehouseInventory> result = getWarehouseOrders(order, warehouseInventories);
	PrintTestOutput(expectedOutput, result);

	return result == expectedOutput;
}

//All fruits can be ordered from a single warehouse at the end of the list
bool testExample6()
{
	ItemList order;
	order["apple"] = 2;

	std::unordered_map<std::string, WarehouseInventory> warehouseInventories;
	warehouseInventories["owd"]["apple"] = 1;
	warehouseInventories["dm"]["apple"] = 1;
	warehouseInventories["wam"]["apple"] = 2;

	std::unordered_map<std::string, WarehouseInventory> expectedOutput;
	expectedOutput["wam"]["apple"] = 2;

	std::unordered_map<std::string, WarehouseInventory> result = getWarehouseOrders(order, warehouseInventories);
	PrintTestOutput(expectedOutput, result);

	return result == expectedOutput;
}

void PrintTestOutput(const std::unordered_map<std::string, WarehouseInventory> & expectedOutput, const std::unordered_map<std::string, WarehouseInventory> & myOutput)
{
	std::cout << "Expected Output: ";
	PrintWarehouseList(expectedOutput);
	std::cout << "My Output:       ";
	PrintWarehouseList(myOutput);
}