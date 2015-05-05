import os
import datetime, time

# This script opens a command line interface that will provide the users with project-specific
# sample counts produced by the LS 13-320 Laser Diffraction Particle Size Analyzer

# Separate counts are provided for QC samples and Actual samples
# QC samples are detected by all caps CONTROL in the sample ID
# If there are Actual samples that have 'control' in the sample ID, make sure 'control'is entered lower case



#######PROJECT SPECIFIC PARAMETERS#######

folder = r"C:/..../"
# Main directory in which all daily folders are stored
# This script assumes folders will be created for each day with a mM_dD_YY format
# Example: April 14 2015: 4_14_15

Project_Total = 656
# Set your project sample total here
Samples_per_day = 30
# Set your anticipated daily throughput here
# SLEEP = 4
# Default refresh time (seconds) for daily counts
# Still implementing sleep feature - may need threading to simulataneously accept raw_input
# and 
#########################################



raw = []
refresh = ''

def mostRecent(f):
# This function finds the most recently created $av file in the current day's folder
    for x,y,z in os.walk(f):
        for item in z:
            if item.endswith("$av"):           
                yield os.path.join(x,item)


def searchIt(term_):
# This function allows the user to search for a folder name from the command line interface
    n=0
    print 'search results for %s:' % term_
    print
    for x,y,z in os.walk(folder):
        for item in z:
            if item.endswith("$av"):
                if term_.lower() in item.lower():
                    print os.path.join(x,item).split("/")[-1].replace("\\", ": ")[:-9]
                    # This line splits the date from the file name and removes the extra characters at the end
                    n+=1
    if n == 0:
        print "no results found"
        print
        
    userprompt()
    # Return to user prompt


def getAll():
# This function allows the user to see counts of all of the project samples processed to date
# it also estiamtes time remaining

    Actual = 0
    Control = 0
    Total = 0

 

    for x,y,z in os.walk(folder):
        for item in z:
            if item.endswith("$av"):
                Total+=1
                if "control" in item.lower():
                    Control +=1
                else: Actual += 1
    # The above for loop tallies all samples in the project folder            

    print
    print "Project Totals: "
    print 
    print "Actual: %i" %Actual
    print "Control: %i" %Control
    print "Total: %i" %Total
    print "Remaining: %i" %(Project_Total - Actual)
    daysR = (float(Project_Total) -Actual) / float(Samples_per_day)
    print
    print "Estimated days remaining: %s" % '{:.1f}'.format(daysR)
    # Formatted to guess remaining days to one decimal
    print

         

    userprompt()
    # Return to user prompt

    
def getCounts():
# This function tells the user the counts for the current day
# It detects the current date and searches the corresponding folder for $av files
# Reminder - folders must be in mM_dD_YY format

    if len(raw)>1:
        date = raw
    else:
        i =datetime.datetime.now()

        date = "%s_%s_%s" %(i.month, i.day, str(i.year)[-2:])
        

    print "Samples processed today (%s):" %date

                                   

    path = folder + date

    Actual = 0
    Control = 0
    Total = 0

    for x,y,z in os.walk(path):
        for item in z:
            if item.endswith("$av"):
                Total+=1
                if "CONTROL" in item:
                    Control +=1
                else: Actual += 1
    print
    
    print "Actual: %i" %Actual
    print "Control: %i" %Control
    print "Total: %i" %Total
    print
    print "Most recently processed sample: %s" %max(mostRecent(path), key=os.path.getmtime).split("\\").pop()[:-9]
    print

    userprompt()
    # Return to user prompt

  
def userprompt():
# This is the prompt that appears after a function is run, it uses logical conditionals
# to excecute a specific function based on the contents of the raw_input variable 'refresh'
    
    
##    def repeater():
##        TC = int(time.time())
##        refresh = raw_input("")
##        while refresh == "":
##            
##            if int(time.time()) == TC + SLEEP:
##                print "DFSFDSRFE"
##                os.system('cls')
##                getCounts()
##    repeater()
    # This refreshes the daily counts every n seconds as defined by SLEEP
    

    print 
    print "enter " + "'" + "t" + "'" + " to see project totals"
    print "enter a sample name to search project folders"
    print
    print

    refresh = raw_input("")
    os.system('cls')
    if len(refresh) == 0:
        os.system('cls')

        getCounts()
    
    
    print
    
    # clears the terminal so that previous results are not displayed

        
    if refresh.lower() == "t":
        getAll()
    else: searchIt(refresh)
    
    
    
    
getCounts()
# When the program is first opened, the function for counting the current day's samples is run





