from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    # shared memory
    # 'd'(float) 'i'(sign int) = type code
    num = Value('d', 0.0)
    arr = Array('i', range(5))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
