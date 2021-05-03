subj = {}
with open('Uroki', 'r') as file:
    for line in file:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Оьщее количество часов по предмету: {subj}')
