# Singelton Design Pattern in Java

Singelton design pattern is the one of most common design pattern used in programming.

Here,I added most popular 3 ways to implement singelton design pattern.
**1.Lazy**
**2.Eager**
**3.ENUM**

## **1.Lazy Method:** 
In this method, object is created only if it is needed.
This may prevent resource wastage. An implementation of getInstance() method is required which return the instance. 
There is a null check that if object is not created then create, otherwise return previously created.

## **2.Eager Method:** 

This is the simplest method of creating a singleton class.
In this, object of class is created when it is loaded to the memory by **JVM**. 
It is done by assigning the reference an instance directly.

## **3.ENUM Method:** 

All of the above problems can be solved very easily by using the enum type to make singletons.
Since enums are inherently serializable we don’t need to implement it with serializable interface.
Reflection problem is also not there. 
Therefore, it is 100% guaranteed that only one instance of the singleton is present within a **JVM**.


If you want to find about more details go here,[Link to google](https://dzone.com/articles/java-singletons-using-enum)


