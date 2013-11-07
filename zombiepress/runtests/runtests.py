from __future__ import absolute_import
import os
import sys

# fix sys path so we don't need to setup PYTHONPATH
sys.path.insert(0, os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'zombiepress.runtests.settings'

from django.conf import settings
from django.test.utils import get_runner
from django.core.management import call_command


def main():
    TestRunner = get_runner(settings)

    call_command('syncdb', interactive=False)
    call_command('migrate', interactive=False)

    test_runner = TestRunner()
    failures = test_runner.run_tests(
        [],
        verbosity=9,
        interactive=False
    )

    sys.exit(failures)

if __name__ == '__main__':
    main()
