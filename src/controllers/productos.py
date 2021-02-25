from src import app

@app.route('/productos')
def productos():
    return 'En productos'