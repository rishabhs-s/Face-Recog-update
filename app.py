from flask import Flask

import views

app=Flask(__name__)

#URL
app.add_url_rule('/base','base',views.base)
app.add_url_rule('/','index',views.index)
app.add_url_rule('/emotion','emotion',views.emotion,methods=['GET','POST'])



#run
if __name__=="__main__":
    app.run(port=8000,debug=True)