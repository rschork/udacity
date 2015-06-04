-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
DROP DATABASE IF EXISTS tournaments;

CREATE DATABASE tournament;
\c tournament

CREATE TABLE players(
	pid    SERIAL PRIMARY KEY,
	name   varchar(75) NOT NULL CHECK (name <> '')
);

CREATE TABLE matches(
	p1	integer references players(pid),
	p2	integer references players(pid),
	win	integer references players(pid)
);
