from textnode import *
from htmlnode import *
from static_operations import StaticOperations




def main():
	copier = StaticOperations()
	delete_public_and_copy_static_to_public_log = copier.delete_public_and_copy_static_to_public()
	print(delete_public_and_copy_static_to_public_log)
main()