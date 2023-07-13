import hashlib
import datetime
import logging
import os

logging.basicConfig(filename='file_integrity.log', format='%(message)s', level=logging.INFO)

# Calculate the hash of a file, readings in blocks for better memory efficiency.
def calc_hash(file_path, block_size=65536):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for block in iter(lambda: file.read(block_size), b''):
            hasher.update(block)
    return hasher.hexdigest()

# Scan and record hashes of every file (recursively) within the path argument.
def scan_dirs(path):
    file_hashes = {}

    # Initial scan/mapping of path's files.
    if os.path.isfile(path):
        file_hashes[path] = calc_hash(path)
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    file_hashes[file_path] = calc_hash(file_path)
    else:
        raise FileNotFoundError("Provided path is not a valid file or directory.")
    
    logging.info("-" * 80)
    logging.info(f"{datetime.datetime.now()} - MONITORING IN PROGRESS: {path}")
    logging.info("-" * 80)

    # Continually check path's files for changes
    while True:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    if file_path in file_hashes:
                        # A file's hash has changed from it's previous value.
                        if calc_hash(file_path) != file_hashes[file_path]:
                            logging.info(f"{datetime.datetime.now()}\tFile modified:\t{file_path}")
                            file_hashes[file_path] = calc_hash(file_path)
                    # A file not in the map has been found meaning it was just created.
                    else:
                        logging.info(f"{datetime.datetime.now()}\tFile created:\t{file_path}")
                        file_hashes[file_path] = calc_hash(file_path)
        
        # Check for deleted files
        deleted_files = set(file_hashes.keys()) - set([os.path.join(root, file) for root, dirs, files in os.walk(path) for file in files])
        for deleted_file in deleted_files:
            logging.info(f"{datetime.datetime.now()}\tFile deleted:\t{deleted_file}")
            del file_hashes[deleted_file]

scan_dirs(os.path.expanduser("~/Desktop/"))
