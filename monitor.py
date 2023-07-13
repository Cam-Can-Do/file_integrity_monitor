import hashlib
import datetime
import logging
import os

logging.basicConfig(filename='file_integrity.log', format='%(message)s', level=logging.INFO)

def calc_hash(file_path, block_size=65536):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for block in iter(lambda: file.read(block_size), b''):
            hasher.update(block)
    return hasher.hexdigest()

def scan_dirs(path):
    file_hashes = {}

    if os.path.isfile(path):
        file_hashes[path] = calc_hash(path)
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    file_hashes[file_path] = calc_hash(file_path)
    
    logging.info("\n")
    logging.info("MONITORING IN PROGRESS")
    logging.info("-" * 30)

    while True:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    if file_path in file_hashes:
                        if calc_hash(file_path) != file_hashes[file_path]:
                            logging.info(f"File modified - {datetime.datetime.now()} - {file_path}")
                            file_hashes[file_path] = calc_hash(file_path)
                    else:
                        logging.info(f"File added - {datetime.datetime.now()} - {file_path}")
                        file_hashes[file_path] = calc_hash(file_path)
        
        # Check for deleted files
        deleted_files = set(file_hashes.keys()) - set([os.path.join(root, file) for root, dirs, files in os.walk(path) for file in files])
        for deleted_file in deleted_files:
            logging.info(f"File deleted - {datetime.datetime.now()} - {deleted_file}")
            del file_hashes[deleted_file]

scan_dirs(os.path.expanduser("~/Desktop/"))
