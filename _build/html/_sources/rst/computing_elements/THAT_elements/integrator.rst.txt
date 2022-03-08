==========
Integrator
==========

.. list-table::
   :widths: 75 75 
   :header-rows: 0

   * - .. image:: ../../images/computing_elements/THAT_Integrator.png
     	      :width: 150
  	      :alt: Alternative text
  	      :align: center
     - .. image:: ../../images/computing_elements/integrator_symbol.png
     	      :width: 350
  	      :alt: Alternative text
  	      :align: center
  	      	      
   * - THAT integrator unit
     - Integrator symbol

.. contents::
   :depth: 3

Basics
======

Next to the summer, the **integrator** is the most important computing element, which is to be found on most if not all electrical analog computers.

It fullfills the equation

.. math::

   \begin{aligned}
     \ U_{out}&=-\int_{0}^{T}\sum_{i=1}^{n} \frac{1}{R_iC}U_i(t)dt+U(0)
    \end{aligned}
    
where:

.. math::

   \begin{aligned}
     \ C&=\text{Feedback capacitor}\\
     \ R_i&=\text{Input resistor}\\
     \ U_i&=\text{Input voltage}\\
     \ U(0)&=\text{Integration constant / Starting value}\\
    \end{aligned} 
    
    
**Note the sign change at the integrator output!**

Electrical circuits
===================

Principle electronic circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 75
   :header-rows: 0

   * - .. image:: ../../images/computing_elements/integrator_principle_circuit.png
     	      :width: 350
  	      :alt: Alternative text
  	      :align: center       
    
   * - Principle circuit of an integrator

There is only one difference between the summer and principle integrator circuit: The feedback resistor :math:`R_f` of the summer is replaced by a capacitor C.

Just as in the summer ciruit, the operation amplifier always tries to compensate any current occuring at it's negative input caused by the input voltages.

In opposition to the summer, the integrator circuit cannot really compensate the input current because the feedback capacitor blocks direct current. Instead it increases it's output voltage as long as the sum of the input voltages is greater zero (and decreases the output for negative inputs).
Therefore, this circuit **performs a mathematical integration of given inputs over time.**

The integrator is the only computing element which includes time as free variable in it's computing result, which is why **the integrator dictates the time course of any calculation performed on electrical analog computers.**

Practial electronic circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The principle integrator circuit is not very usefull because, once it is supplied with power, it will integrate till infinity.

In the practical circuit shown below you find two relais switches **r** and **h**, which are used to control the operation mode of the integrator and thus to control the simulation.

.. list-table::
   :widths: 75
   :header-rows: 0

   * - .. image:: ../../images/computing_elements/integrator_practical_circuit.png
     	:width: 350
  	:alt: Alternative text
  	:align: center      
    
   * - Practical circuit of an integrator
   
Operation modes
===============

Initial contition
~~~~~~~~~~~~~~~~~

Before running the program/simulation, the condensator C needs to be charged to the starting value of the to be performed integration. This is acieved by setting both switches **r** and **h** to **0**.

Every electrical analog computer needs to be in **initial contidion mode** before the program ist started. (IC mode on THAT switch)

Operation
~~~~~~~~~

In **operation mode** (OP mode on THAT switch) both relais **r** and **h** are set to 1.

By switching **r** to 1, the resistors Rf and R'f are pinned to ground so **U(0)** is no longer applied.

By switching **h** to 1, the input resistors and therefore the input voltages are connected to the integrator.

Overall, this configuration equals the principle inverter circuit.

HALT
~~~~

The **HALT mode** allows a (short) interuption of the simulation at any point in time.
Therefore **r** is set to 1 and **h** is set to 0.

In this mode the inputs no longer effect the circuit, instead the last value just before switching **h** is hold at the inverter output. 

This is very usefull for diagnostic purposes.

**Note: Due to leak currents and not ideal amplifiers the HALT mode cannot be hold indefinetly. The value will (slowly) change over time.**


