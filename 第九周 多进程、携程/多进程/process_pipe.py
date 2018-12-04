from multiprocessing import Process,Pipe
import os

def fp(childcnn):
    childcnn.send("Hello there!")

if __name__ == "__main__":
    childcnn,parentcnn = Pipe()   #类似于socket的通信
    p = Process(target=fp,args=(childcnn,))
    p.start()
    print(parentcnn.recv())

