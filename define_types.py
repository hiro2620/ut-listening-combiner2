from dataclasses import dataclass, field, asdict
from typing import List, Union, Dict
from pathlib import Path


@dataclass(frozen=True)
class Section:
    src: Union[str, int]
    trim: List[Union[int, None]] = field(default_factory=lambda: [None, None])
    silent_after: float = 0.0


@dataclass(frozen=True)
class NamedAsset:
    path: Path
    name: str


@dataclass(frozen=True)
class Metadata:
    artist: str = ""
    album: str = ""
    comments: str = ""

    def as_dict(self) -> Dict[str, str]:
        return asdict(self)


@dataclass(frozen=True)
class Config:
    sections: List[Section]
    metadata: Metadata = field(default_factory=lambda: Metadata())
    named_assets: List[NamedAsset] = field(default_factory=lambda: [])
    out_path: Path = field(default_factory=lambda: Path("./out/out.mp3"))
    base_path: Path = field(default_factory=lambda: Path("."))
