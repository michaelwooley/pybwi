# pybwi  <!-- omit in toc -->

- [Development](#development)
- [Documentation](#documentation)
- [License](#license)

## Development

Quickstart:

```bash
pyenv install 3.6.12 -s
pyenv virtualenv -f 3.6.12 pybwi
pyenv activate pybwi

g clone [...]

cd pybwi

# Set up pyenv
poetry env use $(which python)
poetry env info --path # Should enc with: /**/.pyenv/versions/3.6.12/envs/pybwi

poetry install

poetry run pytest
```

## Documentation

[TODO]

## License

⚖️  [**GNU General Public License v3.0**](./LICENSE)
