class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if ((ord(coordinates[0]) - 96) % 2 == 0 and int(coordinates[1]) % 2 == 0) or ((ord(coordinates[0]) - 96) % 2 != 0 and int(coordinates[1]) % 2 != 0):
            return False
        else:
            return True