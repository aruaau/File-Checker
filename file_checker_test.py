import os
import requests
from tqdm import tqdm
import argparse

# parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--source", help="path to file with URLs", required=True)
args = parser.parse_args()

# read file URLs from text file
with open(args.source, 'r') as f:
    file_urls = f.read().splitlines()

# check if each file exists on server
available_files = []
unavailable_files = []
with tqdm(total=len(file_urls)) as pbar:
    for file_url in file_urls:
        try:
            response = requests.head(file_url, timeout=10)
        except:
            response = None
        if response and response.status_code == 200:
            available_files.append(os.path.basename(file_url))
        else:
            unavailable_files.append(os.path.basename(file_url))
        pbar.update(1)
        pbar.set_description(f'Processed {len(available_files) + len(unavailable_files)} of {len(file_urls)} files. ETA: {pbar.format_dict.get("remaining", "?")}')

# output results to console
print(f'{len(available_files)} files available:')
for filename in available_files:
    print(filename)
print(f'{len(unavailable_files)} files unavailable:')
for filename in unavailable_files:
    print(filename)
print("\nThanks for using the Script, Hope you have a great Day! - Arihant")