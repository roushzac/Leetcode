class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        DMatrix=[]
        for i in range(rows):
            r =[]
            for j in range(cols):
                r.append(0)
            DMatrix.append(r)
        
        DMatrix[0][0] = 1
        blocked= False
        #fill 1st row
        for i in range(cols):
            # if we hit an obstacle, the rest of cells in 
            # the row are blocked
            if obstacleGrid[0][i] == 1:
                blocked = True
            if blocked:
                DMatrix[0][i] = 0
            else:
                DMatrix[0][i] = 1
        blocked = False        
        # fill the 1st col
        for j in range(rows):
            if obstacleGrid[j][0] ==1:
                blocked = True
            if blocked:
                DMatrix[j][0] = 0
            else:
                DMatrix[j][0] = 1
                
        
            
        for i in range(1,rows):
            for j in range(1,cols):
                if obstacleGrid[i][j] ==1:
                    DMatrix[i][j] =0
                else:
                    DMatrix[i][j] = DMatrix[i-1][j] + DMatrix[i][j-1]
                
        return DMatrix[rows-1][cols-1]