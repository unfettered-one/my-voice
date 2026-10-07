# mt-voice
Train a local(free-model) to speak in your own voice

## Setup

Requires Python 3.14.8 (see `.python-version`) on Apple Silicon.

```bash
brew install ffmpeg espeak
rm -rf .venv && uv venv --python 3.14.8 .venv
source .venv/bin/activate
uv pip install pip --python .venv/bin/python
pip install -e ".[dev]"
```

Verify:

```bash
python -c "import torch; print(torch.__version__)"
python -c "import f5_tts; print('f5 ok')"
python -c "import omnivoice; print('omni ok')"
```
