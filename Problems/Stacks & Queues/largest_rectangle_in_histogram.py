#Given an array heights representing histogram bar heights, find the maximum rectangular area that can be formed.
#heights = [2, 1, 5, 6, 2, 3]
#Output: 10


def largestRectangleArea(heights):
    stack = []  # stack to store indices
    max_area = 0
    heights.append(0)  # Add a sentinel to pop all remaining bars at the end

    for i, h in enumerate(heights):
        while stack and h < heights[stack[-1]]:
            # Pop the top
            height = heights[stack.pop()]
            # Calculate width
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i
            # Update max_area
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area

# Example usage
heights = [2, 1, 5, 6, 2, 3]
print("Largest Rectangle Area:", largestRectangleArea(heights))



#Output for Example:

#Largest Rectangle Area: 10

# How it Works

# Stack keeps indices of bars in increasing height order.

# When a smaller height is found, pop from stack and calculate the area using the popped bar as height.

# Width = difference between current index i and the previous index in stack (i - stack[-1] - 1) or i if stack is empty.

# Sentinel 0 at the end ensures all remaining bars are processed.