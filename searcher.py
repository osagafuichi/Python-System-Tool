import database
from datetime import datetime

def search(name, extension=None, min_size=None, max_size=None, sort_by="name"):

    conn = database.connect()
    results = database.search_files(
        conn,
        name,
        extension,
        min_size,
        max_size,
        sort_by
    )



    if not results:
        print("No results found.")
        return

    for abs_path, file_name, ext, size, last_modified in results:
        print(
        f"{file_name} | "
        f"{format_size(size)} | "
        f"{format_time(last_modified)} | "
        f"{abs_path}"
        )


def format_size(bytes_size):
    if bytes_size < 1024:
        return f"{bytes_size} B"
    elif bytes_size < 1024 ** 2:
        return f"{bytes_size / 1024:.1f} KB"
    else:
        return f"{bytes_size / (1024 ** 2):.1f} MB"


def format_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M")
