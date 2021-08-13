# **Project-2 - Practical Project**

## **Introduction**

The Goal of this project was to create an application that would generate "objects" from a set of pre-defined criteria. These objects could be anything we wanted however the app was to use  service-orientated architecture and be comprised of at least 4 services working together. 

<details>
  <summary>Service Breakdown</summary>

### Service #1
The core service - this was to render all of the templates needed to interact with the application. It was also responsible for communicating with the other 3 services and persisting information in the database. 

### Service #2 + #3
These both generated "objects" that were sent to service 4

### Service #4
This final service would create a new "object" based on the information passed to it from service 2 and 3. 

</details>
<br>
The goal of this project is to demonstrate some of the key aspects of our learning so far. 
Some of those aspects are:
- project management ability
- effective use of the python coding language
- the effective use of version control systems like Git
- the use of the Agile principles
- the use of the continuous design/integration models
- the effective use of databases

By displaying these aspects of my learning I hope to show a working knowledge of the Agile and DevOps principles and a competence in complimentary skills. 
<br/>
<br/>
<br/>

## **Design Process**
<br/>

**1 - The Brainstorm**<br/>
The first thing in my design process is to brainstorm ideas, review them then filter out the weak ones until I land on one to take forward. <br/>
Through this process I came up with 5 viable Ideas that I weighed up the pros and cons for which helped my whittle them down to one. 
The first and second ideas were based around playing cards. One being a blackjack hand reviewer and the other being a poker hand reviewer. 
<br/>
<br/>
I ultimately ended dropping these two, as dealing with cards would take more coding than necessary, as the focus of this project was more on the architecture implementation and less on the application's complexity. <br/>
<br/>
The 3rd idea had a very similar issue to the first and second, that being overcomplexity of coding. I had planned on making a countdown style application where the **service2** would generate 1-4 vowels and **service3** would generate up to 8 consonants, which on it's own wouldn't be hard, however evaluating the presence of words inside that string of characters would require an extremely large pre-populated database which is waaay out of the scope of this project. 
<br/>
<br/>
The 4th was a top contender which only lost out to the eventual winner on account of its lack of complexity. This Idea was a lottery machine where **service2** would generate 3 numbers and **service3** would generate a further 4 numbers. *service 4** would then put those 2 together in ascending order, generate its own 7 number string and compare the 2. If they matched, you won if not, you lost.
<br/>
<br/>
The idea I ultimately ended up running with was a mini battle simulator.  **service 2** would generate an enemy with a randomly selected name, attack rating and defence rating. **service 3** would generate a player with a randomly selected name, attack rating and defence rating. And finally **service 4** would add up the attack and defence of each service and compare them. if the player's score was higher, you win if not, you lose. I liked this idea over the others because it seemed to have the right amount of complexity to show off my python skills, but not enough to have me bogged down in the inner workings of it. 
<br/>
<br/>
<br/>

**2 - The Tracker**<br/>
After landing on an idea suitable to pursue, I took to Jira to whip up a timetable and add user stories. I chose Jira because I had great success with it in the previous project, however this time I didn't make the same mistake as last time and went with the Kanban approach off the bat.<br/>
At the beginning of my project the Kanban board looked like this;
<br/>
<br/>
![Jira1](https://i.imgur.com/8BZZvJX.png)
<br/>
<br/>
But as the project matured I added more tasks and user stories as potential new functionality came to me. 
In the end the board was more filled out and had many more tasks included in. There was also an out of scope list for a future sprint should I have the opportunity to do one. 
<br/>
<br/>
![Jira2](https://i.imgur.com/RTUpjQy.png)
<br/>
<br/>

**3 - The Plans**<br/>
Once I had the project tracking taken care of it was time to whip up some EDs and other diagrams to illustrate how everything was all going to work together. 
This stage is very important as in making these I can weed out some of the potential issues I may run into before I write a line of code. Following the example of my last project I mapped out my ED first as that took my attempts to get right originally, and was key in the discovery of the main flaw in my last project's design. 
<br/>
I drafted my ED board in Lucid first as that seemed the easiest to map out quickly.  
<br/>
<br/>
![ED1](https://i.imgur.com/J62nYcq.png)
<br/>
<br/>
After that it was back to Lucid again to map out CI/CD pipeline to follow.
<br/>
<br/>
![CICD1](https://i.imgur.com/LSh4NJa.png)
<br/>
<br/>
Second last on the list is to map out my services. This allows at a glance comprehension of the basic service flow occurring between user and backend. 
<br/>
<br/>
![services](https://i.imgur.com/plKwUlQ.png)
<br/>
<br/>
The last thing to map was my interactions diagram.<br/>
I had never made this before however as it was a visual representation of what was going on in my app it was easy to picture it and using Lucid again, document it. <br/>
<br/>
Infrastructure Diagram;<br/>
<br/>
![infd1](https://i.imgur.com/DgFCCQ9.png)

I had originally planned on having my sql instance contained in a container also however this would have lead to unnessasary work and yeilding no great benifits so I instead opted for this disign in the end
<br/>
<br/>
![infd2](https://i.imgur.com/aa2IsA3.png)
<br/>
<br/>
Building these really reinforced my understanding of my project and the innerworkings of it, making the physical coding of the app and it's infrastructure quick and easier. 
<br/>
<br/>

**4 - Disaster Avoidance**<br/>
No good planning stage would be complete without a risk assessment Fortunately the risk assessment I did for my first project was very relevant so I was able to use and add to it for this project. 
Below is the updated risk assessment;
<br/>
<br/>
![riskass](https://i.imgur.com/swbbuQH.png)
<br/>
<br/>
Risk assessments are extremely important in the prediction, evasion and mitigation of issues that can and will come up. Unfortunately it is impossible to avoid all issues so getting the upper hand on them can significantly reduce the impact they have on a project or development process, <br/>

*"Forewarned is forearmed!"*<br/>
Abraham Tucker, 1768
<br/>
<br/>
<br/>

## **Application**
<br/>
With the planning stages all completed, the application followed quickly behind it. Thankfully the app it's self wasn't to complicated and I was able to knock its main functionality out before I had even managed to deploy it, which was very reassuring when I finally got it up on docker. 
<br/>
The application its self looks like this;
<br/>
<br/>

![tour](https://i.imgur.com/o8smX5g.png)
<br/>
<br/>

**1 - Player's stats**
This area is the players stats and is generated by service 1 sending a get request to service 2 and receiving a list containing 3 attributes; name, attack and defence the routes.py passes this information into the main.html page which uses jinga 2 syntax to display the information.<br/>
<br/>

**2 - Opponent's stats**
This functions exactly the same as section 1 however his is service 3 that provides the name, attack and defence scores this time. Then service 1 passes the results to the main.html which displays it.<br/>

<br/>

**3 - Results**
This functions similar to sections 1 and 2 however this time it also takes in some data in the form of the attack and defence scores of you and your opponent. When it receives these numbers it adds them up and compares them to each other to determine which is higher. If yours is the same or higher than your opponents, you win. If not you lose. 
The result is sent back to service 1 which again, passes it to main.html which displays it for you.

**4 - Match History**
For this service 1 sends a request to the database for all results limited to the most recent 5 and passes that in nested list format to main.html which then uses a for loop to display the information 

<details>
  <summary>An un annotated image can been viewed here</summary>
  

![apptour2](https://i.imgur.com/AVaOY1j.png)

</details>


<br/>
<br/>
<br/>

## **Jenkins**

The implementation of Jenkins in this project was much more hands on than in Project-1 however I was also able to get more out of it this time. 
I was able to use Jenkins to test, configure, build and deploy my app via use of a webhook from Github. Meaning anytime I make a push to Github it will automatically pull those changes down, test, build and deploy the app including them. 
Using Jenkins in this way allowed the building process to run much smoother as I didn't need to do it all by hand. 
It also enabled me to obtain insights into my build history and details of why builds failed. 

Here is a graph showing the build history. 
Key:
x = build numbers 
y = time to fully build 
RED = failed builds
Grey = canceled builds
BLUE = successful builds.

![jb1](https://i.imgur.com/xJUs2iz.png)

As you can see there were A LOT of failed builds, however as it reaches then end the builds are more frequently successful as things started coming together. 

<br/>
To aid me with debugging when things went wrong I used the logs section in the Jenkins pipeline; <br/>
<br/>

![jb2](https://i.imgur.com/E16yqm8.png)
<br/>
<br/>
To trouble shoot the issue and as it brakes everything down in chunks It was easy to locate the issues when they occurred. <br/>
Another benefit of using Jenkins pipeline to build my application was that it stopped building if the current step encounters a problem. This is extremely useful as it helps prevent broken code reaching the live environment. 
<br/>
I also used Jenkins to deploy automatically run my unit testing for my app. <br/>
Unit testing is extremely important do a DevOps development process as it keeps the project running on track while the app is being built. <br/>
Using additional add-ons such as Pytest-cov I was able to make sure all of my app was being covered by my testing and that the tests were successful. 
<br/>

![pytest](https://i.imgur.com/tDaAvCu.png)
<br/>
<br/>
Carrying out these tests helped me to spot mistakes I had made in my code that would have otherwise gone unnoticed until I attempted to deploy the application at which point I would have wasted all the build time and would need to check back over everything to find the issue. 
<br/>
Unit testing decreases makes Time Till Discovery(TTD),  the whole process just that much easier and a lot less frustrating. 
<br/>
<br/>

## **Programs, applications and installs**

During the development of my project and its dependencies I have used a verity of different tools some of which I have already spoken about. 

<details>
  <summary>Here is a breakdown of the majority of the tools I utilized</summary>

it shows what tools I used and where I used them form the major elements of the projects. Below that is a more detailed breakdown of the elements, why they were used and the likelihood of using them again based on my experience with them throughout this project. 

<details>
  <summary>Source Code</summary>
  

## Python
I chose python as my source code to fulfill the requirements of the project as it is the language I have the most knowledge of and ability in.  It was also a good choice doe to its extensive use in the industry and as a result has many guide, information sites and knowledge bases to help during the development process. 
In choosing python I was also able to utilize some of its modules both built in and external
Some of the modules I used were:
- Flask - This is a python driven micro framework which enables easy design and construction of web applications.
- Pytest - This allows for unit testing to occur enabling the length and breadth of a project to be tested with 1 line of code. 
- Requests - This allows for interactions with other sites and servers.

In reflection if I was to do another project like this I would use python again as it was easy to use and find further information on. 


## Visual Studio Code

VS Code is a source-code editor which offers features including debugging, syntax highlighting, intelligent code completing and embedded git. Having used tit in project-1 to great success I decided to use it again. 

</details>

<details>
  <summary>Version Control</summary>
  

## Git-Hub
Git hub was my version control service of choice as I have had some experience in it previously and it is very widely used. 
I really enjoyed using Git Hub as it was very easy to use and worked well with other tools I used such as Jenkins. 
If I were to work on another project like this I would definitely consider using GitHub again.
</details>

<details>
  <summary>Project Tracking</summary>
  

## Jira

I really enjoyed using Jira last time and used it again on this project. Although it is more geared towards the Agile way of working I might look for an alternative next time as it can be a little cumbersome at times. 

</details>

<details>
  <summary>CI Server / Unit Testing</summary>
  

## Jenkins

Jenkins was my CI/CD server of choice and it made the project very manageable, automating some of the tasks for me making the development process much easier. 

</details>

<details>
  <summary>Artifact Repository and Deployment</summary>
  

## Docker/Docker Swarm

I used docker to deploy my app as it is extremely widely used in the industry. Meaning anything I learn through the process will likely serve me very well in a deployment in the future. <br/>
It also has plenty of help sites available which made troubleshooting very easy. 

## Ansible

I used Ansible in conjunction with Docker to orchestrate the deployment process. Ansible allows you to break each phase of the deployment process down into manageable steps which can be customised endlessly to allow you to work in whatever way you want. <br/>
I enjoyed using it although it was hard to get my head around it at first and will likely use it again in the future. 

</details>


<details>
  <summary>Miscellaneous </summary>
  

## Google Cloud Platform

GCP was my cloud provider for my project due to its free trial period I made good use of the many free services it offers and will likely use it again in the future as a result of its easy to use website and easy to understand services. 

## MySQL
I chose MySQL for its entry level understandability. The interactions with python via SQLAlchemy made it easy to manipulate the database as needed. 

## Linux
Last but not least I used Linux, Ubuntu 18 for my virtual machine as it is open source meaning there is a tonne of help websites and a large community behind it when you get stuck. Another big reason was its customisability. There are a mountain of addons, plug-ins and apps to expand its functionality and tailor it to your needs. This came in handy during the project. 
A final thing is it's very light weight making it very good for using on virtual machines as it doesn't cost to much to have it running. 

I will definitely be using Linux in future projects. 

</details>


</details>

## **Sprint Review**

Having completed the first sprint on this project I have collated some of the things that went well, went poorly and that I would like to do in the future, should the opportunity arise for another sprint. <br/>
<br/>

**Positives**<br/>
The process of building the app went very well. I have some issues with deploying my application which I will touch on in the negatives, which meant I was not able to test if my app worked for a while, and to my surprise and delight it worked first time. This fulled me with positivity for the rest of project as I was able to jump right into the testing phase of development much earlier than expected. <br/>
<br/>

Another positive from this sprint was when the testing phase which also went pretty quickly and without much of a hitch. Leaving me more time to working on the Docker integration which I was less confident in.<br/>
<br/>

**Negatives**<br/>
As mentioned above I struggled implementing Docker initially with my application to the point I could not test it. Thankfully I had taken good notes during the training for docker and was able to debug the issues I faced within the same day. 

I also struggled a lot with the Jenkins implementation and unfortunately my notes were not so good for this section. Learning it I didn't quite grasp the concept and putting it into practise left some holes which were blocking my entire progress. <br/>
To overcome this I utilised my help channel in teams and consulted many of the available web pages dedicated to helping people like me. Using the resources available to me I managed to sus out the issue and get the project back on track. <br/>
<br/>

**Project Aspirations**<br/>
Given another sprint on this I would like to implement: 
- more customisability in terms of characters and enemies
- logging in functionality
- leader boards
- win loss ration
Some of these were possible during the development phase however were out of scope and therefor were dropped to achieve deadline.<br/>
<br/>
<br/>

## **Acknowledgements**


### Trainers<br/>
Oliver Nichols<br/>
Ryan Wright<br/>
<br/>
### colleagues<br/>
Kwame<br/>
Natalie<br/>
Suman<br/>
Chasminder<br/>
<br/>

### Tools<br/>
The internet