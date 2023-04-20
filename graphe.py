import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import csv

plt.style.use('dark_background')

x_values = []
y_values = []
moving_avg = []

fig, ax = plt.subplots()

def animate(i, x_values, y_values, moving_avg):

    del x_values[:]
    del y_values[:]
    del moving_avg[:]

    with open('data.csv','r') as csvfile:
        tableau = csv.reader(csvfile, delimiter='/')
        for column in tableau:
            x_values.append(column[1])
            y_values.append(float(column[0]))
            moving_avg.append(float(column[2]))

    ax.plot(x_values, y_values, color = '#b21f1f', linestyle = 'solid', marker = ',')
    ax.plot(x_values, moving_avg, color = '#F3F9A7', linestyle = 'dashed')

    ax.legend(['cours actuel' , 'moyenne mobile'], loc="lower right")    
    ax.set_xlabel("Date et heure")
    ax.set_ylabel("Valeur du Bitcoin en € ")
    ax.set_title("Cours du Bitcoin", fontsize = 15)
    plt.tight_layout()
    plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
    ax.set_xticks([0,9,19,29,39,49,59])

ani = FuncAnimation(fig, animate, fargs=(x_values,y_values,moving_avg))
plt.show()