class UndergroundSystem(object):

    def __init__(self):
        self.check_ins = {}
        self.travel_times = defaultdict(lambda: defaultdict(list))

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        start_station, start_time = self.check_ins[id]
        self.travel_times[start_station][stationName].append(t - start_time)

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        avg = sum(self.travel_times[startStation][endStation]) / float(len(self.travel_times[startStation][endStation]))

        return avg

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)