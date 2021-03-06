# Censys-Take-Home

## Getting Started

The library can be installed using `pip`.

```bash
pip install censys
```

To configure your search credentials run `censys config` or set both `CENSYS_API_ID` and `CENSYS_API_SECRET` environment variables.

```bash
$ censys config
Censys API ID: XXX
Censys API Secret: XXX
Successfully authenticated for your@email.com
```

## How to Run

Clone this repository

```bash
git clone https://github.com/jchoi25/Censys-Take-Home.git
```

Install dependencies

```bash
cd Censys-Take-Home
pip install pandas
```

Run the program in CLI

```bash
python3 main.py
```

This will return a csv file named `out.csv`. The output path is the same location of the `main.py` file.
To change the output location, edit the filepath variable in `main.py`.
