class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [[0] * rows for _ in range(26)]
        

    def setCell(self, cell: str, value: int) -> None:
        self.sheet[ord(cell[0]) - ord("A")][int(cell[1:])-1] = value

    def resetCell(self, cell: str) -> None:
        self.sheet[ord(cell[0]) - ord("A")][int(cell[1:])-1] = 0        

    def getValue(self, formula: str) -> int:
        regex = r"^=(\d+|[A-Z]+\d+)\+(\d+|[A-Z]+\d+)$"
        m = re.match(regex,formula)
        first,sec = m.groups()
        ans = 0
        if first.isnumeric():
            ans += int(first)
        else:
            ans += self.sheet[ord(first[0]) - ord("A")][int(first[1:])-1]
        
        if sec.isnumeric():
            ans += int(sec)
        else:
            ans += self.sheet[ord(sec[0]) - ord("A")][int(sec[1:])-1]
        
        return ans
        
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)