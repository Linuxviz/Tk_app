"""
    File contains class "Data". This class using for manipulation with save and load data from disk.
"""

from datetime import datetime
from pandas import DataFrame, read_csv


class Data:
    def __init__(self):
        """init today date accurate to the day"""
        datetime.now().strftime("%d-%m-%Y %H:%M")
        self.day = datetime.now().day
        self.month = datetime.now().month
        self.year = datetime.now().year
        self.df = read_csv('data\\health_index.csv')

    def first_create(self):
        """init csv file with columns"""
        df = DataFrame({
                'day':             [],
                'month':           [],
                'year':            [],
                'mass':            [],
                'top_pressure':    [],
                'bottom_pressure': [],
                'pulse':           []
        })
        df.to_csv('.\\data\\health_index.csv', index_label=False)

    def save_data(self, mass, top_pressure, bottom_pressure, pulse):
        """save on disk and load in memory new csv table"""
        df = read_csv('data\\health_index.csv')
        input_df = DataFrame({
                'day':             [self.day],
                'month':           [self.month],
                'year':            [self.year],
                'mass':            [mass],
                'top_pressure':    [top_pressure],
                'bottom_pressure': [bottom_pressure],
                'pulse':           [pulse]
        })
        new_df = df.append(input_df, ignore_index=True)
        new_df.to_csv('.\\data\\health_index.csv', index_label=False)
        self.df = read_csv('data\\health_index.csv')

    def data_backup(self):
        """create copy of csv file"""
        df = read_csv('data\\health_index.csv')
        df.to_csv('.\\data\\health_index' + '_{}.{}.{}_backup'.format(self.day, self.month, self.year) + '.csv',
                  index_label=False)

    """ ↓↓↓ functions load and return row and dates ↓↓↓ """

    def get_mass(self) -> (tuple, tuple):
        x = self.__concatenate_data(self.df['day'], self.df['month'], self.df['year'])
        y = self.df['mass']
        return x, tuple(y)

    def get_top_pressure(self) -> (tuple, tuple):
        x = self.__concatenate_data(self.df['day'], self.df['month'], self.df['year'])
        y = self.df['top_pressure']
        return x, tuple(y)

    def get_bottom_pressure(self) -> (tuple, tuple):
        x = self.__concatenate_data(self.df['day'], self.df['month'], self.df['year'])
        y = self.df['bottom_pressure']
        return x, tuple(y)

    def get_pulse(self) -> (tuple, tuple):
        x = self.__concatenate_data(self.df['day'], self.df['month'], self.df['year'])
        y = self.df['pulse']
        return x, tuple(y)

    def __concatenate_data(self, day: str, month: str, year: str) -> tuple:
        """Reformat row parameters in one string and return tuple of strings"""
        str_list = list()
        for i in range(len(day)):
            str_list.append('{}.{}.{}'.format(day[i], month[i], year[i]))
        return tuple(str_list)
