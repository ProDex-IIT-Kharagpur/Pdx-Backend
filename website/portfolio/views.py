from flask import Blueprint, render_template

portfolio = Blueprint('portfolio', __name__)


@portfolio.route('/cgiu')
def portfolio_cgiu():
    return render_template('portfolio/cgiu.html')


@portfolio.route('/ges')
def portfolio_ges():
    return render_template('portfolio/ges.html')


@portfolio.route('/masterpiece')
def portfolio_masterpiece():
    return render_template('portfolio/masterpiece.html')


@portfolio.route('/openiit18')
def portfolio_openiit18():
    return render_template('portfolio/openiit18.html')


@portfolio.route('/prakriti')
def portfolio_prakriti():
    return render_template('portfolio/prakriti.html')


@portfolio.route('/r3')
def portfolio_r3():
    return render_template('portfolio/r3.html')


@portfolio.route('/rth')
def portfolio_rth():
    return render_template('portfolio/rth.html')


@portfolio.route('/siemens')
def portfolio_siemens():
    return render_template('portfolio/siemens.html')
