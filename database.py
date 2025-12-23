import sqlite3

def connect():
    conn = sqlite3.connect('my_database.db')
    return conn

def create_table(conn):
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Metadata (
        abs_path TEXT PRIMARY KEY, 
        file_name TEXT,
        file_size INTEGER, 
        last_modified FLOAT, 
        extension TEXT
    );'''
    cursor.execute(create_table_query)
    conn.commit()

def get_file(conn, abs_path):
    cursor = conn.cursor()
    query = "SELECT last_modified FROM Metadata WHERE abs_path=?"
    cursor.execute(query, (abs_path,))
    absp = cursor.fetchone()
    if absp!= None:
        return(absp[0])
    else:
        return None

def insert_file(conn, metadata):
    cursor = conn.cursor()
    query = "INSERT INTO Metadata (abs_path, file_name, file_size, last_modified, extension) VALUES (?, ?, ?, ?, ?)"
    data = (
        metadata["abs_path"],
        metadata["file_name"],
        metadata["file_size"],
        metadata["last_modified"],
        metadata["extension"]
    )
    cursor.execute(query, data)
    conn.commit()

def update_file(conn, metadata):
    cursor = conn.cursor()
    query = "UPDATE Metadata SET file_name=?, file_size=?,last_modified=?, extension=? WHERE abs_path=?"
    data = (
        metadata["file_name"],
        metadata["file_size"],
        metadata["last_modified"],
        metadata["extension"],
        metadata["abs_path"],
    )
    cursor.execute(query, data)
    conn.commit()
def search_files(conn, name, extension=None, min_size=None, max_size=None, sort_by="name"):

    cursor = conn.cursor()
    sort_map = {
        "name": "file_name",
        "size": "file_size",
        "date": "last_modified"
    }
    order_column = sort_map.get(sort_by, "file_name")
    
    query = f"""
    SELECT abs_path, file_name, extension, file_size, last_modified
    FROM Metadata
    WHERE file_name LIKE ?
    """
    params = [f"%{name}%"]

    if extension:
        query += " AND extension = ?"
        params.append(extension)

    if min_size:
        query += " AND file_size >= ?"
        params.append(min_size)

    if max_size:
        query += " AND file_size <= ?"
        params.append(max_size)

    query += f" ORDER BY {order_column}"


    cursor.execute(query, tuple(params))
    return cursor.fetchall()
