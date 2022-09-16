class Solution(object):
    def convert(self, s, numRows):
        a = [[] for _ in range(numRows)]

        def dfs(a, left_string, direction):
            if not left_string:
                return a

            if direction == "godown":
                for i in range(numRows):
                    if left_string:
                        a[i].append(left_string[0])
                        left_string = left_string[1:]
                direction = "upper_right"
            else:
                for i in range(numRows - 1, 1, -1):
                    if left_string:
                        a[i - 1].append(left_string[0])
                        left_string = left_string[1:]
                direction = "godown"
            return dfs(a, left_string, direction)

        arrays = dfs(a, s, "godown")
        result = ""
        for arr in arrays:
            result += "".join(arr)
        return result
