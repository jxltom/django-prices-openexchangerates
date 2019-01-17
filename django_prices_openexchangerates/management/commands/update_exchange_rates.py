from django.core.management.base import BaseCommand

from ...tasks import update_conversion_rates, create_conversion_dates


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--all',
            action='store_true',
            dest='all_currencies',
            default=False,
            help='Create entries for all currencies')

    def handle(self, *args, **options):
        if options['all_currencies']:
            all_rates = create_conversion_dates()
        else:
            all_rates = update_conversion_rates()

        verbosity, count = options['verbosity'], 0
        for conversion_rate in all_rates:
            count += 1
            if verbosity >= 1:
                self.stdout.write('%s' % (conversion_rate, ))

        self.stdout.write(
            'Exchange rates for %s currencies are created or updated.' % (count,))
