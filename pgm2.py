class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
class Block:
    def __init__(self, data):
        self.data = data
        self.next_block = None
def sequential_allocation(files, disk_blocks):
    allocated_space = 0
    for file in files:
        if allocated_space + file.size <= disk_blocks:
            allocated_space += file.size
            print(f"Allocated {file.name} using sequential allocation")
        else:
            print(f"Not enough space to allocate {file.name} using sequential allocation")
def indexed_allocation(files, disk_blocks):
    index_blocks = len(files)
    if index_blocks <= disk_blocks:
        print("Allocating index blocks...")
        for file in files:
            print(f"Allocated index block for {file.name}")
            allocated_blocks = 0
            while allocated_blocks < file.size:
                print(f"Allocated data block for {file.name}")
                allocated_blocks += 1
    else:
        print("Not enough space to allocate index blocks for each file")
def linked_allocation(files, disk_blocks):
    print("Allocating data blocks...")
    for file in files:
        if file.size <= disk_blocks:
            allocated_blocks = 0
            current_block = Block(file.name)
            while allocated_blocks < file.size:
                print(f"Allocated data block for {file.name}")
                allocated_blocks += 1
                if allocated_blocks < file.size:
                    current_block.next_block = Block(file.name)
                    current_block = current_block.next_block
        else:
            print(f"Not enough space to allocate {file.name} using linked allocation")
# Example usage:
if __name__ == "__main__":
    disk_blocks = 10
    files = [
        File("file1", 3),
        File("file2", 5),
        File("file3", 2)
    ]
    print("Sequential Allocation:")
    sequential_allocation(files, disk_blocks)
    print("\nIndexed Allocation:")
    indexed_allocation(files, disk_blocks)
    print("\nLinked Allocation:")
    linked_allocation(files, disk_blocks)
