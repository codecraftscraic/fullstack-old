#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    #Connect to the PostgreSQL database.  Returns a database connection.
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    #Remove all the match records from the database.
    DB = connect()

    cursor = DB.cursor()

    cursor.execute('DELETE FROM Matches;')
    cursor.commit()

    cursor.close()

def deletePlayers():
    #Remove all the player records from the database.
    DB = connect()

    cursor = DB.cursor()

    cursor.execute('DELETE FROM Players;')
    cursor.commit()

    cursor.close()

def countPlayers():
    #Returns the number of players currently registered.
    DB = connect()

    cursor = DB.cursor()

    cursor.execute('SELECT COUNT(*) DISTINCT FROM Players;')

    cursor.close()

def registerPlayer(name):
    #Adds a player to the tournament database.
  
    #The database assigns a unique serial id number for the player.  (This
    #should be handled by your SQL database schema, not in your Python code.)
  
    #Args:
    #  name: the player's full name (need not be unique).
    DB = connect()

    cursor = DB.cursor()

    cursor.execute('INSERT INTO Players values (name);')
    cursor.commit()

    cursor.close()

def playerStandings():
    #Returns a list of the players and their win records, sorted by wins.

    #The first entry in the list should be the player in first place, or a player
    #tied for first place if there is currently a tie.

    #Returns:
    #  A list of tuples, each of which contains (id, name, wins, matches):
    #    id: the player's unique id (assigned by the database)
    #    name: the player's full name (as registered)
    #    wins: the number of matches the player has won
    #    matches: the number of matches the player has played
    DB = connect()
    playersarray = []

    cursor = DB.cursor()
    
    playersarray = cursor.execute('SELECT *, (WINS + LOSSES) AS MATCHES FROM Players ORDER BY WINS ASC;')

    cursor.close()

    return playersarray

def reportMatch(winner, loser):
    #Records the outcome of a single match between two players.

    #Args:
    #  winner:  the id number of the player who won
    #  loser:  the id number of the player who lost
    DB = connect()
    rows = []

    cursor = DB.cursor()

    cursor.execute('INSERT INTO Matches values (' + winner + ',' + loser ');')
    cursor.commit()

    cursor.execute('SELECT PID, WINS, LOSSES FROM Players WHERE PID = ' + winner + ' OR ' + loser + ';')
    rows = cursor.fetchall()

    #check returned PIDs against winner and loser IDs
    if rows[0][0] == winner && rows[1][0] == loser:
        wins = rows[0][1] + 1
        cursor.execute('UPDATE Players WHERE PID = ' + winner + 'SET WINS = ' + wins + ';')
        cursor.commit()

        losses = rows[1][2] + 1
        cursor.execute('UPDATE Players WHERE PID = ' + loser + 'SET LOSSES = ' + losses + ';')
        cursor.commit()
    else:
        wins = rows[1][1] + 1
        cursor.execute('UPDATE Players WHERE PID = ' + winner + 'SET WINS = ' + wins + ';')
        cursor.commit()

        losses = rows[0][2] + 1
        cursor.execute('UPDATE Players WHERE PID = ' + loser + 'SET LOSSES = ' + losses + ';')
        cursor.commit()

    cursor.close()
 
def swissPairings():
    #Returns a list of pairs of players for the next round of a match.
  
    #Assuming that there are an even number of players registered, each player
    #appears exactly once in the pairings.  Each player is paired with another
    #player with an equal or nearly-equal win record, that is, a player adjacent
    #to him or her in the standings.
  
    #Returns:
    #  A list of tuples, each of which contains (id1, name1, id2, name2)
    #    id1: the first player's unique id
    #    name1: the first player's name
    #    id2: the second player's unique id
    #    name2: the second player's name
    DB = DB.connect()
    cursor = DB.cursor()
    playersarray = []
    matchesarray = []
    roundarray = []

    #get player info from players, and store in an array
    cursor.execute('SELECT PID,NAME,WINS FROM Players ORDER BY WINS DESC')
    playersarray = cursor.fetchall()

    count = 0
    while 


    #get previous matches, and store in array
    cursor.execute('SELECT * FROM Matches');
    matchesarray = cursor.fetchall();

    #randomize players and return matches (for help: http://stackoverflow.com/questions/7225906/forming-random-pairs-from-a-list-sort-of)
    def player_matches (playersarray, matchesarray):
        matches = list(matchesarray);

        #where the players' wins are the same, put in separate arrays
        #go through the arrays of players one at a time, randomize, check, re-randomize if needed, else push to roundarray


        valid_match = false

        while not valid_match:
            random.shuffle(players)
    
    #function
    #check new matches to matches table
    #if matches have been played, return false
    #/function

    #if false, re-randomize
    #repeat until matches are set
    
    #once matches are set, send PID1, Name1, PID2, Name2 to array, and commit to matches and player tables
    #return array

    return roundarray;