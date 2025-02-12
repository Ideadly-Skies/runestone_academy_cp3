from Queue import Queue

def Russian_Roulette(name_list, num):
    """the player at the nth turn must eliminate themselves akin to russian roulette"""
    # init an instance of Queue() 
    sim_queue = Queue()
    
    # enqueue name into list 
    for name in name_list:
        sim_queue.enqueue(name)
    
    # run the simulation
    while sim_queue.size() > 1:
        for i in range(num):
            # enqueue and dequeue back into the queue
            sim_queue.enqueue(sim_queue.dequeue())
        
        sim_queue.dequeue()

    # return the last element 
    return sim_queue.dequeue()

# driver code
if __name__ == "__main__":
    print(Russian_Roulette(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))