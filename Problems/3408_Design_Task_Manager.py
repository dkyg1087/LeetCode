class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.priority = []
        self.edit_dict = {}

        for task in tasks:
            self.add(*task)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.priority,(-priority,-taskId,userId))
        self.edit_dict[taskId] = (-priority,userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId not in self.edit_dict:
            return
        self.edit_dict[taskId] = (-newPriority,self.edit_dict[taskId][1])
        heapq.heappush(self.priority,(-newPriority,-taskId,self.edit_dict[taskId][1]))
        
    def rmv(self, taskId: int) -> None:
        del self.edit_dict[taskId]

    def execTop(self) -> int:
        while True:
            if len(self.priority) == 0:
                return -1
            prio,task,user = self.priority[0]
            if -task not in self.edit_dict or self.edit_dict[-task][0] != prio or user != self.edit_dict[-task][1]:
                heapq.heappop(self.priority)
            else:
                heapq.heappop(self.priority)
                del self.edit_dict[-task]
                return user
                


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()