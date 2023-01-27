class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j, total, count, person = 0, len(people) - 1, 0, 0, 0
        while j >= i:
            if total + people[j] <= limit and person < 2:
                total += people[j]
                j -= 1
                person += 1
            elif total + people[i] <= limit and person < 2:
                total += people[i]
                i += 1
                person += 1
            else:
                count += 1
                total, person = 0, 0
        if total != 0:
            count += 1
        return count