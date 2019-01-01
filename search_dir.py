import os,re,zipfile
from PIL import Image
from pytesseract import image_to_string

'''Quick script that will back up files of given extension and file path '''

def search_parse_zip(path,file_extension,backup_file_name):
    is_match = []
    for dirpath, dirname, filename in os.walk(path):
        for file in os.listdir(dirpath):
            if file.endswith(file_extension):
                is_match.append('{0}/{1}'.format(dirpath,file))   
                              
    for file in is_match:
        with zipfile.ZipFile(backup_file_name, 'w') as Z:
            Z.write(file)
            print('{} has been written to archive '.format(file))  
    
def zipFiles():
    options  = ['Target Directory:','File Extension:','Backup File Name:']
    resp = [] 
    for opt in options:
        user_response = input('Please enter {} '.format(opt))
        resp.append(user_response)
    print(str(resp))
    search_parse_zip(str(resp[0]),str(resp[1]),str(resp[2]))
    


if __name__ == '__main__':
    zipFiles()
#utility script to search, parse and compress files of certain file extension non-binary  by Elliot Arnold     12-30-18  


