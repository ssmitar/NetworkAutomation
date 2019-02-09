import threading

#Creating threads
def create_threads(list, fuction):

    threads = []            #Creating an empty list

    for ip in list:
        th = threading.Thread(target = fuction, args = (ip,))        #args is a tuple with a single element
        th.start()          #starts the thread 
        threads.append(th)
    
    for th in threads:
        th.join()           #instruct program to wait till all threads are done working                            
