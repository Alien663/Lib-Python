import  os
import sys
import time
import signal

def interrupt_handler(signum, frame):
    print("Kill Main Process")
    time.sleep(1)
    raise KeyboardInterrupt

def child_halde_interrupt(signum, frame):
    print("Kill Time Out Counter")
    sys.exit(0)


if __name__ == "__main__":
    time_out_second = 5
    for job in range(4):
        pid = os.fork()
        if(pid > 0):
            try:
                signal.signal(signal.SIGINT, interrupt_handler)
                for i in range((job+1)*2):
                    print(str(os.getpid()) +  "Kero " + str(i))
                    time.sleep(1)
                os.kill(pid, signal.SIGINT)
            except KeyboardInterrupt:
                print("Job : " + str(job) + " timeout")
                continue
        else:
            signal.signal(signal.SIGINT, child_halde_interrupt)
            for i in range(5):
                time.sleep(1)
            os.kill(os.getppid(), signal.SIGINT)
            break
                
