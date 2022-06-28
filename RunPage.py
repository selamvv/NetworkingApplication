#RunPge
import subprocess
#import Numbers.py

def main():
    result = subprocess.check_output(['Numbers.py'])
    print(result)
    N=subprocess.Popen(['Numbers.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    with open("Numbers.txr","wb") as out:
        p = subprocess.Popen(['python', 'Number.py'], out)

#    file.write(N)
    #file.close()
main()
