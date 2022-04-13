
Hindmarsh-Rose Neuron Model
===========================

Background and Mathematics
--------------------------

Beginning in the early 20th century, the behaviour of neurons has been 
described by increasingly realistic mathematical models. The very first of
these models is called *integrate-and-fire* and is due to 
*Lous Lapicque* who developed it in 1907. A better model was developed
in the early 1960s by *Richard FitzHugh* and *J. Nagumo* and 
is described by 

.. math::

   \dot{v}&=v-\frac{v^3}{3}-w+I_\text{ext}\quad\quad\text{and}\\
   \tau\dot{\omega}&=v+a+-bw.


This model is still pretty simple and it can be shown that is basically 
equivalent to the \textsc{van der Pol} equation

.. math::

   \ddot{y}+\mu\left(y^2-1\right)\dot{y}+y=0,

which was devised by *Balthasar van der Pol* in 1920 as a result of
his pioneering work on vacuum tubes and oscillator circuits. Accordingly,
the *FitzHugh-Nagumo* model is basically a relaxation
oscillator (In contrast to a harmonic oscillator which is typically
based on an amplifier with suitable feedback, running in resonance mode, a
relaxation oscillator switches abruptly between charge and discharge mode and
thus yields non-harmonic output signals.) controlled by an external stimulus 
:math:`I_\text{ext}`.

A much more interesting model is due to *Hindmarsh* and 
*Rose*\ (See hindmarsh_rose_1982 and 
hindmarsh_rose_1984) and consists of three coupled differential
equations

.. math::

    \begin{aligned}
    \dot{x}&=-ax^3+bx^2+y-z+I_\text{ext}\\
    \dot{y}&=-dx^2+c-y\\
    \dot{z}&=r(s(x-x_r)-z)
    \end{aligned}

with the parameters :math:`a=1`, :math:`b=3`, :math:`c=1`, :math:`d=5`,
:math:`r=10^{-3}`, :math:`s=4`,
:math:`x_r=-\frac{8}{5}` and initial conditions of 2 for all three integrators in 
the final setup.

For a quick numerical simulation, see for instance
`Analog Paradigm Application Note 28 <https://analogparadigm.com/downloads/alpaca_28.pdf>`_.

Implementation on THAT
----------------------

The resulting program looks like this:

.. image:: hindmarsh_rose/Hindmarsh_rose_prg.png
   :width: 900

The output of the simulated neuron is x, while Iext represents the input to the neuron. Setting Iext to +1 will cause the neuron to burst with sequences of spikes as shown in this actual screen shot from a digital oscilloscope: 

.. image:: hindmarsh_rose/Hindmarsh_rose_result.jpg
   :width: 700
   :align: center
   
The actual implementation of this program looks like this: 

.. image:: hindmarsh_rose/Hindmarsh_rose_program.jpg
   :width: 500
