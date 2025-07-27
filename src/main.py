from textnode import *
from htmlnode import *
from static_operations import StaticOperations
from generate_pages_recursive import generate_pages_recursive
import os
import sys

def main():

	if len(sys.argv)>=2 and (basepath:=sys.argv[1])!='/':
		RUNNING_LOCALLY = False
	else:
		basepath = '/'
		RUNNING_LOCALLY = True
	public_path = 'public/' if RUNNING_LOCALLY else 'docs/'
	copier = StaticOperations(RUNNING_LOCALLY)
	delete_public_and_copy_static_to_public_log = copier.delete_public_and_copy_static_to_public()
	print(delete_public_and_copy_static_to_public_log)
	generate_pages_recursive(basepath,os.path.abspath('content/'),os.path.abspath('template.html'),os.path.abspath(public_path))
main()