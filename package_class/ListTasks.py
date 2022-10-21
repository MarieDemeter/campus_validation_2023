from Task import test


class ListTasks:
    def __init__(self):
        self.list = []

    def add_task(self, task):
        self.list.append(task)

    def size_list(self):
        return len(self.list)

    def contains(self, task):
        return task in self.list

    def upper(self):
        list_upper = ListTasks()
        for task in self.list:
            list_upper.list.append(task.upper())

        return list_upper

    def poo(self):
        test()
