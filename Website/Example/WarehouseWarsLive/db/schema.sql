--- load with 
--- sqlite3 database.db < schema.sql

CREATE TABLE users (
	id VARCHAR(20) UNIQUE,
	password VARCHAR(20),
	name VARCHAR(20),
	email VARCHAR(30),
	gender VARCHAR(10),
	highestScore INTEGER default 0
);

insert into users values('test','test','mikhail','mikhail@mail.com','male',0);


