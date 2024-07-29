from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

def f1(i):
    print('hello worlddddd', i)

if __name__ == '__main__':
    lock = Lock()
    for num in range(5):
        Process(target=f, args=(lock, num)).start()

    for num in range(5):
        Process(target=f1, args=(num,)).start()
