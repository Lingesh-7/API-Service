from flask_wtf import FlaskForm 
from wtforms.validators import DataRequired
from wtforms import StringField,SubmitField,IntegerField,RadioField


class Stock(FlaskForm):
    stock_= RadioField(choices=[('A','MICROSOFT'),('B','APPLE'),('C','AMAZON'),('D','ALPHABET'),("E",'META')],default="A")
    exchange=StringField(label="Exchange\nEg:XNAS")
    sort=StringField(label="Sort:DESC/ASC",default="ASC")
    date_from=StringField(label="Date From")
    date_to=StringField(label="Date To")
    # limit=StringField(label="Limit")
    submit=SubmitField(label="GET!")



class Brewerry(FlaskForm):
    selection_=RadioField('Which one you like!', choices=[('A', 'All Info'), ('B','Random' ),('C','Custom Search')])
    
    submit=SubmitField(label="GET!")



class CustomSearch(FlaskForm):
    by_country=StringField(label="Country")
    by_city=StringField(label="City")
    by_state=StringField(label="State")
    by_name=StringField(label="Name")
    
    sumb=SubmitField(label="GET")




    