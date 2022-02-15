from flask import Flask, Response, send_from_directory, make_response,request
import os
app = Flask('app', static_url_path='/static')

@app.route('/sike.jpg', methods=['GET'])
def sike():
    return send_from_directory(os.path.join(app.root_path, 'static'),
            'sike.jpg', mimetype='image/jpeg')


@app.route('/beatlesblacksabbathrollingstonezepellin.txt', methods=['POST'])
def endgame():
    return send_from_directory(os.path.join(app.root_path, 'static'),
            'beatlesblacksabbathrollingstonezepellin.txt', mimetype='text/plain')

@app.route('/chandler.jpg', methods=['GET'])
def chandler():
    return send_from_directory(os.path.join(app.root_path, 'static'),
            'chandler.jpg', mimetype='image/jpeg')

@app.route('/robots.txt', methods=['GET'])
def robot():
    return send_from_directory(os.path.join(app.root_path, 'static'),
            'robots.txt', mimetype='text/plain')

@app.route('/obladioblada.css', methods=['GET'])
def stylecss():
    return send_from_directory(os.path.join(app.root_path, 'static'),
            'obladioblada.css', mimetype='text/css')

@app.route('/')
def hello_world():
    # response = Response()
    # disable='<script>function disableClick(){document.onclick=function(event){ if (event.button == 2) { alert("Right Click Message"); return false; } } } </script> </head> <body onLoad="disableClick()"> </body>'
    browser=request.headers.get('User-Agent')
    isChrome ='Chrome' in browser
    
    if(isChrome):
        
        response =make_response('<h2>You got unlucky with the browser :(</h2><img src="chandler.jpg"></img>')
        response.set_cookie('Hint', "Don't use Chromium based browsers...doesn't matter much though if you like plain text.", max_age=60)
        response.headers['Refresh'] = '25; url=https://www.youtube.com/watch?v=dQw4w9WgXcQ&autoplay=1'
    else:
        response =make_response('<br><br><h2 style="text-align:center;">Nice browser :)</h2>')
    
    response.headers['Link'] = '</obladioblada.css>; rel=stylesheet;'

    return response

@app.route('/aaokabhihawelipe', methods=['GET'])
def displayhint():
    content=".........flag cipher........."
    response =make_response("<h1>Remember it's something of a rock'n'roll! not rick roll obviously</h1><br><p>"+content+"</p>")
    response.headers['Refresh'] = '5; url=https://www.youtube.com/watch?v=dQw4w9WgXcQ&autoplay=1'

    return response

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=3000, debug=True)
    app.run(debug=True)
