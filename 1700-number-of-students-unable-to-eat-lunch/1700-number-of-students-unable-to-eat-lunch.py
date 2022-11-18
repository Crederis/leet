class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        x = 0
        
        while len(students) > 0:
            if students[0] == sandwiches[0]:
                x = 0
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))
                x += 1
                
            if x > len(students):
                break
                
        return len(students)