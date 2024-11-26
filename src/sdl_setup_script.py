import os
import shutil
import zipfile
import urllib.request

# Define the URL and project directory
SDL_URL = "https://www.libsdl.org/release/SDL2-devel-2.26.0-mingw.zip"
SDL_ZIP = "SDL2.zip"
PROJECT_DIR = "my_sdl_project"

def download_file(url, filename):
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
    else:
        print(f"{filename} already downloaded.")

def download_sdl():
    download_file(SDL_URL, SDL_ZIP)

def extract_and_rename_sdl():
    if not os.path.exists("SDL2"):
        with zipfile.ZipFile(SDL_ZIP, 'r') as zip_ref:
            zip_ref.extractall(".")
        
        extracted_folder = next((name for name in os.listdir(".") if name.startswith("SDL2-") and os.path.isdir(name)), None)
        if extracted_folder:
            os.rename(extracted_folder, "SDL2")
    else:
        print("SDL already extracted and renamed.")

def setup_project():
    sdl_folder = "i686-w64-mingw32"  # Change this if you need to target 64-bit

    # Set paths for include, lib, and DLL
    sdl_include = os.path.join("SDL2", sdl_folder, "include")
    sdl_lib = os.path.join("SDL2", sdl_folder, "lib")
    sdl_dll = os.path.join("SDL2", sdl_folder, "bin", "SDL2.dll")

    os.makedirs(PROJECT_DIR, exist_ok=True)
    shutil.copytree(sdl_include, os.path.join(PROJECT_DIR, "include"), dirs_exist_ok=True)
    shutil.copytree(sdl_lib, os.path.join(PROJECT_DIR, "lib"), dirs_exist_ok=True)
    shutil.copy(sdl_dll, PROJECT_DIR)

    with open(os.path.join(PROJECT_DIR, "main.cpp"), "w") as f:
        f.write("""#include <SDL.h>
#include <iostream>

int main(int argc, char* argv[]) {
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        std::cerr << "SDL could not initialize! SDL_Error: " << SDL_GetError() << std::endl;
        return 1;
    }
    std::cout << "SDL Initialized in C++!" << std::endl;
    SDL_Quit();
    return 0;
}
""")

    with open(os.path.join(PROJECT_DIR, "main.c"), "w") as f:
        f.write("""#include <SDL.h>
#include <stdio.h>

int main(int argc, char* argv[]) {
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        printf("SDL could not initialize! SDL_Error: %s\\n", SDL_GetError());
        return 1;
    }
    printf("SDL Initialized in C!\\n");
    SDL_Quit();
    return 0;
}
""")

    with open(os.path.join(PROJECT_DIR, "Makefile"), "w") as f:
        f.write("""all:
	gcc -Iinclude/sdl2 -Llib -o main_c main.c -lmingw32 -lSDL2main -lSDL2
	g++ -Iinclude/sdl2 -Llib -o main_cpp main.cpp -lmingw32 -lSDL2main -lSDL2""")

    print("Project setup complete.")

if __name__ == "__main__":
    download_sdl()
    extract_and_rename_sdl()
    setup_project()
