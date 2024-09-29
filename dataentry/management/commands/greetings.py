from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "greet the user"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='specify user name')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        greetings = f'hi {name}, good morning!'
        self.stdout.write(greetings)
        self.stderr.write(greetings)
        self.stdout.write(self.style.WARNING(greetings))
        self.stdout.write(self.style.SUCCESS(greetings))