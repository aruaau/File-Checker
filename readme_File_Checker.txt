File Checker
This Python script checks if a list of files are available on a server.

Prerequisites
Python 3
requests and tqdm modules (can be installed via pip)
Usage
Create a text file containing a list of URLs for the files you want to check, with one URL per line. For example:

javascript
Copy code
https://example.com/file1.txt
https://example.com/file2.txt
https://example.com/file3.txt
Open a terminal or command prompt and navigate to the directory containing the script.

Run the script using the following command, replacing Links.txt with the name of the file you created in step 1:

Copy code
python3 file_checker.py -s Path_to_Links.txt
The script will output a list of available and unavailable files to the console.
We're assuming you are running cmd in that folder where file_checker python file saved.

Command Line Arguments
The script accepts the following command line argument:

-s, --source: Required. Path to the file containing the URLs for the files to check.
Example
yaml
Copy code
$ python3 file_checker.py -s Links.txt
Processed 3 of 3 files. ETA: 0:00:00.
2 files available:
file1.txt
file2.txt
1 files unavailable:
file3.txt