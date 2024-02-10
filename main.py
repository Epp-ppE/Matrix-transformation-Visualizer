import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def vplot(v, style, label, linewidth=1):
        plt.plot([0,v[0]], [0,v[1]], style, label = label, linewidth=linewidth)
        # Add an arrowhead to the line
        plt.annotate('', xy=(v[0], v[1]), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=style[0]))
        

class LA_2DTransfomation(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        vbox = QVBoxLayout()
        self.setWindowTitle("Linear Algebra 2D Transformation")
        self.label = QLabel(self)
        self.label.setText("This program show the \n2D transformation of a 2D vector")
        self.label.setStyleSheet("font-size: 18px;\n font-weight: bold;")
        self.label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.label)
        
        self.inputlabel1 = QLabel(self)
        self.inputlabel1.setText("Input 2x2 Matrix [[a,c],[b,d]]: as a,c,b,d")
        self.inputlabel1.setStyleSheet("font-size: 12px;")
        vbox.addWidget(self.inputlabel1)
        self.input2x2 = QLineEdit(self)
        vbox.addWidget(self.input2x2)
        self.inputlabel2 = QLabel(self)
        self.inputlabel2.setText("Input 2D vector [x,y]: as x,y")
        self.inputlabel2.setStyleSheet("font-size: 12px;")
        vbox.addWidget(self.inputlabel2)
        self.input1x2 = QLineEdit(self)
        vbox.addWidget(self.input1x2)
        
        self.listlabel = QLabel(self)
        self.listlabel.setText("List of transformation matrix")
        self.listlabel.setStyleSheet("font-size: 12px;")
        vbox.addWidget(self.listlabel)
        self.list = QListWidget(self)
        self.list.addItem("Sheer:1,0,1,1")
        self.list.addItem("Scale:2,0,0,2")
        self.list.addItem("Rotate-90 CW:0,-1,1,0")
        self.list.addItem("Rotate-90 CCW:0,1,-1,0")
        self.list.addItem("Reflection:-1,0,0,1")
        self.list.addItem("Projection_x:1,0,0,0")
        self.list.addItem("Projection_y:0,0,0,1")
        self.list.addItem("Reflection_xy:0,1,1,0")
        vbox.addWidget(self.list)
        self.list.itemClicked.connect(self.listClicked)
        self.list.setCurrentRow(0)
        self.list.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.list.setFixedHeight(150)
        self.list.setFixedWidth(200)
        self.list.setWordWrap(True)
        self.list.setAlternatingRowColors(True)
        self.plot_button = QPushButton("Plot", self)
        self.plot_button.clicked.connect(self.plot)
        vbox.addWidget(self.plot_button)
        self.animated_plot_button = QPushButton("See transformation", self)
        self.animated_plot_button.clicked.connect(self.animated_plot)
        vbox.addWidget(self.animated_plot_button)
        self.setLayout(vbox)
        self.show()
        
        
        self.max = 0
        self.animation = None

    def listClicked(self, item):
        self.input2x2.setText(item.text().split(":")[1])
        return
    

    def plot(self):
        try:
            self.max = 0
            transformation_matrix = self.get2x2Matrix()
            vector = self.get1x2Matrix()
            unit_vectorX = np.array([1, 0])
            unit_vectorY = np.array([0, 1])
            transformed_vector = np.dot(vector, transformation_matrix)
            #get length of this vector
            if self.max < np.linalg.norm(transformed_vector):
                self.max = np.linalg.norm(transformed_vector)
            transformed_unit_vectorX = np.array(transformation_matrix[0])
            if self.max < np.linalg.norm(transformed_unit_vectorX):
                self.max = np.linalg.norm(transformed_unit_vectorX)
            transformed_unit_vectorY = np.array(transformation_matrix[1])
            if self.max < np.linalg.norm(transformed_unit_vectorY):
                self.max = np.linalg.norm(transformed_unit_vectorY)
            self.max *= 1.1

            
        except:
            Error = QDialog(self)
            Error_layout = QVBoxLayout()
            Error.setWindowTitle("Error")
            Error.setStyleSheet("background-color: rgb(255, 0, 0);")
            Error_label = QLabel(self)
            Error_label.setText("Invalid input")
            Error_label.setStyleSheet("font-size: 18px;\n font-weight: bold;")
            Error_label.setAlignment(Qt.AlignCenter)
            Error_layout.addWidget(Error_label)
            close_button = QPushButton("Close", self)
            close_button.clicked.connect(Error.close)
            Error_layout.addWidget(close_button)
            Error.setLayout(Error_layout)
            Error.show()

        vplot(unit_vectorX, 'r--', 'unit vector x', 2)
        vplot(unit_vectorY, 'b--', 'unit vector y', 2)
        vplot(vector, 'g--', 'original vector', 2)
        vplot(transformed_unit_vectorX, 'r', 'transformed unit vector x')
        vplot(transformed_unit_vectorY, 'b', 'transformed unit vector y')
        vplot(transformed_vector, 'g', 'transformed vector')
        plt.axis('square')
        plt.axis([-self.max,self.max,-self.max,self.max])
        plt.grid()
        plt.legend()
        plt.show()
        
        return
    
    def animated_plot(self):
        try:
            self.max = 0
            transformation_matrix = self.get2x2Matrix()
            vector = self.get1x2Matrix()
            unit_vectorX = np.array([1, 0])
            unit_vectorY = np.array([0, 1])
            transformed_vector = np.dot(vector, transformation_matrix)
            #get length of this vector
            if self.max < np.linalg.norm(transformed_vector):
                self.max = np.linalg.norm(transformed_vector)
                print(self.max)
            transformed_unit_vectorX = np.array(transformation_matrix[0])
            if self.max < np.linalg.norm(transformed_unit_vectorX):
                self.max = np.linalg.norm(transformed_unit_vectorX)
                print(self.max)
            transformed_unit_vectorY = np.array(transformation_matrix[1])
            if self.max < np.linalg.norm(transformed_unit_vectorY):
                self.max = np.linalg.norm(transformed_unit_vectorY)
                print(self.max)
            self.max *= 1.1
            print(self.max)
            
        except:
            Error = QDialog(self)
            Error_layout = QVBoxLayout()
            Error.setWindowTitle("Error")
            Error_label = QLabel(self)
            Error_label.setText("Invalid input")
            Error_label.setStyleSheet("font-size: 18px;\n font-weight: bold;")
            Error_label.setAlignment(Qt.AlignCenter)
            Error_layout.addWidget(Error_label)
            close_button = QPushButton("Close", self)
            close_button.clicked.connect(Error.close)
            Error_layout.addWidget(close_button)
            Error.setLayout(Error_layout)
            Error.show()

        fig, ax = plt.subplots()

        def update(frame):
            ax.clear()

            ax.plot([0, vectors[frame][0]], [0, vectors[frame][1]], 'g-', label='Vector v')
            ax.annotate('', xy=(vectors[frame][0], vectors[frame][1]), xytext=(0, 0),
                        arrowprops=dict(arrowstyle='->', color='g'))

            ax.plot([0, unit_vX[frame][0]], [0, unit_vX[frame][1]], 'r-', label='Unit vector x')
            ax.annotate('', xy=(unit_vX[frame][0], unit_vX[frame][1]), xytext=(0, 0),
                        arrowprops=dict(arrowstyle='->', color='r'))
            
            ax.plot([0, unit_vY[frame][0]], [0, unit_vY[frame][1]], 'b-', label='Unit vector y')
            ax.annotate('', xy=(unit_vY[frame][0], unit_vY[frame][1]), xytext=(0, 0),
                        arrowprops=dict(arrowstyle='->', color='b'))

            # ax.set_xlim(0, max(1, max(vectors[frame][0], vectors[frame][1])))
            # ax.set_ylim(0, max(1, max(vectors[frame][0], vectors[frame][1])))
            ax.axis('square')
            ax.axis([-self.max, self.max, -self.max, self.max])
            ax.grid(True)
            ax.legend()

        # Create the animation
        vectors = np.vstack([np.linspace(vector, transformed_vector, 100)])
        unit_vX = np.vstack([np.linspace(unit_vectorX, transformed_unit_vectorX, 100)])
        unit_vY =  np.vstack([np.linspace(unit_vectorY, transformed_unit_vectorY, 100)])

        animation = FuncAnimation(fig, update, frames=len(vectors), interval=50, repeat=True, repeat_delay=3000)
        self.animation = animation
        plt.show()


    def get2x2Matrix(self):
        matrix = self.input2x2.text()
        matrix = matrix.split(",")
        print(matrix)
        if len(matrix) != 4:
            print("length != 4")
            raise Exception("Invalid input")
        for i in range(4):
            print(matrix[i])
            if not matrix[i].lstrip('+-').isnumeric():
                print("matrix not numeric")
                raise Exception("Invalid input")
            if abs(float(matrix[i])) > self.max:
                self.max = float(matrix[i])
        matrix = [float(i) for i in matrix]
        # print(matrix)
        matrix = np.array(matrix).reshape(2,2)
        return matrix
    
    def get1x2Matrix(self):
        vector = self.input1x2.text()
        vector = vector.split(",")
        # print(vector)
        if len(vector) != 2:
            print("length != 2")
            raise Exception("Invalid input")
        for i in range(2):
            if not vector[i].lstrip('+-').isnumeric():
                print("vector not numeric")
                raise Exception("Invalid input")
            if abs(float(vector[i])) > self.max:
                self.max = float(vector[i])
        vector = [float(i) for i in vector]
        print(vector)
        vector = np.array(vector)
        return vector

    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LA_2DTransfomation()
    sys.exit(app.exec())