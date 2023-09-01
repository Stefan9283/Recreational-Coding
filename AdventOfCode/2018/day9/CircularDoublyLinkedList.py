

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self) -> str:
        return f'{self.data}'


class CircularDoublyLinkedList:
    def __init__(self) -> None:
        self.curr = None
        self.size = 0
    
    def add(self, data):
        n = Node(data)
        
        self.size += 1
        
        if self.curr == None:
            self.curr = n
            n.next = n
            n.prev = n
            return
        next_ = self.curr.next
        self.curr.next = n
        n.prev = self.curr
        n.next = next_
        next_.prev = n
        
    def get(self):
        return self.curr.data
    
    def remove(self):
        if not self.curr:
            return

        self.size -= 1

        # TODO
        if self.curr == self.curr.next:
            self.curr = None
            return    
        
        prev_ = self.curr.prev
        next_ = self.curr.next
        
        self.curr = next_
        prev_.next = next_
        next_.prev = prev_
    
    def shift(self, pos):
        if pos > 0:
            for _ in range(pos):
                self.curr = self.curr.next
        else:
            for _ in range(-pos):
                self.curr = self.curr.prev
                
    def __repr__(self) -> str:
        curr = self.curr
        tmp = curr
        nodes = []
        while True:
            if tmp in nodes:
                break
            if tmp == curr:
                nodes.append((tmp,))
            else:
                nodes.append(tmp)
            tmp = tmp.next
        return ' <-> '.join(list(map(str, nodes)))
    
