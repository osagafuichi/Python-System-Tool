# Python-System-Tool

CLI-based filesystem indexer with SQLite and fast search

## Overview

Python-System-Tool is a command-line utility that indexes files in a directory, stores metadata in a local SQLite database, and allows fast searching without repeatedly scanning the filesystem.

The tool is designed with a clear separation between indexing, storage, and querying logic, and supports incremental updates using file modification timestamps.

## Features

- Recursive directory indexing
- SQLite-backed persistent storage
- Incremental updates using file modification timestamps
- Fast search without filesystem access
- Partial filename search
- Optional filtering by file extension
- Optional filtering by file size
- Sorting by name, size, or last modified time
- Command-line interface using argparse

## Project Structure

- `main.py` – CLI entry point
- `indexer.py` – Filesystem traversal and indexing logic
- `searcher.py` – Search logic and output formatting
- `extractor.py` – File metadata extraction
- `database.py` – SQLite access layer

## Usage

### Index a directory:
  `python3 main.py index --path /path/to/directory`
### Search indexed files:
  `python3 main.py search --name report`
### Sort results by Name:
  `python3 main.py search --name report --sort name`
### Sort results by size:
  `python3 main.py search --name report --sort size`
### Sort results by last modified time:
  `python3 main.py search --name report --sort date`

## Design Notes

- The filesystem is scanned only during indexing
- File changes are detected using modification timestamps
- Database access is isolated in a dedicated module
- Search operations query SQLite directly for speed
- The project avoids unnecessary dependencies

## Why This Project

This project was built to practice backend-style program structure, working with persistent storage, designing clean CLI tools, and separating concerns between indexing, storage, and querying.

## Notes

This project was developed and tested on macOS. SQLite is used as an embedded database and requires no setup.
