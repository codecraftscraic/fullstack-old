-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE Players {
	PID INT PRIMARY KEY NOT NULL autofill unsigned,
	FNAME CHAR(60) NOT NULL,
	LNAME CHAR(60) NOT NULL,
	WINS INT unsigned,
	LOSSES INT unsigned,
}

CREATE TABLE Matches {
	MID INT PRIMARY KEY NOT NULL autofill unsigned,
	TID INT FOREIGN KEY NOT NULL,
	--WinnerID stores PID from Participants Table
	WinnerID INT FOREIGN KEY NOT NULL,
	--LoserID stores PID from Participants Table
	LoserID INT FOREIGN KEY NOT NULL,
}

CREATE TABLE Tournaments {
	TID INT PRIMARY KEY NOT NULL autofill unsigned,
	MID INT FOREIGN KEY NOT NULL,
	--TournWinner stores PID of tournament winner from Participants Table
	TournWinner INT FOREIGN KEY NOT NULL,
}