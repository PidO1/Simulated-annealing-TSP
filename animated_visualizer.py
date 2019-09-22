import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import csv

names=[]
xs = []
ys = []
with open('Locations.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                # print(f'\t{row[0]} ***** {row[1]} ***** {row[2]}.')
                    names.append(row[0])
                    xs.append(float(row[2]))
                    ys.append(float(row[1]))




def animateTSP(history, points):
    print(points)
    print(history)
   

  
    key_frames_mult = len(history) // 1500

    fig, ax = plt.subplots()
    for i, txt in enumerate(names):
        ax.annotate(txt, (xs[i],ys[i]))
    
    time_text = fig.text(0.02, 0.95, '')

    ''' path is a line coming through all the nodes '''
    line, = plt.plot([], [], lw=2)

    def init():
        ''' initialize node dots on graph '''
        x = [points[i][0] for i in history[0]]
        y = [points[i][1] for i in history[0]]
        time_text.set_text('Start')
        plt.plot(x, y, 'co')

        ''' draw axes slighty bigger  '''
        extra_x = (max(x) - min(x)) * 0.05
        extra_y = (max(y) - min(y)) * 0.05
        ax.set_xlim(min(x) - extra_x, max(x) + extra_x)
        ax.set_ylim(min(y) - extra_y, max(y) + extra_y)

        '''initialize solution to be empty '''
        line.set_data([], [])
        return line, time_text

    def update(frame):
        
        ''' for every frame update the solution on the graph '''
        x = [points[i, 0] for i in history[frame] + [history[frame][0]]]
        y = [points[i, 1] for i in history[frame] + [history[frame][0]]]
        ax.set_title('Frame ' + str(frame))
        line.set_data(x, y)
        
        # time_text.set_text(str(history[frame]))
        return line ,time_text

    ''' animate precalulated solutions '''

    ani = FuncAnimation(fig, update, frames=range(0, len(history), key_frames_mult), #  stuur x points en y points aan en werk die distance uit 
                        init_func=init, interval=3, repeat=False)

    plt.show()
