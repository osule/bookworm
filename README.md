# bookworm
Search books in a catalogue

## Build

```bash
docker build -t bookworm .
```

## Run

Copy `env_example` to `.env`

```bash
cp env_example .env
```

Then run
```bash
docker run -it --rm --env-file .env -p 8000:8000 bookworm
```
