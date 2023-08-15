from django.core.management.base import BaseCommand
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class Command(BaseCommand):
    help = 'Watch for changes and automatically restart the Django development server'

    def handle(self, *args, **options):
        class Handler(FileSystemEventHandler):
            def on_any_event(self, event):
                if event.is_directory:
                    return
                if event.src_path.endswith('.py'):
                    subprocess.call(['python', 'manage.py', 'runserver'])

        event_handler = Handler()
        observer = Observer()
        observer.schedule(event_handler, '.', recursive=True)
        observer.start()

        try:
            while True:
                observer.join()
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
