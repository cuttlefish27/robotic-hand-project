# Robotic Hand Project

An ongoing personal robotics project exploring robotic dexterity, motion control, and tactile sensing. This project includes a tendon-driven robotic hand, control software, and a custom magnetic tactile sensor that are all under development.

The long-term goal is to explore how mechanical design, control systems, and sensory feedback can work together to enable more capable robotic manipulation.

## Repository Structure

```text
robotic-hand-project/
├── hand-controller/            # Hand control software
    ├── mcu-firmware/               # MCU code
    ├── software/                   # Blender script & blender-mcu bridge
    └── hand_telemetry_rig.blend
├── sensor-dev/                 # Tactile sensor development
    ├── hardware/                   # PCB schematics & layout
    ├── software/                   # Sensor validation & data display
    └── firmware/                   # MCU firmware
├── .gitignore
├── LICENSE
└── README.md
```

### [`hand-controller/`](/hand-controller/README.md) — Robotic Hand Control

Contains the software for controlling the robotic hand from a computer and microcontroller.

The control system connects virtual hand poses to the physical robotic hand, using computer-side processing and embedded control to translate target movements into actuator commands.

The project explores:
- Blender-based hand pose control and visualization.
- Joint-angle calculations and kinematics.
- Communication between computer-side software and the microcontroller.
- Servo-based actuation of the robotic hand.

### [`sensor-dev/`](/sensor-dev/README.md) — Soft Magnetic Tactile Sensor

Contains the hardware designs and software for developing a compact tactile sensor for the robotic hand.

The sensor uses magnetic field measurements to investigate how applied forces can be measured at the fingertip. The design combines magnetic sensing components with custom PCB electronics.

Development focuses on:
- Sensor circuit and PCB design.
- Hall-effect sensor readout and data collection.
- Characterizing sensor response to applied forces.
- Developing calibration methods for force measurement.
- Exploring tactile sensing for future robotic manipulation.

The sensor is a work in progress, with measurement consistency, calibration, and integration remaining areas of development.

## System Overview

The project has two complementary systems:

**Hand control:** A computer generates or processes target poses, calculates the corresponding joint commands, and communicates with the microcontroller. The microcontroller then controls the hand's servos.

**Tactile sensing:** A custom magnetic sensor measures changes in magnetic fields associated with applied contact forces. The sensor electronics and software are being developed to make these measurements useful for robotic applications.

Together, these systems provide a foundation for exploring the relationship between robotic motion and tactile perception.

## Hardware

The project uses or explores the following hardware:

| Component | Purpose |
|---|---|
| ESP32 | Microcontroller for hand control |
| PCA9685 | Multi-channel servo control |
| Servo motors | Robotic hand actuation |
| Hall-effect sensors | Magnetic field measurements for tactile sensing |
| Custom PCBs | Tactile sensor electronics |

Hardware configurations will change as the design evolves.

## Software and Tools

- **Python** — Computer-side control, kinematics, serial communication, and sensor data processing.
- **Blender** — Hand pose control and 3D visualization.
- **C/C++** — Microcontroller firmware.
- **PlatformIO / Arduino framework** — Embedded development.
- **Fusion 360** — Mechanical CAD and hardware design.
- **KiCAD** — Circuit design and PCB layout.

## Development Goals

Current and planned areas of development include:

- Improving the robotic hand's mechanical design and range of motion.
- Developing responsive and reliable computer-to-microcontroller control.
- Designing a compact magnetic tactile sensor suitable for a robotic fingertip.
- Calibrating sensor measurements against known applied forces.
- Exploring how tactile feedback could support future VLA-based closed-loop control and robotic manipulation.

## Project Status

This is an active work-in-progress project. The hand controller, mechanical design, and tactile sensor are developed iteratively. Sensor integration and improvements to the broader mechanical design remain ongoing development goals.

