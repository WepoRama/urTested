CREATE TABLE [dbo].[Answer]
(
	[answer_id] INT NOT NULL PRIMARY KEY, 
    [question_id] INT NOT NULL, 
    [answer] NCHAR(50) NOT NULL, 
    [correct] INT NOT NULL, 
    CONSTRAINT [QuestionFK] FOREIGN KEY ([question_id]) REFERENCES [Question]([question_id])
)
