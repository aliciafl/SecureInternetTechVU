import webbrowser 

# ************************************************************* Generic Functions *************************************************************

def readFile(fileName):
    fileObj = open(fileName, "r")
    lines = fileObj.read().splitlines()
    fileObj.close()
    return lines

def monthsConversion(month):
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    return months[int(month)-1]
 
def generatePage(authDate,kernDate,syslogDate,dpkgDate,authData,kernData,syslogData,dpkgData):
    authDateString,authDataString=codeString(authDate,kernDate,syslogDate,dpkgDate,authData,kernData,syslogData,dpkgData)
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

    f.write(message)
    f.close()
    webbrowser.open_new_tab('presentation.html')

def codeString(authDate,kernDate,syslogDate,dpkgDate,authData,kernData,syslogData,dpkgData):
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    monthsDefs=[]
    value=False
    sameAuth=False
    sameKern=False
    sameSyslog=False
    sameDpkg=False
    dat=""  
    authDatas=""
    kernDatas=""
    syslogDatas=""
    dpkgDatas=""
    dateString=""
    dataString=""

    #Generate array of months
    for month in months:   
        if month == authDate[0].split()[0] or month == kernDate[0].split()[0]:
            value=True   
        if value == True:
            monthsDefs.append(month)
    j=0

    for month in monthsDefs:       
        for i in range(31):   

            k=0
            for auth in authDate:
                dat=auth.split()[1] #Number
                if dat == " ":
                    dat=auth.split()[2]
                if month == auth.split()[0] and str(i) == dat and sameAuth==False:
                    sameAuth=True
                    authDatas=authData[k]   
                    dataString=dataString+"""<li id="""+'"'+str(j)+'"'+""">""" 
                    dataString=dataString+"""<h1>"""+"Auth.log"+"""</h1><br/><div id="logblock">"""+str(authDatas)+"""</div>"""               
                k=k+1
            
            k=0
            for auth in syslogDate:
                dat=auth.split()[1] #Number
                if dat == " ":
                    dat=auth.split()[2]
                if month == auth.split()[0] and str(i) == dat and sameSyslog==False:
                    sameSyslog=True
                    syslogDatas=syslogData[k] 
                    if sameAuth==False:  
                        dataString=dataString+"""<li id="""+'"'+str(j)+'"'+""">""" 
                    dataString=dataString+"""<h1>"""+"Syslog"+"""</h1><br/><div id="logblock">"""+str(syslogDatas)+"""</div>"""               
                k=k+1 
            
            k=0
            for auth in kernDate:
                dat=auth.split()[1] #Number
                if dat == " ":
                    dat=auth.split()[2]
                if month == auth.split()[0] and str(i) == dat and sameKern==False:
                    sameKern=True
                    kernDatas=kernData[k]    
                    if sameAuth==False and sameSyslog==False:
                        dataString=dataString+"""<li id="""+'"'+str(j)+'"'+""">""" 
                    dataString=dataString+"""<h1>"""+"Kern.log"+"""</h1><br/><div id="logblock">"""+str(kernDatas)+"""</div>"""             
                k=k+1

            k=0
            for auth in dpkgDate:
                dat=auth.split()[1] #Number
                if dat == " ":
                    dat=auth.split()[2]
                if month == auth.split()[0] and str(i) == dat and sameDpkg==False:
                    sameDpkg=True
                    dpkgDatas=dpkgData[k]    
                    if sameAuth==False and sameSyslog==False and sameKern==False:
                        dataString=dataString+"""<li id="""+'"'+str(j)+'"'+""">""" 
                    dataString=dataString+"""<h1>"""+"Dpkg.log"+"""</h1><br/><div id="logblock">"""+str(dpkgDatas)+"""</div>"""             
                k=k+1

            if sameAuth==True or sameKern==True or sameSyslog==True or sameDpkg==True:
                dateString=dateString+"""<li><a href="#"""+str(j+1)+"""">"""+month+" "+str(i)+"""</a></li>"""
                dataString=dataString+"""</li>"""
                j=j+1
                sameAuth=False
                sameKern=False
                sameSyslog=False
                sameDpkg=False
            
            
            # dataString=dataString+"""<li id="""+'"'+str(i)+'"'+"""><h1>"""+"Auth.log"+"""</h1><br/><div id="logblock">"""+str(datas)+"""</div></li>"""

        
            
    # i=0
    # for dat in date:
    #     print(dat)
    #     dateString=dateString+"""<li><a href="#"""+str(i+1)+"""">"""+str(dat)+"""</a></li>"""
    #     dataString=dataString+"""<li id="""+'"'+str(i)+'"'+"""><h1>"""+header+"""</h1><br/><div id="logblock">"""+str(data[i])+"""</div></li>"""
    #     i+=1

    return str(dateString),str(dataString)

# **************************************************************** Analize logs ****************************************************************

def analizeLog(firstDate, lastDate, filepath, format):
    events = readFile(filepath) # Read the log
    if format == 1: 
        if firstDate != '' and lastDate != '':                    
            events = filterbyDates(firstDate, lastDate, events) # Filter the events between firstdate and lastdate
        data, date = splitDays(events) # Group events by days
    if format == 2:
        if firstDate != '' and lastDate != '':                    
            events = filterbyDates_format(firstDate, lastDate, events) # Filter the events between firstdate and lastdate (second format
        data, date = splitDays_format(events) # Group events by days (second format)
    return data, date

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
    month = ''
    dayString = ''
    dayArray =[]
    indexArray=[events[0][:6]]
    for event in events:
        if (event.split()[1] != day or (event.split()[0]).capitalize() != month)  and event != events[0]:
            dayArray.append(dayString)
            indexArray.append(event[:6])
            dayString = ''
        day = event.split()[1]
        month = (event.split()[0]).capitalize()
        dayString=dayString+"""<p><strong class="hour">"""+event[7:15]+"</strong> "+event[16:]+"</p>"
        if event == events[-1]:
            dayArray.append(dayString)
            dayString = ''
    return dayArray, indexArray

def filterbyDates_format(firstDate, lastDate, events):
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    newEvents=[]
    firstDay=firstDate.split()[1]
    firstMonth=months.index((firstDate.split()[0]).capitalize())+1
    lastDay=lastDate.split()[1]
    lastMonth=months.index((lastDate.split()[0]).capitalize())+1

    for event in events:
        if int(firstMonth) <= int(event[5:7]) <= int(lastMonth):
            if int(firstMonth) == int(lastMonth):
                if int(firstDay) <= int(event[8:10]) <= int(lastDay):
                    newEvents.append(event)
            else:
                if int(firstMonth) == int(event[5:7]) and int(firstDay) <= int(event[8:10]):
                    newEvents.append(event)
                if int(firstMonth) < int(event[5:7]) < int(lastMonth):
                    newEvents.append(event)
                if int(lastMonth) == int(event[5:7]) and int(lastDay) >= int(event[8:10]):
                    newEvents.append(event)
    return newEvents

def splitDays_format(events):
    day = ''
    dayString = ''
    dayArray =[]
    indexArray=[]
    month_a=''

    for event in events:    #split0 date, split1 hour, split2... rest
        if (event[8:10] != day or month_a != event[5:7]) and event != events[0]:
            dayArray.append(dayString)
            indexArray.append(date)
            dayString = ''
        dayString=dayString+"""<p><strong class="hour">"""+event[11:19]+"</strong> "+event[19:]+"</p>"
        month_a=event[5:7]
        if event[5:6]=='0':
            month_a=event[6]
        month=monthsConversion(int(month_a))
        day=event[8:10]
        if day[0] == '0':
            day_a = day.replace("0","")
        else:
            day_a = day
        date=month+' '+day_a

        if event == events[-1]:
            dayArray.append(dayString)
            indexArray.append(date)
            dayString = ''

    return dayArray, indexArray

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
                                print("Wrong Format, day of range")
                        else:
                            print("Wrong Format, day must be a number")    
                    else:
                        print("Wrong Format, wrong month")  
                else:
                    print("Wrong format, wrong number of arguments (take care with extra spaces)")
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
        firstDate=askDate(True) #Ask and validate the date format
        lastDate=askDate(False)
        invalidDates = compareDates(firstDate, lastDate) #Check if firstDate is previous to lastDate
    authData, authDate = analizeLog(firstDate, lastDate,'logs/auth.log',1) # In Ubuntu '/var/log/auth.log'
    kernData, kernDate = analizeLog(firstDate, lastDate,'logs/kern.log',1) # In Ubuntu '/var/log/kern.log'
    syslogData, syslogDate = analizeLog(firstDate, lastDate,'logs/syslog',1) # In Ubuntu '/var/log/syslog'
    dpkgData, dpkgDate = analizeLog(firstDate, lastDate,"logs/dpkg.log",2) # In Ubuntu '/var/log/dpkg.log'
    generatePage(authDate,kernDate,syslogDate,dpkgDate,authData,kernData,syslogData,dpkgData)
  
if __name__ == "__main__":
    main()