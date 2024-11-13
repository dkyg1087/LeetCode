class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Create a set of all words in the word list for quick lookup.
        wordSet = set(wordList)

        # If endWord is not in the word list, return 0.
        if endWord not in wordSet:
            return 0

        # Use a queue to perform BFS (Breadth-First Search).
        wordQueue = deque([beginWord])

        # Distance from the beginWord (initially 1).
        distance = 1

        while wordQueue:
            size = len(wordQueue)
            distance += 1  # Increase distance at each level of BFS

            for _ in range(size):
                currWord = wordQueue.popleft()

                # Try changing each character of the current word
                for i in range(len(currWord)):
                    for j in range(26):  # Try all lowercase letters
                        temp = currWord[:i] + chr(ord('a') + j) + currWord[i+1:]

                        # If the new word matches the endWord, return the distance
                        if temp == endWord:
                            return distance

                        # If the new word is in the set, add it to the queue and remove it from the set
                        if temp in wordSet:
                            wordQueue.append(temp)
                            wordSet.remove(temp)

        return 0  # Return 0 if no transformation sequence is found
