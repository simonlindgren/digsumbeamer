# digsumbeamer

This is a [Beamer](https://github.com/josephwright/beamer) theme for DIGSUM (Centre for Digital Social Research, Umeå University).

## Usage

- Clone the repository and unzip it.
- Run `python3 digsumbeamer.py` for an automatic workflow to create the presentation.
- Upload the generated `main.tex` along with all `*.sty`-files to a blank [Overleaf](https://www.overleaf.com/) project. 
- Create a directory named `images` on Overleaf and upload `logo.png` alongside any images you want to use in the presentation to that directory.
- Compile and download pdf.
- When this has been done once, it will be enough to only upload the `*.tex` and any new images to the same Overleaf project for future presentations.

## Slide types

1. Bullets -- Slide with a header, and a number of bullet points.
2. Centered -- Slide with centered lines of text.
3. Image -- Slide covered by a 16:9 `*.png`-file, named (including the png extension) when running the `digsumbeamer.py` workflow. All images to be used must be in the `images` directory.

## Demo slides

<img src="https://github.com/simonlindgren/digsumbeamer/blob/master/demo/demoslides.png">
