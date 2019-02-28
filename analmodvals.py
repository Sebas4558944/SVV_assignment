# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 10:59:12 2019
@author: Sorin
"""
import numpy as np
'''xloc, vz, vy, t,my, mz in up config in global coord '''
def analmodvals():
    xloc=np.array([0,
    14.9,
    29.8,
    44.7,
    59.6,
    74.5,
    89.4,
    104.3,
    119.2,
    134.1,
    149,
    149,
    175.9,
    202.8,
    229.7,
    256.6,
    283.5,
    310.4,
    337.3,
    364.2,
    391.1,
    418,
    418,
    445.2,
    472.4,
    499.6,
    526.8,
    554,
    554,
    581.2,
    608.4,
    635.6,
    662.8,
    690,
    690,
    775.1,
    860.2,
    945.3,
    1030.4,
    1115.5,
    1200.6,
    1285.7,
    1370.8,
    1455.9,
    1541,
    1541,
    1571,
    1601,
    1631,
    1661,
    1691,
    ])
    vz=np.array([0,
    0.0177009885361962,
    0.0354019770723923,
    0.0531029656085885,
    0.0708039541447846,
    0.0885049426809808,
    0.106205931217177,
    0.123906919753373,
    0.141607908289569,
    0.159308896825765,
    0.177009885361962,
    -243.999570058842,
    -243.967613240613,
    -243.935656422383,
    -243.903699604153,
    -243.871742785923,
    -243.839785967693,
    -243.807829149464,
    -243.775872331234,
    -243.743915513004,
    -243.711958694774,
    -243.680001876545,
    -207.972940132608,
    -207.940626918636,
    -207.908313704664,
    -207.876000490692,
    -207.84368727672,
    -207.811374062748,
    123.887009541191,
    123.919322755163,
    123.951635969136,
    123.983949183108,
    124.01626239708,
    124.048575611052,
    89.9842812563135,
    90.0853788485571,
    90.1864764408008,
    90.2875740330444,
    90.3886716252881,
    90.4897692175317,
    90.5908668097753,
    90.691964402019,
    90.7930619942626,
    90.8941595865062,
    90.9952571787499,
    -0.178197871169772,
    -0.142558296935817,
    -0.106918722701863,
    -0.0712791484679087,
    -0.0356395742339544,
    0,
    ])*(-1)
    vy=np.array([0,
    -0.0362924047955141,
    -0.0725848095910281,
    -0.108877214386542,
    -0.145169619182056,
    -0.18146202397757,
    -0.217754428773084,
    -0.254046833568598,
    -0.290339238364113,
    -0.326631643159627,
    -0.362924047955141,
    57.1328180784412,
    57.0672968912601,
    57.0017757040789,
    56.9362545168977,
    56.8707333297166,
    56.8052121425354,
    56.7396909553542,
    56.6741697681731,
    56.6086485809919,
    56.5431273938108,
    56.4776062066296,
    73.8931038610808,
    73.82685195434,
    73.7606000475992,
    73.6943481408584,
    73.6280962341175,
    73.5618443273767,
    -10.1142398044283,
    -10.1804917111691,
    -10.2467436179099,
    -10.3129955246507,
    -10.3792474313915,
    -10.4454993381323,
    -27.0597658014383,
    -27.2670465831899,
    -27.4743273649414,
    -27.681608146693,
    -27.8888889284446,
    -28.0961697101961,
    -28.3034504919477,
    -28.5107312736992,
    -28.7180120554508,
    -28.9252928372024,
    -29.1325736189539,
    0.365359779820622,
    0.292287823856498,
    0.21921586789238,
    0.146143911928256,
    0.0730719559641315,
    0,
    ])
    mz=np.array([0,
    0.000131872364594661,
    0.000527489458378645,
    0.00118685128135195,
    0.00210995783351458,
    0.00329680911486653,
    0.00474740512540781,
    0.00646174586513841,
    0.00843983133405833,
    0.0106816615321676,
    0.0131872364594661,
    0.0131872364594661,
    -6.5499713789182,
    -13.1122703558855,
    -19.6737096944424,
    -26.2342893945889,
    -32.7940094563251,
    -39.3528698796508,
    -45.9108706645662,
    -52.4680118110712,
    -59.0242933191658,
    -65.57971518885,
    -65.57971518885,
    -71.236139700747,
    -76.8916852932238,
    -82.5463519662807,
    -88.2001397199175,
    -93.8530485541342,
    -93.8530485541342,
    -90.4828824349038,
    -87.1118373962533,
    -83.7399134381828,
    -80.3671105606923,
    -76.9934287637817,
    -76.9934287637817,
    -69.3314647263194,
    -61.6608972837573,
    -53.9817264360951,
    -46.2939521833331,
    -38.5975745254711,
    -30.8925934625092,
    -23.1790089944474,
    -15.4568211212856,
    -7.72602984302396,
    0.0133648403377791,
    0.0133648403377791,
    0.00855349781621051,
    0.00481134252148863,
    0.00213837445401133,
    0.000534593613437551,
    0,
    ])
    my=np.array([0,
    0.000131872364594661,
    0.000527489458378645,
    0.00118685128135195,
    0.00210995783351458,
    0.00329680911486653,
    0.00474740512540781,
    0.00646174586513841,
    0.00843983133405833,
    0.0106816615321676,
    0.0131872364594661,
    -0.027037841572658,
    1.50895370476982,
    3.04318273117713,
    4.57564923764927,
    6.10635322418623,
    7.63529469078802,
    9.16247363745464,
    10.6878900641861,
    12.2115439709823,
    13.7334353578434,
    15.2535642247694,
    15.2535642247694,
    17.2625556238591,
    19.2697449710855,
    21.2751322664485,
    23.2787175099481,
    25.2805007015845,
    25.2805007015845,
    25.0044923529723,
    24.7266819524969,
    24.447069500158,
    24.1656549959559,
    23.8824384398904,
    23.8824384398904,
    21.5708325729244,
    19.2415871114314,
    16.8947020554114,
    14.5301774048643,
    12.1480131597901,
    9.74820932018891,
    7.33076588606065,
    4.89568285740532,
    2.44296023422292,
    -0.0274019834865307,
    -0.0274019834865307,
    -0.0175372694313709,
    -0.00986471405512201,
    -0.00438431735780709,
    -0.00109607933943145,
    3.46389583683049E-14,
    ])
    t=np.array([0,
    -0.00125208796544524,
    -0.00250417593089047,
    -0.00375626389633571,
    -0.00500835186178094,
    -0.00626043982722618,
    -0.00751252779267141,
    -0.00876461575811665,
    -0.0100167037235619,
    -0.0112687916890071,
    -0.0125208796544524,
    -0.0125208796544524,
    -0.0147813606122025,
    -0.0170418415699526,
    -0.0193023225277027,
    -0.0215628034854528,
    -0.023823284443203,
    -0.0260837654009531,
    -0.0283442463587032,
    -0.0306047273164533,
    -0.0328652082742035,
    -0.0351256892319536,
    3.05353515161855,
    3.05124946083599,
    3.04896377005344,
    3.04667807927088,
    3.04439238848832,
    3.04210669770576,
    3.04210669770576,
    3.0398210069232,
    3.03753531614065,
    3.03524962535809,
    3.03296393457553,
    3.03067824379297,
    0.0841167821080995,
    0.0769655951376707,
    0.0698144081672418,
    0.062663221196813,
    0.0555120342263842,
    0.0483608472559554,
    0.0412096602855265,
    0.0340584733150977,
    0.0269072863446689,
    0.0197560993742401,
    0.0126049124038112,
    0.0126049124038112,
    0.0100839299230491,
    0.00756294744228692,
    0.00504196496152431,
    0.00252098248076216,
    0,
    ])
    return xloc/1000, vz*1000, vy*1000, t*1000,my*1000,mz*1000