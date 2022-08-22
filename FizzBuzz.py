from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        i = 1
        while i <= n:
            if i % 3 == 0 and i % 5 == 0:
                output.append("FizzBuzz")
            elif i % 3 == 0:
                output.append("Fizz")
            elif i % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(i))
            i += 1
        return output
