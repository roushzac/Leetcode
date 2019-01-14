class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows= len(grid)
        cols=len(grid[0])
        
        MinMatrix=[]
        
        for i in range(rows):
            Mrow =[]
            for j in range(cols):
                Mrow.append(0)
            MinMatrix.append(Mrow)
            
        # initialize first cell
        MinMatrix[0][0]= grid[0][0]
        # fill top row
        for i in range(1,cols):
            MinMatrix[0][i] = MinMatrix[0][i-1] + grid[0][i]
            
        # fill 1st column
        for j in range(1,rows):
            MinMatrix[j][0] =MinMatrix[j-1][0]+ grid[j][0]
            
        for row in range(1,rows):
            for col in range(1,cols):
                downpath = MinMatrix[row-1][col] + grid[row][col]
                rightpath = MinMatrix[row][col-1] + grid[row][col]
                
                gridcell = grid[row][col]
                
                MinMatrix[row][col]= min(downpath,rightpath)
                
        return MinMatrix[rows-1][cols-1]