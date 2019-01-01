##from datetime import datetime
import json 
class Resolv:
        def __init__(self):
                self.list = {}
                
               
        def caseClosed(self,resolved):
                with open("resolvedList.txt","a") as ink:
                        json.dump(resolved,ink)
                print("Resolved task has been written to file sucessfully.\n")
                
 	 
class NTO:
        def __init__(self):
                self.queue = {}

        def memento(self,mode):
                if mode == "add":
                        self.ticket = str(input("Please enter ticket number to add.\n"))
                elif mode == "edit":
                        self.ticket = str(input("Please enter ticket number to edit.\n"))                       
                self.start = str(input("Please enter the Start Date MM/DD/YYYY.\n"))
                self.end = str(input("Please enter the End Date MM/DD/YYYY.\n"))
                self.device = str(input("Description of the device.\n"))
                self.issue = str(input("Enter brief description of issue.\n"))
                self.url = str(input("Enter url or resource used to research this issue.\n"))
                self.newEntry = {"Ticket Number ":self.ticket,"Start Time ":self.start,"Description of device ":self.device,"Description of Issue ":self.issue,"Research links ":self.url,"End Date ":self.end}
                self.queue[self.ticket]= self.newEntry
                self.wq(self.queue)
             
        def wq(self,task):
                with open("taskList.txt","w") as ink:
                        json.dump(task,ink)
                        print("New task has been written to file sucessfully.\n")

        def readTaskList(self):
                try:
                        with open("taskList.txt","r") as file:
                                self.queue = json.load(file)
                                return self.queue
                except FileNotFoundError:
                        self.queue = {}
                        return self.taskList

        def purgeTaskRecord(self,tasklist):
                if len(tasklist) == 0:
                        print("Empty Dictionary Detected.\n")
                        new = NTO()
                        new.memento(mode="add")
                taskNumber = input("Please enter the ticket number to purge.\n")
                deletedTask = str(tasklist.pop(taskNumber,"null"))
                print("Task " + str(deletedTask) + " has been deleted.\n")
                
        def showTasks(self,tasklist):
                if len(tasklist) == 0:
                        print("Empty List. Generating New Task.\n")
                        new = NTO()
                        new.memento(mode="add")
                caseNumber = str(input("Enter Ticket Number.\n"))
                if caseNumber in tasklist:
                        selected = tasklist[caseNumber]
                        for i in selected.keys():
                                print(i + " = " + selected[i])
                else:
                        print("Entry Not Found.\n Please Create a New Entry.\n")
                        new = NTO()
                        new.memento(mode="add")
                        
        def getResolv(self,taskList):
                if len(taskList) == 0:
                        print("The current list is empty. Please create a new task list.\n")
                        new = NTO()
                        new.memento(mode="add")
                self.caseNumber = str(input("Please enter the resolved ticket number.\n"))
                self.resolved = str(taskList.pop(self.caseNumber,"null"))
                self.queue[self.caseNumber] = self.resolved
                return self.queue
                        

def main():
        print("New Case Repo:\n")
        resolv = Resolv()
        nto = NTO()
        while True:
                print("What would you like to do?")
                response  = input("1.) 'New' Task\n2.) 'List' Tasks\n3.) 'Edit' Task\n4.) 'Purge' Task\n5.) 'Resolve Task'\n")
                if response.lower() == "new":
                                  nto.memento(mode="add")
                elif response.lower() == "list":
                                  tasks = nto.readTaskList()
                                  nto.showTasks(tasks)
                elif response.lower() == "edit":
                                  nto.memento(mode="edit")
                elif response.lower() == "purge":
                                  tasks = nto.readTaskList()
                                  nto.purgeTaskRecord(tasks)
                elif response.lower() == "resolved":
                                  tasks = nto.readTaskList()
                                  resolved = nto.getResolv(tasks)
                                  resolv.caseClosed(resolved)
                elif response.lower() == "quit":
                                  print("Goodbye!")
                                  break
                else:
                        continue                                
                        
if __name__ == "__main__":     #learning Python3 MURACH ch.14 Creating Custom Classes OOP  si3mshady aka ElAlquimista  task manager enhanced still WIP   8-21-18   ELAD 
        main()
        
         

