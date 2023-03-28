import sys
import csv
from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow,QLabel,QVBoxLayout,QHBoxLayout,QPushButton,QFrame
from PyQt5.QtCore import Qt
from itertools import count  

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.animation as animation

class ProjectWindow(QMainWindow):
    # Basic window is popped by QMainWindow tahts why we inherit that

    def __init__(self):
        super().__init__()

        # Setting the window size and name
        self.setWindowTitle("Team-Kalpana-Project")
        self.setGeometry(200,200,1200,800)
        self.setStyleSheet("background-color: #222222;")

        # Create labels and buttons
        self.label = QLabel("Press start to begin", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.update_plot)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.start_button)


        
        # frame_width = int(self.width() * 0.6)
        # self.frame.setMinimumWidth(frame_width)
        # self.frame.setMaximumWidth(frame_width)


        self.label1 = QLabel("", self)
        self.label2 = QLabel("", self)
        self.label3 = QLabel("", self)

        self.tele1 = QLabel("", self)
        self.tele2 = QLabel("", self)
        self.tele3 = QLabel("", self)
        self.tele4 = QLabel("", self)
        self.tele5 = QLabel("", self)
        self.tele6 = QLabel("", self)
        self.tele7 = QLabel("", self)
        self.tele8 = QLabel("", self)

        self.label1.setStyleSheet("background-color: #555555; text-align:center; padding:10px; font-weight:bold; height:100px; border: 1px solid black; max-height: 100px; font-size: 19px; color:white;")
        self.label2.setStyleSheet("background-color: #555555; text-align:center; padding:10px;  font-weight:bold; height:100px; border: 1px solid black; max-height: 100px; font-size: 19px; color:white;")
        self.label3.setStyleSheet("background-color: #555555; text-align:center; padding:10px; font-weight:bold; height:100px; border: 1px solid black; max-height: 100px; font-size: 19px; color:white;")
        
        self.tele1.setStyleSheet("background-color: #555555; text-align:center; padding:10px; font-weight:bold; height:100px; border: 1px solid black; max-height: 100px; font-size: 19px; color:white;")
        self.tele2.setStyleSheet("background-color: #555555; text-align:center; padding:10px; font-weight:bold; height:100px; border: 1px solid black; max-height: 100px; font-size: 19px; color:white;")
        self.tele3.setStyleSheet("background-color: #555555; text-align:center; padding:10px; font-weight:bold; height:100px; border: 1px solid black; max-height: 100px; font-size: 19px; color:white;")
        self.tele4.setStyleSheet("background-color: #555555; text-align:center; padding:10px; font-weight:bold; height:100px; border: 1px solid black; max-height: 100px; font-size: 19px; color:white;")
        self.tele5.setStyleSheet("background-color: #555555; text-align:center; padding:10px; font-weight:bold; height:100px; border: 1px solid black; max-height: 100px; font-size: 19px; color:white;")
        self.tele6.setStyleSheet("background-color: #555555; text-align:center; padding:10px; font-weight:bold; height:100px; border: 1px solid black; max-height: 100px; font-size: 19px; color:white;")
        self.tele7.setStyleSheet("background-color: #555555; text-align:center; padding:10px; font-weight:bold; height:100px; border: 1px solid black; max-height: 100px; font-size: 19px; color:white;")
        self.tele8.setStyleSheet("background-color: #555555; text-align:center; padding:10px; font-weight:bold; height:100px; border: 1px solid black; max-height: 100px; font-size: 19px; color:white;")
       
        self.label1.setAlignment(Qt.AlignCenter)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label3.setAlignment(Qt.AlignCenter)

        self.tele1.setAlignment(Qt.AlignCenter)
        self.tele2.setAlignment(Qt.AlignCenter)
        self.tele3.setAlignment(Qt.AlignCenter)
        self.tele4.setAlignment(Qt.AlignCenter)
        self.tele5.setAlignment(Qt.AlignCenter)
        self.tele6.setAlignment(Qt.AlignCenter)
        self.tele7.setAlignment(Qt.AlignCenter)
        self.tele8.setAlignment(Qt.AlignCenter)

        self.frame = QFrame(self)
        # self.frame.setStyleSheet("max-height:450px; background-color: #2A2A2A;")
        vbox = QVBoxLayout(self.frame)

        self.labelFrame = QFrame(self)
        self.labelFrame.setStyleSheet("max-height:450px; background-color: #2A2A2A;")
        labelBox = QVBoxLayout(self.labelFrame)

        self.teleFrame = QFrame(self)
        self.teleFrame.setStyleSheet("max-height:450px; background-color: #2A2A2A;")
        teleBox = QHBoxLayout(self.teleFrame)

        self.teleLeftFrame = QFrame(self)
        self.teleLeftFrame.setStyleSheet("max-height:450px; background-color: #2A2A2A;")
        teleLeftBox = QVBoxLayout(self.teleLeftFrame)

        self.teleRightFrame = QFrame(self)
        self.teleRightFrame.setStyleSheet("max-height:450px; background-color: #2A2A2A;")
        teleRightBox = QVBoxLayout(self.teleRightFrame)

        labelBox.addWidget(self.label1)
        labelBox.addWidget(self.label2)
        labelBox.addWidget(self.label3)

        teleLeftBox.addWidget(self.tele1)
        teleLeftBox.addWidget(self.tele2)
        teleLeftBox.addWidget(self.tele3)
        teleLeftBox.addWidget(self.tele4)

        teleRightBox.addWidget(self.tele5)
        teleRightBox.addWidget(self.tele6)
        teleRightBox.addWidget(self.tele7)
        teleRightBox.addWidget(self.tele8)

        teleBox.addWidget(self.teleLeftFrame)
        teleBox.addWidget(self.teleRightFrame)

        vbox.addWidget(self.labelFrame)
        vbox.addWidget(self.teleFrame)


        # self.layout.addWidget(self.frame)
        
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
    

    def update_plot(self):

        global pointer
        global rollSeq1,rollTotals1,index1
        global rollSeq2,rollTotals2,index2
        global rollSeq3,rollTotals3,index3

        pointer=1
        numRolls = 300

        index1=count()
        index2=count()
        index3=count()
     
        rollTotals1 = []
        rollTotals2 = []
        rollTotals3 = []

        rollSeq1 = []
        rollSeq2 = []
        rollSeq3 = []


        self.infoFrame = QFrame(self)
        self.infoFrame.setStyleSheet("background-color: #201E20;")
        infoBox = QHBoxLayout(self.infoFrame)


        self.headFrame = QFrame(self)
        self.headFrame.setStyleSheet("background-color: #201E20;")
        headBox = QVBoxLayout(self.headFrame)
        
        

        heading = QLabel("Team Kalpana")
        heading.setAlignment(Qt.AlignCenter)
        heading.setStyleSheet("font-size: 24px; font-weight: bold; color:white;")

        subheading = QLabel("Team ID: #abc")
        subheading.setAlignment(Qt.AlignCenter)
        subheading.setStyleSheet("font-size: 16px; font-weight: normal; color:white;")

        headBox.addWidget(heading)
        headBox.addWidget(subheading)
        infoBox.addWidget(self.headFrame)

        self.leftmenu = QFrame(self)
        self.leftmenu.setObjectName("leftmenu")
        self.leftmenu.setStyleSheet("#leftmenu { border-radius: 10px; background-color: #3D3D3D; }")
        # self.leftmenu.setStyleSheet(
        #     "background-color: #3D3D3D;",
        #     "border-top-left-radius :35px;",
        #     "border-top-right-radius : 20px;",
        #     "border-bottom-left-radius : 50px;",
        #     "border-bottom-right-radius : 10px"
        # )
        left_side = QVBoxLayout(self.leftmenu)


        #  CREATING BUTTON CONTAINER

        self.main_btn_frame = QFrame(self)
        self.main_btn_frame.setStyleSheet("background-color: #2A2A2A;")
        main_btnbox = QVBoxLayout(self.main_btn_frame)


        self.btnFrame = QFrame(self)
        self.btnFrame.setStyleSheet("background-color: #2A2A2A; height:25%;")
        btnbox = QHBoxLayout(self.btnFrame)

        self.halfbtnFrame = QFrame(self)
        self.halfbtnFrame.setStyleSheet("background-color: #2A2A2A;")
        halfbtnbox = QVBoxLayout(self.halfbtnFrame)

        commandHeader = QLabel("COMMANDS")
        commandHeader.setAlignment(Qt.AlignCenter)
        commandHeader.setStyleSheet("font-size: 24px; font-weight: bold; color:white; height:10%;")

        self.otherhalfbtn = QFrame(self)
        self.otherhalfbtn.setStyleSheet("background-color: #2A2A2A;")
        otherbtnbox = QVBoxLayout(self.otherhalfbtn)

        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")
        button4 = QPushButton("Button 4")
        button5 = QPushButton("Button 5")
        button6 = QPushButton("Button 6")
        button7 = QPushButton("Button 7")
        button8 = QPushButton("Button 8")

        button1.setStyleSheet("QPushButton { background-color: #1C72B1; padding:20px; color: white; font-weight: bold; border-radius:12px; font-size: 18px; margin:10px;} \QPushButton:hover { background-color: #1C94E0; }")
        button2.setStyleSheet("QPushButton { background-color: #1C72B1; padding:20px; color: white; font-weight: bold; border-radius:12px; font-size: 18px; margin:10px;} \QPushButton:hover { background-color: #1C94E0; }")
        button3.setStyleSheet("QPushButton { background-color: #1C72B1; padding:20px; color: white; font-weight: bold; border-radius:12px; font-size: 18px; margin:10px;} \QPushButton:hover { background-color: #1C94E0; }")
        button4.setStyleSheet("QPushButton { background-color: #1C72B1; padding:20px; color: white; font-weight: bold; border-radius:12px; font-size: 18px; margin:10px;} \QPushButton:hover { background-color: #1C94E0; }")
        button5.setStyleSheet("QPushButton { background-color: #1C72B1; padding:20px; color: white; font-weight: bold; border-radius:12px; font-size: 18px; margin:10px;} \QPushButton:hover { background-color: #1C94E0; }")
        button6.setStyleSheet("QPushButton { background-color: #1C72B1; padding:20px; color: white; font-weight: bold; border-radius:12px; font-size: 18px; margin:10px;} \QPushButton:hover { background-color: #1C94E0; }")
        button7.setStyleSheet("QPushButton { background-color: #1C72B1; padding:20px; color: white; font-weight: bold; border-radius:12px; font-size: 18px; margin:10px;} \QPushButton:hover { background-color: #1C94E0; }")
        button8.setStyleSheet("QPushButton { background-color: #1C72B1; padding:20px; color: white; font-weight: bold; border-radius:12px; font-size: 18px; margin:10px;} \QPushButton:hover { background-color: #1C94E0; }")

        halfbtnbox.addWidget(button1)
        halfbtnbox.addWidget(button2)
        halfbtnbox.addWidget(button3)
        halfbtnbox.addWidget(button4)
        otherbtnbox.addWidget(button5)
        otherbtnbox.addWidget(button6)
        otherbtnbox.addWidget(button7)
        otherbtnbox.addWidget(button8)
        
        btnbox.addWidget(self.halfbtnFrame)
        btnbox.addWidget(self.otherhalfbtn)
        
        main_btnbox.addWidget(commandHeader)
        main_btnbox.addWidget(self.btnFrame)
        

        left_side.addWidget(self.infoFrame)
        
        left_side.addWidget(self.main_btn_frame)



        self.mainframe = QFrame(self)
        self.mainframe.setStyleSheet("background-color: #201E20; border-radius: 10px;")
        vmbox = QHBoxLayout(self.mainframe)
        

    
        self.frame2 = QFrame(self)
        self.frame2.setStyleSheet("border-radius:10px; background-color: #2A2A2A;")
        figure_graph = plt.figure(facecolor='none')
        canvas_graph = FigureCanvas(figure_graph)
        canvas_graph.setAttribute(Qt.WA_OpaquePaintEvent, False)


        vbox3 = QVBoxLayout(self.frame2)
        vbox3.addWidget(canvas_graph)

        vmbox.addWidget(self.leftmenu)
        vmbox.addWidget(self.frame)
        vmbox.addWidget(self.frame2)
        
        
        self.layout.removeWidget(self.start_button)
        self.layout.addWidget(self.mainframe)
        

        self.ax1 = figure_graph.add_subplot(3,1,1)
        self.ax2 = figure_graph.add_subplot(3,1,2)
        self.ax3 = figure_graph.add_subplot(3,1,3)
        
        plt.subplots_adjust(top = 0.93, bottom = 0.07, hspace = 0.45,wspace=0.3)
        self.ani = animation.FuncAnimation(figure_graph, self.animate, frames=numRolls, interval=1000, repeat=False)


        canvas_graph.draw()


    def animate(self,i):
        global pointer
        with open("data.csv", 'r') as file:
            csvreader = csv.reader(file)
            row_counter = 0
            for row in csvreader:
                if row_counter == pointer:
                    currentRoll1 = row[6]
                    currentRoll2 = row[7]
                    currentRoll3 = row[8]

                    mission_time = row[1]
                    packet_count = row[2]
                    packet_type = row[3]
                    mode = row[4]
                    payload = row[5]
                    altitude = row[6]
                    temp = row[7]
                    voltage = row[8]

                    pointer+=1
                    break
                row_counter+=1


        # Drawing altitude graph
        currentRoll1=float(currentRoll1)
        rollTotals1.append(next(index1)) 
        rollSeq1.append(currentRoll1)
        self.ax1.clear()
        self.ax1.plot(rollTotals1,rollSeq1,color='#1F402B')
        xlim = len(rollSeq1)
        self.ax1.set_xlim(xlim - 30, xlim)
        self.ax1.set_title("Altitude",fontsize=22)

        self.ax1.spines['bottom'].set_color('white')
        self.ax1.spines['left'].set_color('white')
        self.ax1.patch.set_facecolor('lightgray')
        self.ax1.tick_params(axis='x', colors='white')
        self.ax1.tick_params(axis='y', colors='white')
        self.ax1.xaxis.label.set_color('white')
        self.ax1.yaxis.label.set_color('white')
        self.ax1.spines[['right', 'top']].set_visible(False)
        self.ax1.title.set_color('white')
        self.ax1.title.set_fontsize(16)
        self.ax1.title.set_fontweight('bold')



        # Drawing temperature graph
        currentRoll2 = float(currentRoll2)
        rollTotals2.append(next(index2)) 
        rollSeq2.append(currentRoll2)
        self.ax2.clear()
        self.ax2.plot(rollTotals2,rollSeq2,color='#1F402B')
        xlim = len(rollSeq2)
        self.ax2.set_xlim(xlim - 30, xlim)

        self.ax2.spines['bottom'].set_color('white')
        self.ax2.spines['left'].set_color('white')
        self.ax2.patch.set_facecolor('lightgray')
        self.ax2.tick_params(axis='x', colors='white')
        self.ax2.tick_params(axis='y', colors='white')
        self.ax2.xaxis.label.set_color('white')
        self.ax2.yaxis.label.set_color('white')
        self.ax2.spines[['right', 'top']].set_visible(False)
        self.ax2.title.set_color('white')
        self.ax2.title.set_fontsize(16)
        self.ax2.title.set_fontweight('bold')


        # Drawing voltage graph
        currentRoll3 = float(currentRoll3)
        rollTotals3.append(next(index3)) 
        rollSeq3.append(currentRoll3)
        self.ax3.clear()
        self.ax3.plot(rollTotals3,rollSeq3,color='#1F402B')
        xlim = len(rollSeq3)
        self.ax3.set_xlim(xlim - 30, xlim)
        self.ax2.set_title("Temperature",fontsize=22)
        self.ax3.set_title("Voltage",fontsize=22)

        self.ax3.spines['bottom'].set_color('white')
        self.ax3.spines['left'].set_color('white')
        self.ax3.patch.set_facecolor('lightgray')
        self.ax3.tick_params(axis='x', colors='white')
        self.ax3.tick_params(axis='y', colors='white')
        self.ax3.xaxis.label.set_color('white')
        self.ax3.yaxis.label.set_color('white')
        self.ax3.spines[['right', 'top']].set_visible(False)
        self.ax3.title.set_color('white')
        self.ax3.title.set_fontsize(16)
        self.ax3.title.set_fontweight('bold')
        
        self.label1.setText(f"Mission Time: {mission_time}")
        self.label2.setText(f"Packet Recieved: {packet_count}")
        self.label3.setText(f"Packet Type: {packet_type}")


        self.tele1.setText(f"Mission Time: {mission_time}")
        self.tele2.setText(f"Packet Count: {packet_count}")
        self.tele3.setText(f"Packet Type: {packet_type}")
        self.tele4.setText(f"Mode: {mode}")
        self.tele5.setText(f"Payload: {payload}")
        self.tele6.setText(f"Altitude: {altitude}")
        self.tele7.setText(f"Temperature: {temp}")
        self.tele8.setText(f"Voltage: {voltage}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProjectWindow()
    window.show()
    sys.exit(app.exec_())