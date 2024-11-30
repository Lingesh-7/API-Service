from flask import Flask, render_template,redirect,url_for
import requests
from flask_bootstrap import Bootstrap5
from form import Stock,Brewerry,CustomSearch


# stock 8445a652db9735d5c1cd67230f51d30d

#Lord of Rings   q9GX1aDDj_Xp4TWdLMhP


app=Flask(__name__)
FLASK_KEY="123456789"
app.config['SECRET_KEY'] = FLASK_KEY
Bootstrap5(app)

STOCK_URL="https://api.marketstack.com/v1/eod?access_key=8445a652db9735d5c1cd67230f51d30d"
BREWERRY_URL="https://api.openbrewerydb.org/v1/breweries"

@app.route('/')
def home():
    return render_template('home.html')




# @app.route('/book')
# def book_():
#     return render_template("info.html",infp="BUMA")

# @app.route('/movie')
# def movie_():
#     return render_template("info.html",infp="SUma")

# @app.route('/movie_or_book',methods=["GET","POST"])
# def movie_or_book_():
#     forms_=CreateForm()
#     if forms_.validate_on_submit():
#         if forms_.doc.data == 'A':
#             return redirect(url_for('book_'))
#         return redirect(url_for('movie_'))
#     return render_template('form_fill.html',forms=forms_)


@app.route('/stock_market',methods=["GET","POST"])
def intrest_stock():
    forms_=Stock()
    if forms_.validate_on_submit():
        stock_dict={'A':'MSFT','B':"AAPL",'C':'AMZN',"D":'GOOGL','E':'FB'}
        para={
            "symbols":f"{stock_dict[forms_.stock_.data]}",
            'exchange':f"{forms_.exchange.data}",
            'sort':f"{forms_.sort.data}",
            'date_from':f"{forms_.date_from.data}",
            'date_to':f"{forms_.date_to.data}"
            }
        response = requests.get(url=STOCK_URL, params=para)
        data_=response.json()
         
        return render_template('info.html',datas=data_['data'],head_=stock_dict[forms_.stock_.data])
    return render_template('form_fill.html',forms=forms_)


@app.route('/all')
def list_():
    response=requests.get(url=BREWERRY_URL)
    data_=response.json()
    return render_template("info2.html",datas=data_)

    
@app.route('/random')
def random_():
    response=requests.get(url=f"{BREWERRY_URL}/random")
    data_=response.json()
    return render_template("info2.html",datas=data_)

@app.route('/custom_search',methods=["GET","POST"])
def custom_search_():
    form=CustomSearch()
    if form.validate_on_submit():
        type_={'A': 'micro', 'B':'nano' ,'C':'Planning','D':'Bar','E':'Brewpub'}
        
        para={
            'by_city':form.by_city.data,
            'by_country':form.by_country.data,
            'by_state':form.by_state.data,
            
        }
        
        response=requests.get(url=BREWERRY_URL,params=para)
        data_=response.json()
        print(data_)
        return render_template("info2.html",datas=data_)
    return render_template("form_fill.html",forms=form,needed=True)

@app.route('/brewerry',methods=["GET","POST"])
def brewerry_():
    forms_=Brewerry()
    if forms_.validate_on_submit():
        # print(forms_.selection_.data)
        if forms_.selection_.data=='A':
            return redirect(url_for('list_'))
        elif forms_.selection_.data=='B':
            return redirect(url_for('random_'))  
        return redirect(url_for('custom_search_'))
    return render_template('form_fill.html',forms=forms_)



if __name__=='__main__':
    app.run(debug=True)