# More hierarchical documentation for THE ANALOG THING

This repository is supposed to hold the [Sphinx](https://sphinx-doc.org/)
source code for [The Analog Thing](https://the-analog-thing.org/). 
This is an experiment to replace 
[The Analog Thing Wiki](https://the-analog-thing.org/wiki/) which is 
percieved as crowdy amongst the 
[anabrid](https://anabrid.com/) developers.

## How to contribute (workflow)

You have to install Sphinx locally in order to edit "interactively" and
build the output files. There is no web frontend (unlike the Wiki).
For minor modifications, you can also use Github or Gitlab as a web
frontend to simple tasks as editing text files and uploading images.

The documentation is managed within Git, so you also need a git client.
This however makes it easy to clone, fork and create pull requests.
We can also build upon Github for user managament.

Once you [got Sphinx installed](https://www.sphinx-doc.org/en/master/usage/installation.html),
editing is as simple as typing `make html` and opening `_build/html/index.html`
with the Browser.

Hint: Use https://serialized.net/2013/01/live-sphinx-documentation-preview/
