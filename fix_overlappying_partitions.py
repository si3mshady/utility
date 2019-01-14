#This program  will produce the required DBCheck command needed to remediate Overlapping Partitions on an ESM
#syntax   ./fixPartitions.py  NitroTID.txt 
#The NitroTID output should be from the Alert table using option 4
import subprocess,csv,os,sys,re,fileinput,glob

def CreateRepairString():
   array = array2 = []
   FILE1 = 'raw.txt'
   FILE2 = 'clean.txt'
   startString = "DBCheck -d '/usr/local/ess/data/ngcp.dfl|127.0.0.1|1110' --balance-rewrite --balance-partition-range="
   endString =  "--balance-overlapped-only --balance-rebuild -t Alert -v"
   processString = "grep -A9999 Ove raw.txt | tr -d [aA-zZ.,] | awk '{print $1}' | sort -n | uniq -u > "
   w = open(FILE1,"w")
   for line in fileinput.input(sys.argv[1:]):
      w.write(str(line))
   w.close()
   os.system(processString + FILE2)
   readf = open(FILE2,"r")
   matrix = readf.readlines()
   readf.close()
   writef = open(FILE2, "w")
   for spoon in matrix:
      noSpoon = spoon.replace("\n","")
      array2.append(noSpoon)
   writer = csv.writer(writef)
   writer.writerow(array2)
   writef.close()
   one = subprocess.Popen("cat clean.txt",stdout=subprocess.PIPE,shell=True)
   (out,err) = one.communicate()
   midString = out.rstrip('\n')
   dbc = str(startString + midString + endString)
   print (dbc)

def main():
   CreateRepairString()


if __name__=="__main__":
   main()
#Elliott Arnold aka Si3mShady 5-5-2018         for use on the Mcafee SIEM 