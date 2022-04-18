===================================
Operation modes of analog computers
===================================

As mentioned in the integrator article, every electrical analog computer must have the ability to switch between different operation modes in order to control the simulation.

The most basic operation modes derive from the practical integrator circuit: *Initial condition (short "IC"), Operation (or "OP") and HALT.*

The following article shall give an overview of the **operation modes** of a THAT as well as an outlook on operation modes found on larger analog computers.

.. contents::
   :depth: 3

THAT operation modes
====================

OFF
~~~

Turns off the computer, all elements are disconnected from the supply line.

COEFF
~~~~~

After the implementation of a program on an electrical analof computer, the coefficents are to be set up according to the calculation plan. The quality of a simulation is often dependent on very accurate potentiometer settings.

Therefore the THAT as many other electrical analog computers comes with the **COEFF** mode.

In this mode the potentiometers are supplied with a full machine unit on it's input. The output of a coefficient is given to the display so it can be fine adjusted.

In order to display a certain coefficient, turn the coefficient switch to the desired potentiometer.

IC
~~

**IC** refers to **initial condition**.

Before an actual calculation can be performed, the intergators must be loaded to their initial state (--> initial condition), which can be understood as the integration constant occuring when solving integrals.

The **IC** state is indicated with the yellow LED next to the display.

OP
~~

In **operation mode** the actual calculation is performed, which is indicated with the green LED.

In this mode the analog computer will not stop calculating until it is manually interrupted with the operation mode switch.

HALT
~~~~

The **HALT** mode is a mode made mainly for diagnostic purposes.

When the operation mode switch is set to HALT, all integrators and therefore also all other computing elements will freeze in their current state, holding their current value.

This is very useful to debug a program, e.g. in case of an overload a user can stop the machine and check at which computing element the overload occured.

**Note:** The HALT mode is not perfect. Due to small leak currents and other imperfections the results can drift over time. Therefore HALT should be used "as fast as possible".

REP and REPF
~~~~~~~~~~~~

The **repetitive mode** is a very useful operation mode.

When set to **REP**, analog computers will continiously switch between **IC** and **OP**, so the calculation is repeated. The display shows the approximate operation time, where 1.000 equals 10 seconds operation time before reset.

In **REPF (--> repetitive fast)** the reset is performed 100 times faster, so 1.000 on the display equals 100 milliseconds operation time.

The LEDs will blink between **IC** and **OP**.

The simulation of a (simple) damped oscillation is a good example for the usage of repetitive operation.

MINION
~~~~~~

The **MINION** mode was implement in order to connect and syncronize multiple THATs which each other on order to realize programs where their realizations exceed the number of available elements on one THAT.

When a THAT is set to MINION mode, it is controlled by another THAT and will be set to the same operation mode as the **MASTER THAT** (except for COEFF mode, this still needs to be done manually for each THAT in the daisy chain).

The MASTER THAT is to be set into the desired operation mode by the user, which is likely not MINION mode.


Other operation modes
=====================

ZERO
~~~~

Static test
~~~~~~~~~~~

Dynamic test
~~~~~~~~~~~~

Timescale test
~~~~~~~~~~~~~~

Operating with HALT
~~~~~~~~~~~~~~~~~~~

Iterative operation
~~~~~~~~~~~~~~~~~~~
