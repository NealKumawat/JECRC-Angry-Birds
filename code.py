import matplotlib.pyplot as plt
df=pd.read_csv("finalp.csv")
dict = {0:0, 10:0, 20:0, 30:0, 40:0, 50:0, 60:0, 70:0, 80:0, 90:0}
for i in df['data']:
  if i <= 10:
    dict[0] = dict[0] + 1
  if i>10 and i<=20:
    dict[10] = dict[10] + 1
  if i>20 and i<=30:
    dict[20] = dict[20] + 1
  if i>30 and i<=40:
    dict[30] = dict[30] + 1
  if i>40 and i<=50:
    dict[40] = dict[40] + 1
  if i>50 and i<=60:
    dict[50] = dict[50] + 1
  if i>60 and i<=70:
    dict[60] = dict[60] + 1
  if i>70 and i<=80:
    dict[70] = dict[70] + 1
  if i>80 and i<=90:
    dict[80] = dict[80] + 1
  if i>90 and i<=100:
    dict[90] = dict[90] + 1
x=list(dict.keys())
y=list(dict.values())
plt.figure(figsize=(9,5))
plt.plot(x,y, color='purple', marker='o', linewidth=1, markersize=5, markerfacecolor='yellow', label='Number of people having anger issues')
plt.xticks(ticks=range(0,101,5), labels=range(0,101,5))
plt.yticks(range(0,23,2))
plt.title("JECRC Angry Birds")
plt.grid(color='grey', linestyle='--', linewidth = 0.5, alpha=1)
plt.xlabel("Percentage", color='maroon', fontweight='bold')
plt.ylabel("Number of people", color='maroon', fontweight='bold')
plt.tight_layout(pad=0.1)
plt.legend()
plt.show()