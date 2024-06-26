class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0

        for i in range(len(points)-1):
            offsetX = abs(points[i+1][0] - points[i][0])
            offsetY = abs(points[i+1][1] - points[i][1])

            result += max(offsetX, offsetY)
            
        return result
