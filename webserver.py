from app import app
from app import db
from app.models import teacher, admin

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'teacher': teacher, 'admin': admin}

if __name__ == '__main__':
    app.run(debug=True)
