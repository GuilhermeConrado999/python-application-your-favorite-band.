import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect("users_songs.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        fav_song TEXT,
        song_album TEXT,
        band TEXT,
        year TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_user(name, fav_song, song_album, band, year):
    conn = sqlite3.connect("users_songs.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, fav_song, song_album, band, year) VALUES (?, ?, ?, ?, ?)",
                    (name, fav_song, song_album, band, year))
    conn.commit()
    conn.close()
    print(f"USER '{name}' added successfully.")

def get_all_users():
    conn = sqlite3.connect("users_songs.db")
    df = pd.read_sql("SELECT * FROM users", conn)
    conn.close()
    return df

def update_status(user_id, new_year):
    conn = sqlite3.connect("users_songs.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET year = ? WHERE id = ?", (new_year, user_id))
    conn.commit()
    conn.close()
    print(f"YEAR updated for User ID {user_id}.")

def delete_user(user_id):
    conn = sqlite3.connect("users_songs.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print(f"USER id {user_id} deleted.")

def main():
    init_db()
    while True:
        print('''SAVE YOUR FAVORITE SONG!!''')
        print("1️⃣ Your name, song, album and year")
        print("2️⃣ View users")
        print("3️⃣ Update year of album")
        print("4️⃣ DELETE user")
        print("5️⃣ Exit")
        
        choice = input("\nSelect an option: ")

        if choice == "1":
            name = input("Enter user name: ")
            fav_song = input("Enter Your favorite song: ")
            song_album = input("Enter Your favorite album: ")
            band = input("Enter the name of the band: ")
            year = input("Enter year (default: XXXX): ") or "XXXX"
            add_user(name, fav_song, song_album, band, year)

        elif choice == "2":
            print("\n📋 User List:")
            print(get_all_users())

        elif choice == "3":
            user_id = input("Enter Your User ID to update: ")
            new_year = input("Enter new year (1992, 1993, 1994, etc.): ")
            update_status(user_id, new_year)
        
        elif choice == "4":
            user_id = input("enter user id to delete: ")
            delete_user(user_id)

        elif choice == "5":
            print("EXITING YOUR FAVORITE SONG MANAGER, GOODBYE!!")
            break

        else: 
            print("invalid option, try again")

if __name__ == "__main__":
    main()