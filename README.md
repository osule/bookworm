# bookworm
Search books in a catalogue

## Build

```bash
docker build -t bookworm .
```

## Run

```bash
docker run -it --rm --env-file .env -p 8000:8000 bookworm
```
