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

