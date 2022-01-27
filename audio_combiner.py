from pathlib import Path
from typing import Dict, List, Optional
from logging import Logger, getLogger, WARNING
import re

from define_types import Config

from pydub import AudioSegment
import animation

default_logger = getLogger(__name__)
default_logger.setLevel(WARNING)


class AudioCombiner:
    """
    How to use:

    config = Config(
        // your config
    )

    a = AudioCombiner(config)
    a.exec()
    """

    def __init__(self, conf: Config, out_format: str = "mp3", logger: Logger = default_logger) -> None:

        self.logger = logger

        self.conf = conf
        self.base_path = self.conf.base_path

        self.named_assets: Dict[str, AudioSegment] = {}
        self.numbered_assets: List[AudioSegment] = []

        self.out_format = out_format
        self.result = AudioSegment.silent(duration=0)

    def exec(self) -> None:
        wait_animation = animation.Wait(
            animation=['-', '\\', '|', '/'],
            speed=0.7,
            color="cyan",
        )

        self.logger.warning("loading files...")

        wait_animation.start()
        self.load_numbered_assets()
        self.load_named_assets()
        wait_animation.stop()

        self.logger.warning(
            f"  got {len(self.numbered_assets)} numbered file(s)")
        self.logger.warning(f"  got {len(self.named_assets)} named file(s)")

        self.logger.warn("preparing...")
        self.prepare_join()

        self.logger.warn("saving file...")
        wait_animation.start()
        self.save()
        wait_animation.stop()
        self.logger.warn(
            f"\033[33mfile has been saved to {str(self.conf.out_path)}\033[0m")

    def load_numbered_assets(self) -> None:
        if not self.base_path.exists():
            self.logger.error("source file path is incorrect")
            return

        try:
            src_files_path = sorted(self.base_path.glob(
                "*.mp3"), key=lambda n: int(re.sub(r"\D", "", str(n))))
        except ValueError as e:
            self.logger.error(
                f"{e}\nplease include an integer in the name of mp3 files in base dir")
            return

        self.numbered_assets = [AudioSegment.from_file(
            str(f), format="mp3") for f in src_files_path]

    def load_named_assets(self) -> None:
        for a in self.conf.named_assets:
            p = Path(a.path)
            if not p.exists():
                self.logger.warning(
                    f"{a.path}({a.name}) does not exist")
                self.named_assets[a.name] = None
                continue

            self.named_assets[a.name] = AudioSegment.from_file(str(p), "mp3")

    @staticmethod
    def second2pos(sec: float) -> Optional[int]:
        if sec == None:
            return None

        else:
            return int(1000 * sec)

    def prepare_join(self) -> None:
        """
        Modify self.result
        """
        for s in self.conf.sections:
            if isinstance(s.src, int):
                src = self.numbered_assets[s.src]
            else:
                src = self.named_assets.get(s.src)
                if not src:
                    self.logger.error(f"{s.src} has not been loaded")
                    return

            start = self.second2pos(s.trim[0])
            end = self.second2pos(s.trim[1])

            silent_after = int(1000*s.silent_after)

            self.result += src[start:end]
            if silent_after > 0:
                self.result += AudioSegment.silent(duration=silent_after)

    def save(self) -> None:
        self.result.export(str(self.conf.out_path),
                           format=self.out_format, tags=self.conf.metadata.as_dict())
