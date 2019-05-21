/*
Continuous Assessment
Dublin Business School
B8IT104 Data Warehousing and Business Intelligence
Lecturer: Noel Cosgrave (noel.cosgrave@dbs.ie)

# ##################################################

 Daniel Pereira (10391381@mydbs.ie)
 Maja Pomohaczi (10392409@mydbs.ie)
 Sylwia Wojciechowska (10392584@mydbs.ie)

# ##################################################

  This script will return Orders from Northwind in a way to be stagged 
*/

CREATE VIEW [dbo].[VW_Staging_SalesOrder] AS

	SELECT
		o.CustomerID AS [CustomerID],
		o.EmployeeID AS [EmployeeID],
		o.OrderID AS [OrderID],
		o.OrderDate AS [OrderDate],
		prod.ProductID AS [ProductID],
		od.Quantity AS [Quantity],
		od.UnitPrice AS [UnitPrice],
		od.Discount AS [Discount],
		(od.Quantity * od.UnitPrice)  AS [TotalPrice],
		od.Discount*(od.Quantity * od.UnitPrice) AS [TotalDiscount],
		CONVERT(money,(od.Quantity * od.UnitPrice) - od.Discount*(od.Quantity * od.UnitPrice)) AS [FinalPrice]

	FROM
		[dbo].[Orders] o
		INNER JOIN [dbo].[Order Details] od ON o.OrderID = od.OrderID 
		INNER JOIN [dbo].[Products] prod ON od.ProductID = prod.ProductID
		INNER JOIN [dbo].[Customers] cus ON o.CustomerID = cus.CustomerID
		INNER JOIN [dbo].[Employees] e ON o.EmployeeID = e.EmployeeID
