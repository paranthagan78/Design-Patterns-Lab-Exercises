#CPU-bound & IO-bound discussion
'''forces threads to release the GIL after a fixed interval of continuous use and
if nobody else acquired the GIL,the same thread could continue its use.'''


#Solution to GIL
#Multi-processors & apply()
'''The apply() function should be used for issuing target task functions to
the process pool where the caller can or must block until the task is complete.'''

from multiprocessing import Pool, cpu_count
import time

print(cpu_count())

COUNT = 50000000
def countdown(n):
    while n>0:
        n -= 1

if __name__ == '__main__':
    pool = Pool(1)
    
    start = time.time()
    r1 = pool.apply(countdown, [COUNT//2])
    r2 = pool.apply(countdown, [COUNT//2])
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken in seconds:', end - start)

'''

#Multi-processors & apply_async()
#The apply_async() function should be used for issuing target task functions to the process pool
#where the caller cannot or must not block while the task is executing.

from multiprocessing import Pool, cpu_count
import time

print(cpu_count())

COUNT = 50000000
def countdown(n):
    while n>0:
        n -= 1

if __name__ == '__main__':
    pool = Pool(8)
    
    start = time.time()
    r1 = pool.apply_async(countdown, [COUNT//2])
    r2 = pool.apply_async(countdown, [COUNT//2])
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken in seconds -', end - start)
'''