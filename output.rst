1. Problem Statement
====================

We have 2 offshore production plants in 2 locations and an estimated
demand for our products.

We want to produce a schedule of production from both plants that meets
our demand with the lowest cost.

A factory can be in 2 states:

-  Off – Producing zero units

-  On – Producing between its minimum and maximum production capacities

2. Sets and Indices
===================

2.1. Sets
---------

*I*: set of all factories, I = {0,1}

*J*: set of all months, J = {0,1,2.….11}

2.2. Indices
------------

*i*: Denotes the factory number/index, :math:`i\ \epsilon I\ `

*j*: Denotes the month number/index,\ :math:`\ \ \ \ j\ \epsilon\ J`

3. LP Formulation
=================

Formulating the problem as a MILP problem

3.1. Decision Variables
-----------------------

-  :math:`x_{ij}` : Quantity produced in factory ‘i’ in month ‘j’

All :math:`x_{ij}` are integers as quantity produced can’t be a fraction

-  :math:`y_{ij}\ :\ `\ Represents the open or closed status a factory
   ‘i’ in month ‘j’

:math:`y_{ij} = \left\{ \begin{array}{r}
1\ if\ factory{\ 'i}^{'}\ is\ open\ in\ month\ 'j' \\
0\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Otherwise
\end{array} \right.\ `

3.2. Parameters
---------------

:math:`Var\_ cost_{ij}\ \ \ \ \ \ \ \ \ \ :\ \ \ `\ Variable cost of
production in factory ‘i’ in the month ‘j’

:math:`Fixe{d\_ cost}_{ij}\ \ \ \ \ \ :` Fixed cost of production in
factory ‘i’ in the month ‘j’

:math:`Demand_{j}\ \ \ \ \ \ \ \ \ \ \ \ :` Demand to be met at month
‘j’

:math:`Min\_ capacity_{ij}\ :\ ` Minimum quantity that should be
produced by factory i in month j

:math:`Max\_ capacity_{ij}\ :` Maximum quantity that should be produced
by factory i in month j

3.3. Objective Function 
------------------------

.. math:: \sum_{j\epsilon J}^{}{(Var\_ cost_{ij}*x_{ij} + Fixed\_\cos t_{ij}\ }*{\ y_{ij})}_{\ }\ \ \ \ \ \ \forall i\ \epsilon\ I

3.3. Constraints
----------------

-  Production-Demand Constraint:

The sum of quantities produced from each of the factories in a month
must be equal to the demand in that month

.. math:: \sum_{i\epsilon I}^{}{{(x}_{ij} = Demand_{ij}})\ \ \ \ \ \ \ \ \forall\ j\ \epsilon\ J

-  Capacity constraints

   -  Minimum capacity constraint:

..

   Production at each factory a month should be greater than the minimum
   production limit of the factory that month given that the factory is
   open in that month

   .. math:: x_{ij} \geq min\text{\_}capacity_{ij}*y_{ij}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \forall i\ \epsilon\ I\ \ and\ \ \forall\ \ j\epsilon J

-  Maximum capacity constraint:

..

   Production at each factory a month should be less than the minimum
   production limit of the factory that month given that the factory is
   open in that month

   .. math:: x_{ij} \leq \ max\text{\_}capacity_{ij}*y_{ij}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \forall i\ \epsilon\ I\ \ and\ \ \forall\ \ j\epsilon J

-  Sign Constraints:

The decision variables for production quantity considered should be
non-negative

   :math:`x_{ij} \geq 0\ \ \ \ \ \ \ \ \ \ `
   :math:`\forall\ i\epsilon I\ and\ \ j\epsilon J`

   :math:`y_{ij}\epsilon\left\{ 0,1 \right\}\ `
   :math:`\forall\ i\epsilon I\ \ and\ \ j\epsilon J`
