class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cutomer_waiting_time = list()
        last_finish_time = 0
        for customer, (arrival, time) in enumerate(customers):
            if(last_finish_time < arrival):
                last_finish_time = arrival
            prepration_finish_time = last_finish_time + time
            cutomer_waiting_time.append(prepration_finish_time - arrival)
            last_finish_time = prepration_finish_time
        
        return sum(cutomer_waiting_time)/len(cutomer_waiting_time)
        