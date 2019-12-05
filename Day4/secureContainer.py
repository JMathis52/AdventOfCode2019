# How many different passwords within the range given
# in your puzzle input meet the following criteria?
#
# Key facts about the password:
#   - It is a six digit number
#   - The value is within the range given in the puzzle
#     input
#   - Two adjacent digits are the same (like 22 in 122345)
#   - Going from left to right, the digits never decrease;
#     they only ever increase or stay the same
#     * e.g. 111123 or 135679
#
# Other than the range rule, the following are true:
#   - 111111 meets these criteria
#   - 223450 does not meet these criteria (decreasing)
#   - 123789 does not meet these criteria (no double)
#
# Part 2 Information
#
# New Criteria
#   - the two adjacent mathcing digits are not part of a larger group of matching
#     digits
#       * 112233 meets the criteria
#       * 123444 no longer meets the criteria
#       * 111122 meets the criteria

FILE_PATH = "passwordRange.txt"

# Brute force approach
# what about using a hashtable??
############################################################################
# def differentPasswords(low, high):
#     # print(low, high)
#     matches = [] 
#     for i in range(low, high + 1):
#         # convert number to string so we can have access to string methods
#         numString = str(i)
#         adjacentMatch = False
#         decreasing = False
#         for j in range(0, len(numString) - 1):
#             # break if we have decreasing order
#             if (numString[j] > numString[j + 1]):
#                 decreasing = True
#                 break
#             if (numString[j] == numString[j + 1]):
#                 adjacentMatch = True
        
#         if (adjacentMatch and not decreasing):
#             matches.append(i)
    
#     return len(matches)

def differentPasswords(low, high):
    matches = []
    for num in range(low, high + 1):
        # convert number to string so we can have access to string methods
        numString = str(num)
        hashTable = {}
        for i in range(0, len(numString)):
            currVal = int(numString[i])
            maxKey = max(hashTable.keys()) if len(hashTable.keys()) > 0 else -1
            # decreasing
            if (currVal < maxKey):
                break
            hashTable.update({currVal: hashTable.get(currVal, 0) + 1})
        
        hashValues = hashTable.values()
        hashLength = sum(hashValues)
        # password length must be 6
        if (hashLength == 6):
            adjacentMatch = True if 2 in hashValues else False
            if (adjacentMatch):
                matches.append(num)
    
    return len(matches)

def getPasswordRange(filename):
    file = open(filename, "r")
    passwordRange = file.readline()
    return list(map(lambda x: int(x), passwordRange.strip().split('-')))

if __name__ == "__main__":
    low, high = getPasswordRange(FILE_PATH)
    print(differentPasswords(low, high))
