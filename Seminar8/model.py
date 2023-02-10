journal = {}
path = ''
subject = ''


def set_class(class_path: str):
    global path
    path = 'HomeWorkPython/Seminar8/' + class_path + '.txt'


def set_subject(our_subject: str):
    global subject
    subject = our_subject


def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for line in data:
        if line.split(';')[0] == subject:
            for study in line.split(';')[1].strip().split(', '):
                journal[study.split(':')[0]] = study.split(':')[1].split()
    # print(journal)


def save_file():
    global journal
    new_file = []
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for line in data:
        if line.split(';')[0] != subject:
            new_file.append(line.strip())
    item = []
    for student, marks in journal.items():
        item.append(student + ':' + ' '.join(list(map(str, marks))))
    item = subject + ';' + ', '.join(item)
    new_file.append(item)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(new_file))


def student_mark(student: str, mark: int):
    marks = journal.get(student)
    marks.append(mark)
    journal[student] = marks


def get_journal():
    global journal
    return journal