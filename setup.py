from setuptools import setup

setup(
    name="GenomeXtract",
    version="0.1.0",
    packages=["genomextract"],
    entry_points={
        "console_scripts": [
            "findGenome = genomextract.findGenome:main",
            "findClosestGenome = genomextract.findClosestGenome:main",
            "assembleGenome = genomextract.assembleGenome:main",
            "assembleGenes = genomextract.assembleGenes:main",
        ]
    },
)

