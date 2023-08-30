SymbolicCI
----------
The program generate Configuration Interaction wavefunction and expression of couplings and dibatic energy in terms of one electron and two electron integral expressions for an arbitrary multiplicity and for a given number of electrons. With this program used can not only choose the multiplicity of the whole system but also the muliplicities of the subsystem and their order as well as the sign of mutual interactions. 


-----------
Description
-----------
This program the generate the configurations state function using branching diagram for a given spin state based on $S^{2}$ and $S_{z}$ with a specific spin configuration of it's subsystem using branching diagram. The program allow the configuration of electrons to be distributed in set of spatial orbital/site. Based on the spin and site of electron it generate the qbit operator using pauli matrix for creation and annhilation of electron. Then it evaluates the coupling 
$$\\langle \\Psi \\vert H \\vert\\Phi\\rangle =  \\substack{\\langle C_{s_{1},a_{1}} \\otimes...\\otimes C_{s_{n},a_{n}} \\vert \\mathbf{O_{1}}\\vert C^{\\dagger}_{s_{1},a_{1}}\\otimes...\\otimes C^{\\dagger}_{s_{n},a_{n}} \\rangle  \\\\ + \\frac{1}{2} \\langle C_{s_{1},a_{1}} \\otimes...\\otimes C_{s_{n},a_{n}} \\vert \\mathbf{O_{2}}\\vert C^{\\dagger}_{s_{1},a_{1}}\\otimes...\\otimes C^{\\dagger}_{s_{n},a_{n}} \\rangle } $$
from the derived electronic configuration of state using symbolic python.


------------
Installation
------------

.. code-block:: bash

     pip install git+https://github.com/roehr-lab/SymbolicCI.git

-----
Run
-----
To evaluate the coupling expression use program SymbolicCI-Coupling.py


.. code-block:: bash

     SymbolicCI-Coupling.py

Before running the coupling program it is advised to visit https://roehr-lab.github.io/im1.html to explore the spin chain configuration you want to evaluate. You can enter the number of electrons that is desired in your system and slide the sliders of "final S", "Pathway of S" and  "Final M". The website will show the constructed many electron spin state. 
An example of evaluation of coupling between the states $\\langle S_{1}S_{0} \\vert  H \\vert ^{1}T T \\rangle$ is shown here. Please note-down the value of "final S", "Pathway of S" and  "Final M" for the desired Bra and Ket. 

.. image:: images/i10.png
    :height: 850px
    :width: 1000px

This is the branching diagram of two singlet subsystem combination giving Singlet. This will serve the spin configuration for $S_{0}S_{1}$ 

.. image:: images/i11.png
    :height: 850px
    :width: 1000px

This is the branching diagram of two triplet subsystem combination giving Singlet. This will serve the spin configuration for $^{1}TT$ 

.. image:: images/i1.png
    :height: 450px
    :width: 1000px

.. image:: images/i4.png
    :height: 450px
    :width: 1000px


After selecting the spin configuration for the Bra and Ket of the wave function the spatial orbital for each electron is selected.

.. image:: images/i6.png
    :height: 750px
    :width: 1000px

.. image:: images/i7.png
    :height: 750px
    :width: 1000px

After the selection of spatial orbitals  is complete the program iterate overall the determinants of bra, kets , one electron symbolic operator and two electron symbolic operators during the  evaluation process.

.. image:: images/i9.png
    :height: 450px
    :width: 1000px


.. image:: images/i12.png
    :height: 950px
    :width: 1000px

The coupling terms are printed out. (Note that example coupling has two electron integrals  only. So no One electron integral terms are printed)

The package includes an additional script for comprehensive analysis:

Apart from the previously mentioned functionalities, this package also provides a script designed to calculate couplings among all possible states across all singlet multiplicities within the slipped stack trimer system. This calculation considers both longitudinal (x) and transverse (y) axis slipping configurations. The various states that are considered include local excitons, charge transfer states, and paired triplets with singlet multiplicity.

The usage of this script involves providing command line arguments in the following format:

.. code-block:: bash

     TrimerCalculate.sh ethene.xyz 0.7 0.0


This command initiates the execution of two Python scripts, "SymbolicCI-TrimerCoupling.py" and "SymbolicCI-TrimerPlot.py," sequentially. Here's a breakdown of their roles:

1. **SymbolicCI-TrimerCoupling.py**:
   This script takes three command line arguments:
   1. An XYZ file containing the monomer's structure.
   2. The amount of slipped stacking along the x-axis (in angstroms).
   3. The amount of slipped stacking along the y-axis (in angstroms).

   The script's tasks encompass:
   - Constructing a trimer structure based on the provided monomer's XYZ file and the specified slipped stacking values.
   - Conducting initial electronic structure calculations on the trimer.
   - Transforming the integrals used in electronic structure calculations.

2. **SymbolicCI-TrimerPlot.py**:
   This script is responsible for calculating dibatic couplings and plotting them on an energy plot. Its functions include:
   - Calculating dibatic couplings using data obtained from electronic structure calculations.
   - Creating a plot to visualize the calculated couplings in terms of energy.

By sequentially executing these scripts with the provided command line arguments, a series of analyses and calculations regarding the electronic structure and coupling properties of the slipped stack trimer system are performed. These scripts collectively contribute to a more comprehensive understanding of the system's characteristics and interactions.



------------
Requirements
------------

Required python packages:

 * pytorch
 * numpy, scipy, matplotlib
 * sympy
 * pip 10+
 * pyscf

------
Author
------
* Anurag Singh

---------
Reference
---------
