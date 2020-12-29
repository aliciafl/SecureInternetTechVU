import webbrowser 


#line 1 prueba

#line 2 prueba 


def generatePage(date,data):
    authDateString,authDataString=codeString(date,data,'syslog')
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
    <ul id="dates">"""+str(authDateString)+"""
    </ul>
    <ul id="issues">
    """+str(authDataString)+"""
    </ul>
    </div>
    <footer><img src="images/VUlogo.png" alt="VUlogo" width="20%" height="auto"><p>©️ Alicia Fernández and Unai Ruiz</p></footer>
    </body>"""

    f.write(message.encode('cp850','replace').decode('cp850')) # print(data.decode('utf-8').encode('cp850','replace').decode('cp850'))
    f.close()
    webbrowser.open_new_tab('presentation.html')

# **************************************************************** Auth.log ****************************************************************

# HTML

def codeString(date,data,header):
    dateString=""
    dataString=""
    
    i=0
    for dat in date:
        dateString=dateString+"""<li><a href="#"""+str(i+1)+"""">"""+str(dat)+"""</a></li>"""
        dataString=dataString+"""<li id="""+'"'+str(i)+'"'+"""><h1>"""+header+"""</h1><br/><div id="logblock">"""+str(data[i])+"""</div></li>"""
        i+=1

    return str(dateString),str(dataString)

# Logic

def analizeLog(firstDate, lastDate, filepath):
    events = readFile(filepath) 
    if firstDate != '' and lastDate != '':                    
        events = filterbyDates(firstDate, lastDate, events)
    data, date = splitDays(events)   # En un futuro hacer return de los arrays
    return data, date

def readFile(fileName):
    fileObj = open(fileName, "r")
    lines = fileObj.read().splitlines()
    fileObj.close()
    return lines

def filterbyDates(firstDate, lastDate, events):
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    newEvents=[]
    for event in events:
        if (months.index((firstDate.split()[0]).capitalize()) <= months.index(event.split()[0])) and (months.index((lastDate.split()[0]).capitalize()) >= months.index(event.split()[0])):
            if (months.index((firstDate.split()[0]).capitalize()) == months.index((lastDate.split()[0]).capitalize())):
                if (int(firstDate.split()[1]) <= int(event.split()[1]) <= int(lastDate.split()[1])):
                    newEvents.append(event)
            else:
                if (months.index((firstDate.split()[0]).capitalize()) == months.index(event.split()[0])) and (int(firstDate.split()[1]) <= int(event.split()[1])):
                    newEvents.append(event)
                if (months.index((firstDate.split()[0]).capitalize()) < months.index(event.split()[0]) < months.index((lastDate.split()[0]).capitalize())):
                    newEvents.append(event)
                if (months.index((lastDate.split()[0]).capitalize()) == months.index(event.split()[0])) and (int(lastDate.split()[1]) >= int(event.split()[1])):
                    newEvents.append(event)
    return newEvents

def splitDays(events):
    day = ''
    dayString = ''
    dayArray =[]
    indexArray=[events[0][:6]]
    for event in events:
        if event.split()[1] != day and event != events[0]:
            dayArray.append(dayString)
            indexArray.append(event[:6])
            dayString = ''
        day = event.split()[1]
        dayString=dayString+"""<p><strong class="hour">"""+event[7:15]+"</strong> "+event[16:]+"</p>"
        if event == events[-1]:
            dayArray.append(dayString)
            dayString = ''
    return dayArray, indexArray

# **************************************************************** Faillog ****************************************************************




# ***************************************************************** Dates *****************************************************************

def askDate(first):
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    invalidDate = True
    spaceNumber = 0
    while invalidDate:
        if first == True:
            date = input("Introduce the desired first day in the following format: mmm dd (left blank if no filter desired) :")
        else:
            date = input("Introduce the desired last day in the following format: mmm dd (left blank if no filter desired) :")
        for i in date:
            if i == ' ':
                spaceNumber += 1
        if (date==''):
            invalidDate = False
        else:
                if spaceNumber == 1 and len(date.split()) == 2:
                    if (date.split()[0].capitalize() in months):
                        if ((date.split()[1]).isnumeric()):
                            if(0 < int(date.split()[1]) < 32):
                                invalidDate = False
                            else:
                                print("Wrong Format dia fuera de rango")
                        else:
                            print("Wrong Format dia tiene que ser un numero")    
                    else:
                        print("Wrong Format mes incorrecto")  
                else:
                    print("Wrong format - wrong number of arguments (take care with extra spaces)")
                spaceNumber = 0
    return date

def compareDates(firstDate, lastDate):
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    if firstDate == "" or lastDate == "":
        return False
    if (months.index((firstDate.split()[0]).capitalize()) == months.index((lastDate.split()[0]).capitalize())):
        if (int(firstDate.split()[1]) <= int(lastDate.split()[1])):
            return False
        else:
            print("Start date must be previous than last date.")
            return True
    if (months.index((firstDate.split()[0]).capitalize()) <= months.index((lastDate.split()[0]).capitalize())):
        return False
    else:
        print("Start date must be previous than last date.")
        return True


# ****************************************************************** Main ******************************************************************

def main():
    invalidDates = True
    while invalidDates:
        firstDate=askDate(True)
        lastDate=askDate(False)
        invalidDates = compareDates(firstDate, lastDate)
    # authData, authDate = analizeLog(firstDate, lastDate,'logs/auth.log') # In Ubuntu '/var/log/auth.log'
    # kernData, kernDate = analizeLog(firstDate, lastDate,'logs/kern.log') # In Ubuntu '/var/log/kern.log'
    sysData, sysDate = analizeLog(firstDate, lastDate,'logs/syslog') # In Ubuntu '/var/log/syslog'
    generatePage(sysDate, sysData)
  
if __name__ == "__main__":
    main()