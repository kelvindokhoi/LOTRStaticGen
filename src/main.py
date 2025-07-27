from textnode import *
from htmlnode import *
from static_operations import StaticOperations
from generate_pages_recursive import generate_pages_recursive
import os
import sys
from MACHINE_CONFIG import *

def main():
	public_path = 'public/' if RUNNING_LOCALLY else 'docs/'
	copier = StaticOperations()
	delete_public_and_copy_static_to_public_log = copier.delete_public_and_copy_static_to_public()
	print(delete_public_and_copy_static_to_public_log)
	if len(sys.argv)>=2:
		basepath = sys.argv[1]
	else:
		basepath = '/'
	generate_pages_recursive(basepath,os.path.abspath('content/'),os.path.abspath('template.html'),os.path.abspath(public_path))
main()