#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("TRUNCATE matches CASCADE;")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("TRUNCATE players CASCADE;")
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT count(pid) FROM players;")
    count = c.fetchone()
    conn.commit()
    conn.close()
    return int(count[0])


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s);", (name,))
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT a.pid as id, a.name as name, coalesce(b.wins,0) as wins, \
        coalesce(d.count_p2,0) + coalesce(c.count_p1,0) as matches \
        FROM players as a\
        LEFT JOIN \
        (SELECT win, count(win) AS wins FROM matches GROUP BY win \
            ORDER BY wins) as b ON a.pid=b.win\
        LEFT JOIN \
        (SELECT p1, count(p1) as count_p1 FROM matches GROUP BY p1)\
         as c ON a.pid=c.p1\
        LEFT JOIN \
        (SELECT p2, count(p2) as count_p2 FROM matches GROUP BY p2)\
         as d ON a.pid=d.p2\
        ORDER BY wins DESC")
    standings = c.fetchall()
    conn.commit()
    conn.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO matches VALUES (%s, %s, %s)",
              (winner, loser, winner))
    conn.commit()
    conn.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT id1,name1,id2,name2 FROM (SELECT z.id as id1, z.name as name1,\
                lead(z.id) over (ORDER BY wins DESC) as id2, \
                lead(z.name) over (ORDER BY wins DESC) as name2, \
                row_number() over (ORDER BY wins DESC) as rank FROM \
                (SELECT a.pid as id, a.name as name, \
                    coalesce(b.wins,0) as wins, \
                coalesce(d.count_p2,0) + coalesce(c.count_p1,0) as matches \
                FROM players as a\
                LEFT JOIN \
                (SELECT win, count(win) AS wins FROM matches \
                    GROUP BY win ORDER BY wins) as b ON a.pid=b.win\
                LEFT JOIN \
                (SELECT p1, count(p1) as count_p1 FROM matches GROUP BY p1)\
                 as c ON a.pid=c.p1\
                LEFT JOIN \
                (SELECT p2, count(p2) as count_p2 FROM matches GROUP BY p2)\
                 as d ON a.pid=d.p2\
                ORDER BY wins DESC) as z) as w \
                where name2 <> '' and mod(rank,2) = 1")
    pairings = c.fetchall()
    conn.commit()
    conn.close()
    return pairings
