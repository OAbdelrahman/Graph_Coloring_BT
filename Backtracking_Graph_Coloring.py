class MyStack:
    def __init__(self):
        self.stack= []
    
    def push(self, x):
        return self.stack.append(x)
    
    def pop(self):
        try:
            return self.stack.pop()
        except:
            print("Stack is empty... NOTHING to pop!")

    def empty(self):
        if not len(self.stack):
            return True
        else:
            return False

    def top(self):
        if self.empty():
            raise ValueError("Requested top of an empty stack")
        else:
            return self.stack[-1]

    def str(self):
        return str(self.stack)

def graphColoring(G, colors):
    # Each state will include only the nodes that have been colored so far
    initialState = [] # Initial empty state ( No nodes have been colored)
    s = MyStack() # For a depth first search
    s.push(initialState) # Push the initial state onto the Stack
    n= len(G)
    
    #  While we still have states to explore
    while not s.empty():
        currentState = s.pop() # Grab the next state from the stack
        currentNode = len(currentState)
        
        # See if we found a solved state at a leaf node
        # That is, we have colored every bode
        if currentNode == n:
            print(currentState) # Display the solution
            break
        
        else:
            # Produce the state's children (if they are feasible)            
            for color in reversed(colors):
                feasible = True
                for prevNode in range(len(currentState)):
                    if (currentState[prevNode] == color) and G[prevNode][currentNode]:
                        feasible = False 
                        break
                
                if feasible:
                    # Create child by making a copy and appending new col
                     
                    childState = currentState.copy() 
                    childState.append(color)
                    s.push(childState) # Push child onto data structure
                    

                                
if __name__ == "__main__":
    graph = [[False, True, False, False, False, True ], 
            [True, False, True, False, False, True ], 
            [False, True, False, True, True, False], 
            [False, False, True, False, True, False], 
            [False, False, True, True, False, True ], 
            [True, True, False, False, True, False]]
    colors = ['r', 'g', 'b'] 
    graphColoring(graph, colors)