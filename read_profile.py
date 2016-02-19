import cProfile
import pstats
import os
import shutil
import read

def run():
    read.main()

if __name__ == '__main__':
    if os.path.isfile('result.prof'):
        shutil.move('result.prof', 'result.prof.old') 
        p = pstats.Stats('result.prof.old')
        p.strip_dirs().sort_stats('time').print_stats(20)

    cProfile.run('run()', 'result.prof')
    p = pstats.Stats('result.prof')
    p.strip_dirs().sort_stats('time').print_stats(20)

