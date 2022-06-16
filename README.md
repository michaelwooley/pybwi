# pybwi  <!-- omit in toc -->

- [Development](#development)
  - [Quickstart](#quickstart)
  - [Open questions](#open-questions)
- [Documentation](#documentation)
- [License](#license)

## Development

### Quickstart

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

### Open questions

1. Relationship of `opyrator` to `streamlit`?
2. Is `opyrator` necessary?
3. Ability to add github- or google-based auth.

TODO #4 Add setup.py [pipenv docs](https://pipenv.pypa.io/en/latest/advanced/#pipfile-vs-setup-py)

## Documentation

[TODO]

## License

⚖️  [**GNU General Public License v3.0**](./LICENSE)
