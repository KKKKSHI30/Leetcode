# Union-Find Approach
# Time: O(nklognk)
# Space: O(nk)
# 2023.07.13: no
class DSU:
    def __init__(self, sz):
        self.representative = [i for i in range(sz)]
        self.size = [1] * sz

    def findRepresentative(self, x):
        if x == self.representative[x]:
            return x
        self.representative[x] = self.findRepresentative(self.representative[x])  # Path compression
        return self.representative[x]

    def unionBySize(self, a, b):
        representativeA = self.findRepresentative(a)
        representativeB = self.findRepresentative(b)

        if representativeA == representativeB:
            return

        if self.size[representativeA] >= self.size[representativeB]:
            self.size[representativeA] += self.size[representativeB]
            self.representative[representativeB] = representativeA
        else:
            self.size[representativeB] += self.size[representativeA]
            self.representative[representativeA] = representativeB


class Solution:
    def accountsMerge(self, accountList):
        accountListSize = len(accountList)
        dsu = DSU(accountListSize)
        emailGroup = {}

        for i in range(accountListSize):
            accountSize = len(accountList[i])

            for j in range(1, accountSize):
                email = accountList[i][j]
                accountName = accountList[i][0]

                if email not in emailGroup:
                    emailGroup[email] = i
                else:
                    dsu.unionBySize(i, emailGroup[email])

        components = {}
        for email, group in emailGroup.items():
            components[dsu.findRepresentative(group)] = components.get(dsu.findRepresentative(group), []) + [email]

        mergedAccounts = []
        for group, emails in components.items():
            component = [accountList[group][0]] + sorted(emails)
            mergedAccounts.append(component)

        return mergedAccounts


# DFS Approach
# Time: O(nklognk)
# Space: O(nk)
# 2023.07.13: no
class Solution2:
    def __init__(self):
        self.visited = set()
        self.adjacent = {}

    def DFS(self, mergedAccount, email):
        self.visited.add(email)
        mergedAccount.append(email)

        for neighbor in self.adjacent[email]:
            if neighbor not in self.visited:
                self.DFS(mergedAccount, neighbor)

    def accountsMerge(self, accountList):
        for account in accountList:
            accountSize = len(account)
            accountFirstEmail = account[1]

            for j in range(2, accountSize):
                email = account[j]
                self.adjacent.setdefault(accountFirstEmail, []).append(email)
                self.adjacent.setdefault(email, []).append(accountFirstEmail)

        mergedAccounts = []
        for account in accountList:
            accountName = account[0]
            accountFirstEmail = account[1]

            if accountFirstEmail not in self.visited:
                mergedAccount = [accountName]
                self.DFS(mergedAccount, accountFirstEmail)
                mergedAccount[1:] = sorted(mergedAccount[1:])
                mergedAccounts.append(mergedAccount)

        return mergedAccounts


# Tests:
test = Solution2()
test.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],
                    ["John","johnsmith@mail.com","john00@mail.com"],
                    ["Mary","mary@mail.com"],
                    ["John","johnnybravo@mail.com"]])
