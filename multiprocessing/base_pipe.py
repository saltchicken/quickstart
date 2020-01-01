from multiprocessing import Process, Pipe

def reader_proc(pipe):
    p_output, p_input = pipe
    p_input.close()     #Reading only, input unnecessary
    while True:
        msg = p_output.recv()
        print(msg)
        if msg=='DONE':
            break

def writer(pipe):
    p_output, p_input = pipe
    p_output.close()    #Writing only, output unnecessary
    msg = "test message"
    p_input.send(msg)
    p_input.send('DONE')

if __name__=='__main__':
    p_output, p_input = Pipe()
    reader_p = Process(target=reader_proc, args=((p_output, p_input),))
    reader_p.daemon = True
    reader_p.start()
    writer((p_output, p_input))
    
    p_input.close()
    p_output.close()
    reader_p.join()
