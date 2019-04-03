from pymongo import MongoClient
from datetime import datetime 

def init_mdb():
    database_name=input('Enter Database Name: ')
    mongo_db_client=MongoClient()   #instantiate db cursor 
    selected_database=create_new_db(database_name,mongo_db_client)
    return selected_database

def create_new_db(new_database,mongo_db_client):
        database_list=list_databases(mongo_db_client)
        if new_database not in database_list:
                active_db=mongo_db_client[new_database]
                print('{} has been created: '.format(new_database))
                print('{} is online: '.format(new_database))
                return active_db
        else:
                active_db=mongo_db_client[new_database]
                print('{} is online : '.format(new_database))
                return active_db      

def list_databases(mongo_database_client):
    db_names=[mdb for mdb in mongo_database_client.list_database_names()]   
    return db_names

def get_collection(mongo_database,collection_name):        
        try:
                current_collection=mongo_database[collection_name]
                print('Collection: {} is selected!\n'.format(current_collection))
                return current_collection
        except:
                print('Creating new collection: ')
                new_collection_name=input('Name your collection: ')
                current_collection=mongo_database[new_collection_name]
                print('Collection: {} is selected!'.format(current_collection))
                return current_collection        

def make_document(filename):
        time_stamp=datetime.now()
        data_to_input=None
        name_of_file=filename
        document={'filename':name_of_file,'data':data_to_input,'time_stamp':datetime.now()}
        return document

def insert_document(document,current_collection):
        id_reference=current_collection.insert_one(document).inserted_id
        print('Insert job complete: ')

def main():
        while True:
                selected_database=init_mdb()
                collection_name=input('Please enter a collection name: ')
                current_collection=get_collection(selected_database,collection_name)
                file_name=input('Please enter a value for the "filename" key to be inserted into a dictionary: ')
                document=make_document(file_name)                
                insert_document(document,current_collection)
                cont=input('Would you like to continue? "y/n": ')
                if cont.lower() != 'y':
                        print("Goodbye!")
                        break

main()                

