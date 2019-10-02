log_file = open("um-server-01.txt") #save file um-server-01.txt to log_file


def sales_reports(log_file):    #a function that takes in the log file
    for line in log_file:       #step through every line in the log file
        line = line.rstrip()    #"rstrip" with each line **remove whitespace from right**
        day = line[0:3]         #store the first 3 chars of line in day 
        if day == "Mon":        #check if day is Tue
            print(line)         #print the whole line if it is


sales_reports(log_file)         #execute the function
