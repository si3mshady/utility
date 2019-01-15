from PIL import Image
import pyqrcode 

def instructions():
    print('\nThis program will generate Quick Response codes from the input you provide while saving and displaying them to screen.\n')

def the_Prestige(string,filename):
    result = pyqrcode.create(string)
    result.png(filename, scale = 10)
    prestige = Image.open(filename)
    prestige.show()

def abracadabra_QRC():
    instructions()
    abracadabra = True 
    while abracadabra:
        qrc =  input('Please enter a string to generate a QR code:> ')
        file = input('Save QR code as:> ')
        the_Prestige(qrc,file)
        response = input('Would you like to continue? \'y/n\':> ')
        if response.lower() != 'y':
            print('Goodbye!')
            abracadabra = False

if __name__ == '__main__':
    abracadabra_QRC()

#exploring python3 libraries:  Creating QR codes with 'pyqrcode':  diy   1-14-19  Elliott Arnold 

    
