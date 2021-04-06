import window_cl


class MainCommander:
    """MainCommander

    EN:
    When the object is created, initializes the reminder window.
    Responsible for linking application windows to each other.

    RU:
    При создании объекта инициализирует окно с напоминанием.
    Отвечает за связь окон приложения между собой.
    """

    def __init__(self):
        self.start_rem_window()

    def start_rem_window(self):
        """start_rem_window

        EN:
        Creates a reminder window.
        Requests the willingness to work from the user.
        If successful,  it calls the authorization window function.

        RU:
        Создает окно с напоминанием.
        Запрашивает готовность работать у пользователя.
        В случае успеха вызывает функцию окна аторизации.
        """
        obj = window_cl.ReminderWindow()
        obj.create()
        if obj.is_ready():
            obj.stop()
            del obj
            self.start_authorization_window()

    def start_authorization_window(self):
        """start_authorization_window

        EN:
        Creates a authorization window.
        Requests the password from the user.
        If successful, it calls the main window function.

        RU:
        Создает окно авторизации.
        Запрашивает пароль у пользователя.
        В случае успеха вызывает функцию главного окна.
        """
        obj = window_cl.AuthorizationWindow()
        obj.create()
        if obj.is_authorization_complete():
            obj.stop()
            del obj
            self.start_main_window()

    def start_main_window(self):
        """start_main_window
        EN:
        Creates a main window.

        RU:
        Создает главное окно.
        """
        obj = window_cl.MainWindow()
        obj.create()
        del obj


if __name__ == '__main__':
    run = MainCommander()
