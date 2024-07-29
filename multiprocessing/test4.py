import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    # windows / mac os default is 'spawn', linux default is 'fork'
    print(mp.get_start_method())
    #mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()
