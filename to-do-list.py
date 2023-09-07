import datetime

class Task:
    def __init__(self, name, priority, estimated_time):
        self.name = name
        self.priority = priority
        self.estimated_time = estimated_time
        self.time_block = None

class TimeBlock:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.tasks = []

class TimeBlockedToDoScheduler:
    def __init__(self, work_start_time, work_end_time):
        self.work_start_time = work_start_time
        self.work_end_time = work_end_time
        self.time_blocks = []
        self.tasks = []  

    def add_task(self, task):
        self.tasks.append(task)

    def schedule_tasks(self):
        self.tasks.sort(key=lambda x: x.priority, reverse=True)
        current_time = self.work_start_time

        while current_time < self.work_end_time and self.tasks:
            task = self.tasks.pop(0)

            if current_time + datetime.timedelta(minutes=task.estimated_time) <= self.work_end_time:
                start_time = current_time
                end_time = current_time + datetime.timedelta(minutes=task.estimated_time)
                time_block = TimeBlock(start_time, end_time)
                time_block.tasks.append(task)
                task.time_block = time_block
                self.time_blocks.append(time_block)
                current_time = end_time

    def display_schedule(self):
        for time_block in self.time_blocks:
            print(f"Time Block: {time_block.start_time.strftime('%H:%M')} - {time_block.end_time.strftime('%H:%M')}")
            for task in time_block.tasks:
                print(f"  Task: {task.name} (Priority: {task.priority}, Estimated Time: {task.estimated_time} min)")

if __name__ == "__main__":
    work_start_time = datetime.datetime.strptime("09:00", "%H:%M")
    work_end_time = datetime.datetime.strptime("18:00", "%H:%M")

    scheduler = TimeBlockedToDoScheduler(work_start_time, work_end_time)

    task1 = Task("Write Proposal", 5, 120)
    task2 = Task("Review Presentation", 3, 60)
    task3 = Task("Email Client", 2, 30)
    task4 = Task("Brainstorm Ideas", 4, 90)
    task5 = Task("Update Website", 2, 45)

    scheduler.add_task(task1)
    scheduler.add_task(task2)
    scheduler.add_task(task3)
    scheduler.add_task(task4)
    scheduler.add_task(task5)

    scheduler.schedule_tasks()
    scheduler.display_schedule()
