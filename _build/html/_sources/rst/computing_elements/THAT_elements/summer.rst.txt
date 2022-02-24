Summer
======

.. list-table::
   :widths: 75 75
   :header-rows: 0

   * - .. image:: ../../images/computing_elements/summer_circuit.png
     	      :width: 250
  	      :alt: Alternative text
  	      :align: center
     - .. image:: ../../images/computing_elements/summer_symbol.png
     	      :width: 350
  	      :alt: Alternative text
  	      :align: center       	      
   * - Electrical circuit
     - Summer circuit symbol
     
     
.. image:: ../../images/computing_elements/summer_that.png
     	      :width: 350
  	      :alt: Alternative text
  	      :align: right
     
The **summer** is the simplest active computing part. As the name suggests, it gives out the sum of given inputs.

**Note: The output of a summer is inverted, so the equation:**

**U_out = - (U1 + U2 + ... + Un)**

**is fulfilled.**

On the basis of the output inversion **a summer with one input functions as inverter** and therefore the **summer and the inverter share the same circuit symbol.**

The output inversion is the result of the function principle: The output of the operation amplifier is always trying to compensate all currents at it's negative input caused by the input voltages.

The ratio between the input resistors **Ri** and the feedback resistor **Rf** determines the summing factor. If the overall input resistance equals the feedback resistor, the sum factor is one.
When changing **Ri** to a tenth of **Rf** so **Ri = Rf/10** is fullfilled, an input factor of 10 is achieved. 

The **SJ** connection gives the opportunity to extent the number of inputs by simply connecting this point with a resitor array **XIR**.

By connecting the **FB** panel with the ground panel directly below, the summer is converted into an open amplifier in order to create inverse functions.
