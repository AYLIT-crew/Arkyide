# Project Arkyide

![Arkyide Logo](assets/logo.jpg)

**Project Arkyide** is a simple and complex suite of tools and an author tool installer developed in Python by AYLIT. The primary goal of Arkyide is to create a streamlined design for a suite of tools and additional features, with plans for a CLI (Command Line Interface) in the near future.

## Features

- **Tool Suite**: A collection of tools aimed at simplifying various tasks.
- **Author Tool Installer**: Easy installation and management of authoring tools.
- **Simple Design**: Focus on user-friendly and straightforward interfaces.
- **CLI Development**: A command line interface is in the works to enhance usability.

## Development Status

Project Arkyide is currently in development. The estimated completion time is expected in winter 2024.

## Getting Started
### Termux
### 1. Install ncurses-utils
1.1 `apt install ncurses -y`

1.2 `apt install ncurses-utils -y`

### 3. "Make sure to have Poetry installed.
Look to https://python-poetry.org/docs/#installation for more info

Manual installation method
`curl -sSL https://install.python-poetry.org | python3 - `

### 3. Clone the repository
git clone "[https://github.com/AYLIT-crew/Arkyide.git](https://github.com/AYLIT-crew/Arkyide.git)"

### 4. Enter the directory and install requirements
4.1. `cd arkyide-repo`

4.2. `poetry install`

### 5. Run
### Running on Linux 🐧

1. Clone the Arkyide repository to your local machine using Git.

2. Open a terminal and navigate to the directory where you cloned the Arkyide repository.

3. Run the following command in the terminal to install the required dependencies: 
```poetry install```

4. Activate the python virtual environment by running:
```poetry shell``

6. Run Arkyide within the virtual environment:
```python arkyide.py```
### Running on Docker 🐳
#### Step 1: Install Docker

1. Visit the [official Docker website](https://www.docker.com/get-started):
2. Download Docker for your operating system (Windows, macOS, or Linux).
3. Follow the installation instructions provided on the website.
4. Once the installation is complete, verify Docker installation by opening a terminal/command prompt and typing `docker --version.` You should see the installed Docker version.

#### Step 2: Navigate to Arkyide Root Folder

1. Open a terminal/command prompt/shell.
2. Use the `cd` command to navigate to the root folder of your Arkyide project.

#### Step 3: Build the Docker Image

1. In the terminal, run the following command to build the Docker image from your Arkyide root file:

`docker build -t arkyide .`
#### Step 4: Run the Docker Container

After building the image, run the Docker container using the following commands:
Try running this command first:
`docker run -it arkyide`
If the above command fails, try this alternative:
`docker run -it --env TERM=xterm-256color arkyide`

- Now you should access the Menu on terminal.

## Contributing

Check `CONTRIBUTING.md` for more info.

## License

This project is licensed under the GNU General Public License v3.0.

## Contact

For more information, please contact AYLIT.

---

Follow the project for updates and new features!
