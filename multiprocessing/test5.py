from multiprocessing import Process, Queue

def f(q):
    q.put([1, None, 'hello'])

if __name__ == '__main__':
    #queue
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()