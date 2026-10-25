# Magnetic Tactile Sensor

This folder contains the hardware designs and software for developing a custom magnetic tactile sensor for a robotic hand.

The goal is to develop a compact, soft sensor capable of measuring tactile forces at the fingertip. The project explores magnetic sensing as an approach to tactile perception in robotic manipulation.

## Sensor Design

The sensor uses changes in magnetic fields caused by elastic deformation to estimate applied contact forces.

The current design concept combines a compliant silicone structure containing magnetically permeable particles with Hall-effect sensors that measure changes in the surrounding magnetic field. As the sensor deforms under an applied force, the magnetic field measurements can provide information about the contact.

The sensor is intended to fit within a robotic fingertip, placing an emphasis on compact electronics, measurement consistency, and reliable force estimation.

## Hardware

The sensor development involves the following components:

- **Hall-effect sensors:** Measure magnetic field changes associated with sensor deformation.
- **Permanent magnet:** Provides the magnetic field used for sensing.
- **Silicone elastomer:** Forms the compliant sensor structure.
- **Iron particles:** Incorporated into the silicone to explore deformation-dependent magnetic responses.
- **Custom PCB:** Provides the electrical connections and sensor readout circuitry.
- **Microcontroller:** Collects measurements from the sensor electronics for processing and analysis.

The hardware is subject to change as the design is tested and refined.

## Repository Contents

This folder contains the files associated with sensor development, including PCB designs and software used to interface with and evaluate the sensor.

The specific files and their organization may evolve as the project progresses.

## Development Process

### 1. Sensor and PCB Design

Designing a compact sensing circuit that can be integrated into a robotic fingertip. This includes selecting magnetic sensing components, developing the circuit, and laying out the PCB.

### 2. Data Acquisition

Reading the Hall-effect sensor outputs through the electronics and collecting measurements for analysis. An important consideration is maintaining stable electrical connections and minimizing measurement variability.

### 3. Calibration

Characterizing the relationship between sensor output and applied force using known loads. Calibration is necessary to determine whether the sensor can provide repeatable and meaningful force measurements.

### 4. Force Estimation

Investigating how measurements from multiple sensing elements can be used to estimate applied forces. Future development may explore machine learning methods to infer contact forces or locations from the sensor readings.

## Current Development Goals
Steps 1 and 2 have been completed. Currently there is a working prototype of the sensor that has proved that the magnetic response is measureable and is dependent on the applied force. The current software can accurately detect when the sensor is being pressed.

- Improve the consistency and reliability of magnetic field measurements.
- Establish a calibration procedure using known applied forces.
- Investigate the relationship between sensor deformation, magnetic field measurements, and applied force.
- Explore compact, multi-sensor arrangements for contact localization
- Evaluate methods for estimating contact forces and locations from sensor data.

## Project Status

This sensor is under active development. The current focus is on hardware prototyping, measurement stability, and establishing a reliable relationship between sensor output and applied force.

Force calibration, performance characterization, and integration with the robotic hand's control system are ongoing development goals.

