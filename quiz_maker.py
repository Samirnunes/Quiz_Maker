import random 
import os
import sys

class quiz():
    def __init__(self, file):
        self.questions = file.readlines() # When it reaches a blank line, it stops.

    def __str__(self):
        all_questions = ''
        for question in self.questions:
            all_questions += question
        return all_questions

    def get_random_question(self):
        try:
            rand_question = random.sample(self.questions,1)
        except:
            print(f"It seems like one or more quiz files don't have any questions. Please delete them or add new questions to them.")
            return ''
        else:
            return rand_question[0]

    @staticmethod
    def get_quiz_files(n):
        quiz_files = []
        for i in range(1, n + 1):
            quiz_files.append(open(os.path.join(sys.path[0],f'quiz{i}.txt'))) # os.path.join(sys.path[0],'file.txt') --> acessing file in the current directory.
        return quiz_files

    @staticmethod
    def generate_student_quiz(n):
        '''Generate the final .txt quiz to the student from n .txt quiz files.'''
        quiz_files = quiz.get_quiz_files(n)
        student_quiz_file = open(os.path.join(sys.path[0],"student_quiz.txt"),'w+') # w+ --> write and read
        student_quiz = quiz(student_quiz_file)
        for file in quiz_files:
            random_question = quiz(file).get_random_question()
            student_quiz_file.write(random_question)
            student_quiz.questions.append(random_question)
        return student_quiz