#include<iostream>
#include<vector>
#include <memory>
#include <ctime>
#include <tuple>
#include "cgc.h"
#include <cstring>
#include <pybind11/pybind11.h>
#include <pybind11/stl_bind.h>
using namespace std;
namespace py = pybind11;
PYBIND11_MAKE_OPAQUE(std::vector<int>);
PYBIND11_MAKE_OPAQUE(std::vector<double>);



int JUST_PRINT = 0;

class point{
public:
    int i,j;
    vector<weak_ptr<point>> conn;
    
    point(int m,int n){
        this->i = m;
        this->j = n;
    }
    void tracePrev(vector<int> &plc, vector<vector<int>> &ad ){
        if(this->conn.size() == 0){
            plc[this->i] = this->j;
            vector<int> new_plc(plc.size());
            copy(plc.begin(),plc.end(),new_plc.begin());
            if(JUST_PRINT){
                for(auto i : plc){
                    cout<<i<<" ";
                }   
                cout<<endl;
            }
            else{
                ad.push_back(new_plc);
            }
        }
        for (int i = 0; i < this->conn.size() ;i++){
            plc[this->i] = this->j;
            auto sharedCon = this->conn[i].lock();
            sharedCon->tracePrev(plc,ad);
        }
    }
    ~point(){
        this->conn;
    }

};

tuple< vector<vector<shared_ptr<point>>>, vector<vector<int>>> generateSTree(int n_electron){
    vector<vector<int>> spoint;
    vector< vector < shared_ptr<point> > > s_point;
    for(int i = 0; i < n_electron + 1; i++){
        vector<int> bp;
        vector< shared_ptr<point>> bp_;
        for(int j = 0; j < i + 1; j++){
            if((i+j)%2 == 0 ){
                //cout<<j<<" ";
                bp.push_back(j);
                bp_.push_back(make_shared<point>(i,j));

            }
        }
        spoint.push_back(bp);
        s_point.push_back(bp_);
        //cout<<"bp size : "<<bp.size();
        //cout<<endl;
    }
    return make_tuple(s_point,spoint);
}

vector<vector<shared_ptr<point>>> make_m(vector<int> multiplicity){
    vector<vector<shared_ptr<point>>> mpoint;
    vector<int> min_m(multiplicity.size());
    for(int i = 0; i < multiplicity.size(); i++){
        min_m[i] = -multiplicity[i];
    }
    for(int i = 0; i < multiplicity.size(); i++ ){
        vector<shared_ptr<point>> s1p;
        for(int j = min_m[i]; j < multiplicity[i]+1; j+=2 ){
            s1p.push_back(make_shared<point>(i,j));
        }
        mpoint.push_back(s1p);
    }
    return mpoint;
}

void make_Mconnection(vector<vector<shared_ptr<point>>> &mpoint){
    for(int i = 0; i < mpoint.size(); i++){
        for(int j = 0; j < mpoint[i].size(); j++){
            if(i > 0){
                for(int k = 0; k < mpoint[i - 1].size() ; k++){
                    if(abs(mpoint[i][j]->j - mpoint[i-1][k]->j) == 1){
                        mpoint[i][j]->conn.push_back(weak_ptr<point>(mpoint[i-1][k]));
                    }
                }
            }
        }
    }
}

void GenerateConnection( vector< vector < shared_ptr<point> > > &pt){
    
    for(size_t i = 0; i < pt.size(); i++){
        for(size_t j = 0; j < pt[i].size(); j++){
            if(i > 0){
                if(j < pt[i-1].size()){
                    pt[i][j]->conn.push_back( weak_ptr<point>(pt[i-1][j]));
                }
                if(j+1 < pt[i-1].size()){
                    if(i%2 == 1){
                        pt[i][j]->conn.push_back( weak_ptr<point>(pt[i-1][j+1]));
                    }            
                }
                
            }
            if(j > 0){
                if(i %2 == 0){
                    pt[i][j]->conn.push_back( weak_ptr<point>(pt[i-1][j-1]));
                }
            }
        }
    }
}



int main_(){
    cout<<clock()<<endl;
    cout<<"fire"<<endl;
    int n_electron = 8;
    int finalS = 0;
    int mpath = 0;
    //for(int i = 4; i < 500; i+= 2){
    //    auto c1 = clock();
    //    auto point = generateSTree(i);
    //    cout<<clock()-c1<<" "<<i<<endl;
    //}

    auto [Point_,Point] = generateSTree(n_electron);
    for(auto i : Point){
        for(auto j : i){
            cout<<j<<" ";
            //cout<<clock()<<endl;
        }
        cout<<endl;
    }
    int m= 0;
    cout<<endl;
    for(auto i = Point.begin(); i != Point.end(); i++){
        int n = 0;
        for (auto j = i->begin(); j != i->end(); j++){
            //cout<<*j<< " ";
            cout<<Point_[m][n]->j<<" ";
            n++;
        }
        m++;
        cout<<endl;
    }
    cout<<endl;
    GenerateConnection(Point_);
    cout<<endl;
    vector<int> bm;
    for(int i = 0; i < n_electron+1;i++){
        bm.push_back(-1);
    }
    vector<vector<int>> bl;
    
    Point_[n_electron][finalS]->tracePrev(bm,bl);
    for(auto i : bl){
        for(auto j : i){
            cout<<j<<" ";
        }
        cout<<endl;
    }
    cout<<bl.size();
    for(mpath = 0; mpath <bl.size(); mpath++){
        int finalM = 0;
        auto c = make_m(bl[mpath]);
        make_Mconnection(c);
        
        for(finalM = 0; finalM < c[n_electron].size() ; finalM++){
            vector<int> bm2;
            for(int i = 0; i < n_electron+1;i++){
                bm2.push_back(-1);
            }
            vector<vector<int>> bl2;
            c[n_electron][finalM]->tracePrev(bm2,bl2);
            cout<<endl;
            
            cout<<"\\begin{equation}\n \\substack{\n";
            cout<<"^{"<<mpath+1<<"} \\vert "<<finalS<<":"<<c[n_electron][finalM]->j*0.5<<"\\rangle = "<<endl;
            for(int j = 0; j < bl2.size(); j++){
                double cg = 1;
                string sl = " ";
                for(int i = 0 ; i < bl2[j].size() ; i++){
                    if(i > 0){
                        cg *= ClebschGordan(bl[mpath][i-1]*0.5, 0.5 , bl2[j][i-1]*0.5,(bl2[j][i] - bl2[j][i-1])*0.5, bl[mpath][i]*0.5, bl2[j][i]*0.5 );
                        if(bl2[j][i] -bl2[j][i-1] != 1){
                            sl += "\\downarrow";
                        }
                        else{
                            sl += "\\uparrow";
                        }
                    }
                }
                cout<< DecimalToFraction_S(cg)+"\\vert"+sl+"\\rangle ";
                if(j%3 == 2){
                    cout<<"\\\\"<<endl;
                }
                else{
                    cout<<endl;
                }
            }
            cout<<"} \\end{equation}\n";
        }
    }
    return 0;
}


struct SpinConf{
    vector<int> spin;
    vector<double> CG;
};

SpinConf getSpinFunction(int n_electron, int finalS, int mpath , int finalM ){
    auto [Point_,Point] = generateSTree(n_electron);
    int m= 0;
    GenerateConnection(Point_);
    vector<int> bm;
    for(int i = 0; i < n_electron+1;i++){
        bm.push_back(-1);
    }
    vector<vector<int>> bl;
    
    Point_[n_electron][finalS]->tracePrev(bm,bl);
    auto c = make_m(bl[mpath]);
    make_Mconnection(c);
    vector<int> bm2;
    for(int i = 0; i < n_electron+1;i++){
        bm2.push_back(-1);
    }
    vector<vector<int>> bl2;
    
    c[n_electron][finalM]->tracePrev(bm2,bl2);
    vector<double> CG;
    vector<int> allSpin;
    for(int j = 0; j < bl2.size(); j++){
        double cg = 1;
        for(int i = 0 ; i < bl2[j].size() ; i++){
            if(i > 0){
                cg *= ClebschGordan(bl[mpath][i-1]*0.5, 0.5 , bl2[j][i-1]*0.5,(bl2[j][i] - bl2[j][i-1])*0.5, bl[mpath][i]*0.5, bl2[j][i]*0.5 );
                if(bl2[j][i] -bl2[j][i-1] != 1){
                    allSpin.push_back(0);
                }
                else{
                    allSpin.push_back(1);
                }
            }
        }
        CG.push_back(cg);

    }
    SpinConf ac;
    ac.spin = allSpin;
    ac.CG = CG;
    
    return ac;
}


PYBIND11_MODULE(cgcCALC, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring
    py::bind_vector<std::vector<int>>(m, "VectorInt");
    py::bind_vector<std::vector<double>>(m, "VectorDouble");
    py::class_<SpinConf>(m, "SpinConf")
        .def(py::init<>())
        .def_readwrite("spin", &SpinConf::spin)
        .def_readwrite("CG", &SpinConf::CG);
    m.def("SpinFunc", &getSpinFunction, "A function that adds two numbers");
	m.def("decimalToFraction",&DecimalToFraction_S,"conver to decimal to frac");
}
