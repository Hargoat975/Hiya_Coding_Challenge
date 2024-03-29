# Hiya Call Duration Analysis Challenge

## Overview

This repository contains my solution to the Hiya challenge aimed at detecting and preventing malicious calling campaigns through real-time analysis of anonymized call traffic. The core problem involves analyzing a time-ordered list of call events to identify callers with an average call duration under 5 seconds.

The solution is implemented in Python and makes use of object-oriented programming concepts to model call events and process them to calculate average call durations.

## Problem Statement

Given a series of call and hangup events, the task is to calculate the average call duration for each caller and return a list of callers whose average call duration is under 5 seconds. A call is represented by two events: a "call" event when the call starts, and a "hangup" event when the call ends. Importantly, it does not matter who ends the call for the purposes of this challenge.

## Solution

The solution involves creating a Python script that:
- Models call and hangup events as objects derived from a common base class.
- Processes a list of these event objects to track active calls and their durations.
- Calculates the average call duration for each caller.
- Filters and returns callers with an average call duration under the specified threshold.

### Key Assumptions

- Callers are only considered if they have initiated at least one call.
- The order of callers in the output list is not specified and thus may vary.
- Timestamps are given as integers representing seconds since the Unix epoch.

## How to Run

1. Ensure you have Python 3.7+ installed on your machine.
2. Clone this repository to your local machine.
3. Navigate to the repository directory in your terminal.
4. Run `python -m pytest` to execute the test suite and verify the solution.
5. To run the main script and see the output for a custom list of events, you can modify the `example_events.py` file (create this file with your data) and run it with `python example_events.py`.

## Testing

This repository includes a test suite written using `pytest`. The tests cover various scenarios, including multiple calls by the same caller, overlapping calls, and varied call durations.

To run the tests, execute the following command in the terminal:

```bash
pytest
