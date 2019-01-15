class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices==[]:
            return 0
        #make min, best, best pairs lists
        mini=None
        best=0
        bests=[]
        best_pair=[]
        
        for stock in prices:
            # if its the first stock, initialize lists and varibles
            if mini==None:
                mini=stock
                bests.append(best)
                best_pair.append((stock,stock))
            else:
                mini=self.UpdateMin(mini,stock)
                self.UpdateBest(stock,mini,bests)                
        return  bests[-1]
        
    def UpdateMin(self,mini,stock):
        if stock < mini:
            return stock
        else:
            return mini
        
    def UpdateBest(self,stock,mini,bests):
        best_val= bests[-1]
        diff= stock-mini
        
        if diff > best_val:
            bests.append(diff)
        else:
            bests.append(best_val)