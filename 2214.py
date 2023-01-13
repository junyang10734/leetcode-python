# 2214. Minimum Health to Beat Game
# Greedy

class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        maxDamage = max(damage)
        if armor >= maxDamage:
            return sum(damage) - maxDamage + 1
        else:
            return sum(damage) - armor + 1