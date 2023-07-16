//=================================================================================================
/*!
//  \file latex.cpp
//  \brief "latex.h" methods definitions.      
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
#include"latex.h"

//---------------------------------------------------------
/*! Method for quick start the Latex file settings*/
//---------------------------------------------------------
void LaTex::BeginLaTex() 
{	
	ofile.open(file_path);
	ofile<<"\\documentclass[10pt,a4paper]{article}\n";
	ofile<<"\\usepackage[utf8]{inputenc}\n";
	ofile<<"\\usepackage[T1]{fontenc}\n";
	ofile<<"\\usepackage{amsmath}\n";
	ofile<<"\\usepackage{amssymb}\n";
	ofile<<"\\usepackage{graphicx}\n";
	ofile<<"\\usepackage{braket}\n";
	ofile<<"\\usepackage{amsmath}\n";
	ofile<<"\\begin{document}\n";
	ofile.close();
}

//---------------------------------------------------------
/*!\brief close the Latex file document.*/
//---------------------------------------------------------
void LaTex::EndLaTex()
{
	ofile.open(file_path,std::ios_base::app);
	ofile<<"\\end{document}\n";
	ofile.close();
}
 
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
/*! Convert decimal_number into fraction form written in laTex eqs format.  
*  	    
* @param decimal_number fraction.    
* @return laTex \f$\frac{A}{B}\f$ format
*/
std::string  LaTexMathFraction(const double& decimal_number) 
{
	int signdec  = decimal_number > 0 ? 1 : -1;
	std::string plusorminus;
	std::string resulted_string;
	if(signdec>0) {
		plusorminus="";
	}
	else if(signdec<0) {
		plusorminus="-";
	}
	
	if(!validInteger(std::abs(decimal_number)) && decimal_number!=0 && decimal_number!=1.  && decimal_number!=-1. )
	{
	 
		double z = decimal_number*decimal_number;

		if(validInteger(z)) 
		{
			//std::cout<<plusorminus+"\sqrt{"<<z;
			resulted_string =plusorminus+"\\sqrt{"+ToString(z)+"}";
		}

		else if (!validInteger(z)) 
		{ 
			int cycles = 10;
			double precision = 5e-4;  
			double number = z;

			int sign  = number > 0 ? 1 : -1;
			number = number * sign; //abs(number);
			double new_number,whole_part;
			double decimal_part =  number - (int)number;
			int counter = 0;

			std::valarray<double> vec_1{double((int) number), 1}, vec_2{1,0}, temporary;

			while( (decimal_part > precision) & (counter < cycles) )
			{
				new_number = 1 / decimal_part;
				whole_part = (int) new_number;

				temporary = vec_1;
				vec_1 = whole_part * vec_1 + vec_2;
				vec_2 = temporary;

				decimal_part = new_number - whole_part;
				counter += 1;
			} 
			if(validInteger(sqrt(sign * vec_1[0])) && validInteger(sqrt(vec_1[1])))
			{
				resulted_string =plusorminus+"\\frac{"+ToString(sqrt(sign * vec_1[0]))+"}{"+ToString(sqrt(vec_1[1]))+"}";
			} 

			else if(validInteger(sqrt(sign * vec_1[0])) && (!validInteger(sqrt(vec_1[1]))) )
			{
				resulted_string =plusorminus+"\\frac{"+ToString(sqrt(sign * vec_1[0]))+"}{\\sqrt{"+ToString(vec_1[1])+"}}";
			}
			else if( !validInteger(sqrt(sign * vec_1[0])) && (validInteger(sqrt(vec_1[1]))) )
			{
				resulted_string =plusorminus+"\\frac{\\sqrt{"+ToString(sign * vec_1[0])+"}}{"+ToString(sqrt(vec_1[1]))+"}";
			}
			else 
				resulted_string =plusorminus+"\\sqrt{\\frac{"+ToString(sign * vec_1[0])+"}{"+ToString((vec_1[1]))+"}}";	 
		}
	}
	else resulted_string=ToString(decimal_number);//std::cout<<decimal_number;

	return resulted_string;
}
 
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
/*! Convert the calculated list of Clebsch–Gordan Coefficients 
* into laTex eqs format.  
* 	    
* @param j1 first angular momentum.	
* @param j2 second angular momentum.
*/
void LaTex::TexListOfAllCGCs(const double& j1, const double& j2)
{
	std::vector<double> J = possibleJ(j1,j2);
	std::vector<double> M;  
 
	for(auto& j : J){
		for(int i =0;i<int(2*j+1);i++){
			M.push_back(MQuantumNumber(j)[i]);
		}
	}
	ofile.open(file_path,std::ios_base::app);
 
	ofile<<"Clebsch-Gordan coefficients for system with $j_1 = ";
	ofile<<LaTexMathFraction(j1);
	ofile<<"$ and $j_2 = ";
	ofile<<LaTexMathFraction(j2);
	ofile<<"$:\n";
 
	for(auto& jj : J){
		for(auto m = -jj; m <= jj; ++m){
			for(auto m1 = -j1; m1 <= j1; ++m1) for(auto m2 = -j2; m2 <= j2; ++m2){
				if( (-jj <= std::abs(m1+m2)) && (std::abs(m1+m2) <= jj) && ( (m1+m2) == m) ){
				    	ofile<<"\\begin{align}\\nonumber\n";
					
					ofile<<"\\braket{";
					ofile<<LaTexMathFraction(j1);
					ofile<<", ";
					ofile<<LaTexMathFraction(j2);
					ofile<<"; ";
					ofile<<LaTexMathFraction(m1);
					ofile<<", ";
					ofile<<LaTexMathFraction(m2);
					ofile<<" | ";
					ofile<<LaTexMathFraction(jj);
					ofile<<", ";
					ofile<<LaTexMathFraction(m1+m2);
					ofile<<"} = ";
					ofile<<LaTexMathFraction(ClebschGordan(j1,j2,m1,m2,jj,m));
					ofile<<"\n";
					
					ofile<<"\\end{align}\n";
					ofile<<"\n";
				}
			}	
		}
	}
	ofile.close();
}
 
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
/*! Convert states the coupled system into laTex eqs format.  
* 	    
* @param j1 first angular momentum.	
* @param j2 second angular momentum.
*/
void LaTex::CoupledStates(const double& j1, const double& j2)
{	
	std::map<CGCcoeff, std::vector<CGCcoeff>> res = CGCcoeffMap(j1,j2);
	
	ofile.open(file_path,std::ios_base::app);
	
	ofile<<"The states of the coupled system $";
	ofile<<LaTexMathFraction(j1);
	ofile<<" +";
	ofile<<LaTexMathFraction(j2);
	ofile<<"$ :\n";
	 
	for(auto itr = res.begin(); itr!=res.end(); itr++) { // start to scan the map "res"
		
		ofile<<"\\begin{align}\\nonumber\n";

		ofile<< "\\ket{";
		ofile<<LaTexMathFraction(itr->first.j); 
		ofile<< ", ";
		ofile<<LaTexMathFraction(itr->first.m);
		ofile<<"}"<< " = ";   //  print keys variables |J, m > = 

		for(auto vitr = itr->second.begin(); vitr != itr->second.end(); vitr++){ //iterate over the values of the res map which are nothing but vectors holding cgcs. 
			CGCcoeff res = *vitr;
			if(ClebschGordan(*vitr)!=0){  
				
				ofile<<"{ ";
				ofile<<LaTexMathFraction(ClebschGordan(*vitr));
				
				if(vitr==itr->second.end()-1) {
					ofile<<" } \\ket{";
					ofile<<LaTexMathFraction(res.j1);
					ofile<<",";
					ofile<<LaTexMathFraction(res.j2);
					ofile<<";";
					ofile<<LaTexMathFraction(res.m1);
					ofile<<",";
					ofile<<LaTexMathFraction(res.m2);
					ofile<<"}";  //here is the real need for the overloaded operator << to print |j1, j2, m1, m2 > 
				}
				else {
					ofile<<" }\\ket{"; ofile<<LaTexMathFraction(res.j1);
					ofile<<",";
					ofile<<LaTexMathFraction(res.j2);
					ofile<<";";
					ofile<<LaTexMathFraction(res.m1);
					ofile<<",";
					ofile<<LaTexMathFraction(res.m2);
					ofile<<"} + ";
				}
			}
		}
		ofile<<"\\end{align}\n";
		ofile<<"\n";		 
	} 	
	ofile.close();
}
