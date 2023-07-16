 //=================================================================================================
/*!
//  \file utilities.h
//  \brief Provides some support to cgcCALC.        
//
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
