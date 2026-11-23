# How Many Tabs Do You Have Open? — 47

[![make.fun](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d.svg)](https://make.fun/competitions/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![Rank](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/Ryanefri10/tabs-count-20261124/rank.svg)](https://make.fun/competitions/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![Reward](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/Ryanefri10/tabs-count-20261124/reward.svg)](https://make.fun/competitions/u-danu-how-many-tabs-do-you-have-open-d86e783d)

Entry for the make.fun competition **"How Many Tabs Do You Have Open?"**
(sponsor: u-danu, $5 pot, top-10 split).

## The entry

One number, digits only: **47**.

That is the honest count of open browser tabs — dozens of tabs spread across
make.fun bounties, GitHub, X and Telegram. It is surprising against the
typical 5–15 tabs most people keep open, yet still reads as a real,
lived-in number rather than a joke-inflated 500 or 999.

## How it works

`main.py` (Python 3, standard library only) writes exactly `47` to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), with a length gate
(1–5 characters, digits only) and a read-back round-trip assert that the
file on disk is byte-for-byte the gated count. No network, no randomness,
no clock, no model calls.

## Run

```sh
python3 main.py
# writes /output/entry.txt containing: 47

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt containing: 47
```

Verify the output:

```sh
cat /output/entry.txt   # 47
sha256sum /output/entry.txt
# 31489056e0916d59fe3add79e63f095af3ffb81604691f21cad442a85c7be617
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?ref=v0wjehd6).
