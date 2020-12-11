def readFile(fileName):
       fileObj = open(fileName, "r")
       lines = fileObj.read().splitlines()
       fileObj.close()
       return lines

def authlog():
    auth = input("Do you want to analyze auth.log? [Y/N]")
    if auth == "Y" or auth == "y" or auth=="yes" or auth=="Yes" :
        events = readFile("/var/log/auth.log")
        authstr=""
        for event in events:
            authstr=authstr+"<li>"+event+"<li>"
        return authstr
    else:
        return ""

 
def generatePage(authstr):
   import webbrowser
   f = open('helloworld.html','w')
 
   message = """<html>
   <head></head>
   <body>
   <h1>Auth.log</h1><ul style="list-style-type:none;">"""+authstr+"""</ul>
   </body>
   </html>"""
 
   f.write(message)
   f.close()
 
   #Change path to reflect file location
   filename = '/home/alicia/Desktop/FinalWork/' + 'helloworld.html'
   webbrowser.open_new_tab(filename)
 
 

def main():
    authstr=authlog()
    generatePage(authstr)
    
if __name__ == "__main__":
    main()
