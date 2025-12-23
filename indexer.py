import os
import database
from extractor import extractor

def index(address):
    conn = database.connect()
    database.create_table(conn)

    for root, dirs, files in os.walk(address):
        for filename in files:
            full_path = os.path.join(root, filename)

            metadata = extractor(full_path)
            if metadata is None:
                continue

            stored_ts = database.get_file(conn, metadata["abs_path"])

            if stored_ts is None:
                database.insert_file(conn, metadata)
            elif stored_ts != metadata["last_modified"]:
                database.update_file(conn, metadata)


