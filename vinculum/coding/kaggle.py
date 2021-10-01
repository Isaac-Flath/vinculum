import os
def create_dataset(dataset_path,dataset_name):
    if not os.path.exists(dataset_path): os.makedirs(dataset_path)
    os.system(f"kaggle datasets init -p {dataset_path}")
    with open(dataset_path/'dataset-metadata.json','r') as f: txt = f.readline()
    txt = txt.replace("INSERT_TITLE_HERE",dataset_name)
    txt = txt.replace("INSERT_SLUG_HERE",dataset_name)
    os.system(f"kaggle datasets create -p {dataset_path}")


def download_dataset(dataset_path,dataset_id):
    '''example: kaggle datasets metadata -p /path/to/download zillow/zecon'''
    os.system(f"kaggle datasets metadata -p {dataset_path} {dataset_id}")

def update_datset(dataset_path,update_message):
    os.system(f'''kaggle datasets version -p {dataset_path} -m "{update_message}"''')

def add_library_to_dataset(library,dataset_path,pip_cmd="pip3",):
    os.system(f"{pip_cmd} download {library} -d {dataset_path}")
    print(f"In kaggle kernal you will need to run special command to install from this")
    print(f"!pip install -Uqq {library} --no-index --find-links=file:///kaggle/input/your_dataset/")
