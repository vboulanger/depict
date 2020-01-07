from core.session import Session
from core.line import line


SESSION = None


def session(width=300, height=300, jupyter_notebook=False):
    global SESSION
    SESSION = Session(width=300, height=300, jupyter_notebook=False)

def get_session():
    global SESSION
    return SESSION
