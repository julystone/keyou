class Solution:
    def defangIPaddr(self, address) -> str: return address.replace(".", "[.]", -1)


if __name__ == '__main__':
    S = Solution()
    print(S.defangIPaddr("1.1.1.1"))
