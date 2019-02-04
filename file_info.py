import pathlib,os

def create_file_dictionary(path):
    #use list comprehension to generate a list of files and file sizes
    full_file_path = [str(pathlib.Path(file)) for file in os.scandir(path)]
    file_size_list  = [os.path.getsize(file) for file in full_file_path]
    fullPathSize = dict(zip(file_size_list,full_file_path))
    return fullPathSize

def filter_files_by_size(dictionary,filesize):
    #filter files based file size returning a results set
    matching = {file_size:file_name for (file_size,file_name) in dictionary.items() if file_size > int(filesize)}
    return matching

def main():    
    while True:
        path = input('Please type a path to scan for files. ')
        dir_contents = create_file_dictionary(path)
        filesize = input('Please enter a file size filter (KB) for your results set. ')
        results = filter_files_by_size(dir_contents, filesize)
        print('There are {} files greater than {} KB'.format(results.__len__(),filesize))   #special method __len__ to sum the matching files 
        response = input('Continue? (y/n) ')
        if response.lower() != 'y':
            break
            print('Goodbye!')

if __name__ == "__main__":
    main()

# DIY practice exercises: Fluent Python Ch.2 - Using list and dictionary comprehension to faciliate data processing  Elliott Arnold  Superbowl Sunday Practice 




