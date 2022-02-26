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


Basics
~~~~~~

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
    \end{aligned} 
    
    
**Note the sign change at the integrator output!**


Electronic circuit
~~~~~~~~~~~~~~~~~~

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



.. list-table::
   :widths: 75
   :header-rows: 0

   * - .. image:: ../../images/computing_elements/integrator_practical_circuit.png
     	:width: 350
  	:alt: Alternative text
  	:align: center      
    
   * - Practical circuit of an integrator


