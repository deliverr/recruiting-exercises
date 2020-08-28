#pragma once
#include "warehouseInventory.h"

bool testExample1();
bool testExample2();
bool testExample3();
bool testExample4();
bool testExample5();
bool testExample6();
void PrintTestOutput(const std::unordered_map<std::string, WarehouseInventory> & expectedOutput,
	                 const std::unordered_map<std::string, WarehouseInventory> & myOutput);
