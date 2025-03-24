import sqlite3

# Create a new SQLite database and establish a connection
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# Define the Roster table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# Insert data into the Roster table
cursor.executemany("""
INSERT INTO Roster (Name, Species, Age)
VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

# Update the name of Jadzia Dax to Ezri Dax
cursor.execute("""
UPDATE Roster
SET Name = "Ezri Dax"
WHERE Name = "Jadzia Dax"
""")

# Retrieve and display the Name and Age of all Bajoran characters
cursor.execute("""
SELECT Name, Age FROM Roster WHERE Species = "Bajoran"
""")
print("Bajoran Characters:")
for row in cursor.fetchall():
    print(row)

# Remove all characters aged over 100 years
cursor.execute("""
DELETE FROM Roster WHERE Age > 100
""")

# Add a new column called Rank to the Roster table
cursor.execute("""
ALTER TABLE Roster ADD COLUMN Rank TEXT
""")

# Update the new Rank column with values
cursor.executemany("""
UPDATE Roster SET Rank = ? WHERE Name = ?
""", [
    ("Captain", "Benjamin Sisko"),
    ("Lieutenant", "Ezri Dax"),
    ("Major", "Kira Nerys")
])

# Retrieve all characters sorted by Age in descending order
cursor.execute("""
SELECT * FROM Roster ORDER BY Age DESC
""")
print("\nCharacters sorted by Age (descending):")
for row in cursor.fetchall():
    print(row)

# Commit changes and close the connection
conn.commit()
conn.close()
