//=================================================================================================
/*!
//  \file latex.h
//  \brief Generate LaTex files for results output.       
//
*/
//=================================================================================================
 
 
#ifndef LATEX_H
#define LATEX_H

//-------------------------------------------------------------------------------------------------
// Includes
//-------------------------------------------------------------------------------------------------
#include<iostream>
#include<cmath>
#include<string>
#include<map>
#include"utilities.h"
#include"cgc.h"
 
//=================================================================================================
//
//  CLASS DEFINITION
//
//=================================================================================================


//*************************************************************************************************
/*! \class LaTex
* \brief Class to generate LaTex files. 
*/
class LaTex {
	private:
		
		std::ofstream ofile; ///< Output file 
		std::string file_path; ///<the output file name including the path 
	public: 
		/*!\brief Default constructor, with default value for file path/name.tex */			
		LaTex(): file_path("output/default.tex") {}
		
		/*!\brief Constructor, with input value for filename.*/
		LaTex(std::string filename): file_path(filename) {}	
		
		//method for quick start the Latex file settings.
		/*!\brief Set and initiate the LaTex typesetting document class.*/
		void BeginLaTex();
 
		/*!\brief close the Latex file document.*/
		void EndLaTex();
		//Direct typing into the Latex file with appending.
		/*!\brief Method allows us to directly write normal text or even latex commands*/
		void Typing(std::string text)
		{
			ofile.open(file_path,std::ios_base::app);
			ofile<<text;
			ofile.close();
		}
		
		/*!\brief Function transform Clebsch–Gordan Coefficients list to latex format.*/
		void TexListOfAllCGCs(const double& j1, const double& j2);
		
		/*!\brief Function transform states of the coupled system to latex format.*/
		void CoupledStates(const double& j1, const double& j2); 
};
//*************************************************************************************************

std::string  LaTexMathFraction(const double& decimal_number);

#endif
