import os,hashlib,base64,sqlite3

sha256_dictionary = {}
database_file = 'hashed.db'
db = sqlite3.connect(database_file)
global c
c = db.cursor() #database cursor is required to execute commands against the database 
create_database = "CREATE TABLE IF NOT EXISTS hash (hash_id TEXT PRIMARY KEY  NULL, file_name TEXT NULL);"
c.execute(create_database)

def generate_hash():
    hash_alchemy  = hashlib.new('sha256')  #used to generate a SHA256 hash of binary string.
    for file in os.listdir(os.getcwd()):  #iterate through current working dir 
        if file.endswith('.py'):
            with open( str(file), 'rb') as hash_file:
                contents = hash_file.read()
                contents = base64.b64encode(contents) #Encodes binary data into base 64 characters
                hash_alchemy.update(contents)
                hashed_value = hash_alchemy.hexdigest()
            sha256_dictionary[hashed_value] = file  #fills dictionary with key/value pairs {hash:filename}  

def insert_values():
    insert_values = '''INSERT into hash (hash_id,file_name) VALUES (?,?)'''
    for key,value in sha256_dictionary.items():        
        c.execute(insert_values,(key,value))
        print('Inserted -> hash: {} || file: {} into database'.format(key,value))

def select_all():
    select_all = "SELECT * from hash;"  
    result = c.execute(select_all)
    return result.fetchall() 

def begin():        
    generate_hash()      
    insert_values()
    file_names = sha256_dictionary.values()
    print('Please enter the file from the list to view it\'s hash value.\n')
    for file in file_names:
        print(file)
    go = True
    while go:          
        val  = input('Enter \'all\' to select all values from "hash" table. ')    
        if val.lower() == 'all':
           query_result = select_all()
           print(query_result)        
        response = input('Would you like to continue \'y/n\' ?> ')
        if response.lower() != 'y':
            print('Goodbye!')
            go = False 

if __name__ == "__main__":
    begin()

#python 3 practice. Generating sha256 hashes of files and , inserting and retrieving data from sqlite3 database     1-13-19  Elliott Arnold = si3mshady  



    