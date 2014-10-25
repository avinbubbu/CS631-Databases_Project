""" Queries are of the form
	Select[space]attributes-list(seperated by comma)[space]From[space]filename[space]Where[space]selected-lists[EOL]
	Select[space]attributes-list.filenames(seperated by comma)[space]From[space]filenames(seperated by comma)[space]Where[space]selected-lists.filenames[EOL]
	create table department(string deptname,string building,int budget);
	insert into department values('Computerscience',’Kresit’, 4);	
"""
import os.path

def select_query(Query):
	print("came to select")
	Querysplit1     = Query.split(' ')
	attributes     = Querysplit1[1].split(',')
	filenames      = Querysplit1[3].split(',')
	selected_lists = Querysplit1[5].split(',')

def create_query(Query):
	print("came to create_query")
	Querysplit = Query.split('(',1)
	firstpart = Querysplit[0].split(' ')
	filename=firstpart[2]
	#for index in range(len(firstpart)):
	#	print(firstpart[index])
	secondpart = Querysplit[1].split(')')
	stringadd =secondpart[0]
	boolenval=os.path.isfile(filename)
	if boolenval:
		print("file already exits")
	else:
		file = open(filename,'w')
		file.write(stringadd)
		file.close()

	#secondpart = Querysplit[1].split(',')	
	#partsplit=secondpart[len(secondpart)-1].split(')')
	#secondpart[len(secondpart)-1]=partsplit[0]
	#for index in range(len(secondpart)):
	#	print(secondpart[index])

def insert_query(Query):
	print("came to insert_query")
	Querysplit = Query.split('(',1)
	firstpart = Querysplit[0].split(' ')
	filename=firstpart[2]
	secondpart = Querysplit[1].split(')')
	stringadd =secondpart[0]
	boolenval=os.path.isfile(filename)
	if boolenval:
		file=open(filename,'a')
		file.write("\n"+ stringadd)
		file.close()
	else:
		print("file doesn't exist")


def delete_query(Query):
	print("came to select")
def join_query(Query):
	print("came to select")
def NaturalJoin_query(Query):
	print("came to select")



print("Enter the Query:")
Query=input();
Querysplit = Query.split(' ')

if Querysplit[0] == "create":
	create_query(Query)
elif Querysplit[0] == "insert":
	insert_query(Query)
elif Querysplit[0] == "delete":
	delete_query(Query)
elif Querysplit[0] == "Select":
	select_query(Query)
else :
	select_query(Query)

