.. role:: raw-latex(raw)
   :format: latex


.. contents::
   :depth: 3

=================
Sprott SQ M model
=================


This application note implements the :math:`SQ_M` model (cf.
:raw-latex:`\cite[pp.~68ff.]{sprott}`), an example of a simple
three-dimensional chaotic flow with a quadratic nonlinearity. The model
consists of three coupled differential equations

.. math::

   \begin{aligned}
     \dot{x}&=-z\\
     \dot{y}&=-x^2-y\\
     \dot{z}&=\alpha+\alpha x+y
    \end{aligned}

with :math:`\alpha=1.7` and the initial conditions
:math:`x(0)=1, y(0)=-0.8, z(0)=0`. To scale the system, three scale
factors :math:`\lambda_x=\lambda_z=\frac{1}{4}` and
:math:`\lambda_y=\frac{1}{6}` are introduced which in turn yield (after
collecting all resulting factors)

.. math::
   :label: sqm01

   \begin{aligned}
     \dot{x}&=-z\label{equ_sqm_x}\\
   \end{aligned}

.. math::
   :label: sqm02
      
   \begin{aligned}  
     \dot{y}&=-2.666x^2-y\label{equ_sqm_y}\\
   \end{aligned}

.. math::
   :label: sqm03
      
   \begin{aligned}
     \dot{z}&=\frac{\alpha}{4}+\alpha x+0.15y.\label{equ_sqm_z}
    \end{aligned}

Thanks to the constant term :math:`\frac{\alpha}{4}`, the initial
conditions mentioned in the original system can be safely ignored as it
will enter its chaotic oscillation right away.

The analog computer setup can be derived directly from the scaled
equations **(1)**, **(2)** and **(3)** as shown in figure 1.

.. list-table::
   :widths: 75 
   :header-rows: 0
   
   * - .. figure:: circuit01.png
       
   * - Figure 1: Analog computer setup for the SQM model

This little program is ideally suited for *THE ANALOG THING* as can be
seen in figure 2. Figure 3 shows a typical phase space plot
of :math:`x` vs. :math:`y` which was caputured using a USB-soundcard
with stereo line in and the software *Oscilloppoi*\  [1]_ running on a
Mac.


.. list-table::
   :widths: 75 75
   :header-rows: 0

   * - .. figure:: sqm_that.jpg
   		:width: 400
     - .. figure:: sqm_result.jpg
   		:width: 400
		:height: 400
		
   * - Figure 2: Implementation of the program shown in figure 1
     - Figure 3: xy phase space plot of the SQ M system
     
     
References
==========

[Sprott(2016)] Julien Clinton Sprott, *Elegant Chaos – Algebraically Simple Chaotic
Flows*, World Scientific, 2016

.. [1]
   See https://anikikobo.com/software/oscilloppoi/index_en.html.
