# Number of Burgers with No Waste of Ingredients
# Math / Greedy

# runtime: faster than 83.59%
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices > 4*cheeseSlices or tomatoSlices < 2*cheeseSlices:
            return []
        elif tomatoSlices == 4*cheeseSlices:
            return [cheeseSlices, 0]
        elif tomatoSlices == 2*cheeseSlices:
            return [0, cheeseSlices]
        else:
            sub = tomatoSlices - 2*cheeseSlices
            if sub%2 == 0:
                n = (tomatoSlices - 2*cheeseSlices)//2
                return [n, cheeseSlices - n]
            else:
                return []
        
        return []