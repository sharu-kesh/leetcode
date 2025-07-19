class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        for path in folder:
            if not res: res.append(path)
            else:
                prev = res[-1]
                if path.startswith(prev) and len(path) > len(prev) and path[len(prev)] == '/':
                    continue     
                else:
                    res.append(path)
        return res