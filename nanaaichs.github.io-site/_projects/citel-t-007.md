---
id: citel-t-007
title: CITEL-T-007 Protocol Sender
category: Engineering
period: "2026"
status: Completed
featured: true
order: 3
summary: >
  Desktop protocol-generation and UDP-transmission application developed with C++ and Qt,
  with XML protocol definitions and SQLite transmission records.
technologies:
  - C++11
  - Qt
  - UDP
  - SQLite
  - XML
  - qmake
outcomes:
  - XML-driven protocol generation and transmission workflow
  - Auditable SQLite transmission records and GUI-based operation
related_publications: []
related_awards: []
links:
  github: ""
  demo: ""
  report: ""
---
## Overview

CITEL-T-007 is a desktop protocol-generation and transmission application implemented with C++ and Qt.

## My Contribution

- Software architecture and module integration
- XML protocol parsing
- Field-level data generation
- UDP transmission control
- SQLite persistence
- GUI workflow and progress reporting

## Architecture

The primary data flow is:

`XML Protocol Definition → ProtocolParser → ProtocolDefinition → DataGenerator → UdpSendController → TransmissionRepository → MainWindow`

## Key Features

- XML-based protocol definitions
- Configurable field generation
- UDP packet transmission
- SQLite transmission records
- Progress and execution-state reporting
- Desktop graphical interface

## Evidence to Add

Add the public repository, screenshots, benchmark results, acceptance evidence, and a concise architecture diagram when appropriate.
