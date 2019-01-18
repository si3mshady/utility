import openpyxl
from weather_data import Brick_Tamland
from pprint import pprint   

class Spreadsheet:
    def __init__(self):
        self.excel_book = self.make_excel_wb()

    def make_excel_wb(self):
        return  openpyxl.Workbook()
    
    def get_sheetnames(self):
        if self.excel_book.sheetnames[0] != "Sheet" or len(self.excel_book.sheetnames) >= 2:
            return self.scribble_sheet()
        else:
            print('Please add sheets to your workbook. ')
            self.add_first_sheet()

    def add_first_sheet(self):
        self.name = input("Please provide a name for the worksheet:> ")
        self.excel_book.create_sheet(index=0 ,title=self.name)  #set user defined workbook to advance get_sheetnames logic
        self.get_sheetnames()
        
    def save_spreadsheet(self):
       self.save_sheet =  input("Save file as:> ")
       self.excel_book.save(self.save_sheet + '.xlsx')
    
    def create_sheet(self,name):        
        self.new_sheet = self.excel_book.create_sheet(index=len(self.excel_book.sheetnames) + 1 ,title=name)
    
    def scribble_sheet(self):       
        for sheetname in self.excel_book.sheetnames:
            print(">> " + sheetname + " <<")
        sheet  = input('Please enter a sheet to edit from the list. ')
        while sheet not in list(self.excel_book.sheetnames):
            sheet  = input('Please enter a sheet to edit from the list. ')
        self.scribble = self.excel_book[sheet]
        cuidad = input('Please enter a city name for a current weather report ')
        self.weather_man = Brick_Tamland(cuidad)
        currently = self.weather_man.weather_report         
        self.scribble['A1'] = currently['location']['name']
        self.scribble['B1'] = currently['location']['localtime']
        self.scribble['C1'] = currently['current']['condition']['text']
        self.scribble['D1'] = currently['current']['feelslike_c']
        self.scribble['E1'] = currently['current']['feelslike_f']        
        self.save_spreadsheet()
        print('Spread saved and updated Weather man is signing off.')

def weather_report():
      weather_man = Spreadsheet()
      weather_man.get_sheetnames()
    
if __name__ == "__main__":
    weather_report()
 
 #Python 3 diy exercies; Inserting data into spreadsheets retrieved from API sources late-night toil, burning the midnight oil  Elliott Arnold 1-18-19

               
            


      
        