from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.image import Image
from kivy.uix.spinner import Spinner
from kivy.uix.image import AsyncImage
import webbrowser  # Import the webbrowser module
import numpy as np
global ta_score
import pickle
from sklearn.tree import DecisionTreeClassifier
from kivy.properties import ColorProperty
from kivy.graphics import Color, Rectangle
from kivy.uix.dropdown import DropDown
from kivy.utils import get_color_from_hex
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView





class MainPage(Screen):
    background_color = ColorProperty([1, 0, 0, 1]) 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        avengers_colors = {
        'primary': (1, 0, 0, .6),  # Red
        'secondary': (0, 0.5, 1, .5),  # Blue
        'accent': (1, 1, 1, .3),  # Gold
        'text': (1, 1, 1, 1)}

        
        
        # Bind size and pos to update the background if the screen size changes
        
        
        
        self.layout = BoxLayout(orientation='vertical',padding=30,spacing=10)
        self.l = Label(text="Quantum Leap Career",  # White text
                        font_size=20,
                        halign='center',
                        valign='middle',color=(0.2, 0.6, 1, 1),bold=True)
        self.spin = Spinner(text="[b]Choose way to predict your career[/b]",
                            values=("By Test", "By Interested Domain"),background_color=(1,.8,.9,.6),color=(1,.7,.6),markup=True)
        self.spin.dropdown_cls.background_color = avengers_colors['primary']
        
        self.button = Button(text='Transform', color=(1,0,.5),background_color=(1,.8,.9,.6),bold=True)
        self.button.bind(on_press=self.go_to_other_page)
        self.layout.add_widget(self.l)
        self.layout.add_widget(self.spin)
        self.layout.add_widget(self.button)
        
        self.layout.bind(size=self.update_background)
        with self.layout.canvas.before:
            self.rect = Rectangle(pos=self.layout.pos, size=self.layout.size, source='tel.jpg')
    
        
        self.add_widget(self.layout)

    
        
       
    

    

        
    def update_background(self, instance, value):
        # Update background Rectangle size
        self.rect.size = instance.size
    
  


    
    def go_to_other_page(self,instance):
        if self.spin.text == "By Interested Domain":
            self.manager.current = 'other_page'
            
            
        elif self.spin.text == "By Test":
            self.manager.current = 'tatest'

        
   

    def open_web_link(self, link):
        webbrowser.open(link)




    


        
class OtherPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.l = Label(text="Suggest Job Role", color=(1, 0.3, 1, 1))
        self.layout.add_widget(self.l)

        
        self.job_role=['Junior_Software_Developer','IT_Support_Specialist',
        'System_Administrator','Quality_Assurance_Tester','Network_Technician',
        'Database_Administrator','Help_Desk_Support','Technical_Support_Engineer',
        'Web_Developer','Junior_Data_Analyst','UI_Designer','Hardware_Engineer']
        self.job_role[0]=Button(text=self.job_role[0],on_press=self.job1)
        self.job_role[1]=Button(text=self.job_role[1],on_press=self.job2)
        self.job_role[2]=Button(text=self.job_role[2],on_press=self.job3)
        self.job_role[3]=Button(text=self.job_role[3],on_press=self.job4)
        self.job_role[4]=Button(text=self.job_role[4],on_press=self.job5)
        self.job_role[5]=Button(text=self.job_role[5],on_press=self.job6)
        self.job_role[6]=Button(text=self.job_role[6],on_press=self.job7)
        self.job_role[7]=Button(text=self.job_role[7],on_press=self.job8)
        self.job_role[8]=Button(text=self.job_role[8],on_press=self.job9)
        self.job_role[9]=Button(text=self.job_role[9],on_press=self.job10)
        self.job_role[10]=Button(text=self.job_role[10],on_press=self.job11)
        self.job_role[11]=Button(text=self.job_role[11],on_press=self.job12)
        
        
        for i in range(len(self.job_role)-1):
               self.layout.add_widget(self.job_role[i])
        
        self.add_widget(self.layout)

    

    



    def job1(self,instance):
        self.manager.current='jds'
        
    def job2(self,instance):
        self.manager.current='its'
        
    def job3(self,instance):
        self.manager.current='sa'
        
    def job4(self,instance):
        self.manager.current='qat'
        
    def job5(self,instance):
        self.manager.current='nt'
        
    def job6(self,instance):
        self.manager.current='da'
        
    def job7(self,instance):
        self.manager.current='hds'
        
    def job8(self,instance):
        self.manager.current='tse'
        
    def job9(self,instance):
        self.manager.current='wd'
        
    def job10(self,instance):
        self.manager.current='jda'
        
    def job11(self,instance):
        self.manager.current='ui'
        
    def job12(self,instance):
        self.manager.current='he'
    


class Tatest(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
                
        self.ta_score=0
        
        self.layout = BoxLayout(orientation='vertical',spacing=10,padding=20)
        self.l = Label(text="Technical Aptitude", color=(1, 0.3, 1, 1), size_hint=(None,None), size=(800,75))
        self.spin1 = Spinner(text="What does the acronym CPU stand for?", values=("a. Central Processing Unit", "b. Computer Processing Unit", "c. Central Peripheral Unit", "d. Central Program Unit"))
        self.spin2 = Spinner(text="Which programming language is commonly used for creating mobile applications?", values=("a. Java", "b. C++", "c. Swift", "d. Python"))
        self.spin3 = Spinner(text="What is the purpose of SQL in the context of databases?", values=("a. Software Query Language", "b. System Question Language", "c. Structured Query Language", "d. Standard Query Logic"))
        self.spin4 = Spinner(text="What is the function of a router in a computer network?", values=("a. Connects devices within the same network", "b. Connects multiple networks together", "c. Manages data storage on a network", "d. Provides electrical power to devices"))
        self.spin5 = Spinner(text="Which type of testing focuses on the internal logic of the software code?", values=("a. Unit Testing", "b. Integration Testing", "c. System Testing", "d. Acceptance Testing"))
        self.spin6 = Spinner(text="What does the term 'responsive design' refer to in web development?", values=("a. Designing visually appealing graphics", "b. Designing websites that work on various devices and screen sizes", "c. Designing secure login interfaces", "d. Designing websites with fast loading times"))
        self.spin7 = Spinner(text="In networking, what is a MAC address used for?", values=("a. Identifying a device on a network", "b. Managing network traffic", "c. Assigning IP addresses", "d. Providing internet access"))
        self.spin8 = Spinner(text="Which version control system is commonly used for tracking changes in source code?", values=("a. SVN (Subversion)", "b. Git", "c. Mercurial", "d. CVS (Concurrent Versions System)"))
        self.spin9 = Spinner(text="What is the primary function of a database index?", values=("a. Store backup copies of data", "b. Speed up data retrieval operations", "c. Encrypt sensitive information", "d. Track changes in the database schema"))
        self.spin10 = Spinner(text="Which of the following is NOT a primary color in web design?", values=("a. Red", "b. Blue", "c. Yellow", "d. Green"))
        self.next=Button(text="next")
        self.next.bind(on_press=self.go_to_page)

        self.spin1.bind(text=self.update_score)
        self.spin2.bind(text=self.update_score)
        self.spin3.bind(text=self.update_score)
        self.spin4.bind(text=self.update_score)
        self.spin5.bind(text=self.update_score)
        self.spin6.bind(text=self.update_score)
        self.spin7.bind(text=self.update_score)
        self.spin8.bind(text=self.update_score)
        self.spin9.bind(text=self.update_score)
        self.spin10.bind(text=self.update_score)

        self.layout.add_widget(self.l)
        self.layout.add_widget(self.spin1)
        self.layout.add_widget(self.spin2)
        self.layout.add_widget(self.spin3)
        self.layout.add_widget(self.spin4)
        self.layout.add_widget(self.spin5)
        self.layout.add_widget(self.spin6)
        self.layout.add_widget(self.spin7)
        self.layout.add_widget(self.spin8)
        self.layout.add_widget(self.spin9)
        self.layout.add_widget(self.spin10)
        self.layout.add_widget(self.next)

        self.add_widget(self.layout)

    def update_score(self, spinner, text):
        if spinner == self.spin1 and text == "a. Central Processing Unit":
            self.ta_score += 1
            print("Updated ta_score:", self.ta_score)  # For debugging

        elif spinner == self.spin2 and text == "c. Swift":
            self.ta_score += 1
        elif spinner == self.spin3 and text == "c. Structured Query Language":
            self.ta_score += 1
        elif spinner == self.spin4 and text == "b. Connects multiple networks together":
            self.ta_score += 1
        elif spinner == self.spin5 and text == "a. Unit Testing":
            self.ta_score += 1
        elif spinner == self.spin6 and text == "b. Designing websites that work on various devices and screen sizes":
            self.ta_score += 1
        elif spinner == self.spin7 and text == "a. Identifying a device on a network":
            self.ta_score += 1
        elif spinner == self.spin8 and text == "b. Git":
            self.ta_score += 1
        elif spinner == self.spin9 and text == "b. Speed up data retrieval operations":
            self.ta_score += 1
        elif spinner == self.spin10 and text == "c. Yellow":
            self.ta_score += 1
        
        self.manager.get_screen('pred').update_label_text(self.ta_score)



        
        

    def go_to_page(self,instance):
        self.manager.current='cc'
        
       




class CS(Screen):
     def __init__(self, **kwargs):
         super().__init__(**kwargs)
         self.cs_score=np.array(0)
         self.layout = BoxLayout(orientation='vertical')
         self.l = Label(text="Coding Skills", color=(1, 0.3, 1, 1),size_hint=(None,None),size=(800,75))
         self.spin1=Spinner(text="What will be the output of the following Python code? x = 5,y = 2,  print(x * y + x).",values=("a. 15","b. 20","c. 25","d. 30"))
         self.spin1.bind(text=self.update_score)
         self.spin2=Spinner(text="Which HTML tag is used to create a hyperlink?",values=("a. <link>","b. <a>","c. <href>","d. <url>"))
         self.spin2.bind(text=self.update_score)

         self.spin3=Spinner(text="In the context of IP addressing, how many bits are in an IPv4 address?",values=("a. 16","b. 32","c. 64","d. 128"))
         self.spin4=Spinner(text="What is the primary key used for in a relational database?",values=("a. Identify duplicate records","b. Establish relationships between tables","c. Ensure data integrity and uniqueness","d. Provide a summary of data"))
         self.spin5=Spinner(text="Which version control system is known for its distributed nature and is widely used in open-source projects?",values=("a. SVN","b. Git","c. Mercurial","d. CVS"))
         
         self.spin3.bind(text=self.update_score)
         self.spin4.bind(text=self.update_score)
         self.spin5.bind(text=self.update_score)
         


         
                                                                         
                                                                                                                               
         self.layout.add_widget(self.l)
        
    
         self.layout.add_widget(self.spin1)
         self.layout.add_widget(self.spin2)
         self.layout.add_widget(self.spin3)
         self.layout.add_widget(self.spin4)
         self.layout.add_widget(self.spin5)
         
         self.layout.add_widget(Button(text="Next",on_press=self.go_to_SS))
         
         self.add_widget(self.layout)
         

         

     def update_score(self, spinner, text):
        if spinner == self.spin1:
            if text == "a. 15":
                self.cs_score += 2
        elif spinner == self.spin2:
            if text == "b. <a>":
                self.cs_score += 2
        # Add similar checks for other spinners
        elif spinner == self.spin3:
          if text=="c. 64":
            self.cs_score+=2
        elif spinner == self.spin4:
           if text=="a. Identify duplicate records":
             self.cs_score+=2
             
        elif spinner == self.spin5:
          if text=="b. Git":
            self.cs_score+=2
        self.manager.get_screen('pred').update_label_text2(self.cs_score)


        
        
     def go_to_SS(self,instance):
        self.manager.current='ss'
                                                         


class SS(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ss_score=np.array(0)
        self.layout = BoxLayout(orientation='vertical')
        self.l = Label(text="Soft Skills", color=(1, 0.3, 1, 1),size_hint=(None,None),size=(800,75))

        self.spin1=Spinner(text="In a team project, what does effective communication primarily involve?",values=("a. Sending frequent emails","b. Sharing personal opinions only","c. Clear and concise expression of ideas","d. Avoiding team meetings"))
        self.spin2=Spinner(text="When faced with a complex technical issue, what is the best approach for problem-solving?",values=("a. Ignoring the problem and hoping it resolves itself","b. Immediately asking for help from a supervisor","c.Collaborating with team members and researching solutions","d. Complaining about the issue to colleagues"))
        self.spin3=Spinner(text="How do you handle unexpected changes in project requirements or deadlines?",values=("a. Resist change and stick to the original plan","b. Blame others for the changes","c. Adapt to the new requirements and adjust priorities","d. Avoid the project until the changes are reversed"))
        self.spin4=Spinner(text="What does effective teamwork involve?",values=("a. Competing with team members for recognition","b. Working in isolation to achieve personal goals","c. Communicating openly and collaborating towards common objectives","d. Taking credit for others work"))
        self.spin5=Spinner(text="How do you prioritize tasks when faced with multiple deadlines?",values=("a. Procrastinate and complete tasks at the last minute","b. Randomly choose tasks to work on","c. Prioritize based on urgency and importance","d. Delegate all tasks to team members"))
        self.button=Button(text="Next",on_press=self.go_to_CTS)
        self.spin1.bind(text=self.update_score)
        self.spin2.bind(text=self.update_score)
        
        self.spin3.bind(text=self.update_score)
        self.spin4.bind(text=self.update_score)
        self.spin5.bind(text=self.update_score)
         

      

         
        self.layout.add_widget(self.l)
        
    
        self.layout.add_widget(self.spin1)
        self.layout.add_widget(self.spin2)
        self.layout.add_widget(self.spin3)
        self.layout.add_widget(self.spin4)
        self.layout.add_widget(self.spin5)
        self.layout.add_widget(self.button)    

        self.add_widget(self.layout)

    

    def update_score(self, spinner, text):
          if spinner == self.spin1:
            if text == "c. Clear and concise expression of ideas":
                self.ss_score += 1
          elif spinner == self.spin2:
            if text == "c. Collaborating with team members and researching solutions":
               self.ss_score += 1
        # Add similar checks for other spinners
          elif spinner == self.spin3:
            if text=="c. Adapt to the new requirements and adjust priorities":
              self.ss_score+=1
          elif spinner == self.spin4:
            if text=="c. Communicating openly and collaborating towards common objectives":
              self.ss_score+=1
             
          elif spinner == self.spin5:
            if text=="c. Prioritize based on urgency and importance":
               self.ss_score+=1
          self.manager.get_screen('pred').update_label_text3(self.ss_score)


          print(self.ss_score)

    def go_to_CTS(self,instance):
        self.manager.current='CTS'

class CTS(Screen):
    def __init__(self, **kwargs):
         super().__init__(**kwargs)
         self.c_score=np.array(0)
         self.layout = BoxLayout(orientation='vertical')
         self.l = Label(text="Critical Thinking Skills", color=(1, 0.3, 1, 1),size_hint=(None,None),size=(800,75))

         self.spin1=Spinner(text="When encountering a recurring technical issue, what is the first step in finding a solution?",values=("a. Implementing a quick fix to resolve the immediate problem",'b. Ignoring the issue and hoping it will eventually go away','c. Analyzing the root cause of the problem',"d. Reporting the issue to a supervisor without investigation"))
         self.spin2=Spinner(text="You discover a security vulnerability in a system just before a major release. What should you do?",values=("a. Ignore the vulnerability and proceed with the release",'b. Immediately stop the release and address the vulnerability','c. Report the issue but proceed with the release as planned',"d. Notify the team after the release and fix the vulnerability later"))
         self.spin3=Spinner(text="Before implementing a major 0software update, what is a crucial aspect of risk assessment?",values=("a. Ignoring potential risks to avoid delaying the update",'b. Conducting thorough testing in a controlled environment','c. Assuming the update will not introduce any new issues',"d. Implementing the update without any prior analysis"))
         self.spin4=Spinner(text="A user reports an intermittent network connectivity issue.\n What is the most effective approach to troubleshoot this problem?",values=("a. Rebooting the user's computer","b. Blaming the network infrastructure","c. Collaborating with the user to gather more information","d. Immediately replacing the user's network cable"))
         self.spin5=Spinner(text="Your team is working on multiple projects with tight deadlines.\n How would you prioritize tasks to ensure successful project completion?",values=("a. Focusing solely on the project with the nearest deadline","b. Randomly selecting tasks without considering project importance","c. Collaborating with the team to evaluate project priorities","d. Ignoring deadlines and working on tasks at your own pace"))
         self.spin1.bind(text=self.update_score)
         self.spin2.bind(text=self.update_score)
        
         self.spin3.bind(text=self.update_score)
         self.spin4.bind(text=self.update_score)
         self.spin5.bind(text=self.update_score)
         


        

         
         self.layout.add_widget(self.l)
        
    
         self.layout.add_widget(self.spin1)
         self.layout.add_widget(self.spin2)
         self.layout.add_widget(self.spin3)
         self.layout.add_widget(self.spin4)
         self.layout.add_widget(self.spin5)
         self.layout.add_widget(Button(text="Next",on_press=self.go_to_TC))

         self.add_widget(self.layout)

    def update_score(self, spinner, text):
          if spinner == self.spin1:
            if text == "c. Analyzing the root cause of the problem":
                self.c_score += 1
          elif spinner == self.spin2:
            if text == "b. Immediately stop the release and address the vulnerability":
               self.c_score += 1
        # Add similar checks for other spinners
          elif spinner == self.spin3:
            if text=="b. Conducting thorough testing in a controlled environment":
               self.c_score+=1
          elif spinner == self.spin4:
            if text=="c. Collaborating with the user to gather more information":
               self.c_score+=1
             
          elif spinner == self.spin5:
            if text=="c. Collaborating with the team to evaluate project priorities":
               self.c_score+=1

          self.manager.get_screen('pred').update_label_text4(self.c_score)

          print(self.c_score)

   
    

    def go_to_TC(self,instance):
        self.manager.current='tc'


class TC(Screen):
    def __init__(self, **kwargs):
         super().__init__(**kwargs)
         self.ts_score=np.array(0)
         self.layout = BoxLayout(orientation='vertical')
         self.l = Label(text="technical Scenario Skills", color=(1, 0.3, 1, 1),size_hint=(None,None),size=(800,75))

         self.spin1=Spinner(text="Your organization's server is experiencing performance issues.\n Users complain about slow response times. \n What is the most appropriate first step to troubleshoot this issue?",values=("a. Upgrade the server hardware immediatel","b. Monitor network traffic to identify bottlenecks","c. Restart the server to clear any temporary issues","d. Conduct a comprehensive security audit"))
         self.spin2=Spinner(text="Your database-driven web application is loading slowly. \n What action would you take to optimize the database performance?",values=("a. Increase the number of database tables","b. Implement database indexing on frequently queried columns","c. Disable caching to reduce server load","d. Decrease the database connection pool size"))
         self.spin3=Spinner(text="Your organization's network intrusion detection system alerts you to a potential security threat.\n What steps would you take to investigate and mitigate the threat?",values=("a. Ignore the alert as it might be a false positive","b. Isolate the affected system from the network","c. Increase user access privileges for better monitoring","d. Shut down the entire network to prevent further damage"))
         self.spin4=Spinner(text="Your team is responsible for deploying a critical software update. How would you ensure a smooth deployment with minimal impact on users?",values=("a. Deploy the update during peak business hours to maximize visibility","b. Skip the testing phase to expedite the deployment process","c. Communicate with stakeholders, schedule a maintenance window, and perform thorough testing","d. Deploy the update without notifying users to avoid panic"))
         self.spin5=Spinner(text="A user reports the accidental deletion of important files. How would you assist the user in recovering the lost data?",values=("a. Advise the user to recreate the lost files from scratch","b. Restore the files from the latest backup","c. Ignore the request as it is the user's responsibility","d. Offer sympathy but inform the user that data recovery is not possible"))

         
         self.spin1.bind(text=self.update_score)
         self.spin2.bind(text=self.update_score)
        
         self.spin3.bind(text=self.update_score)
         self.spin4.bind(text=self.update_score)
         self.spin5.bind(text=self.update_score)
        
         
         self.layout.add_widget(self.l)
        
    
         self.layout.add_widget(self.spin1)
         self.layout.add_widget(self.spin2)
         self.layout.add_widget(self.spin3)
         self.layout.add_widget(self.spin4)
         self.layout.add_widget(self.spin5)
         self.layout.add_widget(Button(text="next",on_press=self.go_to_MK))

         self.add_widget(self.layout)

    def update_score(self, spinner, text):
          if spinner == self.spin1:
            if text == "b. Monitor network traffic to identify bottlenecks":
                self.ts_score += 1
          elif spinner == self.spin2:
            if text == "b. Implement database indexing on frequently queried columns":
               self.ts_score += 1
        # Add similar checks for other spinners
          elif spinner == self.spin3:
            if text=="b. Isolate the affected system from the network":
               self.ts_score+=1
          elif spinner == self.spin4:
            if text=="c. Communicate with stakeholders, schedule a maintenance window, and perform thorough testing":
               self.ts_score+=1
             
          elif spinner == self.spin5:
            if text=="b. Restore the files from the latest backup":
               self.ts_score+=1
          self.manager.get_screen('pred').update_label_text5(self.ts_score)

        
          print(self.ts_score)

    def go_to_MK(self,instance):
         self.manager.current='mk'


class MK(Screen):
    def __init__(self, **kwargs):
         super().__init__(**kwargs)
         
             
         self.mk_score=np.array(0)
         self.layout = BoxLayout(orientation='vertical')
         self.l = Label(text="Math Knowledge", color=(1, 0.3, 1, 1),size_hint=(None,None),size=(800,75))

         self.spin1=Spinner(text="What is the result of 15 + 3 * 8?",values=("a. 39","b. 53","c. 45","d. 48"))
         self.spin2=Spinner(text="If a server's CPU usage is 80%, and it decreases by 20%, what is the new CPU usage?",values=("a. 60%","b. 64%","c. 40%","d. 16%"))
         self.spin3=Spinner(text="If a dataset has values 5, 8, 12, 15, and 20, what is the average (mean) of these numbers?",values=("a. 12","b. 14","c. 15","d. 18"))
         self.spin4=Spinner(text="What is the area of a rectangle with a length of 10 units and a width of 6 units?",values=("a. 60 square units","b. 36 square units","c. 16 square units","d. 30 square units"))
         self.spin5=Spinner(text="If the price of a software license is $120 and it is discounted by 20%, what is the final discounted price?",values=("a. $96","b. $100","c. $110","d. $130"))

         self.spin1.bind(text=self.update_score)
         self.spin2.bind(text=self.update_score)
        
         self.spin3.bind(text=self.update_score)
         self.spin4.bind(text=self.update_score)
         self.spin5.bind(text=self.update_score)
         
         self.layout.add_widget(self.l)
        
    
         self.layout.add_widget(self.spin1)
         self.layout.add_widget(self.spin2)
         self.layout.add_widget(self.spin3)
         self.layout.add_widget(self.spin4)
         self.layout.add_widget(self.spin5)
         self.layout.add_widget(Button(text='Next',on_press=self.go_to_PRED))                                                                                                                    


         self.add_widget(self.layout)

    def update_score(self, spinner, text):
          if spinner == self.spin1:
            if text == "a. 39":
                self.mk_score += 1
          elif spinner == self.spin2:
            if text == "b. 64%":
               self.mk_score += 1
        # Add similar checks for other spinners
          elif spinner == self.spin3:
            if text=="a. 12":
               self.mk_score+=1
          elif spinner == self.spin4:
            if text=="a. 60 square units":
               self.mk_score+=1
             
          elif spinner == self.spin5:
            if text=="a. $96":
               self.mk_score+=1

          self.manager.get_screen('pred').update_label_text6(self.mk_score)


        
          print(self.mk_score)

    def go_to_PRED(self,instance):
        self.manager.current='pred'


class PRED(Screen):
    def __init__(self,test1,test2,test3,test4,test5,test6,**kwargs):
         super().__init__(**kwargs)
         self.test1=test1
         self.test2=test2
         
         self.test3=test3
         self.test4=test4
         self.test5=test5


         self.test6=test6
         
         
         
         
         
         self.layout = BoxLayout(orientation='vertical')
         self.t1=Label(text=str(self.test1.ta_score))
         self.layout.add_widget(self.t1)
         self.t2=Label(text=str(self.test2.cs_score))
         self.layout.add_widget(self.t2)
         self.t3=Label(text=str(self.test3.ss_score))
         self.layout.add_widget(self.t3)
         self.t4=Label(text=str(self.test4.c_score))
         self.layout.add_widget(self.t4)
         self.t5=Label(text=str(self.test5.ts_score))
         self.layout.add_widget(self.t5)
         
         self.t6=Label(text=str(self.test6.mk_score))
         self.layout.add_widget(self.t6)
         
         
         self.b=Label(text=('suggested_job_role:'))
         self.bs=Button(text="guidance",on_press=self.go_guide)
        
         self.layout.add_widget(self.b)
         self.layout.add_widget(self.bs)

         
         
         
         
         
                 
         self.add_widget(self.layout)

  


        



    def update_label_text(self, new_value):
        # Update label text with new value
        self.t1.text = f'Technical aptitude score: {new_value}'

    def update_label_text2(self, new_value):
        # Update label text with new value
        self.t2.text = f' Coding skills Score: {new_value}'

    def update_label_text3(self, new_value):
        # Update label text with new value
        self.t3.text = f' Soft Skills Score: {new_value}'

    def update_label_text4(self, new_value):
        # Update label text with new value
        self.t4.text = f'Critical thinking Score: {new_value}'

    def update_label_text5(self, new_value):
        # Update label text with new value
        self.t5.text = f'Technical Scenario Score: {new_value}'
        


    def update_label_text6(self, new_value):
       
        # Update label text with new value
         self.t6.text = f'Math Knowledge Score: {new_value}'

        # Load the saved model
         with open('model10.pkl', 'rb') as file:
            model = pickle.load(file)

        # Assuming self.test1.ta_score, etc., are available as attributes
        # Prepare input data for prediction
            input_data = [[self.test1.ta_score, self.test2.cs_score, self.test3.ss_score, 
                       self.test4.c_score, self.test5.ts_score, new_value]]

        # Perform prediction
            predicted_role = model.predict(input_data)

        # Convert the predicted role to a string
            self.predicted_role_str = str(predicted_role)

        # Print the predicted role
            print(self.predicted_role_str)

        # Update label text with the predicted role
            self.b.text = f'Suggested Job Role:{self.predicted_role_str}'
            self.bs.text=f"transform"
            mystr="".join(self.predicted_role_str.lower())
            print(mystr)
            

    def go_guide(self,instance):
        string = self.predicted_role_str
        string_without_brackets = string.strip("[]")  # Remove leading and trailing brackets
        string_without_quotes = string_without_brackets.strip("'")  # Remove leading and trailing single quotes
        lower_string = string_without_quotes.lower()  # Convert to lowercase

        print(lower_string)
        if lower_string=='junior software developer':
            self.manager.current='jsd'
        elif lower_string=='it support specialist':
            self.manager.current='its'

        elif lower_string=='system administrator':
            self.manager.current='sa'

        elif lower_string=='quality assurance tester':
            self.manager.current='qat'

        elif lower_string=='network technician':
            self.manager.current='nt'

        elif lower_string=='database administrator':
            self.manager.current='da'

        elif lower_string=='help desk support':
            self.manager.current='hds'

        elif lower_string=='technical support engineer':
            self.manager.current='tse'

        elif lower_string=='web developer':
            self.manager.current='wd'

        elif lower_string=='junior data analyst':
            self.manager.current='jda'


        elif lower_string=='ui designer':
            self.manager.current='ui'

        elif lower_string=='hardware engineer':
            self.manager.current='he'

        
        
        
        



class JSD(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.jsd_label=Label(text="Junior Software Developer specializing in Python",font_size=13,color=(.75,0,1,1),size=(200,100))
        self.layout.add_widget(self.jsd_label)
        self.JSD_button = Button(text='Python Course', on_press=self.open_JSD,size_hint=(None,None),size=(800,50),pos_hint={'center_x': 0.5})
        self.layout.add_widget(self.JSD_button)
        self.JSD1_button = Button(text='Django Course', on_press=self.open1_JSD)
        self.layout.add_widget(self.JSD1_button)
        self.JSD2_button = Button(text='Community', on_press=self.open2_JSD)
        self.layout.add_widget(self.JSD2_button)
        
        self.pred=Label(text="Avg.Fresher Salary per annum:1.8L-2.4L")
        self.layout.add_widget(self.pred)
        self.add_widget(self.layout)

    def open_JSD(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.scaler.com/topics/python/')

    def open1_JSD(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.simplilearn.com/free-python-django-course-skillup')

    def open2_JSD(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://stackoverflow.com/')


class ITS(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.its_label=Label(text="kk",size=(100,100))
        self.layout.add_widget(self.its_label)
        self.ITS_button = Button(text='Technical Support Fundamentals course'
                                         +"(Finance aid available)", on_press=self.open_ITS)
        self.layout.add_widget(self.ITS_button)
        self.ITS1_button = Button(text='Django Course', on_press=self.open1_ITS)
        self.layout.add_widget(self.ITS1_button)
        self.ITS2_button = Button(text='Community', on_press=self.open2_ITS)
        self.layout.add_widget(self.ITS2_button)
        
        self.pred=Label(text="Avg. Fresher Salary per annum:1.2L-6L")
        self.layout.add_widget(self.pred)
        self.add_widget(self.layout)

    

    def open_ITS(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.coursera.org/professional-certificates/google-it-support?utm_source=gg&utm_medium=sem&campaignid=415485976&adgroupid=1216060337702984&device=c&keyword=google%20it%20certificate&matchtype=p&network=o&devicemodel=&adpostion=&creativeid=&hide_mobile_promo&msclkid=ab8a4ee67d2f1fbd22332b177724aaee&utm_campaign=B2C_INDIA_google-it-support_google_FTCOF_professional-certificates_arte_bing&utm_term=google%20it%20certificate&utm_content=Google%20IT%20Support%20Certificate%20Non%20Branded')

    def open1_ITS(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.udemy.com/course/start-it-support-career-no-certs-or-degree-information/')

    def open2_ITS(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.quora.com/')

class SA(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.SA_label=Label(text="System Adminstraton "+"\n")
    
        self.layout.add_widget(self.SA_label)
        self.SA_button = Button(text='System Admin Course', on_press=self.open_SA)
        self.layout.add_widget(self.SA_button)
        self.SA2_button = Button(text='Community', on_press=self.open1_SA)                                                             
        self.layout.add_widget(self.SA2_button)
        
        self.pred=Label(text="Avg.Fresher Salary per annum:1.5L-4.8L inr")
        self.layout.add_widget(self.pred)
        self.add_widget(self.layout)


    def open_SA(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.linkedin.com/learning/career-essentials-in-system-administration-by-microsoft-and-linkedin')

    def open1_SA(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.reddit.com/r/sysadmin/comments/1bbzm62/moronic_monday_march_11_2024/')



class QAT(Screen):
   def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.SA_label=Label(text="Quality Assurance Tester"+"\n")
    
        self.layout.add_widget(self.SA_label)
        self.SA_button = Button(text='Quality Assurance Tester Course', on_press=self.open_QAT)
        self.layout.add_widget(self.SA_button)
        self.SA2_button = Button(text='Community', on_press=self.open1_QAT)                                                             
        self.layout.add_widget(self.SA2_button)
        
        self.pred=Label(text="Avg.Salary:1.7L-2.1L")
        self.layout.add_widget(self.pred)
        self.add_widget(self.layout)


   def open_QAT(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.classcentral.com/course/freecodecamp-quality-assurance-34064')

   def open1_QAT(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.stickyminds.com/')


class NT(Screen):
   def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.SA_label=Label(text="Quality Assurance Tester"+"\n")
    
        self.layout.add_widget(self.SA_label)
        self.SA_button = Button(text='Quality Assurance Tester Course', on_press=self.open_NT)
        self.layout.add_widget(self.SA_button)
        self.SA2_button = Button(text='Community', on_press=self.open1_NT)                                                             
        self.layout.add_widget(self.SA2_button)
        
        self.pred=Label(text="Avg.Salary:3.5L-7L")
        self.layout.add_widget(self.pred)
        self.add_widget(self.layout)


   def open_NT(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.classcentral.com/course/freecodecamp-quality-assurance-34064')

   def open1_NT(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.stickyminds.com/')

 
class DA(Screen):
   def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.SA_label=Label(text="Quality Assurance Tester"+"\n")
    
        self.layout.add_widget(self.SA_label)
        self.SA_button = Button(text='Quality Assurance Tester Course', on_press=self.open_DA)
        self.layout.add_widget(self.SA_button)
        self.SA2_button = Button(text='Community', on_press=self.open1_DA)                                                             
        self.layout.add_widget(self.SA2_button)
        
        self.pred=Label(text="INR 3.5 to 6 lakhs per annum")
        self.layout.add_widget(self.pred)
        self.add_widget(self.layout)


   def open_DA(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.classcentral.com/course/freecodecamp-quality-assurance-34064')

   def open1_DA(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.stickyminds.com/')


class HDS(Screen):
   def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.SA_label=Label(text="Help Desk Supporter"+"\n")
    
        self.layout.add_widget(self.SA_label)
        self.SA_button = Button(text=' Desk Supporter Course', on_press=self.open_HDS)
        self.layout.add_widget(self.SA_button)
        self.SA2_button = Button(text='Community', on_press=self.open1_HDS)                                                             
        self.layout.add_widget(self.SA2_button)
        
        self.pred=Label(text="Avg Fresher Salary: 2.5 to 3.5 lakhs per annum")
        self.layout.add_widget(self.pred)
        self.add_widget(self.layout)


   def open_HDS(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.classcentral.com/course/freecodecamp-quality-assurance-34064')

   def open1_HDS(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.stickyminds.com/')

class TSE(Screen):
   def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.SA_label=Label(text="Technical Software Engineer"+"\n")
    
        self.layout.add_widget(self.SA_label)
        self.SA_button = Button(text='Software Technican Course', on_press=self.open_TSE)
        self.layout.add_widget(self.SA_button)
        self.SA2_button = Button(text='Community', on_press=self.open1_TSE)                                                             
        self.layout.add_widget(self.SA2_button)
        
        self.pred=Label(text="Avg.Fresher Salary:INR 2.5 lakhs to INR 4 lakhs per annum.")
        self.layout.add_widget(self.pred)
        self.add_widget(self.layout)


   def open_TSE(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.classcentral.com/course/freecodecamp-quality-assurance-34064')

   def open1_TSE(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.stickyminds.com/')


class WD(Screen):
   def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.SA_label=Label(text="Web Developer"+"\n")
    
        self.layout.add_widget(self.SA_label)
        self.SA_button = Button(text='Front End Course', on_press=self.open_WD)
        self.layout.add_widget(self.SA_button)
        self.SA2_button = Button(text='Community', on_press=self.open1_WD)                                                             
        self.layout.add_widget(self.SA2_button)
        self.pred=Label(text="Avg Fresher Salary:INR 3L to INR 6L per annum")
        self.layout.add_widget(self.pred)
        self.add_widget(self.layout)


   def open_WD(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.classcentral.com/course/freecodecamp-quality-assurance-34064')

   def open1_WD(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.stickyminds.com/')

   

class JDA(Screen):
   def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.SA_label=Label(text="Junior Data Analyst"+"\n")
    
        self.layout.add_widget(self.SA_label)
        self.SA_button = Button(text='Python', on_press=self.open_JDA)
        self.layout.add_widget(self.SA_button)
        self.SA1_button = Button(text='SnowFlake (PAID)', on_press=self.open1_JDA)
        self.layout.add_widget(self.SA1_button)
        self.SA2_button = Button(text='Community', on_press=self.open2_JDA)                                                             
        self.layout.add_widget(self.SA2_button)
        
        self.pred=Label(text="Avg Fresher Salary:INR 3-6 lakhs per annum")
        self.layout.add_widget(self.pred)
        self.add_widget(self.layout)


   def open_JDA(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.scaler.com/topics/course/python-for-beginners/')

   def open1_JDA(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.udemy.com/course/snowflake-essentials/?utm_source=bing&utm_medium=udemyads&utm_campaign=BG-Search_DSA_Beta_Prof_la.EN_cc.India&campaigntype=Search&portfolio=Bing-India&language=EN&product=Course&test=&audience=DSA&topic=&priority=Beta&utm_content=deal4584&utm_term=_._ag_1327112923136029_._ad__._kw_IT%20en_._de_c_._dm__._pl__._ti_dat-2334744222699522:loc-90_._li_155568_._pd__._&matchtype=b&msclkid=1336df9906f212cc9eb9b81adea1ee08')

   def open2_JDA(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.stickyminds.com/')

class UI(Screen):
   def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.SA_label=Label(text="UI Designer"+"\n")
    
        self.layout.add_widget(self.SA_label)
        self.SA_button = Button(text='UI/UX Design Course', on_press=self.open_UI)
        self.layout.add_widget(self.SA_button)
        self.SA2_button = Button(text='Community', on_press=self.open1_UI)                                                             
        self.layout.add_widget(self.SA2_button)
        
        self.pred=Label(text="Avg Fresher Salary:INR 3-6 lakhs per annum.")
        self.layout.add_widget(self.pred)
        self.add_widget(self.layout)


   def open_UI(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.classcentral.com/course/freecodecamp-quality-assurance-34064')

   def open1_UI(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.stickyminds.com/')

class HE(Screen):
   def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.SA_label=Label(text="Hardware Engineer"+"\n")
    
        self.layout.add_widget(self.SA_label)
        self.SA_button = Button(text='Hardware Components Course', on_press=self.open_HE)
        self.layout.add_widget(self.SA_button)
        self.SA2_button = Button(text='Community', on_press=self.open1_HE)                                                             
        self.layout.add_widget(self.SA2_button)
        
        self.pred=Label(text="Avg Fresher Salary:INR 2.5 lakhs to INR 6 lakhs per annum")
        self.layout.add_widget(self.pred)
        self.add_widget(self.layout)


   def open_HE(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.classcentral.com/course/freecodecamp-quality-assurance-34064')

   def open1_HE(self, instance):
        # Replace 'https://example.com' with your desired web link
        App.get_running_app().root.get_screen('main_page').open_web_link('https://www.stickyminds.com/')




 


 



        
class Myapp(App):
    def build(self):
        

        
        
        sm = ScreenManager()
        layout = BoxLayout(orientation='vertical')

        sm.add_widget(MainPage(name='main_page'))
        sm.add_widget(OtherPage(name='other_page'))
        sm.add_widget(JSD(name='jsd'))
       
        sm.add_widget(ITS(name='its'))
        sm.add_widget(SA(name="sa"))
        sm.add_widget(QAT(name='qat'))
        sm.add_widget(NT(name='nt'))
        sm.add_widget(DA(name='da'))
        sm.add_widget(HDS(name='hds'))
        sm.add_widget(TSE(name='tse'))
        sm.add_widget(WD(name='wd'))
        sm.add_widget(JDA(name='jda'))
        sm.add_widget(UI(name='ui'))
        sm.add_widget(HE(name='he'))
        tatest_screen=Tatest(name='tatest')
        sm.add_widget(tatest_screen)
        
        cs_screen=CS(name='cc')
        sm.add_widget(cs_screen)
        ss_screen=SS(name='ss')
        sm.add_widget(ss_screen)
        ts_screen=TC(name='tc')
        sm.add_widget(ts_screen)
        cts_screen=CTS(name='CTS')
        sm.add_widget(cts_screen)
        Math=MK(name='mk')
        sm.add_widget(Math)
        sm.add_widget(PRED(test1=tatest_screen,test2=cs_screen,test3=ss_screen,test5=ts_screen,test4=cts_screen,test6=Math,name='pred'))
        
        # Add screens to the layout
        

        # Create a ScrollView and add the layout to it

        
        return sm
   


if __name__ == '__main__':
    Myapp().run()
