using DeliverrChallenge;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Collections.Generic;


namespace DeliverAllocationUnitTest
{
    /// <summary>
    /// Summary Tests cover 5 edge cases
    /// 1. Order totally match the inventory
    /// 2. Order contains different inventory
    /// 3. Amount in order exceedes amount in Inventory
    /// 4. Order has negative amount
    /// 5. Warehouse has negative amount of inventory
    /// </summary>
    [TestClass]
    public class InventoryAllocatorTest
    {
        Dictionary<string, int> orderList;
        Orders orders;
        WareHouse wareHouse;
        Locations locations;
        
       [TestMethod]
        public void InventoryMatchTheOrder()
        {
            //Assign
            orderList = new Dictionary<string, int>();
            orderList.Add("Apples", 5);
            orderList.Add("Pears", 5);
            orders = new Orders(orderList);
            wareHouse = new WareHouse("owd");
            locations = new Locations();
            locations.setWareHouse(wareHouse);
            wareHouse.SetInventoryAmount("Apples", 5);
            wareHouse.SetInventoryAmount("Pears", 5);
            InventoryAllocator inventoryAllocator = new InventoryAllocator();

            //Act
            inventoryAllocator.AllocateOrderAmongLocations(orders, locations);
            //Assert
            Assert.IsTrue(wareHouse.InventoryAmounts["Apples"] == 0);
            Assert.IsTrue(wareHouse.StoredInventory["Apples"] == 5);
            Assert.IsTrue(wareHouse.InventoryAmounts["Pears"] == 0);
            Assert.IsTrue(wareHouse.StoredInventory["Pears"] == 5);

        }

        [TestMethod]
        public void InventoryDoesNotMatchTheOrder()
        {
            //Assign
            orderList = new Dictionary<string, int>();
            orderList.Add("Apples", 5);
            orderList.Add("Pears", 5);
            orders = new Orders(orderList);
            wareHouse = new WareHouse("owd");
            locations = new Locations();
            locations.setWareHouse(wareHouse);
            wareHouse.SetInventoryAmount("Apples", 5);
            wareHouse.SetInventoryAmount("Watermelon", 5);
            InventoryAllocator inventoryAllocator = new InventoryAllocator();

            //Act
            inventoryAllocator.AllocateOrderAmongLocations(orders, locations);
            //Assert
            Assert.IsTrue(inventoryAllocator.OrderAmount == -1);

        }

        [TestMethod]
        public void InventoryIsLessThanAmountOfTheOrder()
        {
            //Assign
            orderList = new Dictionary<string, int>();
            orderList.Add("Apples", 10);
            orderList.Add("Pears", 10);
            orders = new Orders(orderList);
            wareHouse = new WareHouse("owd");
            locations = new Locations();
            locations.setWareHouse(wareHouse);
            wareHouse.SetInventoryAmount("Apples", 5);
            wareHouse.SetInventoryAmount("Pears", 5);
            InventoryAllocator inventoryAllocator = new InventoryAllocator();

            //Act
            inventoryAllocator.AllocateOrderAmongLocations(orders, locations);
            //Assert
            Assert.IsTrue(inventoryAllocator.OrderAmount > 0);

        }

        [TestMethod]
        public void OrderHasNegativeAmount()
        {
            //Assign
            orderList = new Dictionary<string, int>();
            orderList.Add("Apples", -1);
            orderList.Add("Pears", 5);
            orders = new Orders(orderList);
            wareHouse = new WareHouse("owd");
            locations = new Locations();
            locations.setWareHouse(wareHouse);
            wareHouse.SetInventoryAmount("Apples", 5);
            wareHouse.SetInventoryAmount("Watermelon", 5);
            InventoryAllocator inventoryAllocator = new InventoryAllocator();

            //Act
            
            //Assert
            Assert.IsTrue(inventoryAllocator.AllocateOrderAmongLocations(orders, locations)==null);

        }

        [TestMethod]
        public void WareHOuseHasNegativeAmount()
        {
            //Assign
            orderList = new Dictionary<string, int>();
            orderList.Add("Apples", 5);
            orderList.Add("Pears", 5);
            orders = new Orders(orderList);
            wareHouse = new WareHouse("owd");
            locations = new Locations();
            locations.setWareHouse(wareHouse);
            wareHouse.SetInventoryAmount("Apples", -1);
            wareHouse.SetInventoryAmount("Watermelon", 5);
            InventoryAllocator inventoryAllocator = new InventoryAllocator();

            //Act

            //Assert
            Assert.IsTrue(inventoryAllocator.AllocateOrderAmongLocations(orders, locations) == null);

        }


    }
}
