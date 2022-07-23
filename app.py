from flask import Flask, render_template, url_for
import plotly as py
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px


app = Flask(__name__)

@app.route('/')
def index():
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    return render_template('index.html')

@app.route('/img.html')
def img():
###########################
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
    fig.update_traces(hoverinfo='label', textinfo='value', textfont_size=10,
                    marker=dict( colors=colors,line=dict(color='#000000', width=0)))
    # fig.show()
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    fig.write_html('./templates/img.html')
    #############################################################
###########################

    return render_template('img.html')

# fig.write_html('./graph/image.html')



if __name__ == "__main__":
    app.run(debug=True)