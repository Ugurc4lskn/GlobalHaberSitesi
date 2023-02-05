from flask import (
    Flask, 
    render_template,
    redirect,
    url_for,
)

from flask_paginate import Pagination, get_page_args

from dateutil.parser import parse
from newsDb import DataBase

app = Flask(__name__, static_folder="static")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' 


db = DataBase()


tota = db.getTotalContent()


def get_users(offset=0, per_page=3):
    return tota[offset: offset + per_page]

@app.route("/")
def index():
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(tota)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    
    return render_template("index.html",
            
            data = tota ,
            parse=parse,
            users=pagination_users,
            page=page,
            per_page=per_page,
            pagination=pagination)







@app.route("/news/<int:Id>")
def details(Id):
    

    query = db.queryIdNumber(Id=Id)
    content = query[4]
    a = content.split(".")
    
    if query:
        if query[0]:
            if Id == query[0]:
                return render_template("details.html",
                data=query, 
                cont=a,
                parse=parse,
                    
                )

                
            else:
                    return redirect(url_for("index" ))
            
        else:
             return redirect(url_for("index"))
   
        
    else:
            return redirect(url_for("index"))
    




@app.errorhandler(404)
def page_not_found(e):
    
    return "Sayfa Bulunamadı ", 404
    





if __name__ == "__main__":
    
    app.run(debug=True)
    



