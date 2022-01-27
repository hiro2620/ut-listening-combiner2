from pathlib import Path

from define_types import Config, Metadata, NamedAsset, Section

config = Config(
    out_path=Path("./out/2016.mp3"),
    sections=[
        Section(src="head", trim=[4.0, None]),
        Section(src="A_pre"),
        Section(src=0, silent_after=30),
        Section(src=0, silent_after=60),
        Section(src="B_pre"),
        Section(src=1, silent_after=30),
        Section(src=1, silent_after=60),
        Section(src="C_pre"),
        Section(src=2, silent_after=30),
        Section(src=2, silent_after=10),
        Section(src="end"),
    ],
    named_assets=[
        NamedAsset(name="head", path="./assets/head.mp3"),
        NamedAsset(name="A_pre", path="./assets/apre.mp3"),
        NamedAsset(name="B_pre", path="./assets/bpre.mp3"),
        NamedAsset(name="C_pre", path="./assets/cpre.mp3"),
        NamedAsset(name="end", path="./assets/end.mp3"),
    ],
    metadata=Metadata(
        artist="駿台",
        album="東大入試詳解15年"
    ),
)


config = Config(
    out_path=Path("./out/2021.mp3"),
    sections=[
        Section(src=0),
        Section(src=1),
        Section(src=2, silent_after=30, trim=[None, -6]),
        Section(src=2, silent_after=60),
        Section(src=3),
        Section(src=4, silent_after=30, trim=[None, -6]),
        Section(src=4, silent_after=60),
        Section(src=5),
        Section(src=6, silent_after=30, trim=[None, -6]),
        Section(src=6),
    ],
    metadata=Metadata(
        artist="駿台",
        album="青本"
    ),
)
