import argparse
from formater import MyFormatter
import hashlib 
from typing import Union
import os
from tabulate import tabulate
from datetime import datetime
import stat
import magic # https://github.com/ahupp/python-magic/tree/master


__author__ = 'Natsu'
__version__ = 'v0.1'

# ANSI color codes
class Colors:
    HEADER = '\033[95m'  # Purple
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'    # Reset color
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
class FileInfo: 
    '''A class for retrieving and managing information about specific file. '''
    
    def __init__(self, filepath: Union[os.PathLike, str]) -> None:
        '''
        Initialize the FileInfo object with the specified file path. 
        :param filepath: the path to the file for which information is to be retrieved.
        '''
        self.filepath = filepath
        self.file_info = os.stat(self.filepath)

    def get_filehash (self, algorithm='sha256'):
        '''
        Compute and return the hexadecimal digest of the file using a specified hash algorithm. 
        :param algorithm: the name of the hash algorithm to use (default: 'sha256'). 
        :return the hexadecimal hash digest of the file if computation successfully, None if an error occurs.
        '''
        try: 
            hash_algorithm = hashlib.new(algorithm)
            with open (self.filepath, 'rb') as f: 
                while chunk := f.read(4096):
                    hash_algorithm.update(chunk)
            return hash_algorithm.hexdigest()
        except Exception as e:
            print(f"Error computing hash: {e}")
            return None
        
    def get_filename(self) -> str: 
        '''
        Extracts and returns the filename from the full file path. 
        '''
        return os.path.basename(self.filepath)
    
    def get_created_time(self): 
        '''Retrieves the creation time of the file.'''
        created_time = os.path.getctime(self.filepath)
        return datetime.fromtimestamp(created_time)
    
    def get_modified_time(self): 
        '''Retrieves the last modification time of the file.'''
        modified_time = self.file_info.st_mtime
        return datetime.fromtimestamp(modified_time)
    
    def get_filesize(self): 
        '''Retrieves the size of the file in kilobytes, formatted as a string.'''
        return f'{(self.file_info.st_size / 1024):.4f} kB'
    
    def get_permission(self):
        '''
        https://stackoverflow.com/questions/15055634/understanding-and-decoding-the-file-mode-value-from-stat-function-output
        https://stackoverflow.com/questions/10741580/using-pythons-stat-function-to-efficiently-get-owner-group-and-other-permissio
        '''
        mode = self.file_info.st_mode
        user_read   = 'r' if mode & stat.S_IRUSR else '-'
        user_write  = 'w' if mode & stat.S_IWUSR else '-'
        user_exec   = 'x' if mode & stat.S_IXUSR else '-'
        group_read  = 'r' if mode & stat.S_IRGRP else '-'
        group_write = 'w' if mode & stat.S_IWGRP else '-'
        group_exec  = 'x' if mode & stat.S_IXGRP else '-'
        other_read  = 'r' if mode & stat.S_IROTH else '-'
        other_write = 'w' if mode & stat.S_IWOTH else '-'
        other_exec  = 'x' if mode & stat.S_IXOTH else '-'
        return f'-{user_read}{user_write}{user_exec}{group_read}{group_write}{group_exec}{other_read}{other_write}{other_exec}'
    
    def get_filetype(self):
        # https://github.com/ahupp/python-magic
        f = magic.Magic(mime=True, uncompress=True)
        return f'{f.from_file(self.filepath)}'
            
    def __str__(self) -> str:
        return f'[{Colors.WARNING}!{Colors.ENDC}] - This code is intended solely for coding practice.'
    
def args_parser():
    parser = argparse.ArgumentParser(prog='file',  usage='%(prog)s [options] ...' ,description='This tool are made by N@T54', epilog='Enjoy the moment! :)', formatter_class=MyFormatter)
    parser.add_argument('-p', '--path', metavar='', help='path to the file for which you want to compute the hash.', required=True)
    args = parser.parse_args()
    return args

def main() -> None: 
    args = args_parser()
    if not os.path.exists(args.path): 
        print(f'[!] - Error: File does not exist - {args.path}')
        exit(-1)
    file_info = FileInfo(args.path)
    
    rows = [
        [f'{Colors.OKBLUE}File Name{Colors.ENDC}', file_info.get_filename()],
        [f'{Colors.OKBLUE}File Hash{Colors.ENDC}', file_info.get_filehash()],
        [f'{Colors.OKBLUE}File Type{Colors.ENDC}', file_info.get_filetype()],
        [f'{Colors.OKBLUE}File Size{Colors.ENDC}', file_info.get_filesize()],
        [f'{Colors.OKBLUE}Created Time{Colors.ENDC}', file_info.get_created_time()],
        [f'{Colors.OKBLUE}Modified Time{Colors.ENDC}', file_info.get_modified_time()],
        [f'{Colors.OKBLUE}Permissions{Colors.ENDC}', file_info.get_permission()]
    ]
    print(tabulate(rows, headers="firstrow", tablefmt="fancy_grid"))
    print (str(file_info))
  
if __name__ == '__main__':
    main()
