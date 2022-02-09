import streamlit as st
from textblob import TextBlob
import plotly.express as px

st.title("sentiment analysis app")
c1,c2 = st.columns([2,3])
c1.header("User input")
message = c1.text_area("enter your data",height=300)
chart_style = c1.radio("select output",['pie','bar','area'])
btn = c1.button("analyse")
c2.header("Results")

if btn and len(message) > 10:
    blob = TextBlob(message)
    result = []
    for sentence in blob.sentences:
        result.append(sentence.polarity)

    sentiment_list = {'positive':0,'negative':0,'neutral':0}
    for val in result:
        if val > 0: 
            sentiment_list['positive']+=1
        elif val < 0: 
            sentiment_list['negative']+=1
        else:
            sentiment_list['neutral']+=1
    if chart_style =='pie':
        fig = px.pie(names=sentiment_list.keys(),values=sentiment_list.values())
    elif chart_style == 'bar':
        fig = px.bar(x=sentiment_list.keys(),y=sentiment_list.values(),color=['green','red','blue'])
    elif chart_style == 'area':
        fig = px.area(x=sentiment_list.keys(),y=sentiment_list.values())
    c2.plotly_chart(fig,use_container_width=True)                


# streamlit run .\nlp\sentiment_app.py