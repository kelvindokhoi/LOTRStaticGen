from textnode import *
from htmlnode import *
from static_operations import StaticOperations
from generate_pages_recursive import generate_pages_recursive
import os


def main():
	copier = StaticOperations()
	delete_public_and_copy_static_to_public_log = copier.delete_public_and_copy_static_to_public()
	print(delete_public_and_copy_static_to_public_log)
	generate_pages_recursive(os.path.abspath('content/'),os.path.abspath('template.html'),os.path.abspath('public/'))
main()