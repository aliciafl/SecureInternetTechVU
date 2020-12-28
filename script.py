import webbrowser 
 
def generatePage(date,data):
    dateString,dataString=codeString(date,data)
    page = 'presentation.html'
    f = open(page,'w')

    message="""
    <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="author" content="Made by Alicia and Unai">
    <title>Logs Analysis</title>
    <link rel="stylesheet" href="css/style.css" media="screen" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
    <script src="js/code.js"></script>
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
    <footer><img src="images/VUlogo.png" alt="VUlogo" width="20%" height="auto"><p>©️ Alicia Fernández and Unai Ruiz</p></footer>
    </body>"""

    
    f.write(message)
    f.close()
    webbrowser.open_new_tab('presentation.html')

# **************************************************************** Auth.log ****************************************************************

# HTML

def codeString(date,data):
    dateString=""
    dataString=""
    
    i=0
    for dat in date:
        dateString=dateString+"""<li><a href="#"""+str(i+1)+"""">"""+str(dat)+"""</a></li>"""
        dataString=dataString+"""<li id="""+'"'+str(i)+'"'+"""><h1>Auth.log</h1><br/><div id="logblock">"""+str(data[i])+"""</div></li>"""
        i+=1

    return str(dateString),str(dataString)

# Logic

def authLog(startDate):
    # splittedAuthEvents = [] # Array which elements are a string formed by all events in each day [day1, day2, day3, ...]
    authEvents = readFile("logs/auth.log") # In Ubuntu '/var/log/auth.log'                    
    authEvents = firstDate(startDate, authEvents)
    splittedAuthEvents,dayArray = splitDays(authEvents)   # En un futuro hacer return de los arrays
    authStr = addFformat(authEvents)
    return splittedAuthEvents,dayArray

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
    indexArray=[events[0].split()[0]+' '+events[0].split()[1]]
    for event in events:
        if event.split()[1] != day and event != events[0]:
            dayArray.append(dayString)
            indexArray.append(event.split()[0]+' '+event.split()[1])
            dayString = ''
        day = event.split()[1]
        dayString=dayString+"""<p><strong class="hour">"""+event.split()[0]+' '+event.split()[1]+":</strong> "+event.split(' ',3)[3]+"</p>"
        if event == events[-1]:
            dayArray.append(dayString)
            dayString = ''
    return indexArray,dayArray

def addFformat(events):
    string=""
    for event in events:
        string=string+"<li>"+event+"</li>"
    return string
 
# **************************************************************** Faillog ****************************************************************




# ***************************************************************** Dates *****************************************************************

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

# ****************************************************************** Main ******************************************************************

def main():
    startDate='Dec 8'
    date,data = authLog(startDate)
    generatePage(date,data)
  
if __name__ == "__main__":
    main()