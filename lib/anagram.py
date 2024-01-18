# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word = word

    def match(self,words):
        result=[]
        # breakpoint()
        for word_match in words:
            if sorted([letter for letter in word_match]) == sorted([letter for letter in self.word]):
                result.append(word_match)
        return result