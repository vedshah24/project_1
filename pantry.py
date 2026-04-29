import sqlite3

def init_pantry():
    # Connects to (or creates) the new database file
    connection = sqlite3.connect('vault.db')
    cursor = connection.cursor()

    # We are defining a more complex table here
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            team TEXT,
            goals INTEGER DEFAULT 0,
            assists INTEGER DEFAULT 0,
            appearances INTEGER DEFAULT 1
        )
    ''')

    # Let's seed it with some initial data
    players_to_add = [
        ('Bruno Fernandes', 'Manchester United', 10, 15, 30),
        ('Marcus Rashford', 'Manchester United', 8, 5, 28),
        ('Alejandro Garnacho', 'Manchester United', 7, 4, 25)
    ]

    # This 'INSERT' logic is cleaner for multiple items
    cursor.executemany('''
        INSERT INTO players (name, team, goals, assists, appearances) 
        VALUES (?, ?, ?, ?, ?)
    ''', players_to_add)

    connection.commit()
    connection.close()
    print("Project_1 Pantry Initialized with 3 players!")

if __name__ == "__main__":
    init_pantry()