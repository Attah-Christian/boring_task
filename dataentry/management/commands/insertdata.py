from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = 'it will insert data to database'

    def handle(self, *args, **kwargs):
        dataset = [
            {'roll_no': 1003, 'name': 'elite', 'age': 18},
            {'roll_no': 1004, 'name': 'isaac', 'age': 24},
            {'roll_no': 1005, 'name': 'kaffi', 'age': 25},
        ]
        for data in dataset:
            roll_no = data['roll_no']
            existed = Student.objects.filter(roll_no=roll_no).exists()

            if not existed:
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'student with roll no {roll_no} already exist'))
        self.stdout.write(self.style.SUCCESS('data inserted successfully!'))