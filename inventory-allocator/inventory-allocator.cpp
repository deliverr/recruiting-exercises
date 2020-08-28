#include <iostream>
#include <unordered_map>
#include "tests.h"

bool (*testFunctions[])() = {
	testExample1,
	testExample2,
	testExample3,
	testExample4,
	testExample5,
	testExample6,
};

int main()
{
	int numTests = sizeof(testFunctions) / sizeof(testFunctions[0]);
	for (int i = 0; i < numTests; ++i)
	{
		std::cout << "Test Example " << i + 1 << ":" << std::endl;
		if (testFunctions[i]())
			std::cout << "SUCCESS";
		else
			std::cout << "FAILURE";
		std::cout << std::endl
				  << std::endl;
	}
	return 0;
}