class PageTable:
    def __init__(self, num_frames):
        self.page_table = {}
        self.num_frames = num_frames

    def map_page(self, logical_address, frame_number):
        self.page_table[logical_address] = frame_number
    def translate_address(self, logical_address):
        if logical_address in self.page_table:
            return self.page_table[logical_address]
        else:
            return None
class Memory:
    def __init__(self, num_frames):
        self.frames = [None] * num_frames
    def load_page(self, frame_number, page_data):
        self.frames[frame_number] = page_data
    def get_page(self, frame_number):
        return self.frames[frame_number]
class Process:
    def __init__(self, process_id, pages):
        self.process_id = process_id
        self.pages = pages
def simulate_paging(processes, memory_size):
    num_frames = memory_size // 4  # Assuming each page is 4 units in size
    memory = Memory(num_frames)
    page_table = PageTable(num_frames)
    for process in processes:
        print(f"Loading process {process.process_id} into memory...")
        for i, page in enumerate(process.pages):
            frame_number = i % num_frames
            memory.load_page(frame_number, page)
            page_table.map_page((process.process_id, i), frame_number)
            print(f"Page {i} of process {process.process_id} loaded into frame {frame_number}")
    print("\nAddress Translation:")
    for process in processes:
        print(f"Process {process.process_id} pages:")
        for i, _ in enumerate(process.pages):
            logical_address = (process.process_id, i)
            physical_address = page_table.translate_address(logical_address)
            print(f"Logical Address: {logical_address} -> Physical Address: {physical_address}")
# Example usage:
if __name__ == "__main__":
    processes = [
        Process(1, ['A', 'B', 'C', 'D', 'E']),
        Process(2, ['F', 'G', 'H', 'I', 'J']),
    ]
    memory_size = 16  # 16 units of memory
    simulate_paging(processes, memory_size)
