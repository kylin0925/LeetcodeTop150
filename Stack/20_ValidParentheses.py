class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        queue = []
        for p in s:
            if p == '(' or p == '[' or p == "{":
                queue.append(p)
            else:
                if len(queue) < 1:
                    return False
                if p == ')':
                    if queue[-1] == '(':
                        queue.pop()
                    else:
                        return False
                elif p == ']':
                    if queue[-1] == '[':
                        queue.pop()
                    else:
                        return False

                elif p == '}':
                    if queue[-1] == '{':
                        queue.pop()
                    else:
                        return False
        if len(queue) == 0:
            return True
        else:
            return False