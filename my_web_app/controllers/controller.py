from app import app

@app.route('/')
@app.route('/<name>') # ADDED
def greet(name): # ADDED
    return f"Hello {name}!"  # ADDED