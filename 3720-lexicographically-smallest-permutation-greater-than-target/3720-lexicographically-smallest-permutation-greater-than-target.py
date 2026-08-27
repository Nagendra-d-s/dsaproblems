class Solution:
    def dfs(self, ind, target, temp, freq, ans):
        n = len(target)
        if ind == n:
            return False

        minChar = ord(target[ind]) - ord('a')
        for ch in range(minChar, 26):
            if freq[ch] == 0:
                continue

            if ch == minChar:
                freq[ch] -= 1
                temp.append(chr(ch + ord('a')))
                if self.dfs(ind + 1, target, temp, freq, ans):
                    return True
                temp.pop()
                freq[ch] += 1
            else:
                freq[ch] -= 1
                temp.append(chr(ch + ord('a')))

                can = temp[:]  # copy current prefix
                tempCnt = freq[:]

                for c in range(26):
                    can.extend([chr(c + ord('a'))] * tempCnt[c])

                ans[0] = ''.join(can)
                temp.pop()
                freq[ch] += 1
                return True
        return False

    def lexGreaterPermutation(self, s, target):
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1

        ans = [""]
        if self.dfs(0, target, [], freq, ans):
            return ans[0]
        return ""