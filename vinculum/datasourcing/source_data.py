import os, zipfile
from pathlib import Path
import requests

def unzip_file(zip_path,extract_path):
    '''
    zip path is a pathlib.Path to the zip file
    Extract path is a pathlib.Path to the file to be created/overwritten
    '''
    out_path = Path(extract_path)
    if not os.path.exists(out_path.parent): os.makedirs(out_path.parent)
    with zipfile.ZipFile(zip_path, 'r') as zipped_archive:
        data_file = zipped_archive.namelist()[0]
        zipped_archive.extract(data_file, out_path)  

def download_file(url,dl_fname):
    out_path = Path(dl_fname)
    if not os.path.exists(out_path.parent): os.makedirs(out_path.parent)
    r = requests.get(url, stream=True)
    with open(out_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=30720):
            f.write(chunk)
            f.flush()