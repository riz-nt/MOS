import numpy as np
class BankersAlgorithm:
    def __init__(self, allocation, max_demand, available):
        self.allocation = np.array(allocation)
        self.max_demand = np.array(max_demand)
        self.available = np.array(available)
        self.num_processes, self.num_resources = self.allocation.shape
    def is_safe_state(self):
        work = self.available.copy()
        finish = np.zeros(self.num_processes, dtype=bool)
        # Check if a process can be satisfied with the current resources
        def can_satisfy(process):
            return all(need <= work) and not finish[process]
        safe_sequence = []
        while np.any(~finish):
            found = False
            for process in range(self.num_processes):
                need = self.max_demand[process] - self.allocation[process]
                if can_satisfy(process):
                    work += self.allocation[process]
                    finish[process] = True
                    safe_sequence.append(process)
                    found = True
                    break
            if not found:
                break
        return len(safe_sequence) == self.num_processes, safe_sequence
# Example usage:
if __name__ == "__main__":
    allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]
    max_demand = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]
    available = [3, 3, 2]
    banker = BankersAlgorithm(allocation, max_demand, available)
    safe, sequence = banker.is_safe_state()
    if safe:
        print("Safe Sequence:", sequence)
    else:
        print("Unsafe State, deadlock may occur")

