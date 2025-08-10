class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        land = min(s + d for s, d in zip(landStartTime, landDuration))
        water = min(s + d for s, d in zip(waterStartTime, waterDuration))
        water_land =  min(max(s, water) + d for s, d in zip(landStartTime, landDuration))
        land_water =  min(max(s, land) + d for s, d in zip(waterStartTime, waterDuration))
        return min(water_land, land_water)
        