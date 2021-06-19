# Pass on file for intructions so that it could be printed by the function.
import time

def read_lines(filename):

        with open(filename, 'r') as f:
            content = f.readlines()
            
        for line in content:
            time.sleep(2)
            print(line)

        f.close()
