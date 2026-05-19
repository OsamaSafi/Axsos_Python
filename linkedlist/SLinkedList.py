class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


class SList: 
    def __init__(self):
        self.head = None
        
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next 
        return self

    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head     
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self
    
    def remove_from_front(self):
        """Removes the first node and returns its value."""
        if self.head is None:
            return None
        
        removed_node = self.head
        self.head = self.head.next
        return removed_node.value

    def remove_from_back(self):
        """Removes the last node and returns its value."""
        if self.head is None:
            return None
        
        if self.head.next is None:
            removed_value = self.head.value
            self.head = None
            return removed_value
        runner = self.head
        while runner.next.next is not None:
            runner = runner.next
        
        removed_value = runner.next.value
        runner.next = None 
        return removed_value

    def remove_val(self, val):
        """Removes the first node with the specified value."""
        if self.head is None:
            return None

        if self.head.value == val:
            return self.remove_from_front()

        runner = self.head
        while runner.next is not None:
            if runner.next.value == val:
                removed_node = runner.next
                runner.next = runner.next.next 
                return removed_node.value
            runner = runner.next
        
        return None