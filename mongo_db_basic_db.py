from pymongo import MongoClient
from datetime import datetime 
import glob

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
                print('Collection: {} is selected!\n'.format(collection_name))
                return current_collection
        except:
                print('Creating new collection: ')
                new_collection_name=input('Name your collection: ')
                current_collection=mongo_database[new_collection_name]
                print('Collection: {} is selected!'.format(new_collection_name))
                return current_collection        

def find_files(pattern):
        pattern='*' + pattern
        matching=glob.glob(pattern)
        return matching

def make_document():    
    pattern=input('Please enter a pattern to match files: ')
    matching=find_files(pattern)
    while len(matching) == 0: #no files found matching the pattern 
            print("No matching files found: ")
            pattern=input('Please enter a pattern to match files:\n')
            matching=find_files(pattern)
    print(matching)  
    file_name=input('Please type the filename of the file to be inserted into the database: ')
    while file_name not in matching:
            file_name=input('Please type the filename of the file to be inserted into the database: ')
    with open(file_name,'rb') as read_me:
        binary_data=read_me.read() #read in a stream of bytes - required or will get error  data must be an instance of bytes 
    time_stamp=datetime.now()
    data_to_input=binary_data
    name_of_file=input('Please enter a value for the "filename" key to be inserted into a dictionary: ')
    document={'filename':name_of_file,'data':binary_data,'time_stamp':time_stamp}
    return document

def insert_document(document,current_collection):
        id_reference=current_collection.insert_one(document).inserted_id
        print('Insert job complete: ')

def count_documents(current_collection):
        count=current_collection.count_documents({})
        print('This collection has {} documents:\n'.format(count))

def main():
        while True:
                selected_database=init_mdb()
                collection_name=input('Please enter a collection name: ')
                current_collection=get_collection(selected_database,collection_name) 
                count_documents(current_collection)             
                document=make_document()                
                insert_document(document,current_collection)
                cont=input('Would you like to continue? "y/n": ')
                if cont.lower() != 'y':
                        print("Goodbye!")
                        break

if __name__=="__main__":
        main()                
#Learning the basics of MongoDB with pymondo- Inserting Binary objects into a database  4-3-19
