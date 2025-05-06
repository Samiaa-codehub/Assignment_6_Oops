###### Constructor and Destructor ######
#Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class logger:
    #Constructer
    def __init__(self):
        print("logger object has been created")
    #Deconstructer
    def __del__(self):
        print("logger object has been destroyed")
#create an object of logger class
logger1 = logger()
#del the object explicity to invoke the destructor
del logger1
