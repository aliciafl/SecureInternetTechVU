
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
    dateString,dataString=codeString()
    page = 'presentation.html'
    f = open(page,'w')
    # message = """<html>
    # <head></head>
    # <body>
    # <h1>"""+name+"""</h1><ul style="list-style-type:none;">"""+string+"""</ul>
    # </body>
    # </html>"""

    # message="""
    # <head>
    # <meta charset="utf-8">
    # <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    # <meta name="author" content="Made with ❤ by Jorge Epuñan - @csslab">

    # <title>Logs Analysis</title>
    # <link rel="stylesheet" href="style.css" media="screen" />
    # <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
    # <script src="code.js"></script>
    # <script>
    # $(function(){
    # $().timelinr({
    # arrowKeys: 'true'
    # })
    # });
    # </script>
    # </head>

    # <body>

    # <div id="timeline">
    # <ul id="dates">
    # <li><a href="#1">Dec 08</a></li>
    # <li><a href="#2">Dec 09</a></li>
    # <li><a href="#3">Dec 10</a></li>
    # <li><a href="#4">Dec 11</a></li>
    # <li><a href="#4">Dec 12</a></li>
    # </ul>
    # <ul id="issues">
    # <li id="1">
    # <h1>Dec 08</h1>
    # <p>Dec 09</p>
    # </li>
    # <li id="2">
    # <h1>1984</h1>
    # <p>Dec 09</p>
    # </li>
    # </ul>
    # </div>
    # </body>"""

    message="""
    <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="author" content="Made with ❤ by Jorge Epuñan - @csslab">

    <title>Logs Analysis</title>
    <link rel="stylesheet" href="style.css" media="screen" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
    <script src="code.js"></script>
    <script>
    $(function(){
    $().timelinr({
    arrowKeys: 'true'
    })
    });
    </script>
    </head>

    <body>

    <div id="timeline">
    <ul id="dates">"""+str(dateString)+"""
    </ul>
    <ul id="issues">
    """+str(dataString)+"""
    </ul>
    </div>
    </body>"""

    
    f.write(message)
    f.close()
    webbrowser.open_new_tab('/Users/alicia/Mega/SecureInternetTech/SecureInternetTechVU/presentation.html')

def codeString():
    dates=['Dec 13','Dec 14','Dec 15','Dec 16','Dec 17']
    datas=["<p>casa</p>","<p>coche</p>","<p>unai</p>","<p>puto</p>","<p>bobo </p>"]
    dateString=""
    dataString=""
    
    i=0
    for dat in dates:
        dateString=dateString+"""<li><a href="#"""+str(i+1)+"""">"""+str(dat)+"""</a></li>"""
        dataString=dataString+"""<li id="""+'"'+str(i)+'"'+"""><h1>"""+str(dat)+"""</h1>"""+str(datas[i])+"""</li>"""
        i+=1

    return str(dateString),str(dataString)


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
            # print(event)
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
