#multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#multiprocessing = better for cpu bound tasks (heavy cpu usages)
#multithreading = better for io bound tasks (waiting around)


from multiprocessing import Process,cpu_count 
import time


def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    start = time.perf_counter()
    a = Process(target=counter,args=(5000000000,))
    b = Process(target=counter,args=(1000000000,))
        
    a.start()
    b.start()

    a.join()
    b.join()
    end = time.perf_counter()

    print("finished in:", end-start , "seconds")

if __name__ == "__main__":
    main()

#this takes 35.77 secons