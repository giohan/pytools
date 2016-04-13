import fnmatch
import os
import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument('-r','--root', 
		    required=True,
		    help='The root dir to search in',
		    default='/')
parser.add_argument('-p','--pattern', 
                    required=True,
		    help='Define the pattern to search for')
args = parser.parse_args()

rootDir = args.root
pattern = args.pattern

for root, dirs, files in os.walk(rootDir):
    for filename in fnmatch.filter(files, pattern):
        print( os.path.join(root, filename))
