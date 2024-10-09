import pandas as pd
import matplotlib.dates as dates
import matplotlib.pyplot as plt

data = [['Meeting', '2024-10-27 12:30', '2024-10-27 13:30'], ['Training', '2024-10-28 14:00', '2024-10-28 15:30'], ['1to1', '2024-10-28 16:30', '2024-10-28 17:00']]
df = pd.DataFrame(data, columns = ['Task', 'Start_Time', 'End_Time'])

df_phase = df
df_phase['Start_Time'] = pd.to_datetime(df_phase['Start_Time'], format='%Y-%m-%d %H:%M')
df_phase['End_Time'] = pd.to_datetime(df_phase['End_Time'], format='%Y-%m-%d %H:%M')

sdate = df_phase['Start_Time'].tolist()
edate = df_phase['End_Time'].tolist()
tasks = df_phase['Task'].tolist()

edate, sdate = [dates.date2num(item) for item in (edate, sdate)]
time_diff = edate - sdate
ypos = range(len(tasks))
fig, ax = plt.subplots()
ax.barh(ypos, time_diff, left=sdate, height=0.8, align='center', color='grey',edgecolor='black')
plt.yticks(ypos, tasks)
ax.axis('tight')

ax.xaxis_date()
plt.show()