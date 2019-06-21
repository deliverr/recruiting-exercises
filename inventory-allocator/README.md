# Inventory Allocator

## Problem

The problem is compute the best way an order can be shipped (called shipments) given inventory across a set of warehouses (called inventory distribution).

## Running the tests

Make sure to clone all files from repository and move to a root of the project. You can either run tests from Intellij IDE or run following on command line.

```
mkdir out
javac -d out ./src/main/java/*
javac -d out -cp out:junit-platform-console-standalone.jar ./src/test/java/Tests.java
java -jar junit-platform-console-standalone.jar --class-path out --scan-class-path
```
