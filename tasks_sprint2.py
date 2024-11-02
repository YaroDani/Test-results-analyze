import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv("StudentsPerformance.csv")
print(df.info())
'''
temp = df.groupby(by='test preparation course')[['math score',
                                                 'reading score', 'writing score']].mean()
print(temp)

categories = ["Math prepare", "Reading prepare","Writing prepare","Math unprepare",
"Reading unprepare","Writing unprepare"] values = [69.69,73.89,74.82, 64.1, 66.53, 64.50]          # Список значень 
plt.bar(categories, values)    # Метод bar створює стовпчасту діаграму; categories - підписи, 
plt.title("Стовпчаста діаграма")  # Додає заголовок діаграми plt.xlabel("Категорії")  # 
plt.ylabel("Значення")   # Підпис осі Y plt.show()
'''

'''
categories = ["Math associate's degree", "Reading associate's degree", "Writing associate's degree",
              "Math bachelor's degree", "Reading bachelor's degree", "Writing bachelor's degree",
              "Math high school", "Reading high school", "Writing high school",
              "Math master's degree", "Reading master's degree", "Writing master's degree",
              "Math some college", "Reading some college", "Writing some college",
              "Math some high school", "Reading some high school", "Writing some high school"]
values = [67.882883, 70.927928,69.896396, 69.389831,73.000000,73.381356, 62.137755,64.704082,62.448980, 69.745763,
          75.372881, 75.677966,67.128319, 69.460177, 68.840708, 63.497207, 66.938547, 64.888268]
plt.bar(categories, values)    # Метод bar створює стовпчасту діаграму; categories - підписи, values - висоти стовпчиків
plt.xticks(rotation=25)
plt.xlabel("Категорії")  # Підпис осі X
plt.ylabel("Значення")   # Підпис осі Y
plt.show()
'''

'''
temp = df.groupby(by='gender')[['math score','reading score', 'writing score']].mean()
categories = ["Math female", "Reading female","Writing female","Math male","Reading male","Writing male"]
values = [63.633205,72.608108,72.467181, 68.728216,65.473029,63.311203]
plt.bar(categories, values)
plt.xticks(rotation=20)
plt.title("Стовпчаста діаграма")
plt.ylabel("Значення")
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
plt.ylabel("Значення")
plt.show()
'''