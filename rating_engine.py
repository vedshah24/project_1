import sqlite3

def calculate_performance_index(goals, assists, appearances):
    # This is the 'Weighted Logic'
    # We give more importance to goals, then assists
    raw_score = (goals * 5) + (assists * 3)
    
    # Avoid division by zero if a player hasn't played yet
    if appearances == 0:
        return 0
        
    index = (raw_score / appearances) * 10 # Scaling it to a score out of 100
    return round(min(index, 100), 2) # Cap it at 100 and round to 2 decimals

def fetch_and_rate_players():
    conn = sqlite3.connect('vault.db')
    cursor = conn.cursor()
    
    # Fetch all stats
    cursor.execute("SELECT name, goals, assists, appearances FROM players")
    players = cursor.fetchall()
    
    print("--- Player Performance Report ---")
    for p in players:
        name, g, a, app = p
        score = calculate_performance_index(g, a, app)
        print(f"Player: {name} | Goals: {g} | Assists: {a} | Rating: {score}/100")
    
    conn.close()

if __name__ == "__main__":
    fetch_and_rate_players()