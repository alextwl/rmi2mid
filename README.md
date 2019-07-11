# rmi2mid

Extract Standard MIDI file (.mid) from RIFF MIDI (RMID) file (.rmi or .mid).

This is a simple tool to extract minimal RMID chunk from RIFF file (usually with extension .rmi or .mid) and write MIDI data to an independent .mid file.

I wrote this because my favorite MIDI player cannot read RIFF MIDI songs I collected many years ago.

## Usage

### Run script directly

```
python3 rmi2mid.py <.rmi or .mid> <.mid>
```

### For installation by pip/wheel

```
python3 -m rmi2mid <.rmi or .mid> <.mid>
```

## Unsupported format

Currently an RIFF file with (nested) LIST chunks is not supported.

## TODO

* Write a chunk parser. [PEP 594](https://www.python.org/dev/peps/pep-0594/) is going to deprecate and remove chunk module from python 3.8 and 3.10.

## Reference

* [Bundling SMF and DLS data in an “RMID” File (RP-029)](http://web.archive.org/web/20110610135604/http://www.midi.org/about-midi/rp29spec(rmid).pdf)
