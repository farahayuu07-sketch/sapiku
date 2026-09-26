from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    jumlah_sapi = 10
    total_komisi = 250000 * jumlah_sapi
    return render_template('index.html', komisi=total_komisi)


if __name__ == '__main__':
    app.run(debug=True)