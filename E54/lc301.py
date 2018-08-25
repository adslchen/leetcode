class Solution:

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        set_ = set()
        lb, rb = 0, 0
        for b in s:
            if b == '(':
                lb += 1
            elif b == ')':
                if lb > 0:
                    lb -= 1
                else:
                    rb += 1

        def rip(s, st, i, lb, rb, open_):
            if i == len(s) and lb == 0 and rb == 0 and open_ == 0:
                set_.add(str(st))
                return
            if lb < 0 or rb < 0 or open_ < 0 or i == len(s):
                return
            if s[i] == '(':
                rip(s, st + s[i], i + 1, lb, rb, open_ + 1)
                rip(s, st, i + 1, lb - 1, rb, open_)
            elif s[i] == ')':
                rip(s, st + s[i], i + 1, lb, rb, open_ - 1)
                rip(s, st, i + 1, lb, rb - 1, open_)
            else:
                rip(s, st + s[i], i + 1, lb, rb, open_)

        rip(s, "", 0, lb, rb, 0)
        return list(set_)
