"""
 File contains class "Plot". This class using for create charts.
"""
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from colors import *
from matplotlib.pyplot import *
from numpy import array


class Plot:
    def __init__(self, window, x, y, name: str, unit, x1, y1):
        self.window = window
        self.xdat = x
        self.x = array(x)
        self.y = array(y)
        self.title = name
        self.x1 = x1
        self.y1 = y1
        self.unit = unit
        self.plot()

    def __init_plot(self):
        fig = Figure(figsize=(7, 2.5), facecolor=main_color_gray)
        a = fig.add_subplot(111)
        a.grid()
        return fig, a

    def __draw(self, fig: Figure):

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()

    def __set_label_and_title(self, a: axis):
        a.set_title(self.title, font='Tahoma', fontsize=18, color=tertiary_color_very_light)
        a.set_ylabel(self.unit, font='Tahoma', fontsize=14, color=tertiary_color_very_light)

    def __xtick_label(self, a, x):
        a.set_xticks(range(0, len(x), 9))
        a.set_xticklabels(self.xdat[0:len(self.xdat):9])

    def plot(self):
        if self.x1 != 0 and self.y1 != 0:
            y = self.y
            y1 = array(self.y1)
            fig, a = self.__init_plot()
            a.plot(range(len(y)),
                   y,
                   color=secondary_color_black,
                   linestyle='-',
                   linewidth=2,
                   label="Верхнее давление")
            a.plot(range(len(y1)),
                   y1,
                   color=secondary_color_black,
                   linestyle='--',
                   linewidth=2,
                   label="Нижнее давление")

            a.legend(loc="upper right", fontsize=10)
            for side in ['bottom', 'top', 'left', 'right']:
                a.spines[side].set_color(tertiary_color_very_light)
            a.tick_params(axis='both', colors=tertiary_color_very_light)
            self.__set_label_and_title(a)
            self.__xtick_label(a, self.x)

            self.__draw(fig)
        else:
            x = self.x
            y = self.y
            fig, a = self.__init_plot()
            a.plot(range(len(y)), y, color=secondary_color_black, label=title)
            self.__set_label_and_title(a)
            a.legend(self.title, loc="upper right", fontsize=10)
            for side in ['bottom', 'top', 'left', 'right']:
                a.spines[side].set_color(tertiary_color_very_light)
            a.tick_params(axis='both', colors=tertiary_color_very_light)
            self.__set_label_and_title(a)
            self.__xtick_label(a, x)
            self.__draw(fig)
