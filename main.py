from logging import getLogger, DEBUG

from audio_combiner import AudioCombiner
from config import config


logger = getLogger(__name__)
logger.setLevel(DEBUG)

if __name__ == "__main__":
    AudioCombiner(config).exec()
