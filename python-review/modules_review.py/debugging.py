#Debugging
# use linting, pycharm has built in linting
# IDE/Editor with builtin tools like formatting
# Read errors
# use pdb (python debugger) -> Allows us to interact with the code
import pdb

def add(n1,n2):
    pdb.set_trace()
    return n1 + n2
add(4,3)
