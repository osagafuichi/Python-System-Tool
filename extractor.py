import os

def extractor(given):
    if not os.path.exists(given):
        return None
    
    return {
        "abs_path": given,
        "file_name": os.path.basename(given),
        "file_size": os.path.getsize(given),
        "last_modified": os.path.getmtime(given),
        "extension": os.path.splitext(given)[1],
    }