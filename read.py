from flask import Flask, render_template, url_for
import plotly as py
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px


df = pd.read_excel('sample.xlsx')
data = df.pivot_table(columns=['Item'],aggfunc='size') #Gives the total number of items in the  Item column#

list1 = ((df.drop_duplicates(subset='Item'))['Item']).tolist() #Removes the entries in Item tab and adds the remaning value in list#
list2 = []

for i in range(len(list1)):
    alpha = list1[i]
    # print(alpha)
    beta = data[alpha]
    list2.append(beta)
    # print(beta)

# print(list2)
# print(data.Binder)
# print(df)

################## Plotly Diagram ############################ 
colors = ['lightcyan', 'cyan', 'royalblue', 'darkblue']
fig = go.Figure(data=[go.Pie(labels=list1,values=list2)])
fig.update_traces(hoverinfo='label', textinfo='value', textfont_size=20,
                  marker=dict( colors=colors,line=dict(color='#000000', width=2)))
fig.show()
fig.write_html('./image1.html')
#############################################################

# data1 = (df.drop_duplicates(subset='Item'))
# list1 = ((df.drop_duplicates(subset='Item'))['Item']).tolist()
# print(test)

