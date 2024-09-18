"""Download data from our server
"""

import requests
import shutil
import os, sys
import zipfile

SERVER_URL= 'http://icarus.cs.weber.edu/~hvalle/cs4580/data/'

def extract_zip_file(zip_path):
    """Extract a ZIP file to the current working directory

    Args:
        zip_path (str): ZIP file absolute path
    """

    print(f"Extracting {zip_path}")
    # Get the current working directory
    extract_path = os.getcwd()

    # Open the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Extract all the contents to the current working directory
        zip_ref.extractall(extract_path)
        print(f"File unzipped successfully and extracted to {extract_path}")
        # List the extracted files
        print(f"Extracted files: {zip_ref.namelist()}")
    # Delete the zip file
    os.remove(zip_path)
    
# TODO: Create a function to download the files from Kaggle directly ny passing data name

def download_zip_file(url):
    """Download a ZIP file from a URL and save ot to a local file.

    Args:
        url (url): File URL to download
    """
    # Get the current working directory
    dest_path = os.path.join(os.getcwd(), os.path.basename(url))

    # Send a GET request to the URL
    response = requests.get(url, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        # Open the destination file in write_binary mode
        with open(dest_path, 'wb') as out_file:
            # Copy the response content to the destination file
            shutil.copyfileobj(response.raw, out_file)
        print(f"File downloaded successfully and saved to {dest_path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

    # Check file extension. If it is a ZIP file, extract it
    if dest_path.endswith('.zip'):
        extract_zip_file(dest_path)

def main():
    """Driven Function
    """
    # If no arguments are provided, print a usage message
    if len(sys.argv) < 2:
        print("Usage: python download_data.py <data_file>")
        sys.exit(1)

    # data01 = f'{SERVER_URL}/pandas01Data.zip'
    # take data file as input parameter
    data_file = sys.argv[1]
    print(f"Data file: {data_file}")
    data01 = f'{SERVER_URL}/{data_file}'
    download_zip_file(data01)

    # data02 = f'{SERVER_URL}/pandas02Data.zip'
    # download_zip_file(data02)

    #TODO: Set input user options to extract file
    # from different sources: -url, -kaggle



if __name__ == '__main__':
    main()