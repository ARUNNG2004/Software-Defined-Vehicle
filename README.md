# Jetson GPIO Control

## Project Overview
The Jetson Nano is a powerful AI computer for makers, learners, and developers. It can be used to create software-defined vehicles, enabling features like autonomous driving, advanced driver assistance systems, infotainment systems, and vehicle-to-vehicle communication. With its affordable price, the Jetson Nano democratizes access to AI technology. [NVIDIA Jetson Nano Getting Started Guide](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)


## Features
- Control GPIO pins on NVIDIA Jetson devices.
- Setup GPIO inputs and outputs.
- Toggle pins and handle interrupts.
- Compatible with mock setups for testing on non-Jetson platforms.
### Requirements
- NVIDIA Jetson device (Nano, TX1, TX2, Xavier NX, etc.)
- Ubuntu-based OS

### Download the OS
1. Visit the [NVIDIA JetPack SDK page](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit) to download the latest JetPack SDK, which includes the necessary OS image.

### Create a Bootable USB Drive
1. Use **Etcher** (or any other flashing tool) to create a bootable USB drive:
   - Insert a USB drive (at least 16 GB recommended).
   - Launch Etcher and select the downloaded JetPack image.
   - Choose your USB drive as the target and click "Flash!".



### Install Jetson.GPIO on Jetson

1. Open a terminal.
2. Run the following commands to install the Jetson GPIO library:
   ```bash
   sudo apt-get install python3-jetson-gpio
   sudo pip3 install Jetson.GPIO

### Verify the installation
1. Run the following commands to verify the package installed:

   ```bash
   python3 -c "import Jetson.GPIO"
### Run  the Code


To run the scripts, execute the following command in your terminal:

```bash
python3 setup.py
