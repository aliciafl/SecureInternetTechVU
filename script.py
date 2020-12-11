
import webbrowser 

def askDate():
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    invalidDate = True
    while invalidDate:
        date = input("Introduce the desired first day in the following format: mmm dd (left blank if no filter desired) :")
        if date.isspace:
            if (date=='') or (date.split(' ')[0] not in months) or ((date.split(' ')[1]).isnumeric and (0 < int(date.split(' ')[1]) < 32)) :
                invalidDate = False
            else:
                print("Wrong Format")
        else:
            print("Wrong Format")     
    return date
 
def generatePage(string):
    name = 'it1'
    page = name+'.html'
    f = open(page,'w')
    message = """<html>
    <head></head>
    <body>
    <h1>"""+name+"""</h1><ul style="list-style-type:none;">"""+string+"""</ul>
    </body>
    </html>"""
    f.write(message)
    f.close()
    webbrowser.open_new_tab(page)

def authLog(startDate):
    # splittedAuthEvents = [] # Array which elements are a string formed by all events in each day [day1, day2, day3, ...]
    authEvents = readFile("auth.log") # In Ubuntu '/var/log/auth.log'                    
    authEvents = firstDate(startDate, authEvents)
    splittedAuthEvents = splitDays(authEvents)   # En un futuro hacer return de los arrays
    authStr = addFformat(authEvents)
    return authStr

def readFile(fileName):
    fileObj = open(fileName, "r")
    lines = fileObj.read().splitlines()
    fileObj.close()
    return lines

def firstDate(date, events):
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    newEvents=[]
    for event in events:
        if (int(date.split()[1]) <= int(event.split()[1])) and (months.index(date.split()[0]) <= months.index(event.split()[0])):
            print(event)
            newEvents.append(event)
    return newEvents

def splitDays(events):
    day = ''
    dayString = ''
    dayArray =[]
    for event in events:
        if event.split(' ')[1] != day:
            dayArray.append(dayString)
            dayString = ''
        day = event.split(' ')[1]
        dayString=dayString+"<li>"+event+"<li>"
        if event == events[-1]:
            dayArray.append(dayString)
            dayString = ''
    return dayArray

def addFformat(events): #a la mierda
    string=""
    for event in events:
        string=string+"<li>"+event+"</li>"
    return string
 
def main():
    startDate='Dec 8'
    authStr = authLog(startDate)
    generatePage(authStr)
  
if __name__ == "__main__":
    main()


# def authlog(logName):
#     auth = input("Do you want to analyze "+logName+"? [Y/N]")
#     if auth == "Y" or auth == "y" or auth=="yes" or auth=="Yes" :
#         return True
#     else:
#         return False


# def filterEvents(events):
#     return events
