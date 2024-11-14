# SDL_Auto_setup
This repository contains a Python script that automates the setup of the SDL (Simple DirectMedia Layer) library for C++ projects using the MinGW compiler on Windows.

## Setup 
## [Download here](https://github.com/acedmicabhishek/SDL_Auto_setup/releases)

###Setting up your SDL Library###

***Author : Prabhat***

How to set up your SDL- Library - Follow the below instructions carefully.

#### Prerequisites:- 

**Python Installation**: Ensure Python is installed on your machine.
**mingw Installation** : Ensure mingw is installed on your machine.

1. Extract the files to a desired location inside a folder.
2. Run "mingw32-make-3.80.0-3.exe" and install mingw32-make using the follow-ups.
3. After Installation press "SHIFT + RIGHT CLICK" inside the current folder then select "Open Power shell Window here"
4. Type "python sdl_setup_script.py" Hit enter.
5. Exit power shell when you see the message "Project setup complete".
6. Open "my_sdl_project" on any code editor and make changes in main.cpp

******TO RUN THE PROGRAM*******
In the new terminal write "mingw32-make" and Hit enter. 

type "./main.exe" and Hit enter, You are all set. 



## Features : 
* Automated Download & Extraction: Downloads the specified version of SDL(32bit - universal), extracts it, and renames it for easy reference.
* Project Folder Structure: Creates a project directory with organized folders for includes, libraries, and your project files.
* Generated Starter Code: Sets up a main.cpp file with basic SDL initialization code to get you started.
* Ready-to-Use Makefile: Provides a Makefile for building your project with mingw32-make.

## Prerequisites :
* Python: Ensure you have Python installed.
* MinGW Compiler: Make sure MinGW is installed and added to your system PATH.

