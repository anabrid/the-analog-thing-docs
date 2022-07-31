====================================
Quickstart-guide: Damped oscillation
====================================

.. image:: images/quickstart/ExecutionOfAnAnalogSimulation.jpg
  :width: 400
  :alt: Alternative text
  :align: right
  
The modeling of a damped oscillation is a good starting point for analog programming beginners. This article shall give a detailed step by step explanation how to implement a simulation on The Analog Thing by describing the system with a differential equation, deriving a computer circuit using the full repatriation method (originally developed by Lord Kelvin around 1875) and to get results on an oscilloscope.

There are four major steps to execute a simulation on an analog computer, all of which are equally crucial:

    1) **Describe the to be simulated system with differential equations**
    2) **Derive a computer circuit from these equations**
    3) **Wire the computer circuit on the analog computer (including connection to output device) and adjust parameters**
    4) **Choose operation mode and viable visualization method (usually oscilloscopes).**
  
This article will focus on point 2. to 4. and requires a basic understanding of differential equations.

1. Mathematical description of a damped oscillation
---------------------------------------------------

.. list-table::
   :widths: 75 75
   :header-rows: 0

   * - The first and often hardest step of modeling a to be simulated system on an analog computer is to give an exact mathematical description of the system in the form of differential equations. For this example the full description is rather short:

       Find all acting forces, three in this case::

        - Spring  force Fs = k*x;
            k = spring coefficient, x = deflection
        - Inertia force Fm = m*a;
            m = mass, a = acceleration
        - Damper  force Fd = d*v;
            d = damper coefficient, v = velocity

       Set the sum of all forces to zero (definition of an isolated system)::

         -  Fm  + Fd  + Fs  = 0
         -  m*a + d*v + k*x = 0

       Replace the velocity v with ẋ and the acceleration a with ẍ::

           v = ẋ
         the velocity equals the first derivative of x
           a = ẍ
         the acceleration equals the second derivative of x
           m*a + d*v + k*x
         = m*ẍ + d*ẋ + k*x = 0

       Now we have an exact description of the damped oscillation in the form of a differential equation.

       In outlook of step 2, solve this equation for the highest derivative in order to execute the full repatriation later on::

         -> ẍ = -(d*ẋ + k*x) / m
     - .. image:: images/quickstart/Damped_oscillator.png
                :width: 400
                :alt: Alternative text
                :align: right

2. Derivation of a computer circuit
-----------------------------------

At first, we need to understand three basic computing elements which can probably be found on every electrical analog computer:

Basic computing parts:
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 75 75
   :header-rows: 1

   * - Description
     - Circuit symbol
     
   * - The **coefficient potentiometer**, which is used to multiply an input x with the factor a so a*x is generated.
   
       **Note: a can only accept values between 0 and 1!**
       
       Can also be used as dividing factor so **x/a** is generated. 
     - .. image:: images/quickstart/potentiometersymbol.png
     		:width: 200
  		:alt: Alternative text
  		:align: right
     
   * - The **inverter // summer**, the input (or inputs) can be found on the left and the output on the right.
       
       **Note: Due to technical reasons the output of a summer is negated! Input: x,y --> Output: -(x+y)**

       At the basis of the output inversion **a summer with one input functions as inverter** and therefore the summer and the inverter share the same circuit symbol. 
     - .. image:: images/quickstart/inverter.png
     		:width: 200
  		:alt: Alternative text
  		:align: right
  		
   * - The **integrator**, the input (or inputs) can be found on the left and the output on the right.

       Coming from above you find **ẋ0**, which represents the starting condition of the integrator (often referred to initial condition) and can be thought of as the integration constant. When there is no initial condition drawn in the circuit, it is set to 0.

       **Note: Due to technical reasons the output of an integrator is negated! ẍ -->-ẋ**

       Electrical analog integrators can only integrate over time. 
       
     - .. image:: images/quickstart/integratorsymbol.png
     		:width: 200
  		:alt: Alternative text
  		:align: right
  		
With these basic computing elements we are able to generate ẍ = -(d*ẋ + k*x) / m.

Deriving the actual circuit:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The basic idea of the full repatriation method is to solve the differential equation for it´s highest derivative and assume it (in this case ẍ) as input of the first integrator. From there on you add computing elements to generate -(d*ẋ + k*x) / m, which will then be given as input of the first integrator to close the circuit. 

.. list-table::
   :widths: 75 75
   :header-rows: 1

   * - Description
     - Circuit
     
   * - As mentioned above, start with an integrator and assume the highest derivative as input.

       **ẍ** represents the deflection over time. If **ẋ0** is set to 1, the damped oscillation starts with maximum velocity. 
     - .. image:: images/quickstart/circuit01.png
     		:width: 400
  		:alt: Alternative text
  		:align: right
  		
   * - When putting another integrator behind the first, you can generate **-ẋ** and **x**
     - .. image:: images/quickstart/circuit02.png
     		:width: 400
  		:alt: Alternative text
  		:align: right
  		
   * - To generate **ẋ** from **-ẋ**, branch off the circuit behind the first integrator and put the second wire in an inverter.
     - .. image:: images/quickstart/circuit03.png
     		:width: 400
  		:alt: Alternative text
  		:align: right
  		  		
   * - Insert two coefficient potentiometers to give ẋ and x their coefficients.

       k = spring coefficient

       d = damper coefficient

       To generate **d*ẋ** and **k*x** 
     - .. image:: images/quickstart/circuit04.png
     		:width: 400
  		:alt: Alternative text
  		:align: right
  		  		
   * - Merge the outputs of the coefficient potentiometers in a summer.

       Note the sign change, which is rather useful for this case.

       Output: **-(d*ẋ + k*x)** 
     - .. image:: images/quickstart/circuit05.png
     		:width: 400
  		:alt: Alternative text
  		:align: right
  		  		
   * - As last computing part add another coefficient potentiometer to divide the output of the summer with the mass coefficient.

       Output: **-(d*ẋ + k*x) / m** 
     - .. image:: images/quickstart/circuit06.png
     		:width: 400
  		:alt: Alternative text
  		:align: right
  		  		
   * - Next to final step is to close the computing circuit by connecting the output of the last potentiometer with the input of the first integrator.

       The sign is already correct. 
     - .. image:: images/quickstart/circuit07.png
     		:width: 400
  		:alt: Alternative text
  		:align: right
  		  		
   * - Lastly, branch off the circuit at a given point to use it later on with a given interface.

       In this case the circuit is branched just after the inverter to make the signal (in this case the velocity over time) visible on an oscilloscope later on.

       Usually, outputs are drawn as arrows. 
     - .. image:: images/quickstart/circuit08.png
     		:width: 400
  		:alt: Alternative text
  		:align: right
  		
3. Wiring the circuit on a THAT and adjusting parameters
--------------------------------------------------------

In order to wire the circuit worked out above you need to be familiar with the computing elements used. 

THAT-overview
~~~~~~~~~~~~~
.. list-table::
   :widths: 75 75
   :header-rows: 1

   * - Description
     - Images
     
   * - On the right side you find an overview image of **The Analog Thing** without wiring.

       It has much more computing parts than needed for this task.

       Important basics:

       **Round/circular panels --> Inputs**
       
       **Triangular panels --> Outputs**
       
       **Rectangular panels --> Static signals and advanced things**

       Black inputs (with a 10 next to it) are not important for this task.


       Important for integrators:

       **IC-panel:** IC refers to initial condition and is used to set the starting condition of the integrator.

       If the IC panel is left open, the initial condition is set to zero. 
     - .. image:: images/quickstart/THATv1.0_overview.jpg
     		:width: 400
  		:alt: Alternative text
  		:align: right
     
   * - In this image the for this task important computing elements, panels and switches are highlighted.

       Note that you certainly do not need every marked computing element, just some of each type. 
     - .. image:: images/quickstart/THATv1.0_parts01.jpg
     		:width: 400
  		:alt: Alternative text
  		:align: right 

From this point you can start wiring the actual simulation circuit.

Wiring THAT
~~~~~~~~~~~

Colors from circuit scheme and actual images are matched to make them easier to identify, but have no further meaning. 

.. list-table::
   :widths: 75 75 75
   :header-rows: 1

   * - Description
     - Circuit
     - Images
     
   * - **Step 1:**

       Start with the first integrator.

       Set the initial condition of the integrator to 1 by connecting the IC-panel with the panel directly below (rectangular +1, green wire).

       Also, connect a blue wire to the first integrators input and a red wire to it´s output, but leave them open.

       The blue wire shall be the last wire to be closed at the end. 
     - .. image:: images/quickstart/DO_00.png
     		:width: 400
  		:alt: Alternative text
  		:align: right
     - .. image:: images/quickstart/DO_00.jpg
     		:width: 400
  		:alt: Alternative text
  		:align: right
          
   * - **Step 2:**

       Connect the output of the first integrator (red wire) to the input of the second integrator.

       Connect a yellow cable to the output of the second integrator. 
     - .. image:: images/quickstart/DO_01.png
     		:width: 400
  		:alt: Alternative text
  		:align: right
     - .. image:: images/quickstart/DO_01.jpg
     		:width: 400
  		:alt: Alternative text
  		:align: right
          
   * - **Step 3:**

       Connect the second output of the first integrator with the input of the first inverter with a red wire.

       Be careful not to mix up the SJ panel of the inverter with the input panel.

       Connect a black cable to the output of the first inverter. 
     - .. image:: images/quickstart/DO_02.png
     		:width: 400
  		:alt: Alternative text
  		:align: right
     - .. image:: images/quickstart/DO_02.jpg
     		:width: 400
  		:alt: Alternative text
  		:align: right
          
   * - **Step 4:**

       Connect the output of the second integrator (yellow wire) with the input of the first potentiometer.

       Connect the output of the inverter (black wire) to the input of the second potentiometer.

       Connect both outputs of the just cabled potentiometers with green wires.

       Note: For practical reasons potentiometers are usually numbered in the to be executed circuit plan. 
     - .. image:: images/quickstart/DO_03.png
     		:width: 400
  		:alt: Alternative text
  		:align: right
     - .. image:: images/quickstart/DO_03.jpg
     		:width: 400
  		:alt: Alternative text
  		:align: right
          
   * - **Step 5:**

       Connect both potentiometer outputs (green wires) each with an input of the summer.

       Connect a red wire to the output of the summer. 
     - .. image:: images/quickstart/DO_04.png
     		:width: 400
  		:alt: Alternative text
  		:align: right
     - .. image:: images/quickstart/DO_04.jpg
     		:width: 400
  		:alt: Alternative text
  		:align: right
          
   * - **Step 6:**

       Connect the output of the summer (red wire) with the input of the third potentiometer.

       Connect the input of the first integrator (blue wire) with the output of the third potentiometer.

       The circuit is closed. 
     - .. image:: images/quickstart/DO_05.png
     		:width: 400
  		:alt: Alternative text
  		:align: right
     - .. image:: images/quickstart/DO_05.jpg
     		:width: 400
  		:alt: Alternative text
  		:align: right
          
   * - **Step 7:**

       Connect the output of the inverter with an output panel (x, y, z or u) by plugging a yellow wire on top of the black wire connected with said output. 
     - .. image:: images/quickstart/DO_06.png
     		:width: 400
  		:alt: Alternative text
  		:align: right
     - .. image:: images/quickstart/DO_06.jpg
     		:width: 400
  		:alt: Alternative text
  		:align: right
  		
Wiring complete.

Now the potentiometers have to be set to their corresponding values. In this setup it is good to set every potenetiometer to 0.5 for the beginning.

4. Operation and visualization
------------------------------

4.1 Output device
~~~~~~~~~~~~~~~~~

In order to study the results of a given simulation an output device is necessary. For electrical analog computers oscilloscopes are the tool of choice. They provide a graphic visualization of changing voltages over time, which is exactly what electrical analog computers give.

The THAT machine unit is 10 volts. The chinch outputs **(x,y,z,u)** are connected to a voltage devider with a factor of 1/10. So the maximum output is plus/minus 1 volt, which makes it compatible to standard mircophone inputs so it can be used with soundcard oscilloscopes.

Note: Most oscilloscopes come with BNC-input sockets. Therefore a CHINCH to BNC adapter is needed in order to connect the chinch outputs properly. However, it is possible to connect oscilloscope probes directly with the patch cables.

The trigger output can be very useful in case the oscilloscope has a free input left or even a seperate trigger input.


4.2 Choosing a viable operation mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After setting up the output device the operation mode is to be choosen.

When setting the THAT to **OP**, the calculation will start and will continue until manually interrupted. This will lead to a valid result, but the result is only given one time. Once the damped oscillation is damped completely, the result will be zero (forever).

The damped oscillation is a good example for using the **fast repetitive mode (REPF)** in order to study the behavior of the system with
different potentiometer settings.

In this mode the THAT switches between **operation** and **initial condition**, so both the green and yellow LED appear to shine simultaniously.

For the repetitive mode the operation time needs to be taken into account. At the THAT it is controlled by the nob (OP-TIME) next to the operation mode switch.

The operation time defines the time after which the simulation is repeated. After this time the THAT switches to IC mode for a fixed amount of time in order to prepare the next simulation run.


