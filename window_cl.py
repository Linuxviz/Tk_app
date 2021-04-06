from tkinter import Tk, Label, Button, Entry, PhotoImage, StringVar, CENTER, Frame
import plot
import data_cl
from colors import *

PASS = '1239'


class Window:

    def __init__(self):
        self.win_width = 400
        self.win_height = 800
        self.font = 'Tahoma'
        self.background_color = main_color_gray
        self.title = ''
        self.root = Tk()
        self.root.resizable(width=False, height=False)

    def _special_initialization(self):
        """В этом методе в дочерних классах описывается спецефичное для них поведение во инициализации их параметров"""
        return 0

    def create(self):
        """Публичный метод проводящий инициализацию виджетов tk внутри открытого окна"""
        self.root.geometry(str(self.win_width) + 'x' + str(self.win_height))
        self.root['bg'] = self.background_color
        self.root.title(self.title)
        self._special_initialization()

        self.root.mainloop()

    def _close_button(self, root, text):
        close_button_submit = Button(root,
                                     text=text,
                                     background=main_color_black,
                                     activebackground=main_color_very_light,
                                     activeforeground=secondary_color_very_light,
                                     foreground=secondary_color_very_light,
                                     padx="20",  # отступ от границ до содержимого по горизонтали
                                     pady="8",  # отступ от границ до содержимого по вертикали
                                     font="16",  # высота шрифта
                                     command=self.stop)
        return close_button_submit

    def stop(self):
        self.root.destroy()


class ReminderWindow(Window):
    """Окно напоминания"""

    def __init__(self):
        super().__init__()
        self.title = 'Напоминание'
        self.win_height = 180
        self.win_width = 300
        self.ready = False

    def is_ready(self):
        return self.ready

    def __ready(self):
        self.ready = True
        self.root.quit()

    def _special_initialization(self):
        authorization_text = Label(self.root,
                                   text="У тебя много дел на сегодня!",
                                   background=main_color_gray,
                                   foreground=tertiary_color_very_light,
                                   anchor='center',
                                   font=self.font + ' 15')
        authorization_button_submit = Button(self.root,
                                             text="Готов их сделать!",
                                             background=main_color_black,
                                             activebackground=main_color_very_light,
                                             activeforeground=secondary_color_very_light,
                                             foreground=secondary_color_very_light,
                                             padx="20",  # отступ от границ до содержимого по горизонтали
                                             pady="8",  # отступ от границ до содержимого по вертикали
                                             font="16",  # высота шрифта
                                             command=self.__ready)
        close_button_submit = self._close_button(self.root, "Позже")
        authorization_text.pack(pady=9, expand=1, anchor='n')
        authorization_button_submit.pack(pady=9, expand=1)
        close_button_submit.pack(pady=9, expand=1)


class AuthorizationWindow(Window):
    """Класс окна отвечающего за авторизацию пользователя"""

    def __init__(self):
        super().__init__()
        self.win_height = 300
        self.win_width = 300
        self.title = 'Авторизация'
        self.true_password = PASS
        self.input_password = StringVar()
        self.flag = False
        self.authorization_complete = False

    def is_authorization_complete(self):
        """Метод возвращает состояние поля с успешной атворизацией"""
        return self.authorization_complete

    def __is_user(self, password: str) -> bool:
        """ Проверка пароля """
        if password == self.true_password:
            return True
        else:
            return False

    def __authorization(self):
        """Метод вызываемый при нажатии кнопки, вызывает сравнение пароля введенного пользователем и
        тем что лежит в классе"""
        password = self.input_password.get()
        if self.__is_user(password):
            self.authorization_complete = True
            self.root.quit()
        else:
            if self.flag:
                self.error_text.configure(text='До сих пор не подошел')
                self.error_text.pack()
            else:
                self.flag = True
                self.error_text.pack()

    def _special_initialization(self):
        authorization_text = Label(self.root,
                                   text="Это точно ты? Введи пароль!",
                                   background=main_color_gray,
                                   foreground=tertiary_color_very_light,
                                   anchor='center',
                                   font=self.font + ' 15')
        authorization_password = Entry(self.root,
                                       width=15,
                                       background=main_color,
                                       foreground=tertiary_color_very_light,
                                       textvariable=self.input_password,
                                       justify='center',
                                       font=self.font + ' 15')
        self.error_text = Label(self.root,
                                text="Ошибка, пароль не подошел",
                                justify="center",
                                anchor='center',
                                background=main_color_gray,
                                foreground=tertiary_color_very_light,
                                font=self.font + ' 15')
        authorization_button_submit = Button(self.root,
                                             text="Ввести",
                                             background=main_color_black,
                                             activebackground=main_color_very_light,
                                             activeforeground=secondary_color_very_light,
                                             foreground=secondary_color_very_light,
                                             padx="20",  # отступ от границ до содержимого по горизонтали
                                             pady="8",  # отступ от границ до содержимого по вертикали
                                             font="16",  # высота шрифта
                                             command=self.__authorization
                                             )
        close_button_submit = self._close_button(self.root, "Позже")

        authorization_text.pack(pady=9, expand=1, anchor='n')
        authorization_password.pack(pady=5, expand=1, anchor='n')
        authorization_button_submit.pack(pady=9, expand=1, anchor='n')
        close_button_submit.pack(pady=9, expand=1, anchor='n')


class MainWindow(Window):
    def __init__(self):
        super().__init__()
        self.title = 'Основная информация'
        self.win_height = 750
        self.win_width = 926
        self.input_mass = StringVar()
        self.input_top_pressure = StringVar()
        self.input_bottom_pressure = StringVar()
        self.input_pulse = StringVar()

    def __compute_data(self):
        data = data_cl.Data()
        # ВНЕСТИ ПРОВЕРКИ
        data.save_data(self.input_mass.get(),
                       self.input_top_pressure.get(),
                       self.input_bottom_pressure.get(),
                       self.input_pulse.get())

        self.mass_text.destroy()
        self.mass_entry.destroy()
        self.top_pressure_text.destroy()
        self.top_pressure_entry.destroy()
        self.bottom_pressure_text.destroy()
        self.bottom_pressure_entry.destroy()
        self.pulse.destroy()
        self.pulse_entry.destroy()
        self.button_submit.destroy()
        self.close_button_submit.destroy()
        text = Label(self.inform_frame,
                     text="Успешно",
                     background=main_color_gray,
                     foreground=tertiary_color_very_light,
                     anchor='center',
                     font=self.font + ' 15', )
        text.pack(anchor='center')

    def _special_initialization(self):
        graph_frame = Frame(self.root, background=main_color_gray)
        self.inform_frame = Frame(self.root, background=main_color_gray)
        graph_frame.pack(
                side='left',
                fill='both',
        )
        self.inform_frame.pack(
                fill='both',
                side='left',
                padx=25
        )

        self.mass_text = Label(self.inform_frame,
                               text="Масса",
                               background=main_color_gray,
                               foreground=tertiary_color_very_light,
                               anchor='center',
                               font=self.font + ' 15')
        self.mass_entry = Entry(self.inform_frame,
                                textvariable=self.input_mass,
                                width=15,
                                background=main_color,
                                foreground=tertiary_color_very_light,
                                justify='center',
                                font=self.font + ' 15')
        self.top_pressure_text = Label(self.inform_frame,
                                       text="Верхнее давление",
                                       background=main_color_gray,
                                       foreground=tertiary_color_very_light,
                                       anchor='center',
                                       font=self.font + ' 15')
        self.top_pressure_entry = Entry(self.inform_frame,
                                        textvariable=self.input_top_pressure,
                                        width=15,
                                        background=main_color,
                                        foreground=tertiary_color_very_light,
                                        justify='center',
                                        font=self.font + ' 15')
        self.bottom_pressure_text = Label(self.inform_frame,
                                          text="Нижнее давление",
                                          background=main_color_gray,
                                          foreground=tertiary_color_very_light,
                                          anchor='center',
                                          font=self.font + ' 15')
        self.bottom_pressure_entry = Entry(self.inform_frame,
                                           textvariable=self.input_bottom_pressure,
                                           width=15,
                                           background=main_color,
                                           foreground=tertiary_color_very_light,
                                           justify='center',
                                           font=self.font + ' 15')
        self.pulse = Label(self.inform_frame,
                           text="Пульс",
                           background=main_color_gray,
                           foreground=tertiary_color_very_light,
                           anchor='center',
                           font=self.font + ' 15')
        self.pulse_entry = Entry(self.inform_frame,
                                 textvariable=self.input_pulse,
                                 width=15,
                                 background=main_color,
                                 foreground=tertiary_color_very_light,
                                 justify='center',
                                 font=self.font + ' 15')

        self.button_submit = Button(self.inform_frame,
                                    text="Внести",
                                    background=main_color_black,
                                    activebackground=main_color_very_light,
                                    activeforeground=secondary_color_very_light,
                                    foreground=secondary_color_very_light,
                                    padx="20",  # отступ от границ до содержимого по горизонтали
                                    pady="8",  # отступ от границ до содержимого по вертикали
                                    font="16",  # высота шрифта
                                    command=self.__compute_data
                                    )
        self.close_button_submit = self._close_button(self.inform_frame, "Выйти")
        first_figure = plot.Plot(graph_frame,
                                 data_cl.Data().get_mass()[0],
                                 data_cl.Data().get_mass()[1],
                                 'Масса',
                                 'Кг', 0, 0)
        second_figure = plot.Plot(graph_frame,
                                  data_cl.Data().get_pulse()[0],
                                  data_cl.Data().get_pulse()[1],
                                  'Пульс',
                                  'Ударов в минуту', 0, 0)
        third_figure = plot.Plot(graph_frame,
                                 data_cl.Data().get_top_pressure()[0],
                                 data_cl.Data().get_top_pressure()[1],
                                 'Давление',
                                 'мм ртутного столба',
                                 data_cl.Data().get_bottom_pressure()[0],
                                 data_cl.Data().get_bottom_pressure()[1])

        # title_text = Label(self.root, text="Дела на сегодня")
        # text = Label(self.root, text="Дела на сегодня")

        self.mass_text.pack(pady=3, expand=1, anchor='n')
        self.mass_entry.pack(pady=3, expand=1, anchor='n')
        self.top_pressure_text.pack(pady=3, expand=1, anchor='n')
        self.top_pressure_entry.pack(pady=3, expand=1, anchor='n')
        self.bottom_pressure_text.pack(pady=3, expand=1)
        self.bottom_pressure_entry.pack(pady=3, expand=1)
        self.pulse.pack(pady=3, expand=1)
        self.pulse_entry.pack(pady=3, expand=1)
        self.button_submit.pack(pady=3, expand=1)
        self.close_button_submit.pack(pady=3, expand=1)
