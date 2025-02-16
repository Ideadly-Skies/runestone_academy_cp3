import random
from Queue import Queue

class Printer:
    def __init__(self, ppm):
        """constructor for the printer class"""
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        """update time_remaining while there's still current_task present"""
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        """check if printer is busy"""
        return self.current_task is not None
    
    def start_next(self, new_task):
        """start next task for this printer"""
        self.current_task = new_task
        # makes sense for us to do this to get time_remaining
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate # (minute per page * 60 seconds / 1 minute)

class Task:
    def __init__(self, time):
        """task constructor for printing task for printer"""
        self.timestamp = time                # represent the time the task is created
        self.pages = random.randrange(1, 21) # the number of pages (1-20)
    
    def get_stamp(self):
        """get timestamp for the task"""
        return self.timestamp

    def get_pages(self):
        """get the number of pages for task"""
        return self.pages

    def wait_time(self, current_time):
        """return the wait time for the task"""
        return current_time - self.timestamp

def new_print_task():
    """create new printing task"""
    num = random.randrange(1, 181) # this is basically the num which generates the task 10 students 2x printing for an hour (20 print task / hour -> 1 print task / 180 seconds)
    return num == 180              # if you want to change this, change the number of students and the amount of pages he/she prints

def simulation(num_seconds, pages_per_minutes):
    """function which depicts simulation for printing"""
    # lab printer
    lab_printer = Printer(pages_per_minutes)
    print_queue = Queue()
    waiting_times = []

    # iterate through each seconds
    for current_second in range(num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)
        
        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            nexttask = print_queue.dequeue()
            waiting_times.append(nexttask.wait_time(current_second))
            lab_printer.start_next(nexttask)

        lab_printer.tick()

    # compute average wait time for simulation 
    average_wait = sum(waiting_times) / len(waiting_times)
    print(
        f"Average Wait {average_wait:6.2f} secs" \
        + f"{print_queue.size():3d} tasks remaining."
    )

if __name__ == "__main__":
    simulation(3600, 5)