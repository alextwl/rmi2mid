import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rmi2mid",
    version="0.2",
    author="Wei-Li Tang",
    author_email="alex@ip6.tw",
    description="Extract Standard MIDI file (.mid) from RIFF MIDI (RMID) file (.rmi or .mid).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alextwl/rmi2mid",
    py_modules=["rmi2mid"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio :: Conversion",
        "Topic :: Multimedia :: Sound/Audio :: MIDI",
    ],
)
