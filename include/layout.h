//=================================================================================================
/*!
//  \file layout.h
//  \brief Generate cgcCALC terminal layout and main menu options.       
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
     
#ifndef LAYOUT_H
#define LAYOUT_H

//-------------------------------------------------------------------------------------------------
// Includes
//-------------------------------------------------------------------------------------------------
#include<iostream>
#include<ctime>

//=================================================================================================
//
//  CLASS DEFINITION
//
//=================================================================================================

//*************************************************************************************************
/*! \class ElapsedTime
* \brief Class to displays information about the execution time.
*/
class ElapsedTime {

  public:
	void Start(){
		start = std::clock();
	}
	void End()
	{
		std::cout<<"------------------------------------------"<<std::endl;
		duration = static_cast<double>(std::clock() - start) /static_cast<double>(CLOCKS_PER_SEC);
		
		if (duration < 60.0) {
			std::cout << "Elapsed time: " << duration << " seconds !!" << std::endl;
		}
		else {
			std::cout << "Elapsed time: " << duration/60.0 << " mins" << std::endl;
		}
	}
  private:
	std::clock_t start;
	double duration;
};
//*************************************************************************************************

//*************************************************************************************************
/*! \class ElapsedTime
* \brief Class to displays main layout and information.
*/
class message {
  
  public:
	void Info(void);
	void Name(void);
	void Main_Menu(void);
         
};
//*************************************************************************************************
#endif
