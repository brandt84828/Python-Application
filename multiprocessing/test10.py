from multiprocessing import Process, Manager

def f(d, l):
    d[1] = 'test001'
    d['2'] = 12345
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(5))

        p = Process(target=f, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)
