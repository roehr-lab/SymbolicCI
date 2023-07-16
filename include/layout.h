//=================================================================================================
/*!
//  \file layout.h
//  \brief Generate cgcCALC terminal layout and main menu options.       
//
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
