//=================================================================================================
/*!
//  \file utilities.cpp
//  \brief "utilities.h"functions definitions.      
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
//#include"../include/utilities.h"
#include"utilities.h"
#include <sstream>
 
 
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
/*! Function to convert decimal to fraction  
*  	    
* @param decimal_number.    
* @return \f$\frac{A}{B}\f$ format
*/
void DecimalToFraction(const double& decimal_number ) 
{
        //-------check the sign of the input number to select the sign of the final output.
	int signdec  = decimal_number > 0 ? 1 : -1; 
	std::string plusorminus="";

	if(signdec==-1) {
		plusorminus="-";
	}
	//------ if the number in not integer and not zero or +1/-1 start the procedure to write it in fraction form 
	if(!IsNumber(ToString(std::abs(decimal_number))) && decimal_number!=0 && decimal_number!=1.  && decimal_number!=-1. ) 
	{
	 
		double z = decimal_number*decimal_number;
                //-- if the square of the number z is an integer, then it can be written as + or - square root of z^2.  
		if(IsNumber(ToString(z))) 
		{
			std::cout<<plusorminus+"√"<<z;
		}

		else if (!IsNumber(ToString(z))) //- if the square of the number z is not an integer, proceed to write it as fraction.
		{ 
			int cycles = 10;
			double precision = 5e-4;  
			double number = z;

			int sign  = number > 0 ? 1 : -1; //----check the sign again but for different reason. 
			number = number * sign; //----abs(number);
			double new_number, whole_part;
			double decimal_part =  number - (int)number; //--- exclude the integer on the left or the floating point "."
			int counter = 0;

			std::valarray<double> vec_1{double((int) number), 1}, vec_2{1,0}, temporary;

			while( (decimal_part > precision)  & (counter < cycles) )
			{
				new_number = 1 / decimal_part;
				whole_part = (int) new_number;

				temporary = vec_1;
				vec_1 = whole_part * vec_1 + vec_2;
				vec_2 = temporary;

				decimal_part = new_number - whole_part;
				counter += 1;
			}
                        
			if(IsNumber(ToString(sqrt(sign * vec_1[0]))) && IsNumber(ToString(sqrt(vec_1[1]))))  //--if both numerator and denominator square roots are integers, evaluate them directly. 
			{
				std::cout<<plusorminus<<sqrt(sign * vec_1[0])<<'/'<< sqrt(vec_1[1]);
			} 
			
			//- square root of denominator not an integer, write "√denominator" explicitly 
			else if(IsNumber(ToString(sqrt(sign * vec_1[0]))) && (!IsNumber(ToString(sqrt(vec_1[1])))) )
			{
				std::cout<<plusorminus<<sqrt(sign * vec_1[0])<<'/'<<"√"<< vec_1[1];
			}
			//- square root of the numerator is not an integer, write "√numerator" explicitly  
			else if( !IsNumber(ToString(sqrt(sign * vec_1[0]))) && (IsNumber(ToString(sqrt(vec_1[1])))) )
			{
				std::cout<<plusorminus+"√"<< sign * vec_1[0]<<'/'<< sqrt(vec_1[1]);
			}
			//- square root of both numerator and denominator not an integer, write "√(numerator/denominator" explicitly
			else 
			std::cout<<plusorminus+"√("<< sign * vec_1[0]<<'/'<< vec_1[1]<<")";
	 
		}
	}

	else std::cout<<decimal_number; //<------ if the number in an integer or equal 0, 1 or -1, write it directly as it is.
}



std::string DecimalToFraction_S(const double& decimal_number ) 
{
        //-------check the sign of the input number to select the sign of the final output.
	int signdec  = decimal_number > 0 ? 1 : -1; 
	std::string plusorminus="";
	std::stringstream outss ;

	if(signdec==-1) {
		plusorminus="-";
	}
	else{
		plusorminus="+";
	}
	//------ if the number in not integer and not zero or +1/-1 start the procedure to write it in fraction form 
	if(!IsNumber(ToString(std::abs(decimal_number))) && decimal_number!=0 && decimal_number!=1.  && decimal_number!=-1. ) 
	{
	 
		double z = decimal_number*decimal_number;
                //-- if the square of the number z is an integer, then it can be written as + or - square root of z^2.  
		if(IsNumber(ToString(z))) 
		{
			//std::cout<<plusorminus+"√"<<z;
			outss<<plusorminus+" \\sqrt{ "<<z<<" }";
		}

		else if (!IsNumber(ToString(z))) //- if the square of the number z is not an integer, proceed to write it as fraction.
		{ 
			int cycles = 10;
			double precision = 5e-4;  
			double number = z;

			int sign  = number > 0 ? 1 : -1; //----check the sign again but for different reason. 
			number = number * sign; //----abs(number);
			double new_number, whole_part;
			double decimal_part =  number - (int)number; //--- exclude the integer on the left or the floating point "."
			int counter = 0;

			std::valarray<double> vec_1{double((int) number), 1}, vec_2{1,0}, temporary;

			while( (decimal_part > precision)  & (counter < cycles) )
			{
				new_number = 1 / decimal_part;
				whole_part = (int) new_number;

				temporary = vec_1;
				vec_1 = whole_part * vec_1 + vec_2;
				vec_2 = temporary;

				decimal_part = new_number - whole_part;
				counter += 1;
			}
                        
			if(IsNumber(ToString(sqrt(sign * vec_1[0]))) && IsNumber(ToString(sqrt(vec_1[1]))))  //--if both numerator and denominator square roots are integers, evaluate them directly. 
			{
				//std::cout<<plusorminus<<sqrt(sign * vec_1[0])<<'/'<< sqrt(vec_1[1]);
				outss<<plusorminus<<" \\frac {"<<sqrt(sign * vec_1[0])<<" }{ "<< sqrt(vec_1[1])<<" } ";
			} 
			
			//- square root of denominator not an integer, write "√denominator" explicitly 
			else if(IsNumber(ToString(sqrt(sign * vec_1[0]))) && (!IsNumber(ToString(sqrt(vec_1[1])))) )
			{
				//std::cout<<plusorminus<<sqrt(sign * vec_1[0])<<'/'<<"√"<< vec_1[1];
				outss<<plusorminus<<" \\frac { "<<sqrt(sign * vec_1[0])<<" }{ "<<" \\sqrt { "<< vec_1[1]<<"}}";
			}
			//- square root of the numerator is not an integer, write "√numerator" explicitly  
			else if( !IsNumber(ToString(sqrt(sign * vec_1[0]))) && (IsNumber(ToString(sqrt(vec_1[1])))) )
			{
				//std::cout<<plusorminus+"√"<< sign * vec_1[0]<<'/'<< sqrt(vec_1[1]);
				outss<<plusorminus+" \\sqrt{ \\frac{ "<< sign * vec_1[0]<<" }{ "<< sqrt(vec_1[1])<<"} }";
			}
			//- square root of both numerator and denominator not an integer, write "√(numerator/denominator" explicitly
			else {
				//std::cout<<plusorminus+"√("<< sign * vec_1[0]<<'/'<< vec_1[1]<<")";
				outss<<plusorminus+" \\sqrt{ \\frac{ "<< sign * vec_1[0]<<" }{ "<< vec_1[1]<<" }} ";
			}
		}
	}

	else {
		std::cout<<decimal_number; //<------ if the number in an integer or equal 0, 1 or -1, write it directly as it is.
		outss<<decimal_number;
	} 
	return outss.str();
}

/*!*@param complex_number is a complex variable with "double-type" real and imaginary parts.
*@param numerical_flag is boolean variable to switch between numerical an symbolic output.
*/
void ComplexNumPrint( std::complex<double> complex_number, bool numerical_flag)
{
	double real_part = std::real(complex_number); // take the real part of the input
	double imaginary_part = std::imag(complex_number);   // take the imaginary part of the input
	if( real_part != 0 && imaginary_part != 0 )
    	{
        	if( imaginary_part < 0 )
        	{
            		if(numerical_flag) {
            			std::cout<<real_part<<imaginary_part<<"i"<<"\t";
            		}
            		
            		else { 
		    		DecimalToFraction(real_part);
		    		DecimalToFraction(imaginary_part);
		    		std::cout<<"i"<<"\t";
            		}
        	}

        	else if( imaginary_part > 0 )
        	{
            		if(numerical_flag) {
            			std::cout<<real_part<<"+" <<imaginary_part<<"i"<<"\t";
            		}
            		
            		else {
		    		DecimalToFraction(real_part);
		    		std::cout<<"+";
		    		DecimalToFraction(imaginary_part);
		    		std::cout<<"i"<<"\t";
            		}
        	}
	}
   	else if (imaginary_part == 0 )
    	{   
        	if(numerical_flag) {
        		std::cout<<real_part<<"\t";
        	}
        	
        	else {
			DecimalToFraction(real_part);
			std::cout<<"\t";
        	}
           
    	}
    	else if( real_part == 0 )
    	{
        	if(numerical_flag ){
        		std::cout<<imaginary_part<<"i"<<"\t";
        	}
        	
        	else {
			DecimalToFraction(imaginary_part);
	    		std::cout<<"i"<<"\t";
    		}
    	}    
}
//--------------------------------------------------------------------------
/*!\brief Function to check if the input is an integer. */
//--------------------------------------------------------------------------
bool IsNumber(const std::string& str) 
{
	return str.find_first_not_of( "0123456789" ) == std::string::npos;
}
//---------------------------
bool validInteger(const double& x)
{
	return static_cast<int>(x) - x == 0;
}
//--------------------------------------------------------------------------
/*!\brief Function to check if the input is a half integer. */
//--------------------------------------------------------------------------
bool halfInteger(const double& x)
{
	return !validInteger(x) && validInteger(2*x);
}
//--------------------------------------------------------------------------
/*!\brief  Check the physically valid (spin or orbital) angular m omentum 
 : True only if j is a nonnegative half-integer value
*/
bool validAngularMomentum(const double& x)
{
	return static_cast<int>(2*x) - 2*x == 0;
}
//------------------------------------------------------------------------------------------
//
//------------------------------------------------------------------------------------------
double SquareRoot(const double& x, const double& curr, const double& prev)
{
        return curr == prev
               ? curr
               : SquareRoot(x, 0.5 * (curr + x / curr), curr);
}
//------------------------------------------------------------------------------------------
//
//------------------------------------------------------------------------------------------
double SquareRoot(const double& x)
{
	return x >= 0 && x < std::numeric_limits<double>::infinity()
               ? SquareRoot(x, x, 0)
               : std::numeric_limits<double>::quiet_NaN();
}
//------------------------------------------------------------------------------------------
//
//------------------------------------------------------------------------------------------
double Factorial(const double& n)
{
        return n == 0? 1 : n * Factorial(n-1);
}
//------------------------------------------------------------------------------------------
//
//------------------------------------------------------------------------------------------
double FracFactorial(const double& n)
{  
	return tgamma(n+1.);
}
