# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

nobel_prize_df = pd.read_csv('data/nobel.csv')

#1.- What is the most commonly awarded gender and birth country? 
top_gender = nobel_prize_df['gender'].mode().values[0]
top_country = nobel_prize_df['birth_country'].mode().values[0]
print('Top gender: ' + top_gender)
print('Top country: ' + top_country)

#2.- Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?
nobel_prize_df['is_from_us'] = nobel_prize_df['birth_country'] == 'USA'
nobel_prize_df['decade'] = (nobel_prize_df['awardYear'] // 10) * 10
total_by_decade = nobel_prize_df.groupby('decade').size()
total_by_decade_us = nobel_prize_df[nobel_prize_df['is_from_us']].groupby('decade').size()
ratio = total_by_decade_us / total_by_decade
max_decade_usa = ratio.idxmax()
print('Decade with highest ratio of US-born Nobel Prize winners : ' + str(max_decade_usa))

sns.set_style('white')
g = sns.relplot(data=total_by_decade_us,kind='line')
g.figure.suptitle('US-born Nobel Prize winners per decade')
g.set(ylabel='Number of winners')
plt.show()

#3.- Which decade and Nobel Prize category combination had the highest proportion of female laureates? 
nobel_prize_df['is_female'] =  nobel_prize_df['gender'] == 'female' 
total = nobel_prize_df.groupby(["decade", "category"]).size()
female = nobel_prize_df[nobel_prize_df['is_female']].groupby(["decade", "category"]).size()
ratio = female/total
max_decade_category = ratio.idxmax()
list_index =list(max_decade_category)
max_female_dict = {str(list_index[0]) : list_index[1] }
print(max_female_dict)

female_df = female.reset_index()
female_df.rename(columns={ 0: 'count' }, inplace=True)
sns.set_palette('RdBu')
g = sns.relplot(data=female_df,x='decade',y='count',hue='category',kind='line')
g.figure.suptitle('Decade and Nobel Prize category of female laureates')
g.set(ylabel='Number of winners')
plt.show()

# 3.- Who was the first woman to receive a Nobel Prize, and in what category?
women_winners = nobel_prize_df[ nobel_prize_df['is_female']]
row = women_winners[ women_winners['awardYear']== women_winners['awardYear'].min()]
first_woman_name = row['fullName'].values[0]
first_woman_category = row['category'].values[0]
print( first_woman_name + '  '+ first_woman_category)

# 4.- Which individuals have won more than one Nobel Prize throughout the years?
repeat_winners = nobel_prize_df['fullName'].value_counts()
repeat_list= list(repeat_winners[ repeat_winners >=2 ].index)
print(repeat_list)