CREATE TABLE [dbo].[Test]
(
	[test_id] INT NOT NULL PRIMARY KEY, 
    [name] NCHAR(50) NOT NULL, 
    [author] NCHAR(20) NOT NULL, 
    [expires_date] DATE NOT NULL
);
CREATE TABLE Test
(
	test_id INT NOT NULL PRIMARY KEY, 
	name NCHAR(50) NOT NULL, 
	author NCHAR(20) NOT NULL, 
	expires_date DATE NOT NULL
);
