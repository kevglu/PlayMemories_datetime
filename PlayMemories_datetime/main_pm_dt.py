"""Main module."""

from pathlib import Path
import os

def german2Ymd(mypath:Path, format:str)->str:
    """Converts lowest level folder in a path to Ymd

    Args:
        mypath (Path): a path ending in xx.xx.xxxx

    Returns:
        str: a string of format YYYYMMDD
    """
    from datetime import datetime
    root_date = datetime.strptime(os.path.basename(mypath), '%d.%m.%Y').date()
    # from IPython import embed; embed()
    if format is None:
        return root_date.strftime('%Y%m%d')
    else:
        return root_date.strftime(format)

def getNewPath(root_path:Path, suffix):
    """Yields the new folder name

    Args:
        root_path (Path): A path of old format
        suffix (str): New lowest level folder name

    Returns:
        _type_: _description_
    """
    return Path(os.path.split(root_path)[0]+'\\'+suffix)

def renameFolders(myfolder:Path, format:str):
    import re
    r = re.compile('[0-3][0-9]\\.[0-1][0-9]\\.[0-9]*')
    for root, dirs, files in os.walk(myfolder):
        # if folder name matches the regEx
        if r.match(root[-10:]) is not None:
            root_path = Path(root)
            root_date_str = german2Ymd(root_path,format)
            target_path = getNewPath(root_path,root_date_str)
            print(f'From {root_path} to {target_path}')
            if os.path.exists(target_path):
                print(f'Path {target_path} already exists. Abort.')
                continue
            os.rename(root_path,target_path)
    print('Finished renaming.')

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-r','--root', help='Root folder containing the folders to rename', required=True)
    parser.add_argument('--format', help='Custom format of folder names. Default= \"%Y%m%d\"',required=False)
    args = parser.parse_args()
    renameFolders(myfolder=args.root, format = args.format)

if __name__ == "__main__":
    main()