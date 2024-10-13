import csv
import datetime
from django.apps import apps
from django.core.management.base import BaseCommand, CommandParser
from dataentry.models import Student


class Command(BaseCommand):
    help = "export data from student model to a csv file"

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='model name')

    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name'].capitalize()

        model = None

        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                pass
        if not model:
            self.stderr.write(f'model {model_name} could not be found')
            return
        data = model.objects.all()

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")


        file_path = f'exported_{model_name}_data_{timestamp}.csv'

        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)

            writer.writerow([field.name for field in model._meta.fields])

            for datum in data:
                writer.writerow([getattr(datum, field.name) for field in model._meta.fields])

        self.stdout.write(self.style.SUCCESS('data exported successfully'))