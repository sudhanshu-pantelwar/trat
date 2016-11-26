import tkinter as tk
from tkinter import ttk
from tkinter import HORIZONTAL
from tkinter import PhotoImage

LARGE_FONT = ("Verdana", 24)
SMALL_FONT = ("Verdana", 10)
i, j, k, l = 0, 0, 0, 0
countNo, countNo1, countNo2, countNo3 = 0, 0, 0, 0
a = []
totalMarksOR, totalMarksTR, totalMarksFR, totalMarksPR = 0, 0, 0, 0
overallReadinessButtonState = 0
button6 = 0

class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "TELEHEALTH READINESS ASSESSMENT TOOL")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, OverallReadiness, About, Instructions):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        if(cont == OverallReadiness):
            frame.total_marks()
        if(cont == About):
            frame.about()
        if (cont == Instructions):
            frame.instructions()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        global button6
        print(parent)
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to TRAT", font=LARGE_FONT)
        label.place(x=210, y=20)

        button = ttk.Button(self, text="ORGANIZATIONAL READINESS", width=25,
                            command=lambda: controller.show_frame(PageOne))
        button.place(x=250, y=90)

        button2 = ttk.Button(self, text="TECHNOLOGY READINESS", width=25,
                             command=lambda: controller.show_frame(PageTwo))
        button2.place(x=250, y=120)
        button3 = ttk.Button(self, text="FINANCIAL READINESS", width=25,
                             command=lambda: controller.show_frame(PageThree))
        button3.place(x=250, y=150)
        button4 = ttk.Button(self, text="POLICY READINESS", width=25,
                             command=lambda: controller.show_frame(PageFour))
        button4.place(x=250, y=180)
        button5 = ttk.Button(self, text="ABOUT TRAT",
                             command=lambda: controller.show_frame(About))
        button5.place(x=50, y=270)
        button6 = ttk.Button(self, text="INSTRUCTIONS",
                             command=lambda: controller.show_frame(Instructions))
        button6.place(x=550, y=270)
        button6 = ttk.Button(self, text="Overall Readiness Score", state = 'disabled',
                             command=lambda: controller.show_frame(OverallReadiness))
        button6.place(x=280, y=310)

        photo = PhotoImage(file="logo.png")

        photo = photo.subsample(6, 6)
        label = ttk.Label(self, image=photo)

        label.image = photo
        label.place(x=20, y=120)

        photo1 = PhotoImage(file="logo1.png")

        photo1 = photo1.subsample(2, 2)
        label1 = ttk.Label(self, image=photo1)

        label1.image = photo1
        label1.place(x=550, y=100)





class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        global i
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.countER = 0
        self.countAR = 0
        label = tk.Label(self, text="ORGANIZATIONAL READINESS", font=LARGE_FONT)
        label.pack(pady=10, padx=1)

        self.label1 = tk.Label(self,
                               text='1. Do all the stakeholders approve of using telehealth technology?',
                               wraplength=650)
        self.label1.pack(pady=10, padx=10)

        self.var = tk.StringVar()

        R1 = ttk.Radiobutton(self, text="Yes", variable=self.var, value="Yes")
        R2 = ttk.Radiobutton(self, text="No", variable=self.var, value="No")
        R3 = ttk.Radiobutton(self, text="May be", variable=self.var, value="Maybe")
        self.label1.pack(anchor='w')
        R1.pack(anchor='w')
        R2.pack(anchor='w')
        R3.pack(anchor='w')

        self.nextButton1 = ttk.Button(self, text="Next",
                                      command=self.question_gui)
        self.nextButton1.pack(padx=30, pady=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        self.progressbar = ttk.Progressbar(self, orient=HORIZONTAL, length=200)
        self.progressbar.pack()
        self.progressbar.config(mode='determinate', maximum=10.0, value=i)
        self.label3 = tk.Label(self, text="")
        self.label3.pack(padx=10, pady=20)

    def question_gui(self):

        global i
        global countNo
        global a
        global totalMarksOR
        print(countNo)
        print(self.var.get())
        ER = [0,1,2,3,4,6]
        AR = [7,8,9,10]
        array15 = [0,1]
        array10 = [2,3,7,8,9,10]
        array5 = [4,6]
        if (self.var.get() == ''):
            self.label3.configure(text="Please select an option")
            return
        self.label3.configure(text="")
        if (self.var.get() == "Yes" and (i in array15)):
            totalMarksOR = totalMarksOR + 15
            print("totalMarks", totalMarksOR)
            if(i in ER):
                self.countER = self.countER + 1
            if(i in AR):
                self.countAR = self.countAR + 1
        if (self.var.get() == "Maybe" and (i in array10)):
            totalMarksOR = totalMarksOR + 5
            print("totalMarks", totalMarksOR)

        if (self.var.get() == "Yes" and (i in array10)):
            totalMarksOR = totalMarksOR + 10
            print("totalMarks", totalMarksOR)
            if(i in ER):
                self.countER = self.countER + 1
            if(i in AR):
                self.countAR = self.countAR + 1

        if (self.var.get() == "Maybe" and (i in array10)):
            totalMarksOR = totalMarksOR + 5
            print("totalMarks", totalMarksOR)

        if (self.var.get() == "Yes" and (i in array5)):
            totalMarksOR = totalMarksOR + 5
            print("totalMarks", totalMarksOR)
            if (i in ER):
                self.countER = self.countER + 1
            if (i in AR):
                self.countAR = self.countAR + 1

        if (self.var.get() == "Maybe" and (i in array5)):
            totalMarksOR = totalMarksOR + 2.5
            print("totalMarks", totalMarksOR)

        if (self.var.get() == "No"):

            if i < 3:
                countNo = countNo + 1
                if countNo == 2:
                    self.not_ready_gui()
                    return
        print(self.countER, self.countAR)
        if i == 10:
            self.nextButton1.config(text='Results', command=self.results_gui)

        listOfQuestionsOR = ['2. Has your organization researched and decided on specific telehealth technologies and what would work the best for the organization?',
                             '3. Does the organization have a Physician/Administrator/Clinical champion to promote change?',
                             '4. Do key telehealth team members and other stakeholders have knowledge about various telehealth technologies or intend to gain knowledge (like Videoconferencing, Store and Forward etc.',
                             '5. Has the organization completed a strategic planning process in the previous year?',
                             '6. Will the organization go through this exercise with the proposed telehealth team?',
                             '7. Do you think the level of knowledge that the primary care team has regarding telemedicine is good enough?',
                             '8. Has the organization planned any training or educational sessions on Telehealth either in the past or near future?',
                             '9. Based on past experiences, do you think organization is well able to successfully promote and manage change?',
                             '10. Has the staff been involved, or will they be involved, in selecting technology, establishing policies and evaluation measures?',
                             '11. Have you developed standard lines of communication to keep stakeholders informed about advancement?',
                            ]
        self.label1.config(text=listOfQuestionsOR[i], wraplength=650, justify="left")
        self.label1.update()
        i = i + 1
        print(i)
        self.progressbar.config(mode='determinate', maximum=10.0, value=i)

    def results_gui(self):
        global overallReadinessButtonState
        global totalMarksOR
        readiness = ''
        if (self.countER <= 5):
            readiness = 'Early ready'
        if self.countAR >= 2:
            readiness = 'Advanced ready'
        if(self.countER > 5 and self.countAR==0):
            readiness = 'Early ready'

        label = tk.Label(self, text='', font=SMALL_FONT, justify="center", width=700, height=400)
        label.place(x=0, y=0)
        label1 = tk.Label(self, text="Organization Readiness", font=LARGE_FONT, justify="center")
        label1.place(x=150, y=20)
        textVar = "You are " +str(totalMarksOR)+ "% organizationally(" +readiness + ") ready for telehealth. Please proceed with technical readiness survey."

        label1 = tk.Label(self, text=textVar, wraplength = 600, font=SMALL_FONT, justify="center")
        label1.place(x=40,y=120)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: self.controller.show_frame(StartPage))
        button1.place(x=280, y=180)
        overallReadinessButtonState = overallReadinessButtonState + 1
        if (overallReadinessButtonState >= 4):
            print("normalsdfadfadfafa")
            button6.config(state='normal')

    def not_ready_gui(self):
        global totalMarksOR
        global overallReadinessButtonState
        label = tk.Label(self, text='', font=SMALL_FONT, justify="center", width=700, height=400)
        label.place(x=0, y=0)
        label1 = tk.Label(self, text="Please reevaluate the basic requirements for telehealth. Research into various telehealth options and decide upon a technology before you proceed with survey. Thank you for taking this survey!", wraplength = 600, font=SMALL_FONT, justify="center")
        label1.place(x=30, y=20)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: self.controller.show_frame(StartPage))
        button1.place(x=300, y=180)
        overallReadinessButtonState = overallReadinessButtonState + 1
        if (overallReadinessButtonState >= 4):
            print("normalsdfadfadfafa")
            button6.config(state='normal')

    def init_window(self):
        self.master.title("Telehealth Readiness Assessment Tool(TRAT)")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)

    def questions(self, hey):
        print(hey)

    def client_exit(self):
        exit()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.countER = 0
        self.countAR = 0

        label = tk.Label(self, text="TECHNOLOGY READINESS", font=LARGE_FONT)
        label.pack(pady=10, padx=1)

        self.label1 = tk.Label(self,
                               text="1. Does the organization have a separate room or space designated for telemedicine with internet access, adequate sound, and good lighting available?",
                               wraplength=650, justify="left")
        self.label1.pack(pady=10, padx=10)

        self.var = tk.StringVar()

        R1 = ttk.Radiobutton(self, text="Yes", variable=self.var, value="Yes")
        R2 = ttk.Radiobutton(self, text="No", variable=self.var, value="No")
        R3 = ttk.Radiobutton(self, text="May be", variable=self.var, value="Maybe")
        self.label1.pack(anchor='w')
        R1.pack(anchor='w')
        R2.pack(anchor='w')
        R3.pack(anchor='w')

        self.nextButton1 = ttk.Button(self, text="Next",
                                      command=self.question_gui)
        self.nextButton1.pack(padx=30, pady=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        self.progressbar = ttk.Progressbar(self, orient=HORIZONTAL, length=200)
        self.progressbar.pack()
        self.progressbar.config(mode='determinate', maximum=11.0, value=j)
        self.label3 = tk.Label(self, text="")
        self.label3.pack(padx=10, pady=20)

    def question_gui(self):
        global j
        global countNo1
        global a
        global totalMarksTR
        print(countNo)
        print(self.var.get())
        array10 = [1, 2, 3, 4, 9]
        array5 = [5,6,7,8,10,11]
        array20 = 0
        ER = [0, 1, 2, 3, 4, 5, 8]
        AR = [6,7,10,11]

        if (self.var.get() == ''):
            self.label3.configure(text="Please select an option")
            return
        self.label3.configure(text="")
        if (self.var.get() == "Yes" and (j in array10)):
            totalMarksTR = totalMarksTR + 10
            print("totalMarks10-1", totalMarksTR)
            if (j in ER):
                self.countER = self.countER + 1
            if (j in AR):
                self.countAR = self.countAR + 1

        if (self.var.get() == "Maybe" and (j in array10)):
            totalMarksTR = totalMarksTR + 5
            print("totalMarks10-2", totalMarksTR)

        if (self.var.get() == "Yes" and (j in array5)):
            totalMarksTR = totalMarksTR + 5
            print("totalMarks5-1", totalMarksTR)
            if (j in ER):
                self.countER = self.countER + 1
            if (j in AR):
                self.countAR = self.countAR + 1

        if (self.var.get() == "Maybe" and (j in array5)):
            totalMarksTR = totalMarksTR + 2.5
            print("totalMarks5-2", totalMarksTR)

        if (self.var.get() == "Yes" and (j == array20)):
            totalMarksTR = totalMarksTR + 20
            print("totalMarks20-1", totalMarksTR)
            if (j in ER):
                self.countER = self.countER + 1
            if (j in AR):
                self.countAR = self.countAR + 1

        if (self.var.get() == "Maybe" and (j == array20)):
            totalMarksTR = totalMarksTR + 10
            print("totalMarks20-2", totalMarksTR)

        if (self.var.get() == "No"):
            if j>0 and j < 4:
                print("countNo", countNo1)
                countNo1 = countNo1 + 1
                if countNo1 == 2:
                    print("about to print not ready gui", countNo1)
                    self.not_ready_gui()
                    return

        if j == 11:
            self.nextButton1.config(text='Results', command=self.results_gui)
        ##        a.append(PageOne)
        listOfQuestionsTR = [
            '2. Has the telehealth team developed a workflow for secure transmission of PHI? (PHI includes clinical notes, referrals, prescriptions, consent forms)',
            '3. Has the organization determined the equipment needs for originating and distant sites? (Ex: Client homes and non-hospital based facilities)',
            '4. Has the telehealth team examined different types of telehealth equipment, and about highlights of each device/technology?',
            '5. Has the organization’s IT team done an analysis of the program?',
            '6. Is the telehealth team fully aware of policies and standards regarding handling of personnel health information (PHI) either with paper, electronically or both? (PHI includes clinical notes, referrals, prescriptions, consent forms)',
            '7. Has the telehealth team considered what the impact of telehealth adoption will be on existing workflows, such as reorganization of space, change of job responsibilities, overall change management, training and user adoption?',
            '8. Has the telehealth team considered how their program will integrate or share information with other programs? How do you share documents?',
            '9. Are the quality of internet connection and bandwidth are suitable for telehealth technology?',
            '10. Is the required hardware readily available, such as compatible devices, microphones, and cameras?',
            '11. Does the team have a plan for installation- including dedicated time and staff resources?',
            '12. Have educational and training sessions related to the use of the telehealth technology been set up for staff and clients/patients?'
        ]
        self.label1.config(text=listOfQuestionsTR[j], wraplength=650, justify="left")
        self.label1.update()
        j = j + 1
        print("J", j)
        self.progressbar.config(mode='determinate', maximum=11.0, value=j)


    def results_gui(self):
        global overallReadinessButtonState
        global totalMarksTR
        readiness = ''
        if (self.countER <= 5):
            readiness = 'Early ready'
        if self.countAR >= 2:
            readiness = 'Advanced ready'
        if (self.countER > 5 and self.countAR == 0):
            readiness = 'Early ready'



        label = tk.Label(self, text='', font=SMALL_FONT, justify="center", width=700, height=400)
        label.place(x=0, y=0)
        label1 = tk.Label(self, text="TECHNOLOGY READINESS", font=LARGE_FONT, justify="center")
        label1.place(x=150, y=20)
        textVar = "You are " +str(totalMarksTR)+ "% technology(" +readiness + ") ready for telehealth. Please proceed with financial readiness survey."

        label1 = tk.Label(self, text=textVar, wraplength = 600, font=SMALL_FONT, justify="center")
        label1.place(x=50,y=120)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: self.controller.show_frame(StartPage))
        button1.place(x=280, y=180)
        overallReadinessButtonState = overallReadinessButtonState + 1
        if (overallReadinessButtonState >= 4):
            print("normalsdfadfadfafa")
            button6.config(state='normal')

    def not_ready_gui(self):
        global overallReadinessButtonState
        label = tk.Label(self, text='', font=SMALL_FONT, justify="center", width=700, height=400)
        label.place(x=0, y=0)
        label1 = tk.Label(self, text="Please reevaluate the basic requirements for telehealth. Research into various telehealth options and decide upon a technology before you proceed with survey. Thank you for taking this survey!", wraplength = 600, font=SMALL_FONT, justify="center")
        label1.place(x=30, y=20)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: self.controller.show_frame(StartPage))
        button1.place(x=300, y=180)
        overallReadinessButtonState = overallReadinessButtonState + 1
        print("overallReadinessButtonState",overallReadinessButtonState)
        if (overallReadinessButtonState >= 4):
            print("normalsdfadfadfafa")
            button6.config(state='normal')

    def init_window(self):
        self.master.title("Telehealth Readiness Assessment Tool(TRAT)")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)

    def questions(self, hey):
        print(hey)

    def client_exit(self):
        exit()


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        global k
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.countER = 0
        self.countAR = 0

        label = tk.Label(self, text="FINANCIAL READINESS", font=LARGE_FONT)
        label.pack(pady=10, padx=1)

        self.label1 = tk.Label(self,
                               text="1. Has the telehealth team developed use case scenarios to determine usage rates?",
                               wraplength=650, justify="left")
        self.label1.pack(pady=10, padx=10)
        self.var = tk.StringVar()

        R1 = ttk.Radiobutton(self, text="Yes", variable=self.var, value="Yes")
        R2 = ttk.Radiobutton(self, text="No", variable=self.var, value="No")
        R3 = ttk.Radiobutton(self, text="May be", variable=self.var, value="Maybe")
        self.label1.pack(anchor='w')
        R1.pack(anchor='w')
        R2.pack(anchor='w')
        R3.pack(anchor='w')

        self.nextButton1 = ttk.Button(self, text="Next",
                                      command=self.question_gui)
        self.nextButton1.pack(padx=30, pady=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        self.progressbar = ttk.Progressbar(self, orient=HORIZONTAL, length=200)
        self.progressbar.pack()
        self.progressbar.config(mode='determinate', maximum=9.0, value=k)
        self.label3 = tk.Label(self, text="")
        self.label3.pack(padx=10, pady=20)

    def question_gui(self):
        global k
        global countNo2
        global a
        global totalMarksFR
        print(countNo2)
        print(self.var.get())
        array10 = [0, 1, 2, 3,4,5, 6, 7,8,9]

        ER = [0, 1, 2, 3, 4, 5, 9]
        AR = [6, 7, 8]
        if (self.var.get() == ''):
            self.label3.configure(text="Please select an option")
            return
        self.label3.configure(text="")
        if (self.var.get() == "Yes" and (k in array10)):
            totalMarksFR = totalMarksFR + 10
            print("totalMarksghgjgj10-1", totalMarksFR)
            if (k in ER):
                self.countER = self.countER + 1
            if (k in AR):
                self.countAR = self.countAR + 1

        if (self.var.get() == "Maybe" and (k in array10)):
            totalMarksFR = totalMarksFR + 5
            print("totalMarks10-2", totalMarksFR)




        if (self.var.get() == "No"):


            if k<3:
                print("countNo", countNo2)
                countNo2 = countNo2 + 1
                if countNo2 == 2:
                    print("about to print not ready gui", countNo2)
                    self.not_ready_gui()
                    return

        if k == 9:
            self.nextButton1.config(text='Results', command=self.results_gui)
        ##        a.append(PageOne)
        listOfQuestionsFR = ['2. Has the telehealth team confirmed the practitioner/provider/facility requirements to get reimbursed by Medicare, Medicaid and other government payers and commercial carriers?',
                             '3. Does the business plan include the initial startup costs to operate the telehealth program?',
                             '4. Is the program scalable beyond the pilot state- such as adding on additional sites or providers?',
                             '5. Has the telehealth team conducted a cost-benefit analysis or an Return on Investment (ROI) of the telehealth program and the technology?',
                             '6. Does your ROI include intangible benefits such as patient and provider satisfaction, decrease in unnecessary referrals and readmission, decrease in length of hospitalization?',
                             '7. Has the telehealth team decided on the average charge for telehealth visits for the pilot and/or the ongoing program?',
                             '8. Does the business plan consider the approximate expected cost reductions, e.g., providers who no longer travel to remote clinics or transportation?',
                             '9. Does the business plan include the monthly cost and network costs of equipment?',
                             '10. Have you checked if your organization is in a designated Health Professional Shortage Area(HPSA)? (http://datawarehouse.hrsa.gov/telehealthAdvisor/telehealthEligibility.aspx.)',
                              ]
        self.label1.config(text=listOfQuestionsFR[k], wraplength=650, justify="left")
        self.label1.update()
        k = k + 1
        print("J", k)
        self.progressbar.config(mode='determinate', maximum=9.0, value=k)


    def results_gui(self):
        global totalMarksFR
        global overallReadinessButtonState
        readiness = ''
        if (self.countER <= 5):
            readiness = 'Early ready'
        if self.countAR >= 2:
            readiness = 'Advanced ready'
        if (self.countER > 5 and self.countAR == 0):
            readiness = 'Early ready'


        label = tk.Label(self, text='', font=SMALL_FONT, justify="center", width=700, height=400)
        label.place(x=0, y=0)
        label1 = tk.Label(self, text="FINANCIAL READINESS", font=LARGE_FONT, justify="center")
        label1.place(x=150, y=20)
        textVar = "You are " +str(totalMarksFR)+ "% financial(" +readiness + ") ready for telehealth. Please proceed with policy readiness survey."

        label1 = tk.Label(self, text=textVar, wraplength = 600, font=SMALL_FONT, justify="center")
        label1.place(x=50,y=120)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: self.controller.show_frame(StartPage))
        button1.place(x=300, y=180)
        overallReadinessButtonState = overallReadinessButtonState + 1
        if (overallReadinessButtonState >= 4):
            print("normalsdfadfadfafa")
            button6.config(state='normal')

    def not_ready_gui(self):
        global overallReadinessButtonState
        label = tk.Label(self, text='', font=SMALL_FONT, justify="center", width=700, height=400)
        label.place(x=0, y=0)
        label1 = tk.Label(self, text="Please reevaluate the basic requirements for telehealth. Research into various telehealth options and decide upon a technology before you proceed with survey. Thank you for taking this survey!", wraplength = 600, font=SMALL_FONT, justify="center")
        label1.place(x=30, y=20)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: self.controller.show_frame(StartPage))
        button1.place(x=300, y=180)
        overallReadinessButtonState = overallReadinessButtonState + 1
        if (overallReadinessButtonState >= 4):
            print("normalsdfadfadfafa")
            button6.config(state='normal')

    def init_window(self):
        self.master.title("Telehealth Readiness Assessment Tool(TRAT)")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)

    def questions(self, hey):
        print(hey)

    def client_exit(self):
        exit()


class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        global l
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.countER = 0
        self.countAR = 0

        label = tk.Label(self, text="POLICY READINESS", font=LARGE_FONT)
        label.pack(pady=10, padx=1)

        self.label1 = tk.Label(self,
                               text="1. Has the telehealth team identified and subsequently confirmed what specific clinical needs will be met using telehealth?",
                               wraplength=650, justify="left")
        self.label1.pack(pady=10, padx=10)

        self.var = tk.StringVar()

        R1 = ttk.Radiobutton(self, text="Yes", variable=self.var, value="Yes")
        R2 = ttk.Radiobutton(self, text="No", variable=self.var, value="No")
        R3 = ttk.Radiobutton(self, text="May be", variable=self.var, value="Maybe")
        self.label1.pack(anchor='w')
        R1.pack(anchor='w')
        R2.pack(anchor='w')
        R3.pack(anchor='w')

        self.nextButton1 = ttk.Button(self, text="Next",
                                      command=self.question_gui)
        self.nextButton1.pack(padx=30, pady=10)

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        self.progressbar = ttk.Progressbar(self, orient=HORIZONTAL, length=200)
        self.progressbar.pack()
        self.progressbar.config(mode='determinate', maximum=10.0, value=l)
        self.label3 = tk.Label(self, text="")
        self.label3.pack(padx=10, pady=20)

    def question_gui(self):
        global l
        global countNo3
        global a
        global totalMarksPR
        print(countNo3)
        print(self.var.get())
        array10 = [0, 1, 2, 4, 5, 6, 7, 8, 10]
        array5 = [3, 9]
        ER = [0, 1, 2, 3, 4, 7, 8, 10]
        AR = [5, 6, 9]

        if (self.var.get() == ''):
            self.label3.configure(text="Please select an option")
            return
        self.label3.configure(text="")
        if (self.var.get() == "Yes" and (l in array10)):
            totalMarksPR = totalMarksPR + 10
            print("totalMarksghgjgj10-1", totalMarksPR)
            if (l in ER):
                self.countER = self.countER + 1
            if (l in AR):
                self.countAR = self.countAR + 1

        if (self.var.get() == "Maybe" and (l in array10)):
            totalMarksPR = totalMarksPR + 5
            print("totalMarks10-2", totalMarksPR)

        if (self.var.get() == "Yes" and (l in array5)):
            totalMarksPR = totalMarksPR + 5
            print("totalMarks5-1", totalMarksPR)
            if (l in ER):
                self.countER = self.countER + 1
            if (l in AR):
                self.countAR = self.countAR + 1

        if (self.var.get() == "Maybe" and (l in array5)):
            totalMarksPR = totalMarksPR + 2.5
            print("totalMarks5-2", totalMarksPR)

        if (self.var.get() == "No"):
            if l <= 2:
                countNo3 = countNo3 + 1
                if countNo3 == 2:
                    print("about to print not ready gui", countNo3)
                    self.not_ready_gui()
                    return

        if l == 10:
            self.nextButton1.config(text='Results', command=self.results_gui)
        ##        a.append(PageOne)
        listOfQuestionsPR = ['2. Have licensing and credentialing policies been evaluated and approved?',
                             '3. Has the organization determined if the use of telehealth technology is relevant to its existing/growing needs and is the program developed so that it is sustainable and scalable to meet those growing needs?',
                             '4. Has the telehealth team considered if the telehealth program would improve HEDIS, CAHPS scores?',
                             '5. Have licensing requirements been met?',
                             '6. Has the malpractice carrier been informed of the scope and policies of the telehealth program?',
                             '7. Have pharmacy regulations been considered, especially for controlled substances?',
                             '8. Has the organization’s privacy and security officer been informed of the business plan, policies and procedures for the telehealth program?',
                             '9. Has the team reviewed any requirements for obtaining patient consent- written or verbal- and if consent is required- has a policy been created for this purpose?',
                             '10. Has the telehealth team developed a policy or protocol for the type of patient who is appropriate or inappropriate for a telehealth visit- taking into consideration patient and staff safety and considering if the patient can be left unattended during the visit?',
                             '11. Has a written procedure manual for using telehealth technology have been developed and shared with all stakeholders and obtained approval by leadership?']
        self.label1.config(text=listOfQuestionsPR[l], wraplength=650, justify="left")
        self.label1.update()
        l = l + 1
        print("J", l)
        self.progressbar.config(mode='determinate', maximum=10.0, value=l)



    def results_gui(self):
        global totalMarksPR
        global overallReadinessButtonState
        readiness = ''
        if (self.countER <= 5):
            readiness = 'Early ready'
        if self.countAR >= 2:
            readiness = 'Advanced ready'
        if (self.countER > 5 and self.countAR == 0):
            readiness = 'Early ready'


        label = tk.Label(self, text='', font=SMALL_FONT, justify="center", width=700, height=400)
        label.place(x=0, y=0)
        label1 = tk.Label(self, text="POLICY READINESS", font=LARGE_FONT, justify="center")
        label1.place(x=170, y=20)
        textVar = "You are " +str(totalMarksPR)+ "% policy(" +readiness + ") ready for telehealth."

        label1 = tk.Label(self, text=textVar, wraplength = 600, font=SMALL_FONT, justify="center")
        label1.place(x=180,y=120)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: self.controller.show_frame(StartPage))
        button1.place(x=300, y=180)
        overallReadinessButtonState = overallReadinessButtonState + 1
        if (overallReadinessButtonState >= 4):
            print("normalsdfadfadfafa")
            button6.config(state='normal')

    def not_ready_gui(self):
        global overallReadinessButtonState
        label = tk.Label(self, text='', font=SMALL_FONT, justify="center", width=700, height=400)
        label.place(x=0, y=0)
        label1 = tk.Label(self, text="Please reevaluate the basic requirements for telehealth. Research into various telehealth options and decide upon a technology before you proceed with survey. Thank you for taking this survey!", wraplength = 600, font=SMALL_FONT, justify="center")
        label1.place(x=30, y=20)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: self.controller.show_frame(StartPage))
        button1.place(x=300, y=180)
        overallReadinessButtonState = overallReadinessButtonState + 1
        print("overallReadinessButtonState", overallReadinessButtonState)
        if (overallReadinessButtonState >= 4):
            print("normalsdfadfadfafa")
            button6.config(state='normal')

    def init_window(self):
        self.master.title("Telehealth Readiness Assessment Tool(TRAT)")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)

    def questions(self, hey):
        print(hey)

    def client_exit(self):
        exit()



class OverallReadiness(tk.Frame):
    def __init__(self, parent, controller):
        global l
        tk.Frame.__init__(self, parent)
        self.controller = controller
        print("CALLING OVERALL")


    def total_marks(self):
        global totalMarksOR, totalMarksTR, totalMarksFR, totalMarksPR
        readiness = ''
        totalMarks = (totalMarksOR + totalMarksTR + totalMarksFR + totalMarksPR) / 4
        if(totalMarks<60):
            readiness = 'Early Ready'
        else:
            readiness = 'Advanced Ready'

        print("totalMarksreeere", totalMarks)
        label = tk.Label(self, text='Overall Score', font=LARGE_FONT, justify="center")
        label.place(x=230, y=20)
        label1 = tk.Label(self, text=str(totalMarks)+readiness, font=SMALL_FONT, justify="center")
        label1.place(x=200, y=80)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: self.controller.show_frame(StartPage))
        button1.place(x=300, y=180)


class About(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


    def about(self):
        about = 'This tool helps organization to assess their readiness for adopting telehealth technologies. It helps to identify the strengths and weakness of the organization. It helps to refocus on programs and improve quality of their telehealth technology efforts.'

        label = tk.Label(self, text='About', font=LARGE_FONT, justify="center")
        label.place(x=280, y=20)
        label1 = tk.Label(self, text=about, wraplength=600, font=SMALL_FONT, justify="center")
        label1.place(x=40,y=80)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: self.controller.show_frame(StartPage))
        button1.place(x=300, y=180)

class Instructions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


    def instructions(self):
        instructions = 'TRAT is a tool to assess entire organization based on 4 main domains: Organizational readiness, Technical, financial and product development and policy readiness. If possible it should be completed as many people/staff as possible within the organization. Each question has YES, NO and MAYBE. User must answer any one of the options provided. Each domain approximately has 10 questions. Only after completing the survey user must click the results button. Once user completes one domain he/she must proceed with other domains. Only after completing survey of all 4 domains user must click “Overall Readiness Score” where we get the final output. It is categorized into two parts: '
        label = tk.Label(self, text='Instructions', font=LARGE_FONT, justify="center")
        label.place(x=265, y=20)
        label1 = tk.Label(self, text=instructions, wraplength=600, font=SMALL_FONT, justify="center")
        label1.place(x=40,y=80)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: self.controller.show_frame(StartPage))
        button1.place(x=300, y=240)

class MainButtonFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Pages = [StartPage, PageOne, PageTwo, PageThree, PageFour, OverallReadiness, About, Instructions]
        for button in Pages:
            NewButton = tk.Button(self, text=str(button),
                                  command=lambda: controller.show_frame(button))
            NewButton.pack()


app = SeaofBTCapp()
app.geometry('{}x{}'.format(700, 400))
app.resizable(width=False, height=False)
app.mainloop()

