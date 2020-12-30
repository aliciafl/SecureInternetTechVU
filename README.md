# SecureInternetTechVU

Hi! 👋🏼 This is the final project of Alicia Fernández and Unai Ruiz of the Secure Internet Technologies course of the year 2020 at the Faculty of Mathematics and Informatics of the Vilnius University.

The project consists in an event timeline drawing based on some **/var/log** contents. The result of the project is the piece of script that analyses the logs bellow and produces an html with the representation of events happening on the system over the time.


## About the project

To analyze those log files a script written in **Python** is used. 

The script has a feature of asking the user for the first and last date to define the interval that he wants to analyze. This is an optional functionality and if you want to analyze all the content of the logs without filtering by date, you can leave the answer blank.

### Date format
The inserted dates must have the following format: *Month with the first three letters, space and the day of the month (without 0 on the left)*. Examples: Jan 23, Sep 3, Nov 15

As mentioned, the format is validated in such a way that if it is not respected, it will be asked again. In addition, it is also checked that the start date is prior to the end. 

### Algorithm operation
The content of the files is then read, filtered by date range, if these have been chosen by the user. Next, two arrays are generated ...

### Supported logs

 - **Auth.log**
All authentication related events in Debian and Ubuntu server are logged here. This log can be used to investigate brute-force attacks and other vulnerabilities related to user authorization mechanism.

 - **Kern.log**
This is a very important log file as it contains information logged by the kernel.    This log is perfect for troubleshooting kernel related errors and warnings.

 - **Dpkg.log**
This log is extremely detailed as it includes each of the stages that a package managed by dpkg goes through. It mostly helps to keep a history of the development of the system: one can find the exact moment when a package was installed or updated, and this information can be extremely useful when trying understand a recent behavior change.

 - **Syslog**
It shows general messages, except of type auth, and info regarding the system. Basically a data log of all activity throughout the global system. 

*For convenience, some examples of these files have been included in the project, but if we wanted to apply it to the analysis of the real logs in Linux, we would have to put the path correctly in the code, in particular in the "main" function.


## Credits

 - Timeline https://codetea.com/a-simple-horizontal-timeline/
 - Linux Log files. https://www.eurovps.com/blog/important-linux-log-files-you-must-be-monitoring/
 - Linux Log files. https://debian-handbook.info/browse/es-ES/stable/sect.manipulating-packages-with-dpkg.html
 - Linux Log files. https://askubuntu.com/questions/26237/difference-between-var-log-messages-var-log-syslog-and-var-log-kern-log




<p align="center">
<img width="300" src="https://www.vu.lt/site_images/new_og/logo_lt.png">
</p>