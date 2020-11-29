# -*- coding: utf-8 -*-

from django.db import connection
from django.db.backends.utils import CursorWrapper
from django.core.management.base import BaseCommand, CommandError
from video.models import Category, Registration


class Command(BaseCommand):
    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            self.migrate_data(cursor)

    def migrate_data(cursor: CursorWrapper):
        cursor.execute(
            """
            insert into video_progress registration_id, category_id
            select r.id, c.id
            from registrations as r
            inner join course co on co.id = r.course_id
            inner join categories c on c.id=co.category_id;
            """
        )
