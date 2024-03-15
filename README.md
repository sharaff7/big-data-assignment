# big-data-assignment
*Overview*

This project aims to analyze and visualize data related to military and socioeconomic indicators of Israel and Palestine.

## Prerequisites

- Docker installed on your system
- PowerShell with administrative privileges

## Usage

1. Clone this repository to your local machine.
2. Open PowerShell with administrative privileges.
3. Set the execution policy to allow running scripts:
   
   Set-ExecutionPolicy RemoteSigned
   
4. Navigate to the project directory in PowerShell.
5. Build the Docker image using the following command:
   
   docker build -t project-name .
   
6. Run the Docker container:
   
   docker run -it --rm -v ${PWD}:/home/project-name project-name
   
7. Once inside the container, execute the main script to load, preprocess, analyze, and visualize the data:
   
   python3 load.py Israel-Palestine.csv
   
8. After the execution is complete, you can find the results in the service-result directory on your local machine.

## Docker Commands Used

- docker build -t project-name .: Builds a Docker image named "project-name" from the Dockerfile in the current directory.
- docker run -it --rm -v ${PWD}:/home/project-name project-name: Runs a Docker container interactively, with the current directory mounted inside the container at /home/project-name. The --rm flag removes the container after it exits.

## Directory Structure


project-name/
│
├── data/
│   └── Israel-Palestine.csv
│
├── service-result/
│   ├── res_dpre.csv
│   ├── insights/
│   │   ├── eda_insights_1.txt
│   │   ├── eda_insights_2.txt
│   │   └── ...
│   ├── k.txt
│   └── vis.png
│
├── Dockerfile
├── load.py
├── dpre.py
├── vis.py
├── model.py
└── README.md
