class Employee(object):
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

# breadth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.01: yes
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        def recursion(employees, id):
            employee = emap[id]
            self.total_points += employee.importance
            if employee.subordinates:
                for id in employee.subordinates:
                    recursion(employees, id)
        self.total_points = 0
        emap = {e.id: e for e in employees}
        recursion(employees, id)
        return self.total_points

class Solution2(object):
    def getImportance(self, employees, query_id):
        emap = {e.id: e for e in employees}
        def dfs(eid):
            employee = emap[eid]
            return (employee.importance +
                    sum(dfs(eid) for eid in employee.subordinates))
        return dfs(query_id)
# Tests:
tree = [Employee(2,3,[]),Employee(3,3,[]), Employee(1,5,[2,3])]
tree2 = [Employee(1,2,[5]), Employee(5,-3,[])]
test = Solution()
test.getImportance(tree2, 5)

