.. role:: raw-latex(raw)
   :format: latex


.. contents::
   :depth: 3
   
============================================
The Hindmash-Rose-model of neuronal bursting
============================================

Beginning in the early 20th century, the behaviour of neurons has been
described by increasingly realistic mathematical models. The very first
of these models is called *integrate-and-fire* and is due to Lous
Lapicque who developed it in 1907. A better model was developed in the
early 1960s by Richard FitzHugh and J. Nagumo and is described by

.. math::

   \begin{aligned}
     \dot{v}&=v-\frac{v^3}{3}-w+I_\text{ext}\text{~and}\\
     \tau\dot{\omega}&=v+a+-bw.
    \end{aligned}

This model is still pretty simple and it can be shown that is basically
equivalent to the van der Pol equation

.. math:: \ddot{y}+\mu\left(y^2-1\right)\dot{y}+y=0,

which was devised by Balthasar van der Pol in 1920 as a result of his
pioneering work on vacuum tubes and oscillator circuits. Accordingly,
the FitzHugh-Nagumo model is basically a relaxation oscillator [1]_
controlled by an external stimulus :math:`I_\text{ext}`.

A much more interesting model is due to Hindmarsh and Rose\  [2]_ and
consists of three coupled differential equations

.. math::
   :label: 1

   \begin{aligned}
     \dot{x}&=-ax^3+bx^2+y-z+I_\text{ext}\label{equ_hr_1}\\
   \end{aligned}

.. math::
   :label: 2
      
   \begin{aligned}
     \dot{y}&=-dx^2+c-y\label{equ_hr_2}\\
   \end{aligned}

.. math::
   :label: 3
      
   \begin{aligned}
     \dot{z}&=r(s(x-x_r)-z)\label{equ_hr_3}
    \end{aligned}

with the parameters :math:`a=1`, :math:`b=3`, :math:`c=1`, :math:`d=5`,
:math:`r=10^{-3}`, :math:`s=4`, :math:`x_r=-\frac{8}{5}` and initial
conditions of :math:`2` for all three integrators in the final setup.

As quick numerical simulation shows, see figure 1, the system must be scaled
before programmed on an analog computer. Scaling is most easily done
manually by first applying proper scaling factors to the variables
:math:`x`, :math:`y`, and :math:`z`. If, e.ġ., :math:`z` is to be scaled
by a factor of :math:`\frac{1}{2}`, every input of the integrator
yielding :math:`-z` is scaled down by that factor. To compensate for
this, :math:`-z` (or :math:`z`) must be scaled up by a corresponding
factor of :math:`2` at all inputs of computing elements using this
variable etc. In the end, these various factors scaling values down and
up tend to cancel out in most cases, so that typically only a few
additional potentiometers are required for a scaled analog computer
program as compared with an unscaled program.

.. list-table::
   :widths: 75 
   :header-rows: 0
   
   * - .. figure:: numerical_simulation.jpg
       
   * - Figure 1: Numerical simulation of the three coupled differential equations **(1)**, **(2)** and **(3)**.


The resulting scaled computer setup is shown in figure 2. The scaled parameters are these:
:math:`a^*=4`, :math:`b^*=6`, :math:`c^*=0.066`, :math:`d^*=1.333`,
:math:`r=10^{-3}`, :math:`s=4`, :math:`x^*_r=0.8` with initial
conditions of :math:`\pm1` accordingly. A bit problematic here are the
values :math:`r` and the resulting value of the product
:math:`rsx^*_r=0.0032`. It is not practical to setup values that small
directly on a manual potentiometer. In cases like this, the time-scale
factor of the affected integrator can be used to gain an additional
scaling factor of :math:`10^n` as shown in the setup. Furthermore, the
products :math:`rs=0.004` and :math:`rsx^*_r=0.0032` are setup on
additional potentiometers.

.. list-table::
   :widths: 75 
   :header-rows: 0
   
   * - .. figure:: circuit01.png
       
   * - Figure 2: Scaled analog computer setup for the Hindmarsh-Rose model

Figure 3 shows a typical result
obtained by this analog computer circuit with :math:`I_\text{ext}=1`.
The yellow trace depicts the output potential of the neuron (:math:`x)`,
the green trace corresponds to the amount of potassium channels
(:math:`y`), and the orange channel shows :math:`z`.

.. list-table::
   :widths: 75 
   :header-rows: 0
   
   * - .. figure:: result_1.png
       
   * - Figure 3: Typical result of spiking neuron simulation



[Hindmarsh et al. 1982] J. L. Hindmarsh, R. M. Rose, “A model of the nerve impulse using two
first-order differential eequations”, in *Nature*, Vol. 296, 11th March
1982, pp. 162–164

[Hindmarsh et al. 1984] J. L. Hindmarsh, R. M. Rose, “A model of neuronal
bursting using three coupled first order differential equations”, in
*Prov. R. Soc. Lond.*, B 221, 87–102 (1984)

.. [1]
   In contrast to a harmonic oscillator which is typically based on an
   amplifier with suitable feedback, running in resonance mode, a
   relaxation oscillator switches abruptly between charge and discharge
   mode and thus yields non-harmonic output signals.

.. [2]
   See :raw-latex:`\cite{hindmarsh_rose_1982}` and
   :raw-latex:`\cite{hindmarsh_rose_1984}`.
