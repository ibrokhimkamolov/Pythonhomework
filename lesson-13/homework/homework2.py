import sqlite3

# Create a new SQLite database and establish a connection
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Define the Books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
""")

# Insert data into the Books table
cursor.executemany("""
INSERT INTO Books (Title, Author, Year_Published, Genre)
VALUES (?, ?, ?, ?)
""", [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
])

# Update the Year_Published of 1984 to 1950
cursor.execute("""
UPDATE Books
SET Year_Published = 1950
WHERE Title = "1984"
""")

# Retrieve and display the Title and Author of all Dystopian books
cursor.execute("""
SELECT Title, Author FROM Books WHERE Genre = "Dystopian"
""")
print("Dystopian Books:")
for row in cursor.fetchall():
    print(row)

# Remove all books published before the year 1950
cursor.execute("""
DELETE FROM Books WHERE Year_Published < 1950
""")

# Add a new column called Rating to the Books table
cursor.execute("""
ALTER TABLE Books ADD COLUMN Rating REAL
""")

# Update the new Rating column with values
cursor.executemany("""
UPDATE Books SET Rating = ? WHERE Title = ?
""", [
    (4.8, "To Kill a Mockingbird"),
    (4.7, "1984"),
    (4.5, "The Great Gatsby")
])

# Retrieve all books sorted by Year_Published in ascending order
cursor.execute("""
SELECT * FROM Books ORDER BY Year_Published ASC
""")
print("\nBooks sorted by Year Published (ascending):")
for row in cursor.fetchall():
    print(row)

# Commit changes and close the connection
conn.commit()
conn.close()