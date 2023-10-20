class Student:#Конструктор класса Студент
    def __init__(self, surname, name, patronymic, birth_date, address, phone, faculty, course):#Принимает различные аргументы
        self._surname = surname
        self._name = name
        self._patronymic = patronymic
        self._birth_date = birth_date
        self._address = address
        self._phone = phone
        self._faculty = faculty
        self._course = course

    @property
    def faculty(self):
        return self._faculty#Возвращает поле faculty

    @property
    def course(self):
        return self._course#Возвращает поле course

    def __str__(self):
        return f'Student: {self._surname} {self._name} {self._patronymic}'#Возвращает строковое представление объекта класса Student


student = Student('Петрова', 'Анастасия', 'Левьева', '15.04.2001', 'ул.Максимова 1','12332123', 'IT', 2)#Student с передачей значений для каждого аргумента конструктора
print(student)#Student с передачей значений для каждого аргумента конструктора
print(f'Факультет: {student.faculty}')#Выводится значение свойства faculty объекта student, что вызывает метод faculty

print(f'Курс: {student.course}')#Выводится значение свойства course объекта student, что вызывает метод course
