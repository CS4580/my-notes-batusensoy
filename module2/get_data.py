"""Download data from our server
"""

import requests
import shutil
import os

SERVER_URL= 'http://icarus.cs.weber.edu/~hvalle/cs4580/data/'



def download_file(url, file_name):
    # TODO: Download to pwd

    # TODO: Check extension from file name, if it is zip 
    # Call unzip_file(data01)
    # unzip_file(data01)
    pass

def unzip_file(file_name):
    # TODO: unzip file
    pass

def main():
    """Driven Function
    """
    data01 = 'pandas01Data.zip'
    download_file(SERVER_URL, data01)


if __name__ == '__main__':
    main()