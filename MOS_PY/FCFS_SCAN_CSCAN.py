class DiskScheduler:
    def __init__(self, requests, head_start):
        self.requests = requests
        self.head_position = head_start
    def fcfs(self):
        total_seek_time = 0
        for request in self.requests:
            total_seek_time += abs(request - self.head_position)
            self.head_position = request
        return total_seek_time
    def scan(self):
        total_seek_time = 0
        sorted_requests = sorted(self.requests)
        min_request = sorted_requests[0]
        max_request = sorted_requests[-1]
        # Move the head towards the maximum request
        for request in sorted_requests:
            if request >= self.head_position:
                total_seek_time += abs(request - self.head_position)
                self.head_position = request
        # Move the head towards the minimum request
        total_seek_time += abs(max_request - min_request)
        self.head_position = min_request
        return total_seek_time
    def c_scan(self):
        total_seek_time = 0
        sorted_requests = sorted(self.requests)
        max_request = sorted_requests[-1]
        # Move the head towards the maximum request
        for request in sorted_requests:
            if request >= self.head_position:
                total_seek_time += abs(request - self.head_position)
                self.head_position = request
        # Move the head to the beginning of the disk
        total_seek_time += abs(max_request)
        self.head_position = 0
        return total_seek_time
# Example usage:
if __name__ == "__main__":
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    head_start = 53
    scheduler = DiskScheduler(requests, head_start)
    print("FCFS Seek Time:", scheduler.fcfs())
    print("SCAN Seek Time:", scheduler.scan())
    print("C-SCAN Seek Time:", scheduler.c_scan())
