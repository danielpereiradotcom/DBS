/*
# Continuous Assessment
# Dublin Business School
# B8IT104 Data Warehousing and Business Intelligence
# Lecturer: Noel Cosgrave (noel.cosgrave@dbs.ie)
# ##################################################

 Daniel Pereira (10391381@mydbs.ie)
 Maja Pomohaczi (10392409@mydbs.ie)
 Sylwia Wojciechowska (10392584@mydbs.ie)

# ##################################################

  This script will create tables for our SernikDW database. 

  The SernikDW is the datawarehouse (datamart) solution
*/

USE [SernikDW]
GO

/* Drop existing tables */
DROP TABLE IF EXISTS [dbo].[FactSalesOrder]
GO

DROP TABLE IF EXISTS [dbo].[DimProduct]
GO

DROP TABLE IF EXISTS [dbo].[DimEmployee]
GO

DROP TABLE IF EXISTS [dbo].[DimCustomer]
GO

DROP TABLE IF EXISTS [dbo].[DimDate]
GO



/* Create tables */
CREATE TABLE DimDate(
	DateKey int PRIMARY KEY,
	SystemDateAltKey datetime NOT NULL,
	[FullDateUK] CHAR(10), -- Date in dd-MM-yyyy format
	[FullDateUSA] CHAR(10),-- Date in MM-dd-yyyy format
	CalendarYear int NOT NULL,
	[BusinessYearName] CHAR(7), --CY 2012,CY 2013
	CalendarQuarter int NOT NULL,
	[CalendarQuarterName] VARCHAR(9),--First,Second..
	CalendarMonth int NOT NULL,
	CalendarMonthName nvarchar(15) NOT NULL,
	[BusinessMonthYear] CHAR(10), --Jan-2013,Feb-2013
	[CalendarMMYYYY] INT,
	[MonthOfQuarter] INT,-- Month Number belongs to Quarter
	[CalendarWeekOfYear] INT,--Week Number of the Year
	[CalendarWeekOfQuarter] INT, --Week Number of the Quarter
	[CalendarWeekOfMonth] INT,-- Week Number of Month
	CalendarDayOfMonth int NOT NULL,
	[CalendarDaySuffix] VARCHAR(4), -- Apply suffix as 1st, 2nd ,3rd etc
	CalendarDayName nvarchar(15) NOT NULL,
	[CalendarDayOfYear] INT,
	[CalendarDayOfWeekUSA] INT,-- First Day Sunday=1 and Saturday=7
	[CalendarDayOfWeekUK] INT,-- First Day Monday=1 and Sunday=7
	[DayOfWeekInMonth] INT, --1st Monday or 2nd Monday in Month
	[DayOfWeekInYear] INT,
	[DayOfQuarter] INT,
	[BusinessIsWeekday] BIT-- 0=Week End ,1=Week Day

)
GO

CREATE TABLE DimProduct(
	ProductKey int identity NOT NULL PRIMARY KEY NONCLUSTERED,
	ProductSourceID int NOT NULL,
	ProductName nvarchar(40) NOT NULL,
	UnitPrice money NULL, 
	CategoryID int NULL,
	CategoryName nvarchar(15) NULL
)
GO

CREATE TABLE DimCustomer(
	CustomerKey int identity NOT NULL PRIMARY KEY NONCLUSTERED,
	CustomerSourceID nvarchar(5) NOT NULL,
	CompanyName nvarchar(40) NULL,
	ContactName nvarchar(30) NULL,
	ContactTitle nvarchar(30) NULL 
)
GO

CREATE TABLE DimEmployee(
	EmployeeKey int identity NOT NULL PRIMARY KEY NONCLUSTERED, 
	EmployeeSourceID int NOT NULL,
	LastName nvarchar(20) NOT NULL,
	FirstName nvarchar(10) NOT NULL,
	Title nvarchar(30) NOT NULL,
	HireDateKey int NOT NULL
)
GO
ALTER TABLE [dbo].[DimEmployee]  WITH CHECK ADD FOREIGN KEY([HireDateKey])
REFERENCES [dbo].[DimDate] ([DateKey])
GO


CREATE TABLE FactSalesOrder(
	ProductKey int NOT NULL,
	CustomerKey int NOT NULL,
	EmployeeKey int NOT NULL,
	OrderDateKey int NOT NULL,
	OrderSourceID int NOT NULL,
	UnitPrice money NOT NULL,
	Quantity smallint NOT NULL,
	Discount real NOT NULL,
	TotalPrice money NOT NULL,
	TotalDiscount real NOT NULL,
	FinalPrice money NOT NULL

	CONSTRAINT [PK_FactSalesOrder] PRIMARY KEY NONCLUSTERED
	(
		[ProductKey],
		[CustomerKey],
		[EmployeeKey],
		[OrderDateKey],
		[OrderSourceID]
	)
)
GO
ALTER TABLE [dbo].[FactSalesOrder]  WITH CHECK ADD FOREIGN KEY([CustomerKey])
REFERENCES [dbo].[DimCustomer] ([CustomerKey])
GO
ALTER TABLE [dbo].[FactSalesOrder]  WITH CHECK ADD FOREIGN KEY([EmployeeKey])
REFERENCES [dbo].[DimEmployee] ([EmployeeKey])
GO
ALTER TABLE [dbo].[FactSalesOrder]  WITH CHECK ADD FOREIGN KEY([OrderDateKey])
REFERENCES [dbo].[DimDate] ([DateKey])
GO
ALTER TABLE [dbo].[FactSalesOrder]  WITH CHECK ADD FOREIGN KEY([ProductKey])
REFERENCES [dbo].[DimProduct] ([ProductKey])
GO
