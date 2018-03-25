from collections import UserDict

class PicrossLoader(UserDict):
    
    def __getitem__(self, name):
        problem = UserDict.__getitem__(self, name)
        lines = [[int(s) for s in s_.split(',')]
                 for s_ in problem['lines'].split(' ')]
        columns = [[int(s) for s in s_.split(',')]
                   for s_ in problem['columns'].split(' ')]
        return lines, columns
    

picross = PicrossLoader({
    'moon': {'lines': "2 2 1,2 5 3", 'columns': "2 2 1,2 5 3"},
    'star': {'lines': "2,2 2,2 0 1,1 1,1,1", 'columns': "2,2 2 1 2 2,2"},
    'cat': {'lines': "1,1 2,2 5 1,1,1 7 5,2 3,1 3,1 4,2 7",
            'columns': "1 6 2,6 8 2,6 6,2 1,1 1 1,2 4"},
    'horse': {'lines': "1 4 4,1 8 2,2 3,3 1,5 1,2,2,1 3,3 8",
              'columns': "2,3 2,2 5,3 8,1 1,2,1 1,1,1 1,3,1 7 3,2 2,2"},
    'house': {
        'lines': "1 2,5 2,2,1,2 11 5,1,5 15 1,1 1,5,1 1,1,1,1,5,1 1,5,5,1 1,1,1,1,5,1 1,5,5,1 1,5,1 1,5,1 1,5,1",
        'columns': "10 5 5,5 3,1,1,1 4,5 5,1,1,1 1,1,1,5 6 1,1,1,7 5,7 4,7 3,7 2,7 2 10"
    },
    'duck': {
        'lines': "3 5 4,3 7 5 3 5 1,8 3,3,3 7,3,2 5,4,2 8,2 10 2,3 6",
        'columns': "3 4 5 4 5 6 3,2,1 2,2,5 4,2,6 8,2,3 8,2,1,1 2,6,2,1 4,6 2,4 1"
    },
})