class DLLNode:
    def __init__(self, url: str):
        self.data = url
        self.prev, self.next = None, None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = DLLNode(homepage)
        self.curr = self.history
        

    def visit(self, url: str) -> None:
        new_website = DLLNode(url)
        self.curr.next = new_website
        new_website.prev = self.curr
        self.curr = new_website
        

    def back(self, steps: int) -> str:
        while(steps > 0 and self.curr.prev):
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.data
        

    def forward(self, steps: int) -> str:
        while(steps > 0 and self.curr.next):
            self.curr = self.curr.next
            steps -= 1
        return self.curr.data
        


# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory("homepage")
obj.visit("hello")
print(obj.history.next.data)
# print(obj.forward(2))
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)