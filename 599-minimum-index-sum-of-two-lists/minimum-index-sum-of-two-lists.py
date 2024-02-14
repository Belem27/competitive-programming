class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # Create a dictionary to store indices of strings from list1
        index_dict = {word: i for i, word in enumerate(list1)}
        
        # Initialize variables for minimum index sum and result list
        min_index_sum = float('inf')
        result = []
        
        # Iterate through list2
        for j, word in enumerate(list2):
            # Check if the current word is also in list1
            if word in index_dict:
                # Calculate the index sum
                index_sum = j + index_dict[word]
                # Update the minimum index sum and result list if needed
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    result = [word]
                elif index_sum == min_index_sum:
                    result.append(word)
        
        return result