from textblob import TextBlob


# pip install textblob
# python -m textblob.download_corpora

msg = "this is a good day tom sleep early"

blob = TextBlob(msg)
print(blob.polarity)

if blob.polarity > 0:
    print("your message is positive")

elif blob.polarity > 0:
    print("your message is negative")   

else:
    print("you message is nuetral")     
