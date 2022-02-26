.. role:: raw-latex(raw)
   :format: latex


.. contents::
   :depth: 3

====================
Mathieu\ ’s equation
====================


Introduction
============

This application note deals with the well-known Mathieu equation, a
linear homogenous second order differential equation with many
applications (it can be used to described the vibrations in an elliptic
drum, or the behaviour of an inverted pendulum and many more).

The general form of Mathieu\ ’s equation is

.. math:: \ddot{y}+\left(a-2q\cos(2t)\right)y=0

with the initial conditions

.. math::

   \begin{aligned}
      y_0&=1\text{ and}\\
      \dot{y}_0&=0.
     \end{aligned}

Following :raw-latex:`\cite{eai_mathieu}` we set

.. math:: a:=2q

and define a function **(1)**:

.. math:: x(t)=1-\cos(2t)\label{equ_m_cos_1}

to simplify things a bit yielding **(2)**:

.. math:: \ddot{y}+axy=0\label{equ_m_basic}

leaving out the time as argument of the function :math:`x`.

At first sight, one might be tempted to implement the function :math:`x`
by means of a diode function generator but due to the fixed argument
range of such a function generator, this approach is not viable. As so
often it is much better to generate this function by solving a suitable
differential equation. If we differentiate (1) twice, we get **(3)** and **(4)**:

.. math::

   \begin{aligned}
      \dot{x}&=2\sin(2t)\text{~and}\label{equ_m_cos_2}\\
      \ddot{x}&=4\cos(2t).\label{equ_m_cos_3}
     \end{aligned}

This yields the following defining differential equation for **(1)**, which will be referred to as **(5)**:

.. math:: \ddot{x}+4x=4\label{equ_m_cos_4}

since we have

.. math:: 4\cos(2t)+4\left(1-\cos(2t)\right)=4

with **(3)** and **(4)**.

Scaling and programming
=======================

In order to derive a computer setup for **(2)** we will first create a scaled
computer program for **(5)** which can be written without any scaling like this,
already closely resembling an analog computer program:

.. math::

   \begin{aligned}
      \dot{x}&=\int\ddot{x}\ \mathrm{d}t\nonumber\\
      x&=\int\dot{x}\ \mathrm{d}t\label{equ_m_cos_5}\\
      \ddot{x}&=4-4x\label{equ_m_cos_6}
     \end{aligned}

Obviously, we have :math:`2\leq x\leq 0` due to **(1)**, so we will start by scaling
**(6)** by :math:`1/2` and compensating for this by changing the factor :math:`4` in **(7)** accordingly, yielding

.. math::

   \begin{aligned}
      \dot{x}&=\int\ddot{x}\ \mathrm{d}t\label{equ_m_cos_8}\\
      x&=\int\frac{1}{2}\dot{x}\ \mathrm{d}t\nonumber\\
      \ddot{x}&=4-8x\label{equ_m_cos_7}
     \end{aligned}

Due to **(4)** we know that 
:math:`-4\leq\ddot{x}\leq 4`, so we will now scale
**(9)** by :math:`1/4` and compensate for this in **(8)**:

.. math::

   \begin{aligned}
      \dot{x}&=\int4\ddot{x}\ \mathrm{d}t\nonumber\\
      x&=\int\frac{1}{2}\dot{x}\ \mathrm{d}t\nonumber\\
      \ddot{x}&=1-2x
     \end{aligned}

Now all that is left is :math:`\dot{x}` which is in the range of
:math:`[-2:2]` due to **(3)**:

.. math::

   \begin{aligned}
      \dot{x}&=\int2\ddot{x}\ \mathrm{d}t\nonumber\\
      x&=\int\dot{x}\ \mathrm{d}t\nonumber\\
      \ddot{x}&=1-2x
     \end{aligned}

The resulting computer setup for these equations where no function
exceeds the interval :math:`[-1:1]` is shown in figure 1. Keep in mind that the output
signal has been scaled down from the interval :math:`[0:2]` to
:math:`[0:1]` – a fact that we have to compensate for in the second part
of the computer setup.

Deriving and scaling the computer setup for **(2)** is done similarly. The problem here is
the rather wild behaviour of the Mathieu equation which makes scaling
difficult if :math:`a` is allowed to take on values from a rather large
interval. The setup shown in figure 2
basically allows values :math:`0\leq a\leq10` with the exception of the
regions where the equation is unstable.

Results
=======

Figures 3 and 4 show some typical solutions for Mathieu\ ’s equation for different increasing values for
:math:`a`. These solutions were obtained with the integrator time
constant set to :math:`k_0=10^3` and the computer running in repetitive
operation. The oscilloscope is set to :math:`2` ms per division
horizontally and :math:`2` V/div vertically.


.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - .. image:: m_1.jpg
   		:align: left
   		:width: 400
     - .. image:: m_2.jpg
   		:align: right
   		:width: 400
		:height: 400
		
   * - .. image:: m_3.jpg
     - .. image:: m_4.jpg


Figure 3: Typical solutions of Mathieu’s equation for some values 0  a/10  1


.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - .. image:: m_5.jpg
   		:align: left
   		:width: 400
     - .. image:: m_6.jpg
   		:align: right
   		:width: 400
		:height: 400
		
   * - .. image:: m_7.jpg
     - .. image:: m_8.jpg
     
     
Figure 4: Typical solutions of Mathieu’s equation for some values 0  a/10  1

