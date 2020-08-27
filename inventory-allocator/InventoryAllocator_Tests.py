from InventoryAllocator import InventoryAllocator

inventory_alloc = InventoryAllocator()

# Valid single warehouse order
order = {'orange': 0, 'eggplant': 100}
stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 6, 'eggplant': 10000}}]
print(inventory_alloc.inventory_allocator(order, stock))

# Multiple warehouses
order = {'orange': 2, 'eggplant': 100}
stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 0, 'eggplant': 10000}},
         {'name': 'orange_city', 'inventory': {'orange': 10, 'eggplant': 0}}]
print(inventory_alloc.inventory_allocator(order, stock))

# Negative order value
# Properly check warehouse value did not increase
order = {'orange': 0, 'eggplant': -100}
stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 6, 'eggplant': 10000}}]
print(inventory_alloc.inventory_allocator(order, stock))

# Negative warehouse stock value
order = {'orange': 0, 'eggplant': -100}
stock = [{'name': 'eggplant_inc', 'inventory': {'orange': -6, 'eggplant': -10000}}]
print(inventory_alloc.inventory_allocator(order, stock))

# Order doesnt exist
order = {'banganga': 10, 'cinnamon': 20}
stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 1, 'eggplant': 2}}]
print(inventory_alloc.inventory_allocator(order, stock))

# Exact match
order = {'orange': 2, 'eggplant': 100}
stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 2, 'eggplant': 100}},
         {'name': 'orange_city', 'inventory': {'orange': 10, 'eggplant': 10}}]
print(inventory_alloc.inventory_allocator(order, stock))

# Order number is string
order = {'orange': 'Nen', 'eggplant': 'Gon'}
stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 2, 'eggplant': 100}},
         {'name': 'orange_city', 'inventory': {'orange': 10, 'eggplant': 10}}]
print(inventory_alloc.inventory_allocator(order, stock))

# Warehouse name is number
order = {'orange': 0, 'eggplant': 20}
stock = [{'name': 69, 'inventory': {'orange': 2, 'eggplant': 100}},
         {'name': 'orange_city', 'inventory': {'orange': 10, 'eggplant': 10}}]
print(inventory_alloc.inventory_allocator(order, stock))

# Order item is number
order = {20: 2, 'eggplant': 20}
stock = [{'name': 69, 'inventory': {'orange': 2, 'eggplant': 100}},
         {'name': '20city', 'inventory': {20: 10, 'eggplant': 10}}]
print(inventory_alloc.inventory_allocator(order, stock))

# No warehouses
order = {'apples': 10, 'starfruit': 9001}
stock = []
print(inventory_alloc.inventory_allocator(order, stock))

# No orders here today
order = {}
stock = [{'name': 'eggplant_inc', 'inventory': {'orange': 6, 'eggplant': 10000}}]
print(inventory_alloc.inventory_allocator(order, stock))

# Deliverrr Ironman
order = {'apples': 100, 'bananas': 100, 'carrots': 100, 'dandruff shampoo': 5, 'eggplants': 24,
         'french fries': 2, 'gum gum fruit': 1}
stock =[{'name': 'owd', 'inventory': {'apples': 20}},
        {'name': 'dm', 'inventory': {'apples': 60, 'bananas': 50}},
        {'name': 'mil', 'inventory': {'apples': 100, 'bananas': 500}},
        {'name': 'hq', 'inventory': {'carrots': 0, 'dandruff shampoo': 5}},
        {'name': 'last stop', 'inventory': {'carrots': 100, 'eggplants': 2000, 'gum gum fruit': 1}},
        {'name': "Mc Donald's", 'inventory': {'french fries': 2}}]
print(inventory_alloc.inventory_allocator(order, stock))
