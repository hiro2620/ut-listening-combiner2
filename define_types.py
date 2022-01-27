from dataclasses import dataclass, field, asdict
from typing import List, Union, Dict
from pathlib import Path


@dataclass(frozen=True)
class Section:
    # README.md参照
    src: Union[str, int]
    # 結合に使う[開始位置, 終了位置]で、いずれも秒数(負なら後ろからの時間)
    # Noneは切り取らないことを表す。
    trim: List[Union[int, None]] = field(default_factory=lambda: [None, None])
    # この部分の直後に挿入する無音時間の秒数
    silent_after: float = 0.0


@dataclass(frozen=True)
class NamedAsset:
    path: Path
    # config内で指定するための名前
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
    # 結合するmp3ファイルの各部分　前の要素から順に結合されます。
    sections: List[Section]
    # 出力されるmp3ファイルに書き込まれるメタデータ
    metadata: Metadata = field(default_factory=lambda: Metadata())
    # 出力されるmp3ファイルのパス
    out_path: Path = field(default_factory=lambda: Path("./out/out.mp3"))
    # README.mdを参照
    base_path: Path = field(default_factory=lambda: Path("."))
    named_assets: List[NamedAsset] = field(default_factory=lambda: [])
