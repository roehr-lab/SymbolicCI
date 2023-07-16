 //=================================================================================================
/*!
//  \file utilities.h
//  \brief Provides some support to cgcCALC.        
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
 
#ifndef UTILITIES_H
#define UTILITIES_H

//-------------------------------------------------------------------------------------------------
// Includes
//-------------------------------------------------------------------------------------------------
#include<string>
#include<sstream>
#include <complex>
#include<iostream>
#include<cmath>
#include<fstream>
#include <valarray> 

//--------------------------------------------------------------------------
/*!\brief Convert numbers to string*/
//--------------------------------------------------------------------------
template <typename T>
std::string ToString(const T& numb)
{
    std::stringstream ss;
    ss << numb;
    return ss.str();
}
//--------------------------------------------------------------------------
/*! \brief Print two numbers in literal fraction form (without any manipulation)*/
//--------------------------------------------------------------------------
template <typename T1, typename T2>
std::string ToFraction(T1 numer, T2 denom)
{
    std::string res = ToString<T1>(numer);
    if(denom != 1)
    {
        res += "/";
        res += ToString<T2>(denom);
    }
    return res;
}
 

double SquareRoot(const double& x, const double& curr, const double& prev);
double SquareRoot(const double& x);
double Factorial(const double& n);
double FracFactorial(const double& n);
void DecimalToFraction(const double& decimal_number );//void DecimalToFraction(double number); ///< convert decimal to fraction
std::string DecimalToFraction_S(const double& decimal_number ) ;
bool IsNumber(const std::string& str); ///< gives True if str is an integer, and False otherwise. 
bool validInteger(const double& x);
bool halfInteger(const double& x);
bool IsNumber(const std::string& str);
bool validAngularMomentum(const double& x);
 
#endif
