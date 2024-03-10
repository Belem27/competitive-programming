class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        d = {heights[i] : names[i] for i in range(len(names))}
        heights.sort(reverse=True)
        for i in range(len(heights)):
            names[i] = d[heights[i]]
        return names
        
    def bubbleSort(self, heights):
        for n in range(len(heights)-1, 0, -1):
            for i in range(n):
                if heights[i] > heights[i + 1]:
                    heights[i], heights[i + 1] = heights[i + 1], heights[i]
        return heights

    def selectionSort(self, heights):
        for i in range(len(heights)-1):
            min_idx = i
            for j in range(i + 1, len(heights)):
                if heights[j] < heights[min_idx]:
                    min_idx = j
            heights[i], heights[min_idx] = heights[min_idx], heights[i]
        return heights

        def countingSort(self, heights):
            M = max(heights)
            count_arr = [0] * (M + 1)

            for num in heights:
                count_arr[num] += 1
            
            for i in range(1, len(count_arr)):
                count_arr[i] = count_arr[i - 1]

            output_arr = [0] * len(input_arr)

            for i in range(len(input_arr) - 1, -1, -1):
                output_arr[count_array[input_arr[i]] - 1] = input_arr[i]
                count_arr[input_arr[i]] -= 1

