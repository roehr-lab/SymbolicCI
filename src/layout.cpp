//=================================================================================================
/*!
//  \file layout.cpp
//  \brief Provides member functions definitions for the layout classes.
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
#include <stdio.h>
#include<unistd.h>
#include<iomanip>
#include"layout.h"
#include"cgc.h"
#include"latex.h"
/*!-------------------------------------------------------------------------------------------
\brief Print Author information
-------------------------------------------------------------------------------------------*/
void message::Info(void)
{
	printf("\n");
	printf("===========================================================================\n");
	printf("=                 MOHAMMED MAHER ABDELRAHIM MOHAMMED 2022                 =\n");
	printf("=     UNIVERSITÀ DELLA CALABRIA, DIPARTIMENTO DI FISICA AND INFN-COSENZA  =\n");
	printf("=               VIA P. BUCCI, CUBO 31 C, I-87036 COSENZA, ITALY           =\n");
	printf("=                         mohammed.maher@unical.it                        =\n");
	printf("===========================================================================\n");
	printf("\n");
}

/*!-------------------------------------------------------------------------------------------
\brief Print the app name and version information 
-------------------------------------------------------------------------------------------*/
void message::Name(void)
{
	printf("\n");
	printf("--▂▃▄▅▆▇█▓▒░Clebsch-Gordan v1.1.0-a.1░▒▓█▇▆▅▄▃▂ --\n\n");
	printf("                 ,-----. ,---. ,--.   ,-----. \n");
	printf(" ,---.,---. ,---'  .--.//  O  \\|  |  '  .--./ \n");
	printf("| .--| .-. | .--|  |   |  .-.  |  |  |  |     \n");
	printf("\\ `--' '-' \\ `--'  '--'|  | |  |  '--'  '--'\\ \n");
	printf(" `---.`-  / `---'`-----`--' `--`-----'`-----' \n");
	printf("     `---'                                    \n");
	//printf("\n");
	printf("Symbolic Clebsch-Gordan Coefficients Calculator \n\n");
	printf("    MOHAMMED MAHER ABDELRAHIM MOHAMMED 2022  \n");
	printf("          maherali8932@gmail.com             \n\n");
	//printf("**********************************************\n");
}

//*************************************************************************************************
/*!  
* \brief cgcCALC tmain menu customization.
*/
void message::Main_Menu()
{
	int choice;
	int back;
 	std::cout.fill('-');
	lable1:  while(choice != 6)
	{
		message stamp;
		//stamp.Info();
		stamp.Name();
		double j1,j2;
		double m1,m2;
		double J,M;

		std::cout<< "-----==============[ cgcCALC Main Menu ]==============-----"<<std::endl;
		std::cout<<"[+] Select an option:\n";
		std::cout<<std::endl;
		printf("1 - Compute all the possible Clebsch-Gordan coefficients for given j1 and j2 \n");
		printf("2 - Get states of the coupled system ( j1 + j2 )\n");
		printf("3 - Compute specific Clebsch-Gordan coefficient <j1, j2; m1, m2| J, M>  \n");
		printf("4 - Generate Latex Output file\n");
		printf("5 - Clear the screen\n");
		printf("6 - Exit\n");
		std::cin>>choice;//scanf("%d", &choice);

		if((choice < 1) || (choice > 6))
			printf("\n[!!] The number %d is an invalid selection.\n\n", choice);

		else if (choice < 6)
		{  
			if(choice == 1)   
			{        
				std::cout<<"--------------------------[ Input ]---------------------------"<<std::endl;
				std::cout<<"\"j1 and j2 must be non-negative integers or half integers\"\n";
				std::cout<<"Insert j1 value:\n";
				std::cin>>j1;
				std::cout<<"Insert j2 value:\n";
				std::cin>>j2;
				
				ListOfAllCGCs(j1,j2); 
				std::cout<<std::cout.fill() << std::setw(65) <<"\n";
				std::cout<<"press [1] to back to the Main Menu"<<std::endl;
				std::cout<<"press [2] to Exit"<<std::endl;
				lable2: std::cin>>back;//scanf("%d", &back);

				switch(back){

					case 1:
					goto lable1;
					break;

					case 2:
					//std::cout<<"Bye bye!"<<std::endl;
					std::cout<<"-----======================[ Bye bye! ]======================-----"<<std::endl;
					return;

					default:
					std::cout<<"Invalid option!!\n";
					goto lable2;
				}
			}     

			else if(choice == 2) 
			{
				std::cout<<"--------------------------[ Input ]---------------------------"<<std::endl;
				std::cout<<"\"j1 and j2 must be non-negative integers or half integers\"\n";
				std::cout<<"Insert j1 value:\n";
				std::cin>>j1;
				std::cout<<"Insert j2 value:\n";             
				std::cin>>j2;
				CoupledStates(j1,j2); 
				std::cout<<std::cout.fill() << std::setw(65) <<"\n";	
				std::cout<<"press [1] to back to the Main Menu"<<std::endl;
				std::cout<<"press [2] to Exit"<<std::endl;
				lable3: std::cin>>back;//scanf("%d", &back);

				switch(back){

					case 1:
					goto lable1;
					break;

					case 2:
					//std::cout<<"Bye bye!"<<std::endl;
					std::cout<<"-----======================[ Bye bye! ]======================-----"<<std::endl;
					return;

					default:
					std::cout<<"Invalid option!!\n";
					goto lable3;
				}
			}
			
			else if (choice == 3)
			{
 
				std::cout<<"-------------------[ Input ]---------"<<std::endl;
				std::cout<<"Insert j1 value:\n";
				std::cin>>j1;
				std::cout<<"Insert j2 value:\n";
				std::cin>>j2;
				std::cout<<"Insert m1 value:\n";
				std::cin>>m1;
				std::cout<<"Insert m2 value:\n";
				std::cin>>m2;				
				std::cout<<"Insert J value:\n";
				std::cin>>J;
				std::cout<<"Insert M value:\n";
				std::cin>>M;
								
				std::cout<<"<";
				DecimalToFraction(j1);
				std::cout<<", ";
				DecimalToFraction(j2);
				std::cout<<"; ";
				DecimalToFraction(m1);
				std::cout<<", ";
				DecimalToFraction(m2);
				std::cout<<" | ";
				DecimalToFraction(J);
				std::cout<<", ";
				DecimalToFraction(M);
				std::cout<<">";
				std::cout<<" = ";
				DecimalToFraction(ClebschGordan(j1,j2,m1,m2,J,M));
				std::cout<<std::endl;
				std::cout<<std::cout.fill() << std::setw(65) <<"\n";
				std::cout<<"press [1] to back to the Main Menu"<<std::endl;
				std::cout<<"press [2] to Exit"<<std::endl;
				lable4: std::cin>>back;//scanf("%d", &back);

				switch(back){

					case 1:
					goto lable1;
					break;

					case 2:
					//std::cout<<"Bye bye!"<<std::endl;
					std::cout<<"-----======================[ Bye bye! ]======================-----"<<std::endl;
					return;

					default:
					std::cout<<"Invalid option!!\n";
					goto lable4;
				}
			}     

			else if (choice == 4)
			{
				std::cout<<"--------------------------[ Input ]---------------------------"<<std::endl;
				std::cout<<"\"j1 and j2 must be non-negative integers or half integers\"\n";
				std::cout<<"Insert j1 value:\n";
				std::cin>>j1;
				std::cout<<"Insert j2 value:\n";
			        std::cin>>j2;
				
				LaTex mypdf("output/latex_results.tex");
				mypdf.BeginLaTex();
				mypdf.TexListOfAllCGCs(j1,j2);
				mypdf.CoupledStates(j1,j2);
				mypdf.EndLaTex();
				std::cout<<"[ Your LaTex file has been saved in the output directory. ]"<<std::endl;
				std::cout<<std::cout.fill() << std::setw(65) <<"\n";
				std::cout<<"press [1] to back to the Main Menu"<<std::endl;
				std::cout<<"press [2] to Exit"<<std::endl;
				lable5: std::cin>>back;//scanf("%d", &back);

				switch(back){

					case 1:
					goto lable1;
					break;

					case 2:
					//std::cout<<"Bye bye!"<<std::endl;
					std::cout<<"-----======================[ Bye bye! ]======================-----"<<std::endl;
					return;

					default:
					std::cout<<"Invalid option!!\n";
					goto lable5;
				}
			}
			             
			else if (choice == 5) {
				int check = system("clear");
				if(check ==-1) return; 
			}   
		}	
	}
	std::cout<<"-----===================[ Bye bye! ]===================-----"<<std::endl;
}
