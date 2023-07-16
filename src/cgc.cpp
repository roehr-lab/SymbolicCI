//=================================================================================================
/*!
//  \file cgc.cpp
//  \brief "cgc.h" methods definitions.      
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

#include<iostream>
#include"cgc.h"
#include"utilities.h"

//------------------------------------------------------------------------------------------
/*!Calculate Clebsch–Gordan Coefficients using the Generalized power series representations*/ 
//------------------------------------------------------------------------------------------
double ClebschGordan(const double& j1, const double& j2, const double& m1, 
		     const double& m2, const double& J,  const double& M )
{
	if( !validAngularMomentum(j1) || !validAngularMomentum(m1) || !validAngularMomentum(j2) 
	|| !validAngularMomentum(m2) || !validAngularMomentum(J) ) 
	{
		throw std::domain_error("clebsch_gordan: all parameters must be multiples of 0.5.");
	}
	if( (validInteger(j1) && halfInteger(m1)) || (halfInteger(j1) && validInteger(m1)) ){
		throw std::domain_error("clebsch_gordan: j1 and m1 must both be integral or half integral.");
	}
	if( (validInteger(j2) && halfInteger(m2)) || (halfInteger(j2) && validInteger(m2)) ){
		throw std::domain_error("clebsch_gordan: j2 and m2 must both be integral or half integral.");
	}
	if( (validInteger(j1 + j2) && !validInteger(J)) || (halfInteger(j1 + j2) && !halfInteger(J)) ){
		throw std::domain_error("clebsch_gordan: J is no valid value for j1 and j2 combination.");
	}
	if( j1 < 0 || j2 < 0 ){
		throw std::domain_error("clebsch_gordan: j1 and j2 must be non-negative.");
	}
	if( J > j1 + j2 || J < std::abs(j1 - j2) ){
		throw std::domain_error("clebsch_gordan: J must be |j1-j2| <= J <= j1+j2.");
	}
		if( std::abs(m1) > j1 || std::abs(m2) > j2 || std::abs(M) > J ){
		throw std::domain_error("clebsch_gordan: m1 and m2 must be |m1| <= j1 and |m2| <= j2 and |m1+m2| <= J");
	}
	if( m1 + m2 != M ){
		throw std::domain_error("clebsch_gordan: m1 + m2 != M.");
	} 

 
	double numerator = (2 * J + 1) * Factorial(J + j1 - j2) * Factorial(J - j1 + j2) * Factorial(j1 + j2 - J);
  	numerator *= Factorial(J + M) * Factorial(J - M) * Factorial(j1 - m1) 
  	     		* Factorial(j1 + m1) * Factorial(j2 - m2) * Factorial(j2 + m2);
  	double denominator = Factorial(j1 + j2 + J + 1);

  	int const min = (int) std::max(0., std::max(j2 - J - m1, j1 + m2 - J));
  	int const max = (int) std::min(j2 + m2, std::min(j1 - m1, j1 + j2 - J));
  	double sum = min > max ? 1 : 0;

	for( int k = min; k <= max; ++k ){
    		sum += pow(-1., k) / (Factorial(k) * Factorial(j1 + j2 - J - k)
    			 * Factorial(j1 - m1 - k) * Factorial(j2 + m2 - k) 
    	 			* Factorial(J - j2 + m1 + k) * Factorial(J - j1 - m2 + k));
 	}
	return SquareRoot(numerator / denominator) * sum;
}
//------------------------------------------------------------------------------------------
//--------------------overloaded ClebschGordan function ----------------------
//------------------------------------------------------------------------------------------
double ClebschGordan(const CGCcoeff& cgc){

	return ClebschGordan(cgc.j1,cgc.j2,cgc.m1,cgc.m2,cgc.j,cgc.m);
}
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
/*! calculate the possible magnetic quantum number 
* \f$m\f$ for given spin of length \f$j\f$.  
*  	    
* @param j the length of the spin quantum number.    
* @return list of all possible \f$m\f$ values.
*
*/
std::vector<double> MQuantumNumber(const double &j)
{    
	double spin = j;
	std::vector<double> m_values;
	if(validAngularMomentum(spin))
	{
		for(auto i =-j; i<=j; i++)
		{       
			if(i==0){m_values.push_back(0);}
			else m_values.push_back(i);  
		}
	}
	else{
		throw std::invalid_argument("the system has physically invalid spin!.");
	}	
	return m_values;
}

//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
/*! calculate the possible total angular momenta values   
*	
* @param j1 first angular momentum.	
* @param j2 second angular momentum.     
*  	       
* @return list of all possible total angular momenta \f$J\f$ values.
*/
std::vector<double> possibleJ(const double& j1, const double& j2){

	double Jmin = std::abs(j1-j2);
	double Jmax = j1+j2;
	std::vector<double> J_values;
	if(validAngularMomentum(j1) && validAngularMomentum(j2))
	{
		for(auto i =Jmin; i<=Jmax; i++)
		{       
			if(i==0){J_values.push_back(0);}
			else J_values.push_back(i);  
		}
	}
	else{
		throw std::invalid_argument("the system has physically invalid spin!.");
	}
	return J_values;
}
 
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
/*! calculate all Clebsch–Gordan Coefficients for addition of two 
*  angular momenta.   
*	
* @param j1 first angular momentum.	
* @param j2 second angular momentum.     
*  	       
* @return print the list of all Clebsch–Gordan Coefficients.
*/
void ListOfAllCGCs(const double& j1, const double& j2)
{
	std::vector<double> J = possibleJ(j1,j2);
	std::vector<double> M;  
 
	for(auto& j : J){
		for(int i =0;i<int(2*j+1);i++){
			M.push_back(MQuantumNumber(j)[i]);
		}
	}
	std::cout<<"----------------------------------------------------------------"<<std::endl;
	std::cout<<"Clebsch-Gordan coefficients for system with j1 = ";
	DecimalToFraction(j1);
	std::cout<<" and j2 = ";
	DecimalToFraction(j2);
	std::cout<<" :"<<std::endl;
	std::cout<<"----------------------------------------------------------------"<<std::endl;
	for(auto& jj : J){
		for(auto m = -jj; m <= jj; ++m){
			for(auto m1 = -j1; m1 <= j1; ++m1) for(auto m2 = -j2; m2 <= j2; ++m2){
				if( (-jj <= std::abs(m1+m2)) && (std::abs(m1+m2) <= jj) && ( (m1+m2) == m) ){
					std::cout<<"<";
					DecimalToFraction(j1);
					std::cout<<", ";
					DecimalToFraction(j2);
					std::cout<<"; ";
					DecimalToFraction(m1);
					std::cout<<", ";
					DecimalToFraction(m2);
					std::cout<<" | ";
					DecimalToFraction(jj);
					std::cout<<", ";
					DecimalToFraction(m1+m2);
					std::cout<<">";
					std::cout<<" = ";
					DecimalToFraction(ClebschGordan(j1,j2,m1,m2,jj,m));
					std::cout<<std::endl;
				}
			}	
		}
	} 
}
 
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
/*! Store Clebsch–Gordan Coefficients as a map 
*	
* @param j1 first angular momentum.	
* @param j2 second angular momentum.     
*  	       
* @return mapping each GCcoeff to its all possible values 
* stored as vector.
*/
std::map<CGCcoeff, std::vector<CGCcoeff>>  CGCcoeffMap (const double& j1, const double& j2)
{  ///@TODO under construction 
        std::map<CGCcoeff, std::vector<CGCcoeff>> CGCs;
	std::vector<double> J = possibleJ(j1,j2);
	std::vector<double> M;  
 
	for(auto& j : J){
		for(int i =0;i<int(2*j+1);i++){
			M.push_back(MQuantumNumber(j)[i]);
		}
	}
		
	for(auto& jj : J){
		for(auto m = -jj; m <= jj; ++m){
			for(auto m1 = -j1; m1 <= j1; ++m1) for(auto m2 = -j2; m2 <= j2; ++m2){
				if( (-jj <= std::abs(m1+m2)) && (std::abs(m1+m2) <= jj) && ( (m1+m2) == m) ){
					CGCs[CGCcoeff(jj,m1+m2)].push_back(CGCcoeff(j1,j2,m1,m2,jj,m1+m2));		 
				}	
			}
		}	 
	}
	return CGCs;
}
 
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
/*! List the states of the coupled system. 
*	
* @param j1 first angular momentum.	
* @param j2 second angular momentum.     
*  	       
* @return print the list of all states of the coupled system.
*/
void CoupledStates(const double& j1, const double& j2)
{	
	std::map<CGCcoeff, std::vector<CGCcoeff>> res = CGCcoeffMap(j1,j2);
	std::cout<<"----------------------------------------------------------------"<<std::endl;
	std::cout<<"The states of the coupled system ";
	DecimalToFraction(j1);
	std::cout<<" + ";
	DecimalToFraction(j2);
	std::cout<<" :"<<std::endl;
	std::cout<<"----------------------------------------------------------------"<<std::endl;
	
	for(auto itr = res.begin(); itr!=res.end(); itr++) { // start to scan the map "res"

		std::cout <<"|";DecimalToFraction(itr->first.j); std::cout<< ", ";DecimalToFraction(itr->first.m);std::cout<<">"<< " = ";   //  print key variables |J, m > = 

		for(auto vitr = itr->second.begin(); vitr != itr->second.end(); vitr++){ //iterate over the values of the res map which are nothing but vectors holding cgcs. 

			if(ClebschGordan(*vitr)!=0){  
				
				std::cout<<"{ ";
				DecimalToFraction(ClebschGordan(*vitr));
				
				if(vitr==itr->second.end()-1){
					std::cout<<" } "<<*vitr;  //here is the real need for the overloaded operator << to print |j1, j2, m1, m2 > 
				}
				else std::cout<<" } "<<*vitr<<" + ";
			}

		}
		std::cout<<std::endl;
	} 
}
