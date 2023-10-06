# Cleaning Temporary Files and Prefetch Folder

![Windows Compatible](https://img.shields.io/badge/Windows-Compatible-blue)
[![Python Version](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/)
[![GitHub License](https://img.shields.io/github/license/KarthikUdyawar/data-cleaner)](https://github.com/KarthikUdyawar/data-cleaner/blob/master/LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/KarthikUdyawar/data-cleaner)](https://github.com/KarthikUdyawar/data-cleaner/releases)
[![GitHub Issues](https://img.shields.io/github/issues/KarthikUdyawar/data-cleaner)](https://github.com/KarthikUdyawar/data-cleaner/issues)

This Python script allows you to clean temporary files, the `%temp%` directory, and the prefetch folder on a Windows system. It provides a simple way to free up disk space by removing unnecessary files.

## Table of Contents

- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Download](#download)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## About The Project

This script is designed to clean temporary files, which can accumulate on a Windows system over time and consume valuable disk space. It provides a prompt to ensure you want to proceed with the cleanup, giving you the option to abort if necessary.

### Built With

- Python

## Getting Started

To get started with this script, follow the instructions below.

### Prerequisites

- Python 3.x
- Windows operating system (the script is designed for Windows)

### Installation

1. Clone the repository or download the script.
2. Make sure you have Python 3.x installed on your Windows system.

## Usage

1. Run the script in a Windows command prompt.

    ```cmd
    python cleanup_script.py
    ```

2. The script will prompt you to press Enter to continue or 'q' to quit.
3. If you choose to continue, the script will remove temporary files and prefetch data.
4. After the cleanup process is complete, additional actions can be performed.

### Download

You can download the executable version of this script from the [Data Cleaner](https://github.com/KarthikUdyawar/data-cleaner/releases) GitHub Releases page.

## Roadmap

There are currently no specific plans for future development. Feel free to contribute and enhance the script as needed.

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/KarthikUdyawar/data-cleaner/blob/master/LICENSE) file for details.

## Contact

If you have any questions or comments, please feel free to contact [Karthik-Udyawar](https://github.com/KarthikUdyawar) at [karthikudyawar123@gmail.com](karthikudyawar123@gmail.com
).

## Acknowledgements

[Subprocess](https://docs.python.org/3/library/subprocess.html) module for running commands in the Windows command prompt.
[Python](https://www.python.org/) for providing the scripting language.