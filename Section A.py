class Solution:
    def groupAnagrams(self, strs): # <--- indented this line correctly
        result = {}
        for i in strs:
            x = "".join(sorted(i))  # <--- inserted "i" here
            if x in result:
                result[x].append(i)
            else:
                result[x] = [i]
        return list(result.values())


obj = Solution()
print(obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# Indentation error problem in line 2. Code Python is sensitive to code indentations.
# Problem at line 5. There's no argument passed to 'sorted()'. An error is thrown as there is nothing to be sorted.
# There is no need to create a class for this. A simple function was enough to do exactly the same.
# Good problem solving technique by separating the logic 'groupAnagrams()' from the problem itself.
# There are no comments, another user might not know what is going on e.g. at line 8. Leave comments for other users.
# There are no nested loops, which is a good thing. This operates at O(n).

# All in all good job, just make sure next time you do not include unnecessary things like here you created a class and
# do not forget to pass you arguments, indent code correctly. Good modular approach by separating logic from problems.
# Lastly make sure you include comments.


