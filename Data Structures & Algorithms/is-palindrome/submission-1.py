class Solution:
    def isPalindrome(self, s: str) -> bool:
        single_word = "".join(ch.lower() for ch in s if ch.isalnum())
        front = 0
        back = len(single_word) - 1

        while front<back:
            if single_word[front] != single_word[back]:
                return False
            front += 1
            back -= 1
            
        return True