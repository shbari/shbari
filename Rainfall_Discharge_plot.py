import pandas as pd
import random
import matplotlib.pyplot as plt
import matplotlib.dates as md
plt.style.use('science.mplstyle')

date = ['2009/6/12 2:00', '2009/6/12 3:00', '2009/6/12 4:00', '2009/6/12 5:00', '2009/6/12 6:00', '2009/6/12 7:00', '2009/6/12 8:00', '2009/6/12 9:00', '2009/6/12 10:00', '2009/6/12 11:00', '2009/6/12 12:00', '2009/6/12 13:00', '2009/6/12 14:00', '2009/6/12 15:00', '2009/6/12 16:00', '2009/6/12 17:00', '2009/6/12 18:00', '2009/6/12 19:00', '2009/6/12 20:00', '2009/6/12 21:00', '2009/6/12 22:00', '2009/6/12 23:00',
    '2009/6/13 0:00', '2009/6/13 1:00', '2009/6/13 2:00', '2009/6/13 3:00', '2009/6/13 4:00', '2009/6/13 5:00', '2009/6/13 6:00', '2009/6/13 7:00', '2009/6/13 8:00', '2009/6/13 9:00', '2009/6/13 10:00', '2009/6/13 11:00', '2009/6/13 12:00', '2009/6/13 13:00', '2009/6/13 14:00', '2009/6/13 15:00', '2009/6/13 16:00', '2009/6/13 17:00', '2009/6/13 18:00', '2009/6/13 19:00', '2009/6/13 20:00', '2009/6/13 21:00', '2009/6/13 22:00', '2009/6/13 23:00',
    '2009/6/14 0:00', '2009/6/14 1:00', '2009/6/14 2:00', '2009/6/14 3:00', '2009/6/14 4:00', '2009/6/14 5:00', '2009/6/14 6:00', '2009/6/14 7:00', '2009/6/14 8:00', '2009/6/14 9:00', '2009/6/14 10:00', '2009/6/14 11:00', '2009/6/14 12:00', '2009/6/14 13:00', '2009/6/14 14:00', '2009/6/14 15:00', '2009/6/14 16:00', '2009/6/14 17:00', '2009/6/14 18:00', '2009/6/14 19:00', '2009/6/14 20:00', '2009/6/14 21:00', '2009/6/14 22:00', '2009/6/14 23:00',
    '2009/6/15 0:00', '2009/6/15 1:00', '2009/6/15 2:00']


data = pd.DataFrame({'Date': date,
                     'Count1': [random.randrange(1, 50, 1) for i in range(len(date))],
                     'Count2': [random.randrange(50, 100, 1) for i in range(len(date))]})

data["Date"] = pd.to_datetime(data["Date"], format="%Y/%m/%d %H:%M")


fig, ax = plt.subplots(2, 1, figsize=(12,6))

ax[0].plot("Date", "Count1", data=data, color='tab:blue', label='Rainfall [mm]')

ax[0].set_title("Rainfall and Discharge", fontsize=12)

ax[0].spines["top"].set_alpha(.0)
ax[0].spines["bottom"].set_alpha(.0)
ax[0].spines["right"].set_alpha(.0)
ax[0].spines["left"].set_alpha(1.0)

ax[0].legend(loc='upper left')
ax[0].grid(axis='y', alpha=.3)

ax[0].xaxis.set_major_locator(md.HourLocator(interval = 12))
ax[0].xaxis.set_major_formatter(md.DateFormatter('%m/%d %H:%M'))
plt.setp(ax[0].xaxis.get_majorticklabels(), rotation = 0)
ax[0].set_xlim([data['Date'].iloc[0], data['Date'].iloc[-1]])

ax[1].plot("Date", "Count2", data=data, color='tab:green', label='Discharge [$m^{3} s^{-1}$]')
ax[1].invert_yaxis()
# Add left y-axis line
#ax[0].axvline(x=data['Date'].iloc[0], color='black', linestyle='--', linewidth=1)

# Add left y-axis line
#ax[1].axvline(x=data['Date'].iloc[0], color='black', linestyle='--', linewidth=1)

ax[1].spines["top"].set_alpha(.0)
ax[1].spines["bottom"].set_alpha(.0)
ax[1].spines["right"].set_alpha(.0)
ax[1].spines["left"].set_alpha(1.0)
ax[1].legend(loc='upper left')
ax[1].grid(axis='y', alpha=.3)

ax[1].xaxis.set_major_locator(md.HourLocator(interval = 12))
ax[1].xaxis.set_major_formatter(md.DateFormatter('%m/%d %H:%M'))
plt.setp(ax[1].xaxis.get_majorticklabels(), rotation = 0)
ax[1].set_xlim([data['Date'].iloc[0], data['Date'].iloc[-1]])

ax[1].tick_params(bottom = False, labelbottom = False, top = True, labeltop = True)

plt.tight_layout()

plt.show()