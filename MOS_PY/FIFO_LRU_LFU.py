from collections import deque, Counter
class PageReplacement:
    def __init__(self, page_frames):
        self.page_frames = page_frames
        self.page_queue = deque()
        self.page_access = []
    def fifo(self, page_references):
        page_faults = 0
        for page in page_references:
            if page not in self.page_frames:
                page_faults += 1
                if len(self.page_frames) == len(self.page_queue):
                    if self.page_queue:
                        self.page_frames.remove(self.page_queue.popleft())
                self.page_frames.add(page)
                self.page_queue.append(page)
            elif page in self.page_frames:
                if page in self.page_queue:
                    self.page_queue.remove(page)
                self.page_queue.append(page)
        return page_faults
    def lru(self, page_references):
        page_faults = 0
        for page in page_references:
            if page not in self.page_frames:
                page_faults += 1
                if len(self.page_frames) == len(self.page_access):
                    self.page_frames.remove(self.page_access.pop(0))
                self.page_frames.add(page)
                self.page_access.append(page)
            else:
                if page in self.page_access:
                    self.page_access.remove(page)
                self.page_access.append(page)
        return page_faults
    def lfu(self, page_references):
        page_faults = 0
        page_counter = Counter()
        for page in page_references:
            if page not in self.page_frames:
                page_faults += 1
                if len(self.page_frames) == len(self.page_access):
                    least_frequent_page = min(self.page_access, key=page_counter.get)
                    self.page_frames.remove(least_frequent_page)
                    self.page_access.remove(least_frequent_page)
                self.page_frames.add(page)
                self.page_access.append(page)
            page_counter[page] += 1
        return page_faults
# Example usage:
if __name__ == "__main__":
    page_references = [1, 2, 3, 4, 5, 1, 2, 3, 6, 7, 8, 7, 8, 9, 7, 8, 9, 5, 4, 5, 4, 2, 3, 2, 1, 2, 3, 6]
    page_frames = set()
    pr = PageReplacement(page_frames)
    print("FIFO Page Faults:", pr.fifo(page_references.copy()))
    pr = PageReplacement(page_frames)
    print("LRU Page Faults:", pr.lru(page_references.copy()))
    pr = PageReplacement(page_frames)
    print("LFU Page Faults:", pr.lfu(page_references.copy()))
