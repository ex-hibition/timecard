import pandas as pd
import datetime as dt


class CalcOvertime():

  def __init__(self, csvfile):
    self.df = pd.read_csv(csvfile)

  def calc_overtime(self):
    overtime = 0;

    for index, row in self.df.iterrows():
      work = pd.to_datetime(row['work_time'], format="%H:%M")
      base = dt.datetime.strptime('7:45', "%H:%M")
      overtime += (work - base).seconds

    print("overtime:", overtime / 60, "mins, ",overtime / 60 / 60, "hours")


calc = CalcOvertime('test.csv')
calc.calc_overtime()

