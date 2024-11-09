import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv("StudentsPerformance.csv")

#print(df.info())
#temp = df.groupby(by='test preparation course')[['math score','reading score', 'writing score']].mean()
#print(temp)


'''
categories = ["Math prepare", "Reading prepare","Writing prepare","Math unprepare",
"Reading unprepare","Writing unprepare"]
values_p = [69.69,73.89,74.82]
values_unp = [64.1, 66.53, 64.50]
plt.bar(categories[:3], values_p)
plt.bar(categories[3:], values_unp)
plt.title("Актуальність курсів")
plt.ylabel("Бали")
plt.show()
'''

categories= ["associate's degree","bachelor's degree","high school","master's degree","some college","some high school"]

values_m = [67.882883,69.389831,62.137755,69.745763,67.128319,63.497207]
values_r = [70.927928,73, 64.704082, 75.372881,69.460177,66.938547]
values_w = [69.896396,73.381356,62.448980,75.677966,68.840708,64.888268]

plt.bar(categories, values_m)
plt.title("Математика")
plt.ylabel("Бали")
plt.show()

plt.bar(categories, values_r,color="darkred")
plt.title(" Читання")
plt.ylabel("Бали")
plt.show()

plt.bar(categories, values_w, color="orange")
plt.title("Письмо")
plt.ylabel("Бали")
plt.show()

'''
temp = df.groupby(by='gender')[['math score','reading score', 'writing score']].mean()
categories = ["Math female", "Reading female","Writing female","Math male","Reading male","Writing male"]
values = [63.633205,72.608108,72.467181, 68.728216,65.473029,63.311203]
plt.bar(categories, values)
plt.xticks(rotation=20)
plt.title("Стовпчаста діаграма")
plt.ylabel("Бали")
plt.show()
'''

'''
print((df['math score'] > 60).value_counts())
print((df['reading score'] > 60).value_counts())
print((df['writing score'] > 60).value_counts())

sizes = [661, 725, 699] # Список значень, які будуть представлені у вигляді секторів
labels = ['M', 'R', 'W']  # Підписи для кожного сектору
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Кругова діаграма >60б")
plt.show()

sizes = [339, 275, 301] # Список значень, які будуть представлені у вигляді секторів
labels = ['M', 'R', 'W']  # Підписи для кожного сектору
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Кругова діаграма <60б")
plt.show()
'''

'''
temp = df.groupby(by='lunch')[['math score', 'reading score', 'writing score']].mean()
print(temp)

categories = ["Math had lunch", "Reading had lunch","Writing had lunch","Math hadn't lunch","Reading hadn't lunch",
              "Writing hadn't lunch"]
values = [70.034109,71.654264,70.823256, 58.921127,64.653521,63.022535]
plt.bar(categories, values)
plt.xticks(rotation=20)
plt.title("Стовпчаста діаграма")
plt.ylabel("Бали")
plt.show()
'''