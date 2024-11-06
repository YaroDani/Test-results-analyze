import pandas as pd
df= pd.read_csv("StudentsPerformance.csv")
print(df.info())

temp = df.groupby(by='test preparation course')[['math score', 'reading score', 'writing score']].mean()
print(temp) #актуальність підготовчих курсів аналіз тих хто склав іспит з підготовкою та без

temp = df.groupby(by='parental level of education')[['math score', 'reading score', 'writing score']].mean()
print(temp) #Який зв'язок між рівнем освіти батьків і результатами іспитів?

temp = df.groupby(by='gender')[['math score', 'reading score', 'writing score']].mean()
print(temp) #Як впливає стать студента на його результати вспитів

print((df['math score'] > 60).value_counts())
print((df['reading score'] > 60).value_counts())
print((df['writing score'] > 60).value_counts()) #Скільки студентів здали тести більше 60 балів

temp = df.groupby(by='test preparation course')['parental level of education'].value_counts()
#чи є залежність між проходженням курсів підготовки та рівнем освіти батьків
print(temp)

temp = df.groupby(by='lunch')[['math score', 'reading score', 'writing score']].mean()
print(temp)