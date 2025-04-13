import requests
import sqlite3
from bs4 import BeautifulSoup
import csv
import os

DB_NAME = "jobs.db"

# Step 1: Create SQLite database and table
def create_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            apply_link TEXT,
            UNIQUE(title, company, location)
        )
    """)
    conn.commit()
    conn.close()

# Step 2: Scrape the job listings
def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    job_elements = soup.find_all("div", class_="card-content")

    for job_elem in job_elements:
        title = job_elem.find("h2", class_="title").text.strip()
        company = job_elem.find("h3", class_="company").text.strip()
        location = job_elem.find("p", class_="location").text.strip()
        description = job_elem.find("div", class_="content").text.strip()
        apply_link = job_elem.find("a", string="Apply")["href"].strip()

        jobs.append((title, company, location, description, apply_link))
    return jobs

# Step 3: Insert or update jobs
def upsert_jobs(jobs):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    for job in jobs:
        title, company, location, description, apply_link = job
        c.execute("""
            SELECT description, apply_link FROM jobs
            WHERE title=? AND company=? AND location=?
        """, (title, company, location))
        result = c.fetchone()

        if result is None:
            # New entry
            c.execute("""
                INSERT INTO jobs (title, company, location, description, apply_link)
                VALUES (?, ?, ?, ?, ?)
            """, job)
        else:
            # Existing entry, check for updates
            old_description, old_link = result
            if description != old_description or apply_link != old_link:
                c.execute("""
                    UPDATE jobs
                    SET description=?, apply_link=?
                    WHERE title=? AND company=? AND location=?
                """, (description, apply_link, title, company, location))
    conn.commit()
    conn.close()

# Step 4: Filter and export to CSV
def export_jobs_to_csv(filter_by=None, filter_value=None, filename="filtered_jobs.csv"):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    query = "SELECT title, company, location, description, apply_link FROM jobs"
    params = ()

    if filter_by == "location":
        query += " WHERE location LIKE ?"
        params = (f"%{filter_value}%",)
    elif filter_by == "company":
        query += " WHERE company LIKE ?"
        params = (f"%{filter_value}%",)

    c.execute(query, params)
    rows = c.fetchall()
    conn.close()

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Title", "Company", "Location", "Description", "Application Link"])
        writer.writerows(rows)
    print(f"Exported {len(rows)} job(s) to {filename}")

# Run everything
if __name__ == "__main__":
    create_db()
    jobs = scrape_jobs()
    upsert_jobs(jobs)

    # Example usage of export function
    export_jobs_to_csv(filter_by="location", filter_value="California", filename="california_jobs.csv")
    export_jobs_to_csv(filter_by="company", filter_value="SovTech", filename="sovtech_jobs.csv")
