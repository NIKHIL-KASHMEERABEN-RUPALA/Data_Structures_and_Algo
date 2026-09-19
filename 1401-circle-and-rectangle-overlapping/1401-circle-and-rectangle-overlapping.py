class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the closest point on the rectangle to the circle's center
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        
        # Calculate the squared distance from the center to this closest point
        dx = closest_x - xCenter
        dy = closest_y - yCenter
        
        return dx * dx + dy * dy <= radius * radius