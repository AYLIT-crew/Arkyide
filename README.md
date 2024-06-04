# Project Arkyide

**Project Arkyide** is a simple and complex suite of tools and an author tool installer developed in Python by AYLIT. The primary goal of Arkyide is to create a streamlined design for a suite of tools and other functionalities, with plans for a CLI (Command Line Interface) in the near future.

## Features

- **Tool Suite**: A collection of tools aimed at simplifying various tasks.
- **Author Tool Installer**: Easy installation and management of authoring tools.
- **Simple Design**: Focus on user-friendly and straightforward interfaces.
- **CLI Development**: A command line interface is in the works to enhance usability.

## Development Status

Project Arkyide is currently in development. The estimated completion time is expected in winter 2024.

## Getting Started
### Running on Linux 🐧

1. Clone the Arkyide repository to your local machine using Git.

2. Open a terminal and navigate to the directory where you cloned the Arkyide repository.

3. Run the following command in the terminal to install the required dependencies from the `requirements.txt` file:
```pip install -r requirements.txt```
4. After installing the dependencies, you can execute Arkyide by running the following command in the terminal:
```python arkyide.py```
### Running on Docker 🐳
#### Step 1: Install Docker

1. Visit the official Docker website: https://www.docker.com/get-started
2. Download Docker for your operating system (Windows, macOS, or Linux).
3. Follow the installation instructions provided on the website.
4. Once the installation is complete, verify Docker installation by opening a terminal/command prompt and typing `docker --version.` You should see the installed Docker version.

#### Step 2: Navigate to Arkyide Root Folder

1. Open a terminal/command prompt/shell.
2. Use the cd command to navigate to the root folder of your Arkyide project.

#### Step 3: Build the Docker Image

1. In the terminal, run the following command to build the Docker image from your Arkyide root file:

`docker build -t arkyide .`
#### Step 4: Run the Docker Container

After building the image, run the Docker container using the following command:
`docker run -it arkyide``

- Now you should access the Menu on terminal.

## Contribution

We welcome contributions! Please fork the repository and submit pull requests. If you encounter any issues, feel free to open an issue on GitHub.

## License

This project is licensed under the GNU 3.0 License.

## Contact

For more information, please contact AYLIT.

---

Stay tuned for updates and new features as Project Arkyide evolves!

