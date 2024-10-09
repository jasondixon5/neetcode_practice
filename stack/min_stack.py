"""
Minimum Stack
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in O(1) time.

Example 1:

Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1
Constraints:

-2^31 <= val <= 2^31 - 1.
pop, top and getMin will always be called on non-empty stacks.

"""

class MinStack:

    def __init__(self):

        self.stack = []
        self.min_stack = []

    def push(self, val):
        
        self.stack.append(val)

        # Decide what to add to min stack
        if not self.min_stack:
            min_val = val
        else:
            min_val = min(val, self.min_stack[-1])
        
        self.min_stack.append(min_val)

    def pop(self):

        # Intentionally avoiding Python list's pop() func 
        
        if self.stack:
            del self.stack[-1]
        
        if self.min_stack:
            del self.min_stack[-1]

        return None 

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def get_min(self):

        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None

class MinStackOriginal:

    def __init__(self):
        
        self.stack = []
        self.min_idx = None
        
    def push(self, val: int) -> None:
        
        # print(f"Pre-push state of stack: {self.stack}")
        # print(f"Pre-push min idx: {self.min_idx}")
        if len(self.stack) == 0:
            self.stack.append(val)    
            self.min_idx = 0
        else:
            self.stack.append(val)
            
            if val < self.stack[self.min_idx]:
                self.min_idx = len(self.stack) - 1
        # print(f"Post-push state of stack: {self.stack}")
        # print(f"Post-push min idx: {self.min_idx}")
    
    def pop(self) -> None:

        idx_to_pop = len(self.stack) - 1

        del self.stack[idx_to_pop]

        if idx_to_pop == self.min_idx:
            self._set_new_min_idx()

    def top(self) -> int:
        return self.stack[-1]
    
    def _set_new_min_idx(self) -> int:
        # After popping the minimum item, find the new min in the stack
        new_min_idx = 0

        for i in range(1, len(self.stack)):
            if self.stack[i] < self.stack[new_min_idx]:
                new_min_idx = i 

        self.min_idx = new_min_idx

        return None
    
    
    def getMin(self) -> int:
        return self.stack[self.min_idx]
        
def test_min_stack_create_new_stack():
    stk = MinStack()
    stk.push(0)
    stk.push(1)
    stk.push(2)
    expected = [0, 1, 2]
    assert stk.stack == expected

def test_min_stack_pop():
    stk = MinStack()
    stk.push(0)
    stk.push(1)
    stk.push(2)
    stk.pop()

    assert stk.stack == [0, 1]

def test_min_stack_min_is_first_item_added():

    stk = MinStack()
    stk.push(9)
    stk.push(15)
    stk.push(25)

    assert stk.min_stack[-1] == 9

def test_min_stack_min_is_second_item_added():

    stk = MinStack()
    stk.push(19)
    stk.push(15)
    stk.push(25)

    assert stk.min_stack[-1] == 15

def test_min_stack_pop_and_min_reset():
    stk = MinStack()
    stk.push(9)
    stk.push(2)
    
    stk.push(1)
    stk.pop()

    assert stk.get_min() == 2 

def test_min_stack_push():
    # TODO: Can this be improved? Partly repeats func test_min_stack_create_new_stack()
    stk = MinStack()
    stk.push(0)
    stk.push(1)
    stk.push(2)
    assert stk.stack == [0, 1, 2]
    stk.push(3)
    assert stk.stack == [0, 1, 2, 3,]

def test_min_stack_top():
    stk = MinStack()
    stk.push(0)
    stk.push(1)
    stk.push(2)
    expected = 2
    assert stk.top() == expected

def test_min_stack_get_min_where_min_is_2():
    stk = MinStack()
    stk.push(5)
    stk.push(2)
    stk.push(20)
    stk.push(3)
    expected = 2
    assert stk.get_min() == 2

    return None

def test_min_stack_site_test_case():

    output = []

    stk = MinStack()
    output.append(stk.push(1))
    output.append(stk.push(2))
    output.append(stk.push(0))
    output.append(stk.get_min())
    output.append(stk.pop())
    output.append(stk.top())
    output.append(stk.get_min())

    # Input: ["MinStack", "push", 1, "push", 2, "push", 0, "get_min", "pop", "top", "get_min"]
    # Removed initial null in site test case output 
    # Output: [null,null,null,0,null,2,1]

    assert output == [None, None, None, 0, None, 2, 1]
