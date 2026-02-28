# LeetCode Solutions

A collection of LeetCode solutions with documentation and analysis, organized by difficulty and problem number. Each solution includes implementations in multiple programming languages.

**📖 View the full documentation:** https://lingc2001.github.io/leetcode-solutions/

---

## Directory Structure

- `problems/` — Contains all problem solutions, organized by difficulty:
  - `1-easy/`
  - `2-medium/`
  - `3-hard/`
    - `<number>-<Problem-Name>/`
      - `README.md` — Problem description and analysis
      - `solution.py` — Python solution
      - `solution.cpp` — C++ solution
- `tests/` — Contains all test cases, organized by difficulty to mirror the problems directory:
  - `1-easy/`
  - `2-medium/`
  - `3-hard/`
    - `test_<problem_name>.py` — Pytest test file for the corresponding problem

## Naming Convention

- Problem folders: `<number>-<Problem-Name>` (e.g., `217-Contains-Duplicate`)
- Solution files: `solution.py` and `solution.cpp`

## Documentation (Next.js + Fumadocs)

The documentation site is built with [Next.js](https://nextjs.org/) and [Fumadocs](https://fumadocs.dev/), deployed to GitHub Pages.

### Setup

Navigate to the `docs/` directory:

```sh
cd docs
```

Install dependencies with `pnpm`:

```sh
pnpm install
```

### Development

Start the development server:

```sh
pnpm dev
```

Visit `http://localhost:3000` to view the docs locally.

### Building

Build the static site for production:

```sh
pnpm build
```

The output is generated in the `out/` directory, which is automatically deployed to GitHub Pages on push to `main`.

### Linting & Formatting (Biome)

The docs use [Biome](https://biomejs.dev/) for linting and formatting:

- **Check for issues:**
  ```sh
  pnpm lint
  ```
- **Auto-format code:**
  ```sh
  pnpm format
  ```

## Python Setup (with uv)

This project uses [uv](https://github.com/astral-sh/uv) for fast Python environment management and dependency installation.

### Install dependencies

Use `uv sync` to install all dependencies specified in `pyproject.toml` and `uv.lock`:

```sh
uv sync
```

### Linting (with ruff)

We use [ruff](https://github.com/astral-sh/ruff) for linting Python code. The configuration is managed in `.ruff.toml`.

- **Check for lint errors:**
  ```sh
  uv run ruff check
  ```
- **Auto-fix lint errors:**
  ```sh
  uv run ruff check --fix
  ```

### Tests

All Python solutions are tested using [pytest](https://docs.pytest.org/). Test cases are organized in the `tests/` directory, mirroring the problem folder structure (e.g., `tests/1-easy/test_1_two_sum.py`).

To run all tests:

```sh
uv run pytest
```

## Contributors

- [LingC2001](https://github.com/LingC2001)
- [bkdham](https://github.com/bkdham)

<!-- Add your GitHub username above to be listed as a contributor! -->