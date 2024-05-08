# FileInfo
## Description:
This Python utility class is designed to gather comprehensive details about a specific file. It retrieves essential file attributes including the filename, cryptographic `file_hash`, `file_type`, `file_size`, `created_time`, `modified_time`, and `permissions`. 
## Usage:

```console
(env) PS C:\User\user01\src> python .\file.py -p practicecplus.exe
╒═══════════════╤══════════════════════════════════════════════════════════════════╕
│ File Name     │ practicecplus.exe                                                │
╞═══════════════╪══════════════════════════════════════════════════════════════════╡
│ File Hash     │ ad38650671b4493873b2f47e5dd9331d607bc5144fdb9f18754bb1f997f63a03 │
├───────────────┼──────────────────────────────────────────────────────────────────┤
│ File Type     │ application/x-dosexec                                            │
├───────────────┼──────────────────────────────────────────────────────────────────┤
│ File Size     │ 95.0000 kB                                                       │
├───────────────┼──────────────────────────────────────────────────────────────────┤
│ Created Time  │ 2024-04-30 22:09:10.553612                                       │
├───────────────┼──────────────────────────────────────────────────────────────────┤
│ Modified Time │ 2024-05-06 22:28:20.719599                                       │
├───────────────┼──────────────────────────────────────────────────────────────────┤
│ Permissions   │ -rwxrwxrwx                                                       │
╘═══════════════╧══════════════════════════════════════════════════════════════════╛
[!] - This code is intended solely for coding practice.
```
