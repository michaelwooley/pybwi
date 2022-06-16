# pybwi  <!-- omit in toc -->

- [Development](#development)
- [Documentation](#documentation)
- [License](#license)

## Development

TODO #3 #2 ⚠️ Update README for `pipenv` use.

Quickstart:

```bash
pyenv install 3.6.12 -s
pyenv virtualenv -f 3.6.12 pybwi
pyenv activate pybwi

git clone git@github.com:michaelwooley/pybwi.git

cd pybwi

# Set up pyenv
poetry env use $(which python)
poetry env info --path # Should enc with: /**/.pyenv/versions/3.6.12/envs/pybwi

poetry install

poetry run pytest
```

**Launch the UI:**

```bash
pipenv run opyrator launch-ui pybwi.opy_app:hello_world
```

## Documentation

[TODO]

## License

⚖️  [**GNU General Public License v3.0**](./LICENSE)
