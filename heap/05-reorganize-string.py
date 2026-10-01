class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        import heapq

        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        heap = []

        for ch in freq:
            heapq.heappush(heap , (-freq[ch], ch))

        result = []
        prev_count = 0
        prev_char = ""

        while heap:
            count , char = heapq.heappop(heap)

            if char == prev_char:
                if not heap:
                    return ""

                count2 , char2 = heapq.heappop(heap)

                result.append(char2)

                count2 += 1

                if count2 < 0 :
                    heapq.heappush(heap, (count2, char2))

                heapq.heappush(heap, (count, char))

                prev_char = char2

            else:
                result.append(char)
                count += 1

                if count < 0:
                    heapq.heappush(heap, (count, char))

                prev_char = char

        return "".join(result)
