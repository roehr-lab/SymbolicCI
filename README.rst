SymbolicCI
----------

The program efficiently generates Configuration Interaction (CI) wavefunctions, facilitating the description of intricate electronic structures within the system. It also formulates expressions for couplings and dibatic energy, utilizing both one-electron and two-electron integral expressions. This flexible approach accommodates arbitrary multiplicities and a specified number of electrons, allowing for a comprehensive analysis.

Key features of the program include:
- **Configuration Interaction (CI) Wavefunction Generation**:
  The program constructs CI wavefunctions that accurately represent the electronic configurations and interactions within the system, capturing correlations and electron exchanges.

- **Couplings and Dibatic Energy Expressions**:
  The program derives expressions for couplings and dibatic energy, shedding light on transitions and interactions between electronic states. These expressions are derived from one-electron and two-electron integral components, providing insights into the underlying physics.

- **Multiplicities and Subsystem Configuration**:
  Users can define not only the multiplicity of the entire system but also the multiplicities of the subsystems. This allows for the exploration of diverse electronic scenarios and interactions, encompassing complex interactions between subsystems.

- **Subsystem Order and Interaction Sign**:
  The program allows users to specify subsystem order and the sign of mutual interactions, providing customization for studying various electronic structures.

By combining these capabilities, the program empowers researchers to analyze complex electronic systems, investigating different multiplicities, subsystem configurations, and intricate interaction patterns. This versatile tool provides a comprehensive platform for studying electronic structures and properties in diverse and nuanced scenarios.


-----------
Description
-----------
This program the generate the configurations state function using branching diagram for a given spin state based on $S^{2}$ and $S_{z}$ with a specific spin configuration of it's subsystem using branching diagram. The program allow the configuration of electrons to be distributed in set of spatial orbital/site. Based on the spin and site of electron it generate the qbit operator using pauli matrix for creation and annhilation of electron. Then it evaluates the coupling 
$$\\langle \\Psi \\vert H \\vert\\Phi\\rangle =  \\substack{\\langle C_{s_{1},a_{1}} \\otimes...\\otimes C_{s_{n},a_{n}} \\vert \\mathbf{O_{1}}\\vert C^{\\dagger}_{s_{1},a_{1}}\\otimes...\\otimes C^{\\dagger}_{s_{n},a_{n}} \\rangle  \\\\ + \\frac{1}{2} \\langle C_{s_{1},a_{1}} \\otimes...\\otimes C_{s_{n},a_{n}} \\vert \\mathbf{O_{2}}\\vert C^{\\dagger}_{s_{1},a_{1}}\\otimes...\\otimes C^{\\dagger}_{s_{n},a_{n}} \\rangle } $$
from the derived electronic configuration of state using symbolic python.


The program operates by generating configuration state functions through a branching diagram approach, focusing on a given spin state characterized by $S^2$ and $S_z$. It considers a specific spin configuration of its subsystem, which is represented using branching diagrams. The program's functionality is as follows:

1. **Configuration State Function Generation**:
   The program employs branching diagrams to generate configuration state functions. These functions encapsulate the electronic configurations of the system, considering the spin characteristics denoted by $S^2$ and $S_z$. The branching diagrams illustrate the arrangement of electrons within the system.

2. **Electron Configuration and Qubit Operators**:
   Users can configure the distribution of electrons across spatial orbitals/sites. Based on the electron's spin and orbital information, the program generates qubit operators using Pauli matrices. These operators facilitate the creation and annihilation of electrons, capturing the underlying electronic transitions.

3. **Coupling Evaluation**:
   The program evaluates couplings between different electronic states using the derived configuration state functions. The coupling is computed as:
   \begin{equation}
   \langle \Psi \vert H \vert \Phi \rangle = 
   \substack{
   \langle C_{s_1,a_1} \otimes...\otimes C_{s_n,a_n} \vert \mathbf{O_1} \vert C^{^\dagger}_{s_1,a_1}\otimes...\otimes C^{^\dagger}_{s_n,a_n} \rangle  \\
   + \frac{1}{2} \langle C_{s_1,a_1} \otimes...\otimes C_{s_n,a_n} \vert \mathbf{O_2} \vert C^{^\dagger}_{s_1,a_1}\otimes...\otimes C^{^\dagger}_{s_n,a_n} \rangle 
   }
   \end{equation}
   Here, $C_{s_i,a_i}$ represents an electron operator for the $i$-th electron with spin $s_i$ at site $a_i$, and $\mathbf{O_1}$ and $\mathbf{O_2}$ denote the operators for electron creation and annihilation. The coupling is evaluated using symbolic Python operations.

The program's capabilities facilitate a thorough exploration of electronic structure and interactions, allowing for the computation of couplings between different electronic states. This comprehensive approach utilizes symbolic Python to handle complex calculations and generate insights into the quantum behavior of the system.

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

Prior to initiating the coupling calculation program, it is recommended to visit the following website: [https://roehr-lab.github.io/im1.html](https://roehr-lab.github.io/im1.html). This webpage offers a user-friendly interface to explore and configure the spin chain arrangement that you intend to evaluate. The process involves the following steps:

1. Enter the desired number of electrons for your system.
2. Utilize the sliders provided for "final S," "Pathway of S," and "Final M."
3. The website will dynamically display the constructed many-electron spin state corresponding to your chosen configuration.

As an illustrative example, consider the evaluation of couplings between specific states. To facilitate this, ensure that you take note of the values associated with "final S," "Pathway of S," and "Final M" for both the Bra and Ket states of interest. These values will be instrumental in configuring the coupling calculation program accurately. By leveraging this interactive tool, you can effectively tailor the coupling calculations to your desired spin chain configurations, enhancing the precision and relevance of your analysis.


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

Once the selection of spatial orbitals is finalized, the program proceeds with an iterative process that encompasses various components crucial for the evaluation. This iterative process involves the following key steps:

1. **Bra and Ket Determinants**
2. **One-Electron Symbolic Operator**:
3. **Two-Electron Symbolic Operators**:
   
Throughout this iterative process, the program systematically combines these components to evaluate relevant expressions, such as energies or couplings, based on the selected spatial orbitals and the many-electron states defined by the Bra and Ket determinants.


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
