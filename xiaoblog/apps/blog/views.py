from flask import url_for,redirect,request,flash,render_template
from . import  blog
from .forms import LoginForm
from  apps.models import User,Article
from flask_login import login_user,logout_user

@blog.route("/index.html")
def index():
    page = request.args.get("page")
    if page is None:
        page=1
    page=int(page)
    paginate=Article.query.order_by(Article.create_time.desc()).paginate(page,3,error_out=False)
    articles=paginate.items

    return  render_template("index.html",articles=articles,paginate=paginate)

@blog.route("/")
def index2():
    return redirect(url_for("main.index"))

@blog.route("/login.html",methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user is not None:
            flag=User.verity_password(form.password.data,user.password_hash)
            if flag:
                login_user(user,form.remember_me.data)
                return redirect(request.args.get('next') or url_for("admin.index"))
        flash('无效的用户名或者密码')

    return render_template("login.html",form=form)

@blog.route("/loginout.html")
def loginout():
    logout_user()
    flash("退出成功！")
    return redirect(url_for("main.login"))

@blog.route("/aboutme.html")
def aboutme():
    return render_template("about.html")

@blog.route("/article/<int:id>")
def details(id):
    article=Article.query.filter_by(id=id).first()
    return render_template('article.html',article=article)
