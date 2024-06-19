# Clipboard Manager

A simple clipboard manager that saves and retrieves text data using a text file. This tool allows you to save clipboard content with a key, load previously saved clipboard content, and list all saved clipboard entries.

## Features

- **Save Data**: Save clipboard content with a unique key.
- **Load Data**: Retrieve clipboard content using the key.
- **List Data**: List all saved clipboard entries.

## How It Works

1. **File Initialization**: The program checks if `data_copied.txt` exists. If not, it creates the file.
2. **Saving Data**: User inputs a key, and the current clipboard content is saved with that key in `data_copied.txt`.
3. **Loading Data**: User inputs a key, and the corresponding clipboard content is loaded and copied back to the clipboard.
4. **Listing Data**: All saved clipboard entries are displayed.

## Requirements

- Python 3.x
- `clipboard` module (`pip install clipboard`)

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/clipboard-manager.git
    cd clipboard-manager
    ```

2. Install the required module:
    ```sh
    pip install clipboard
    ```

3. Run the script:
    ```sh
    python clipboard_manager.py
    ```

4. Follow the on-screen instructions to save, load, or list clipboard data.

## Example

1. **Save Data**:
    - Choose option `[1]` to save data.
    - Enter a key (e.g., `email`).
    - The current clipboard content is saved with the key `email`.

2. **Load Data**:
    - Choose option `[2]` to load data.
    - Enter the key (e.g., `email`).
    - The corresponding clipboard content is copied back to the clipboard.

3. **List Data**:
    - Choose option `[3]` to list all saved data.
    - All keys and their corresponding clipboard contents are displayed.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any features, bug fixes, or enhancements.

## License

This project is licensed under the MIT License.
