CREATE TABLE [dbo].[Question]
(
	[question_id] INT NOT NULL PRIMARY KEY, 
    [question] NCHAR(50) NOT NULL, 
    [points] NCHAR(10) NOT NULL, 
    [test_id] INT NOT NULL, 
    CONSTRAINT [FK_Question_Test] FOREIGN KEY ([test_id]) REFERENCES [Test]([test_id])
)
