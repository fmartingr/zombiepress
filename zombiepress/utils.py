import os
from django.conf import settings
from django.contrib.staticfiles.finders import FileSystemFinder
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import SortedDict
from django.utils._os import safe_join
from django.contrib.staticfiles import utils


class ThemeFinder(FileSystemFinder):
    """
    Static files finder to get from the active theme
    (based on AppDirectoriesFinder)
    """
    def __init__(self, apps=None, *args, **kwargs):
        # List of locations with static files
        self.locations = []
        paths = [
            '%s/themes/%s/static' % (
                settings.BASE_PATH,
                get_active_theme()
            ),
        ]
        # Maps dir paths to an appropriate storage instance
        self.storages = SortedDict()
        for root in paths:
            if isinstance(root, (list, tuple)):
                prefix, root = root
            else:
                prefix = ''
            if (prefix, root) not in self.locations:
                self.locations.append((prefix, root))
        for prefix, root in self.locations:
            filesystem_storage = FileSystemStorage(location=root)
            filesystem_storage.prefix = prefix
            self.storages[root] = filesystem_storage
        super(FileSystemFinder, self).__init__(*args, **kwargs)

    def find(self, path, all=False):
        """
        Looks for files in the extra locations
        as defined in ``STATICFILES_DIRS``.
        """
        matches = []
        for prefix, root in self.locations:
            matched_path = self.find_location(root, path, prefix)
            if matched_path:
                if not all:
                    return matched_path
                matches.append(matched_path)
        return matches

    def find_location(self, root, path, prefix=None):
        """
        Finds a requested static file in a location, returning the found
        absolute path (or ``None`` if no match).
        """
        if prefix:
            prefix = '%s%s' % (prefix, os.sep)
            if not path.startswith(prefix):
                return None
            path = path[len(prefix):]
        path = safe_join(root, path)
        if os.path.exists(path):
            return path

    def list(self, ignore_patterns):
        """
        List all files in all locations.
        """
        for prefix, root in self.locations:
            storage = self.storages[root]
            for path in utils.get_files(storage, ignore_patterns):
                yield path, storage



def get_active_theme():
    theme = os.environ.get('ZOMBIEPRESS_THEME', 'fmartingr')
    return theme


def set_current_theme():
    "Get the current active theme."
    theme = get_active_theme()

    # TODO check if path exists!
    settings.TEMPLATE_DIRS += (
        '%s/themes/%s' % (
            settings.BASE_PATH,
            theme
        ),
    )
