class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # Set es como un hashmap. es O(1) para agregar y buscar.
        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)

        return " "
