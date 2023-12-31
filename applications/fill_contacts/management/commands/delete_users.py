import logging
from django.core.management.base import BaseCommand
from applications.fill_contacts.models import PhoneUser


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "--is-only-auto-generated",
            help="delete only auto generated",
            action="store_true",
        )

    def handle(self, *args, **options):
        is_only_auto_generated: bool = options["is_only_auto_generated"]

        logger = logging.getLogger("django")
        queryset = PhoneUser.objects.all()
        logger.info(f"Current amount of users before: {queryset.count()}")

        queryset_for_delete = queryset

        if is_only_auto_generated:
            logger.info("Delete only auto generated users")
            queryset_for_delete = queryset_for_delete.filter(is_auto_generated=True)

        total_deleted, details = queryset_for_delete.delete()
        logger.info(f"Total deleted: {total_deleted}, details: {details}")

        logger.info(f"Current amount of animals after: {queryset.count()}")
