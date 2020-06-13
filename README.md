# Django Codemod

[![PyPI](https://img.shields.io/pypi/v/django-codemod.svg)](https://pypi.python.org/pypi/django-codemod)
[![Test](https://github.com/browniebroke/django-codemod/workflows/Test/badge.svg)](https://github.com/browniebroke/django-codemod/actions?query=workflow%3ATest)
[![codecov](https://codecov.io/gh/browniebroke/django-codemod/branch/master/graph/badge.svg)](https://codecov.io/gh/browniebroke/django-codemod)
[![Documentation Status](https://readthedocs.org/projects/django-codemod/badge/?version=latest)](https://django-codemod.readthedocs.io/en/latest/?badge=latest)
[![Updates](https://pyup.io/repos/github/browniebroke/django-codemod/shield.svg)](https://pyup.io/repos/github/browniebroke/django-codemod/)
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

A tool to help upgrade Django projects to newer version of the framework by automatically fixing deprecations.

## Installation

Install this via pip (or your favourite installer):

`pip install django-codemod`

## Usage

2 main workflow are supported:

- Prepare future upgrades by modifying code which is deprecated in a given version using the `deprecated-in` option
- Fix previous deprecated code which is removed in a given version using the `removed-in` option

**1. Deprecations**

Let's say you just updated to Django 3.0, and suddenly you're flooded with deprecations warning on your CI (you have warning enabled on CI, right?).

You want to resolve them to avoid missing another important warning. You can do so by running the following command from the root of your repo:

```bash
djcodemod --deprecated-in 3.0 .
```

**2. Removals**

This is more a just in time operation, assuming you haven't kept up to date with deprecation warnings, and right before upgrading to a given version (let's assume Django 4.0). In this case, you should be running:

```bash
djcodemod --removed-in 4.0 .
```

### What happens

In either case, the tool will take a few minutes and apply a set of modifications to your code to fix deprecated or removed usages of Django. This should be much faster than doing it manually and much robust than a simple find & replace.

Check out the [documentation](https://django-codemod.readthedocs.io) for more detail on usage and the full list of codemodders.

## How it works

This is based on [libCST](https://libcst.readthedocs.io/en/latest/index.html) and implements codemods for it. This is currently very limited but the aim is to add more for helping with upcoming deprecations.

Not finding what you need? I'm open to contributions, please send me a pull request.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://browniebroke.com"><img src="https://avatars1.githubusercontent.com/u/861044?v=4" width="80px;" alt=""/><br /><sub><b>Bruno Alla</b></sub></a><br /><a href="https://github.com/browniebroke/django-codemod/commits?author=browniebroke" title="Code">💻</a> <a href="https://github.com/browniebroke/django-codemod/issues?q=author%3Abrowniebroke" title="Bug reports">🐛</a> <a href="https://github.com/browniebroke/django-codemod/commits?author=browniebroke" title="Documentation">📖</a></td>
    <td align="center"><a href="https://adamj.eu/"><img src="https://avatars2.githubusercontent.com/u/857609?v=4" width="80px;" alt=""/><br /><sub><b>Adam Johnson</b></sub></a><br /><a href="https://github.com/browniebroke/django-codemod/commits?author=adamchainz" title="Documentation">📖</a></td>
    <td align="center"><a href="https://sobolevn.me"><img src="https://avatars1.githubusercontent.com/u/4660275?v=4" width="80px;" alt=""/><br /><sub><b>Nikita Sobolev</b></sub></a><br /><a href="https://github.com/browniebroke/django-codemod/commits?author=sobolevn" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Credits

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.
