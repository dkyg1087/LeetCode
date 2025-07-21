class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        open_rooms = deque([0])

        visited = {}
        visit_num = 0

        while len(open_rooms) != 0:
            for _ in range(len(open_rooms)):
                key = open_rooms.popleft()
                
                if key in visited:
                    continue
                else:
                    visit_num += 1
                    visited[key] = True
                    for i in rooms[key]:
                        if i in visited:
                            continue
                        else:
                            open_rooms.append(i)
            
            if visit_num == len(rooms):
                return True
        
        return False