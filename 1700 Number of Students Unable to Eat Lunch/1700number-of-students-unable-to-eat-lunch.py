class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        rounds_passed = 0
        while( len(students)!= 0 and rounds_passed < len(students)):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                rounds_passed = 0
            else:
                student = students.pop(0)
                students.append(student)
                rounds_passed+=1
        return len(students)

        