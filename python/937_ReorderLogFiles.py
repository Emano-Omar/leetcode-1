class Solution:
    def reorderLogFiles(self, logs: 'List[str]') -> 'List[str]':
        
        return ['0']

def main():
    print(Solution().reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
    # Output:  ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

if __name__ == '__main__':
    main()
