from multiprocessing import Process, Pipe
import time
import numpy as np

def reader_proc(pipe):
    p_output, p_input = pipe
    p_input.close()
    while True:
        msg = p_output.recv()
        if msg=='DONE':
            break

def writer(count, p_input):
    test = np.array([0]*52400000)
    p_input.send(str(test))
    p_input.send('DONE')

if __name__=='__main__':
    for count in [1024]:
        p_output, p_input = Pipe()
        reader_p = Process(target=reader_proc, args=((p_output, p_input),))
        reader_p.daemon = True
        reader_p.start()

        p_output.close()
        writer(count, p_input)
        p_input.close()
        reader_p.join()
