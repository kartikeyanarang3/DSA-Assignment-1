# Function to implement Tower of Hanoi
def hanoi(n, source, spare, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return 1
    
    # Move n-1 disks from source to spare
    count1 = hanoi(n - 1, source, target, spare)
    
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    
    # Move n-1 disks from spare to target
    count2 = hanoi(n - 1, spare, source, target)
    return count1 + 1 + count2
# The Time Complexity is O(2^n) 
hanoi(3,'A','B','C')
