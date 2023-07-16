SymbolicCI
----------
The program generate Configuration Interaction wavefunction and Hamiltonian expression for an arbitrary multiplicity and for 
a given number of electron.


-----------
Description
-----------
This program the generate the configurations state function using branching diagram for a given spin state based on $S^{2}$ and $S_{z}$ with a specific spin configuration of it's subsystem using branching diagram. The program allow the configuration of electrons to be distributed in set of spatial orbital/site. Based on the spin and site of electron it generate the qbit operator using pauli matrix for creation and annhilation of electron. Then it evaluates the coupling 
$$\\langle \\Psi \\vert H \\vert\\Phi\\rangle =  \\langle C_{s_{1},a_{1}} \\otimes...\\otimes C_{s_{n},a_{n}} \\vert \\mathbf{O_{1}}\\vert C^{\\dagger}_{s_{1},a_{1}}\\otimes...\\otimes C^{\\dagger}_{s_{n},a_{n}} $$
from the derived electronic configuration of state using symbolic python.


------------
Installation
------------

.. code-block:: bash

    $pip install git+https://github.com/roehr-lab/SymbolicCI.git