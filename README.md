# More hierarchical documentation for THE ANALOG THING

This repository is supposed to hold the [Sphinx](https://sphinx-doc.org/)
source code for [The Analog Thing](https://the-analog-thing.org/). 
This is an experiment to replace 
[The Analog Thing Wiki](https://the-analog-thing.org/wiki/) which is 
percieved as crowdy amongst the 
[anabrid](https://anabrid.com/) developers.

## Installation of the Document Builder

This documentation uses https://bashtage.github.io/sphinx-material/

Installation requires Python and Pip and then goes by typing in

   pip install git+https://github.com/bashtage/sphinx-material.git
   
This should also install sphinx as dependency.

## How to contribute (workflow)

You have to use Sphinx locally in order to edit "interactively" and
build the output files. There is no web frontend (unlike the Wiki).
For minor modifications, you can also use Github or Gitlab as a web
frontend to simple tasks as editing text files and uploading images.

The documentation is managed within Git, so you also need a git client.
This however makes it easy to clone, fork and create pull requests.
We can also build upon Github for user managament.

Once you [got Sphinx installed](https://www.sphinx-doc.org/en/master/usage/installation.html),
editing is as simple as typing `make html` and opening `_build/html/index.html`
with the Browser.

You should also be able to type `make latexpdf` and opening
`_build/latex/thatdocs.pdf`, but it is known that Latex is more sensitive
to errors then HTML.

## Tips and Guides

Here is a https://sphinx-cheat-sheet.readthedocs.io/en/latest/

Here is another one: https://sphinx-tutorial.readthedocs.io/cheatsheet/

Sphinx is using ReStructuredText (RST) as markup language. It is
comparable to Markdown but different in some respects. See
https://restructuredtext.readthedocs.io/en/latest/rst_guide.html
for the full guide.

Hint: You could consider using
https://serialized.net/2013/01/live-sphinx-documentation-preview/

## Notes

What we actually wanted to implement is something like
https://kno.wled.ge/, however that site uses 
https://squidfunk.github.io/mkdocs-material/, i.e. mkdocs
instead of Sphinx.
