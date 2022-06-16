# pybwi  <!-- omit in toc -->

- [Development](#development)
- [Documentation](#documentation)
- [License](#license)

## Development

TODO #2 ⚠️ Update README for `pipenv` use.

Quickstart:

```bash

pyenv virtualenv -f 3.6.12 pybwi
pyenv activate pybwi

git clone git@github.com:michaelwooley/pybwi.git

cd pybwi

pyenv install 3.6.12 -s
pyenv local 3.6.12

pipenv --python $(pyenv which python)
pipenv install
```

**Launch the UI:**

```bash
pipenv run opyrator launch-ui pybwi.opy_app:hello_world
```

TODO #4 Add setuppy [pipenv docs](https://pipenv.pypa.io/en/latest/advanced/#pipfile-vs-setup-py)

## Documentation

[TODO]

## License

⚖️  [**GNU General Public License v3.0**](./LICENSE)
