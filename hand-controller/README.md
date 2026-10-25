# Robotic Hand Controller

This folder contains the computer-side software and microcontroller firmware for controlling a tendon-driven robotic hand. The project explores pose-based control, inverse kinematics, and communication between a 3D control interface and physical robotic hardware.

The goal is to connect virtual hand movements to the physical system, translating target poses into actuator commands.

## System Overview

The control system is divided into two main components:

- **Computer-side controller:** Processes target poses, calculates joint commands, and communicates with the microcontroller.
- **Microcontroller firmware:** Receives commands and controls the hand's servo motors.

The current control pipeline connects Blender to the physical hand through Python and an ESP32.

## Control Pipeline

1. **Pose control:** Hand poses are defined and manipulated in Blender.
2. **Pose communication:** The computer-side software receives pose information from Blender.
3. **Kinematics:** Python processes the pose data and calculates the servo angles required to achieve the target configuration.
4. **Serial communication:** The calculated commands are transmitted to the ESP32.
5. **Actuation:** The ESP32 generates servo control signals to move the robotic hand.

This architecture separates high-level pose control and kinematic calculations from low-level actuator control.

## Computer-Side Software

The computer-side software connects the virtual hand model to the physical hardware.

Its responsibilities include:

- Receiving pose information from Blender.
- Processing joint and pose data.
- Calculating joint angles using kinematic methods.
- Transmitting actuator commands over a serial connection.

Python is used for the computer-side processing, with Blender providing the 3D environment for manipulating and visualizing hand poses.

## Microcontroller Firmware

The microcontroller firmware translates incoming commands into physical actuator movements.

The current hardware setup uses an ESP32 and a PCA9685 servo controller.

The firmware is responsible for:

- Receiving commands from the computer.
- Interpreting joint commands.
- Generating servo control signals through the PCA9685.
- Controlling the servos responsible for hand movement.

## Hardware

| Component | Purpose |
|---|---|
| ESP32 | Executes the hand-control firmware |
| PCA9685 | Generates PWM signals for servo control |
| Servo motors | Actuate the hand's tendon mechanisms |
| Computer | Runs the pose-control and kinematics software |

The hardware configuration may evolve as the robotic hand is refined.

## Development Goals

Ongoing development focuses on improving the responsiveness, reliability, and capabilities of the control system.

- Improve communication between Blender, Python, and the microcontroller.
- Refine the kinematics used to translate target poses into joint commands.
- Improve the reliability and consistency of servo movements.
- Explore integration of tactile sensor measurements into future feedback-driven control.
- Explore VLA-based control methods

## Project Status

This controller is part of an ongoing robotic hand project. The control pipeline is being developed iteratively, with continued work on kinematics, communication, and actuator performance. Integration of tactile sensing into closed-loop control is a future development goal.

