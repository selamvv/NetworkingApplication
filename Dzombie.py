#create a dictionary of the zombies and a list of their scripts

def dict():
    scripts = ['count.py', 'form.py', 'calculate.py', 'time.py']
    Clients= {8080: scripts, 8081: scripts, 8082: scripts, 8083: scripts}
    print(Clients)
    return 
def main():
    dict()
main()
