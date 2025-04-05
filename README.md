# How do I set up Torch with UV?

See [./pyproject.toml](./pyproject.toml) for how to configure `tool.uv.sources` and a `tool.uv.index` entry to ensure Torch is downloaded such that CUDA is available.

Once the config is changed, you can simply `uv add torch`