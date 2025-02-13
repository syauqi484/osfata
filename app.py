from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profil')
def profil():
    return render_template('profil.html')

@app.route('/struktur')
def struktur():
    return render_template('struktur.html')

@app.route('/visi_misi')
def visi_misi():
    return render_template('visi_misi.html')

@app.route('/erd')
def erd():
    return render_template('erd.html')

if __name__ == '__main__':
    app.run(debug=True)