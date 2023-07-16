//=================================================================================================
/*!
//  \file cgc.h
//  \brief Header file for Clebsch-Gordan Coefficients Generalized by power series representations.
//  
// For more details see:
// <a href="https://functions.wolfram.com/HypergeometricFunctions/ClebschGordan/06/01/" >functions.wolfram</a>          
//
//  Copyright (c) 2022 Mohammed Maher Abdelrahim Mohammed
//  
//  Permission is hereby granted, free of charge, to any person obtaining a copy
//  of this software and associated documentation files (the "Software"), to deal
//  in the Software without restriction, including without limitation the rights
//  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
//  copies of the Software, and to permit persons to whom the Software is
//  furnished to do so, subject to the following conditions:
//  
//  The above copyright notice and this permission notice shall be included in all
//  copies or substantial portions of the Software.
//
//  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
//  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
//  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
//  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
//  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
//  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
//  SOFTWARE.
*/
//=================================================================================================
//#pragma once
#ifndef CGC_H
#define CGC_H

//-------------------------------------------------------------------------------------------------
// Includes
//-------------------------------------------------------------------------------------------------
#include<limits>
#include<cmath>
#include<complex>
#include<vector>
#include<map>
#include<stdexcept>
#include"utilities.h"

//=================================================================================================
//
//  CLASS DEFINITION
//
//=================================================================================================

//*************************************************************************************************
/*! \class CGCcoeff
* \brief CGCcoeff is a class for Clebsch-Gordan Coefficients representation 
* \f$<j_1, j_2; m_1, m_2 | j, m >\f$.
*
* Note that the coefficients \f$<j_1, j_2; m_1, m_2 | j, m >\f$ = 0. unless \f$m1+m2=m\f$.
*/
class CGCcoeff {
	public:
		double j1=0; ///< the the first particle angular momentum (spin or orbital). 
		double j2=0; ///< the angular momentum (spin or orbital) of the second particle.
		double m1=0; ///< magnetic quantum number of the first particle (or system) 
		double m2=0; ///< magnetic quantum number of the second particle (or system) 
		double j=0; ///< total angular momentum: \f$|j1 - j2| <= j <= |j1 + j2|\f$
		double m=0; ///< total \f$m\f$ located within the rang \f$-j<m<j\f$
		 
		CGCcoeff() = default; ///< Defaulte constructor
		
		/*! \brief constructor with input */
		CGCcoeff(double J1, double J2, double M1, double M2, double J, double M)
		:j1(J1),j2(J2),m1(M1),m2(M2),j(J),m(M)
		{ 
		 //j1 = J1; j2 = J2; m1 = M1; m2 = M2; j = J; m = M;
		}
		
		/*! \brief constructor with input */
		CGCcoeff(double J, double M):j(J),m(M){}
		
		/*! \brief constructor with input */
		CGCcoeff(double J1, double J2,double J, double M)
		:j1(J1),j2(J2),j(J),m(M){}
		
		/*! \brief constructor with input */	 
		CGCcoeff(const CGCcoeff& gc){
			j1 = gc.j1; j2 = gc.j2; m1 = gc.m1; m2 = gc.m2; j = gc.j; m = gc.m;
		}

	        /*!overloading operator "<". required to be used in a std::map*/
		inline bool operator<(const CGCcoeff &rhs) const {
			if( j1 < rhs.j1 ) return true;
			if( j1 > rhs.j1 ) return false;
			if( j2 < rhs.j2 ) return true;
			if( j2 > rhs.j2 ) return false;
			if( m1 < rhs.m1 ) return true;
			if( m1 > rhs.m1 ) return false;
			if( m2 < rhs.m2 ) return true;
			if( m2 > rhs.m2 ) return false;
			if( j  < rhs.j  ) return true;
			if( j  > rhs.j  ) return false;
			return ( m  < rhs.m  );
		}
		/*! Overloading the logical "==" operator*/ 
		bool operator ==(const CGCcoeff& CG){
			
			bool res = false;
			if(j==CG.j && m == CG.m){res = true;}
			return res;
		}
};
//*************************************************************************************************
//--------------------------------------------------------------------------
/*! Overloaded "<<" operator*/
//--------------------------------------------------------------------------
inline std::ostream& operator <<(std::ostream& out, const CGCcoeff& t){
	out<<"|";DecimalToFraction(t.j1);
	out<<", ";
	DecimalToFraction(t.j2);
	out<<"; ";
	DecimalToFraction(t.m1);
	out<<", ";
	DecimalToFraction(t.m2);
	out<<" >";
	 
	return out;
}
 
double ClebschGordan(const double& j1, const double& j2, const double& m1, const double& m2, const double& J, const double& M); ///< Generalized power series representations.
double ClebschGordan(const CGCcoeff& cgc); ///< Overloaded ClebschGordan function.
std::vector<double> MQuantumNumber(const double &j); ///< Calculate the possible magnetic quantum number \f$m\$ for given spin of length \f$j\f$.  
std::vector<double> possibleJ(const double& j1, const double& j2); ///< calculate the possible total angular momenta values  
void ListOfAllCGCs(const double& j1, const double& j2); ///< calculate all Clebsch-Gordan Coefficients for addition of two angular momenta. 
std::map<CGCcoeff, std::vector<CGCcoeff>>  CGCcoeffMap (const double& j1, const double& j2); ///< store Clebsch-Gordan Coefficients as a std::map container. 
void CoupledStates(const double& j1, const double& j2); ///< List the states of the coupled system.
#endif
