# LeetCode Solutions

A collection of LeetCode solutions with documentation and analysis, organized by difficulty and problem number. Each solution includes implementations in multiple programming languages.

## Directory Structure

- `problems/` — Contains all problem solutions, organized by difficulty:
  - `1-easy/`
  - `2-medium/`
  - `3-hard/`
- Each problem folder is named as `<number>-<Problem-Name>` (e.g., `217-Contains-Duplicate`), and contains:
  - `README.md` — Problem description and analysis
  - `solution.py` — Python solution
  - `solution.cpp` — C++ solution

## Setup (with uv)

This project uses [uv](https://github.com/astral-sh/uv) for fast Python environment management and dependency installation.

### Install uv

#### On Windows

- Run the following command in PowerShell:

  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

- Alternatively, download and run the latest `.msi` installer from the [uv releases page](https://github.com/astral-sh/uv/releases).
- Or download the Windows executable (`uv-x86_64-pc-windows-msvc.exe`), rename it to `uv.exe`, and add its location to your system `PATH`.

#### On Mac (and Linux)

- Run the following command in your terminal:

  ```sh
  curl -Ls https://astral.sh/uv/install.sh | sh
  ```

- Or, on Mac, you can use Homebrew:

  ```sh
  brew install astral-sh/uv/uv
  ```

- Or download a prebuilt binary from the [releases page](https://github.com/astral-sh/uv/releases).

For more details, see the [official uv installation guide](https://docs.astral.sh/uv/guides/install-python/).

### Install dependencies

Use `uv sync` to install all dependencies specified in `pyproject.toml` and `uv.lock`:

```sh
uv sync
```

## Linting (with ruff)

We use [ruff](https://github.com/astral-sh/ruff) for linting Python code. The configuration is managed in `.ruff.toml`.

- **Check for lint errors:**
  ```sh
  uv run ruff check
  ```
- **Auto-fix lint errors:**
  ```sh
  uv run ruff check --fix
  ```

## Naming Convention

- Problem folders: `<number>-<Problem-Name>` (e.g., `217-Contains-Duplicate`)
- Solution files: `solution.py` and `solution.cpp`

## Contributing

1. Fork the repository
2. Create a new branch for your feature or fix
3. Add your solution in the appropriate folder
4. Run lint checks before submitting a PR
5. Submit a pull request with a clear description

## License

This project is licensed under the MIT License.

## Contributors

- [LingC2001](https://github.com/LingC2001)
- [bkdham](https://github.com/bkdham)

<!-- Add your GitHub username above to be listed as a contributor! -->