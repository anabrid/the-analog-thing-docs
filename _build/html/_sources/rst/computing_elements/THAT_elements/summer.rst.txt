Summer
======

.. list-table::
   :widths: 75 75 75
   :header-rows: 0

   * - .. image:: ../../images/computing_elements/summer_that.png
     	      :width: 150
  	      :alt: THAT summer unit
  	      :align: center
     - .. image:: ../../images/computing_elements/summer_symbol.png
     	      :width: 550
  	      :alt: Summer circuit symbol
  	      :align: center
     - .. image:: ../../images/computing_elements/summer_circuit.png
     	      :width: 250
  	      :alt: Summer electrical circuit
  	      :align: center
            	      
   * - THAT summer unit
     - Summer circuit symbol
     - Summer electrical circuit
     

     
The **summer** is the simplest active computing part. As the name suggests, it gives out the sum of given inputs.

It fullfills the equation

.. math::

   \begin{aligned}
     \ U_{out}&=-\sum_{i=1}^{n} \frac{R_f}{R_i}U_i
    \end{aligned}
    
where

.. math::

   \begin{aligned}
     \ R_f&=\text{Feedback resistor}\\
     \ R_i&=\text{Input resistor}\\
     \ U_i&=\text{Input voltage}\\
    \end{aligned}   
    
**Note the sign change at the summer output!**

On the basis of the output inversion **a summer with one input functions as inverter** and therefore the **summer and the inverter share the same circuit symbol.**

The output inversion is the result of the function principle: The output of the operation amplifier is always trying to compensate all currents at it's negative input caused by the input voltages.

The ratio between the input resistors **Ri** and the feedback resistor **Rf** determines the summing factor. If the overall input resistance equals the feedback resistor, the sum factor is one.
When changing **Ri** to a tenth of **Rf** so **Ri = Rf/10** is fullfilled, an input factor of 10 is achieved. 

The **SJ** connection gives the opportunity to extent the number of inputs by simply connecting this point with a resitor array **XIR**.

By connecting the **FB** panel with the ground panel directly below, the summer is converted into an open amplifier, e.g. in order to create inverse functions.

Inverter
--------

.. list-table::
   :widths: 75 
   :header-rows: 0

   * - .. image:: ../../images/computing_elements/inverter.png
     	      :width: 150
  	      :alt: THAT summer unit
  	      :align: center
        	      
   * - THAT inverter unit


The inverter circuit equals the summer circuit execpt for the number of inputs. The inverters found on the THAT have a single in- and output, but hold the possibility to extent the number of inputs by connection the SJ-panel of the inverter to a SJ-panel of a XIR-element. 

By simple adding this input network the inverter is converted into a summer, in case you need more summers then already present.
