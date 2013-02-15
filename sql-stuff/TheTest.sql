
CREATE TABLE Test
(
	test_id INT NOT NULL PRIMARY KEY, 
	name NCHAR(50) NOT NULL, 
	author NCHAR(20) NOT NULL, 
	expires_date DATE NOT NULL
);

CREATE TABLE Question
(
	question_id INT NOT NULL PRIMARY KEY, 
	question NCHAR(50) NOT NULL, 
	points NCHAR(10) NOT NULL, 
	test_id INT NOT NULL 
);

CREATE TABLE Answer
(
	answer_id INT NOT NULL PRIMARY KEY, 
	question_id INT NOT NULL, 
	answer NCHAR(50) NOT NULL, 
	correct INT NOT NULL 
);
