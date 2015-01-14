from FSDiff import FSDiff
from FSIndex import FSIndex
SETTINGS_FILE = 'settings.conf'
fsDiff = FSDiff(SETTINGS_FILE)
fsIndex = FSIndex(SETTINGS_FILE)

fsDiff.diff()