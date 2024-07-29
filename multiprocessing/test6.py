from multiprocessing import Process, Pipe

def f(conn):
    conn.send([1, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    # pipe
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()