import matplotlib.pyplot as plt

ev = [3.054709528920425410e-02,-2.071335519844964140e-02,-5.077175516406443739e-02,-1.916172314343920005e-02,-3.806348320962583270e-02,-3.881629065338254581e-02,-4.020959343810594222e-02,3.167787786565631064e-02,2.439072346446716569e-02,-3.372018884564863261e-02,5.036772009883724172e-02,-8.452986501691073240e-03,-4.241680695967971898e-02,-1.073068856470825103e-02,-3.005249414942095035e-02,1.076009606280967611e-02,-7.209000618796673754e-03,1.134816239175409983e-02,2.438004286029099349e-04,2.205655393011592136e-02,-1.797657673554645466e-02,1.125707945241347790e-01,6.054592983669093709e-02,-1.755879268678147906e-02,6.303082917222847803e-03,-2.571883743629906766e-02,-1.437198594895076030e-02,-1.831459173732440451e-02,5.327205858039117670e-02,8.937743047024072907e-02,1.125587300617357771e-03,2.145087362089044547e-02,5.095393703655144019e-02,-3.267982437939628143e-02,1.031424845011242979e-02,-3.590102839090949897e-03,8.676973881551375278e-02,-5.822032075902386361e-02,-6.123239937042061765e-02,4.594933373634677021e-02,-8.829727600477338748e-03,6.437467602249618767e-03,-1.708975456731471471e-02,1.164612889008749194e-02,8.660442929866564443e-02,-8.147965074435796137e-03,7.641390058725403001e-02,8.677560845182041502e-03,-4.183029614495333524e-03,-1.672227378107577281e-02,-9.587179302066968153e-03,7.697534613484446203e-03,-1.202258557165891417e-01,-4.153319616103598455e-02,-1.807627108037680383e-02,-4.909518219161130952e-03,-4.845148249200679352e-02,-5.500276574302877947e-02,-4.453509278133162969e-02,-2.348292942433632957e-02,-9.982621524163034707e-03,1.093946107955976431e-02,-4.405561231953631328e-03,-1.034412289961815501e-02,-8.035516077306685545e-02,6.140160141091384645e-03,-3.197476954655124881e-02,-2.346170986693928400e-04,-3.371939379443901486e-02,2.411489434655594236e-03,-1.022914418462327231e-02,-1.717996669491053367e-07,-2.166125497765112108e-06,1.662179362352778802e-05,1.188593638344542314e-04,8.421644002730129322e-03,1.343125482072104852e-02,1.449536754379066560e-03,1.051558519829386585e-04,-1.336918092964257954e-02,-1.769431620124482275e-03,-3.750832396700673130e-03,-1.229551046974665732e-02,3.204259214682591422e-02,-2.040459974305716684e-02,-5.400618584879854443e-04,-8.959920037366817663e-03,2.681944943033801390e-02,-2.348351910511576116e-02,-5.488086481665665345e-02,1.977163713974159406e-03,3.589313284370425870e-04,-7.809082363995134611e-05,3.676673788582128510e-03,-2.107162514793355784e-02,-4.972003803776140277e-03,1.984919673634018278e-02,-5.211160934872152185e-03,1.629751675460029345e-02,8.252424481241969409e-03,-3.571877928428875831e-02,7.894881318511811838e-03,-1.948486202100379108e-02,9.358826693010351139e-03,8.846813475613272970e-03,5.077135175070538776e-03,5.508663627028515496e-03,-9.550118045350580731e-03,-2.643197040768666562e-03,-3.465505968363729282e-03,1.029282922348250797e-03,-9.656522859325604446e-03,4.811016738478332729e-03,-3.668887495518228896e-03,2.140915286797904615e-03,5.432608484878313944e-03,1.106560412922447459e-02,1.767565705579121843e-03,-2.038691755900673246e-03,-9.729123686163134235e-03,2.911368526299099035e-03,-6.522040724010904830e-03,8.234547642029420994e-03,1.881039004557064943e-03,-1.023143674879620560e-02,-1.299183060931947097e-02,3.111217305077931122e-03,6.745850922767838986e-03,-1.379350472417687108e-03,-4.611913345281189874e-02,-9.812598201379264459e-03,-6.064421594049150543e-05,1.987927320895837777e-02,1.048008052108374269e-03,-8.681568208632679459e-03,2.293105052233294569e-02,-8.737736103103902223e-04,1.834593649887731465e-02,1.649616615335525865e-02,-2.721974808999460746e-02,7.239681785639731420e-05,2.849946759539064792e-03,-4.160208791643957293e-03,7.988043108402701972e-03,3.093020338197812955e-02,-3.570879732751305186e-02,-2.549305514892210092e-02,-1.174807150315908787e-02,-8.678270969837869817e-03,8.781797907342276874e-03,3.295101729188449485e-02,-8.324003331835180602e-04,-1.391596557252569935e-02,-2.423028563642056279e-02,-2.568438195237984431e-02,-5.612076069762743022e-03,-3.371654565808775844e-02,1.367658477118939390e-02,2.772118023298417167e-02,-1.362408933551347012e-02,1.096954512507784113e-01,-2.525542169095805825e-02,-5.137817388249876077e-02,2.018667460347263118e-02,-2.034405695436970751e-02,-2.585806522398157586e-02,2.960110657086437625e-04,1.307947291125765091e-02,-1.398805713389794300e-02,-9.857906295968096866e-03,1.019285714827478442e-03,-1.755376668600455714e-02,1.034270514168407398e-03,8.354637513805535272e-04,1.429829497248383437e-02,-2.991514879748838340e-02,1.099645310053242245e-02,9.235230127289439928e-03,-7.736033201271793301e-03,1.491832090338241629e-02,-4.607657331657051027e-03,-2.358803524019175302e-03,7.577680536542379802e-04,2.214222370607310530e-02,8.146799973452594282e-03,1.935719461677524664e-02,-2.970981657393502191e-03,-3.864862209024838569e-02,1.078282122635104180e-03,1.369902162176864745e-02,-9.970168136355764960e-03,3.603371355733156478e-02,-1.200735236583405988e-02,3.668538186539284721e-03,1.484336644288026912e-02,3.134400134111663908e-03,-1.240774933745398103e-03,-1.478033677028026127e-02,2.405584663920255252e-03,-4.993387745258943272e-03,1.511698196594185063e-02,-4.339488338987351930e-03,-1.027764215069481429e-02,-1.043086996825050815e-02,-1.145407368212460284e-03,-1.975158793707502275e-02,8.366406536204777688e-04,-1.600012728190482875e-02,1.059152952151446933e-02,1.916653315924866235e-02,-2.615506815909369662e-02,2.364284966354158937e-03,-3.915160256987945675e-03,-1.936526279895156577e-02,-2.660318712770420174e-02,1.752162834192660251e-02,2.954236789849378018e-03,6.138760079601176395e-03,-6.991807788092139347e-03,-4.615359904451152295e-02,1.106850052135483365e-03,-1.848713621426067641e-02,1.568222080767805657e-02,1.190516475611737290e-02,7.091567392741361144e-03,-6.780751693479027467e-03,-1.142407545628945642e-02,4.123275500779998229e-03,1.102165721990749220e-02,1.156194824399496665e-13,-1.186023821607307821e-02,-2.853504756728380241e-03,-2.269483475900987979e-03,-4.390182399876517601e-03,-1.979821727455199973e-06,-3.866476687264317706e-03,-5.183418694674217422e-04,-5.744299635455740564e-03,-2.095089017905889077e-03,1.783442072305147300e-02,-3.106028860880584962e-03,2.588412195174080374e-02,2.623779648958201455e-02,1.918643037196267331e-02,1.297654984544644244e-02,-7.452233681941544848e-03,-1.871458615553063705e-03,-4.921814223692720647e-03,-1.871546608457492350e-02,-1.540641068726822556e-02,-4.225978778304684963e-02,6.434804925441075900e-03,1.426537814602600943e-02,-1.536041090847866351e-02,6.094046496219375150e-03,-2.597606118723816762e-02,-4.673952868800713978e-02,1.186628111626977962e-02,-4.424623551436937703e-03,1.763968150795101105e-03,5.043607933770062439e-03,2.332151509397545168e-03,-3.223010448892863530e-03,9.107773233054977657e-03,1.899708931721999852e-02,5.019346990152095782e-03,-2.690946591519840017e-02,-2.177254703951466558e-02,1.397401400953190292e-03,2.420944998529920081e-02,-2.286939391076870526e-02,-9.877283607446088812e-03,-1.522760410142613196e-14,2.943415109304824834e-02,9.542821002620584248e-03,2.420172707782433652e-02,1.272781772761051762e-02,-2.014601437848297094e-02,2.544489480286878796e-02,-1.375038066169247467e-02,-5.516680090079694940e-03,-2.681564715035986840e-02,-1.168006806620566426e-02,-5.901284562140770261e-03,1.135730575051816134e-02,-5.255019107083418878e-02,2.685743929565089991e-02,-1.623368650458887740e-03,5.364721042918735305e-02,3.531052595772474906e-02,-7.408067398614911862e-03,-3.930590653650204358e-04,2.845609360413217746e-03,-3.279950033370627321e-02,5.990934771592933486e-03,-1.128859735799607814e-02,-3.765669128992731041e-02,-4.045143810072994450e-02,-6.221069607080809312e-03,-1.071466308193729736e-03,-7.984649508936200735e-02,1.102259197352058531e-02,1.100765465600663309e-02,2.288800717233288942e-02,9.700528962279552411e-04,6.205739973766354056e-04,-9.062078735410037658e-04,2.466360034440343366e-02,-3.385888113998657134e-02,6.250490766968628403e-03,8.109605947557430722e-03,-3.080728804083915362e-03,-3.431428997625429744e-02,1.404753961720261145e-02,1.093840342637929751e-02,-7.710185302623602521e-02,-8.017377257280694156e-03,2.842934898176802117e-02,2.732104226883161346e-02,-4.493792591827547832e-03,2.382008573637732496e-02,4.222796020216451618e-02,-2.535454467394019154e-02,-4.071229927986360492e-02,1.834969347580909724e-02,-7.794740019991615657e-03,-4.706042949099612654e-02,8.412092775932661359e-03,8.221045453721800844e-02,1.984374720183154986e-02,-5.374316789625611934e-02,4.381570301210974128e-03,4.330172984809022019e-02,1.869439736116011719e-02,1.206111886487096739e-02,2.756975216373136126e-02,-5.249898851258333159e-03,-5.438239491430829284e-03,2.128585604272799012e-02,2.065770038780770021e-02,2.549425856513422989e-02,1.975779258616692721e-02,2.870450844222044440e-02,3.475170747300905527e-02,2.894230635696752249e-02,-5.172627425881237695e-02,-3.523383435715170264e-03,1.004620284845171158e-01,-1.423916237148290832e-02,9.854379785385589813e-03,-1.480179573169625347e-02,5.294937111309032385e-02,-2.624259989727049935e-02,2.155609710458633241e-02,5.765804612027089493e-02,5.559210800166199985e-03,2.736354460180652828e-02,-7.053354214207506294e-03,-8.055745616804931009e-02,-5.802863679601418662e-03,-2.925586368325790165e-02,3.359066565596993681e-03,-1.159802796674519638e-02,7.233166958319332818e-02,-3.802419709881536825e-03,3.329016168185274654e-02,-5.118824986547866086e-03,1.738477413818515990e-02,-6.839543295522128308e-02,-8.584733481703582178e-03,8.261767300914669640e-03,-2.463500354001149292e-02,3.900199199155888422e-03,-3.303760261746815224e-02,3.649496135253839368e-02,4.424314781101312821e-02,6.351472822945303850e-04,2.115411445648718650e-02,-2.596760760158262418e-02,3.565833833907855466e-02,-5.761807854431788209e-03,2.504775864245458502e-03,4.755050552007975169e-03,-4.549568949514997546e-02,1.236159327181899324e-03,2.754885140250823081e-02,-1.755850234853505859e-02,-1.243717712962461724e-02,4.334773649573642369e-03,1.338806718495571223e-02,-1.058163385279686786e-02,6.498203336677584041e-02,-2.486972093895723891e-13,-2.023047819172208026e-14,8.431327255126965764e-15,1.342265595444511357e-02,-2.927109606006362413e-02,4.705486583370978998e-02,7.394656317206003103e-03,3.744681903972801873e-02,2.098240008422722069e-03,-1.757006948533834656e-02,1.420877228081834920e-02,-1.562655820749462438e-02,4.342629029253044365e-02,-7.534237395018883975e-03,6.809649886131248497e-02,-1.344465112627132863e-02,-5.274117535066323581e-02,3.051077494984445958e-15,-7.480749333580767884e-16,-2.415105272721300086e-02,1.250746317242256746e-02,3.331571597721024869e-14,-9.675438160449533614e-03,5.827700074946104772e-03,-6.760080836748946082e-03,-2.362989265980090098e-02,-7.072779743028409505e-02,5.998136035283425233e-02,2.013665596170362282e-02,5.136963459730987946e-02,-2.380702964397382257e-02,6.258421263849579808e-02,7.877513546598736982e-02,1.106166582361788053e-01,-1.034665571059983774e-01,3.537710564936493579e-02,-5.314277603145755452e-02,3.255834487000240467e-03,7.579512144302630772e-14,-2.398850036457128086e-14,-4.098373864122271948e-02,-5.486219000260709328e-02,-8.296054035906191837e-03,1.539559834690048569e-02,-2.096969423864255416e-02,2.356997282519980239e-02,-5.940906832106849624e-14,7.813610685902254438e-02,5.699065322447940257e-02,3.157377852826549064e-02,2.447805023412723095e-03,4.477073463252573965e-02,6.682490679938539457e-02,2.228047695060774054e-03,-1.775694197800164673e-02,3.073846054112337051e-02,-3.638550565201643244e-02,6.405310550499063171e-02,-5.863967336508646433e-02,2.542128218897552958e-02,-3.153570902821276750e-02,2.064028444122043005e-02,5.614246534599400679e-02,5.697909470558223249e-02,-8.437236632034463696e-03,-4.866861734573468823e-02,-8.165806532175767796e-02,-1.813155794835814502e-02,3.199713984483838064e-02,5.781903438744753071e-02,-8.105452441285793033e-04,8.422400103357229051e-03,-2.652518347803559107e-02,-2.519387627014796696e-02,-1.637481560596086919e-02,-9.990314205685836557e-03,-9.798038612660799063e-03,5.991119680859991609e-02,3.199053187294044476e-02,-1.791048121034618038e-02,-3.501352913808654377e-02,-5.224266053068499227e-03,4.044039286559957674e-02,4.399358198141239268e-02,3.290907107290173828e-02,-5.111397596099614971e-02,-3.250036127711898593e-02,8.839555234411041601e-03,1.005389989935929484e-01,-1.082643957722696608e-02,7.060495080254648725e-02,-6.073175533523817587e-02,-1.156602364717922160e-02,2.287812699646338613e-02,-6.730072265686585717e-03,7.970495818765079010e-02,-4.121713718466242515e-02,-8.394481339385716223e-02,1.724031255735682111e-02,-3.903941538071177553e-02,-4.621413329860403491e-14,1.361980970730536426e-13,1.235961744136240499e-13,3.994835955758069125e-14,5.753625909280249149e-14,-3.289003242300796159e-02,6.156452389672167555e-03,-5.795926931705685549e-03,-1.564259591400802380e-03,2.940030028410220084e-02,1.387759222679997226e-02,1.262492608767237616e-02,-3.508411957759639301e-03,6.378300626556343209e-03,7.369708565033866449e-14,4.328706816890690728e-02,1.796601267866984250e-02,-1.148645157000169337e-01,7.508844884940970348e-14,1.552828739161105781e-02,3.003983283318200498e-03,3.593499136040124303e-02,4.748051059819262398e-02,-2.968505879868677672e-02,-2.065700759878272633e-02,5.837611382155454345e-03,-8.393747256011796845e-03,-5.090101995755166343e-15,5.332315859361354574e-14,-8.042212177906482061e-14,4.252897863717262269e-13,1.529469307689769637e-02,-2.075893416789148169e-02,-1.280336448495977310e-02,3.139890586300034259e-02,6.643927276875868204e-14,8.395229969857245907e-15,1.640089322388910836e-02,2.021457948945293293e-02,-1.239511530430692043e-04,3.699257128140522044e-02,6.869087075393658613e-03,-3.246054841423982179e-02,-1.907042216553131442e-02,-1.087267154643124312e-03,-3.928816610268443324e-03,-3.258499996961450494e-14,-5.519934464273444639e-15,5.825888293169105905e-14,-8.904135279029962463e-14,-7.235026392683465820e-14,-2.314749045453032729e-15,-1.504946069489498967e-14,-1.538037840140177541e-14,-6.147546045935328024e-02,5.635753466726184900e-03,-1.450011517673499908e-02,1.222568736897225276e-02,1.113056203804276075e-14,-5.587508337645189705e-15,1.438836707007194916e-13,3.297971026661510393e-14,-7.894404918343932848e-03,-4.986914459681272977e-15,4.182188159880653785e-15,1.933802764682772055e-03,3.948004864191188151e-02,3.574347897512967359e-02,-5.590923199427225848e-03,-7.903517536004581526e-03,2.702528564483526116e-02,9.592515012504448241e-03,9.897636353588758554e-03,2.057784562515897406e-02,3.132741222768006123e-02,1.937346172917417341e-14,3.477796483435226544e-14,-1.129032264114600539e-14,-2.119835156571869955e-14,6.339434864285846096e-14,1.301383569755622256e-14,2.537962849595819595e-02,-5.799184015792829827e-02,4.448773594272313614e-02,4.911039099444558520e-02,2.174483161883568082e-14,-3.056904811074304658e-15,-4.038787890359305519e-15,-1.033051938102704779e-14,5.678564728435196237e-15,1.183544108438601801e-14,2.343019622917559487e-15,-1.062027496195153223e-14,1.663511297981573008e-14,3.306610916844549886e-14,-3.112597644136282429e-14,-1.123357381523674980e-02,-1.947112932808869531e-02,-2.145125635973545511e-02,-2.590558192141906302e-02,-1.529699942564343232e-02,4.843703185914458725e-03,-1.071782180732257748e-02,-2.457264216110697426e-14,-1.763413641452723740e-13,-4.046754081647124324e-14,-1.050272496424923032e-14,-1.704585270686783506e-14,-9.629660475263649820e-16,2.089578751804045919e-14,-1.961508129124269490e-13,2.190091777146973042e-14,-4.098780801669284668e-14,-1.479629844216842722e-13,-2.233834248121902318e-16,4.620994500456226022e-15,-6.206797030298208062e-14,1.751654450763095882e-14,-2.264377071535977324e-14,-2.455514907646901206e-14,-2.105186638023560209e-14,1.815125051048338632e-14,-6.933952899839660928e-15,-1.006822085095794818e-13,-7.047228896003439092e-15,4.234629662418665369e-14,2.757685290858654298e-15,-4.057097384446287559e-14,-7.676087675209934271e-14,-5.312577159138285460e-02,4.593852456926762629e-15,4.144198815140702639e-14,-6.799537931267509776e-15,-1.487140014463149802e-14,2.364398157112652596e-02,-4.773834429059557738e-02,2.681490117436193324e-02,9.598988710320402462e-03,9.612919541020854136e-03,-1.569993405570253159e-02,1.659659528776876239e-02,-5.089101606964677692e-03,-2.771687850505824904e-02,1.828880120803315357e-02,-3.110090183050429652e-15,-6.261536624938565598e-14,-1.185056617331314636e-12,-5.835219547441038412e-12,1.736712892415471594e-13,8.386732324192968868e-14,2.629315817516398623e-14,5.481760673339416273e-15,-6.067903452350542355e-14,4.528676857354206902e-14,3.463709592613906161e-13,-1.107359314461660182e-13,-9.886931674832550469e-14,-1.292383078322629677e-13,1.198647802356569397e-13,1.199750793662142166e-13,4.390750025546723482e-14,-4.163633668954023435e-14,4.101480083275004686e-15,1.226178394983358221e-14,-5.718528273716519568e-03,1.682182111637307636e-03,-2.091521859156396895e-14,2.745159092596916282e-15,-2.398998754055305500e-15,3.656069450382943425e-02,2.834040776544216971e-15,-2.398213617274825367e-14,4.425744088763520544e-15,1.974275855021689575e-14,1.156857049817512497e-14,1.716075304210347836e-14,1.680132843948482432e-02,-2.456966585819057858e-02,-1.712227363056575621e-02,3.121878929435428773e-02,-1.161128865566438996e-02,3.382504400465609376e-13,-1.359141878948761956e-13,-1.232119369692396859e-13,5.331217047441180278e-13,2.104120623173733117e-12,4.544494526339259880e-12,-7.071067811866066366e-01,2.484101598505750732e-13,-4.528469207256672606e-14,2.907766451215346029e-13,-1.005823095926809811e-12,4.662889780939140372e-14,-2.921788092191078892e-02,9.012663428458306258e-02,4.680882325649522724e-02,-1.246288259360383774e-02,-6.738249344718182099e-02,7.241534576047753299e-14,-1.769966136981692659e-14,2.517189887587091631e-14,2.543220276090718893e-02,-1.194570641536868427e-02,3.584016259758300571e-02,1.106797417203636905e-02,4.029398742890911121e-03,-2.976190145505325322e-03,-7.487070538489792670e-14,-2.810474330502454896e-16,1.862669693479801777e-14,-9.228934309790823943e-15,3.757302262447734063e-14,1.539254385384753569e-14,-6.393318582796367963e-14,-1.219155610328890188e-14,6.367799652986670693e-14,3.642083233072951666e-16,-1.808732498811190768e-14,1.000115138260624474e-15,-8.813665671237775108e-15,-2.395046786223235255e-15,1.500993575219878360e-14,-6.084271086760299902e-12,-3.192774060835012985e-16,-6.077115210311984416e-14,5.113629031891266179e-14,9.419888311699505249e-13,-8.685320158805447320e-15,-2.622901559584203366e-14,4.231428662693491327e-02,8.288444734227115594e-13,1.346126710191506912e-02,-6.327472936405306509e-14,-2.505814624371811466e-14,1.417375951990442612e-02,-9.714867925850606545e-03,-2.429466012705930188e-14,-2.718058858507094253e-13,1.017321074021696625e-13,1.485095788325621970e-12,3.094366346422440553e-14,1.203718727466526183e-14,1.601923532445077177e-14,7.976780749474741781e-15,1.540666664513959800e-13,-3.345888653724334635e-14,2.529453214581068243e-15,1.076869025994137522e-14,4.053504494622734447e-15,1.579431116752505289e-14,4.600395053603483634e-14,1.013852175996795588e-13,-9.424681460589756034e-15,-1.157706238337776828e-14,2.665810476773637902e-13,1.724189081638120597e-13,-4.037405736578188110e-14,9.461165969846011001e-15,3.844114867162022693e-14,-1.223258755380156193e-13,-8.300877751781970236e-15,3.921788785630230043e-14,2.080133303602309991e-14,-4.154722695655214557e-14,-1.183122672175923887e-14,4.913128202655534333e-15,1.590540408062049838e-14,-2.560088295152395874e-02,-1.132837477732319758e-14,-3.365449836155860454e-14,9.807823317792071691e-14,-1.173065141758207384e-14,2.083945375171528649e-15,5.641278840229355870e-14,1.345412176871927315e-14,-2.826464173414164338e-02,3.101562756396366097e-02,-3.977031142277314552e-02,2.831773412641958319e-16,9.267655425287116615e-15,-1.365438965938686224e-02,1.328121405395064221e-15,-1.568959204763259395e-15,-4.583227046140475013e-15,4.725598704517031644e-03,-4.958989620537495716e-14,3.474820635852816041e-14,1.043888446112036049e-14,-7.591589552561499249e-15,-2.212313580923410990e-15,4.415788970592561015e-14,-2.932962276190347541e-15,-5.306394201261576200e-15,1.297429446420511341e-14,-9.909587754731357929e-15,7.607674800586800048e-16,6.802572385929507686e-15,5.298721276305469358e-15,-2.621224361595228474e-14,-1.124616663014738140e-14,2.301000483459804805e-14,6.650044640320986747e-16,9.831115495021529952e-17,-2.098626733343619908e-03,-1.115821990857211297e-14,-1.003836005449622403e-14,6.106004033493791076e-15,1.219601684835734841e-02,-1.392371864672703506e-14,-1.137242208941545429e-02,1.964552553174734803e-02,5.246634519442785531e-15,-9.815932949714018593e-15,-1.801304728851065018e-02,-9.105055226579367167e-03,1.827524544015781168e-13,1.310510722485013869e-14,7.466606559076959577e-14,-5.569014118637493834e-15,-6.063967432479817658e-15,-1.574753283489003201e-14,6.235765446435787735e-14,2.622436079361921481e-14,3.325305284143740211e-14,-1.119970536452032046e-15,7.645760142049634133e-14,8.452685841398283541e-14,1.227030271915668099e-14,-6.787084565439627254e-15,-9.367020925742579872e-14,1.105833102045135799e-15,-6.605926311248610928e-16,1.169304981930544760e-14,6.517706452601962841e-15,-3.255259219315170708e-14,-2.189138341088155338e-15,-3.035386666967418560e-14,-4.025419521824219475e-15,3.277089329027119432e-15,-4.675893713804826485e-15,-8.639171120732396723e-15,3.581735684164391835e-14,-6.416311993577076328e-15,7.969319449387508665e-15,4.614412212590977721e-15,1.844538997267691483e-15,4.429092885916928850e-16,-1.419830215663707334e-14,-1.057689144016463148e-13,-1.379684032389026628e-15,-7.139996249241678211e-15,-8.251390143580074956e-15,1.170380873839796608e-14,-2.644044278171458568e-16,2.283922554019225899e-14,2.880140095671309468e-15,2.726925828315397753e-14,6.561235099484903206e-15,-1.327116182312640658e-15,7.122071445182312773e-15,5.857071542713346055e-17,1.954698286235363262e-14,9.289964391351032364e-15,3.305398462146331242e-14,-1.257274815545498989e-14,-1.292419775003682251e-14,-1.072035961967333486e-14,2.401355562451050437e-15,1.662608379948367188e-15,-1.746832566090460454e-14,-4.322894513514180779e-15,2.120561104298329530e-14,5.374982733994682689e-15,3.717160406040020574e-15,5.143297370431987584e-15,2.024899537325247817e-14,-3.026063792566640028e-15,9.221466454505828523e-15,-1.562569999815578507e-14,-3.254305698002407097e-14,1.343985638100224275e-14,-1.646110496453528430e-13,1.875333350426984748e-13,-1.983062636897559628e-14,7.391503075859293702e-16,-5.038404007553933922e-14,1.371112595967178648e-14,8.751237861838369516e-15,-9.005558293682985533e-15,5.478647003114674401e-14,5.986397838179159939e-15,5.173086256365089576e-15,1.588795071243178406e-14,7.685812332660871735e-15,-1.776044619603291632e-14,-2.534404890165879927e-15,7.699556962333670432e-15,-3.766079445426795950e-14,4.369496185260352104e-15,6.328494910769455238e-15,1.130191649305488939e-14,8.546746021723966581e-15,1.323028190377366814e-14,-2.277818551403614241e-14,-1.455370429611799322e-15,-1.899485673981076506e-15,-4.477228348069928617e-15,-9.761989860780160477e-16,1.509136945361975199e-15,-5.323959601257471804e-15,-3.350352732424656290e-15,-3.764520020965418901e-14,2.407359137825692872e-14,4.658381866504295975e-14,4.746512875123102697e-15,-1.658650735306068672e-14,-3.443733247667286492e-15,-1.221796125691484863e-14,-1.561525368077412183e-14,-2.189708319132066660e-14,1.302446768386194294e-16,-2.396764086140247768e-14,-2.191463318332651315e-14,3.941109828683942454e-15,2.609581139864916530e-15,-1.981686443931063093e-14,9.142802388306674318e-16,-1.033168317295874757e-14,1.984605017280298834e-14,7.219733787580302079e-15,1.503073579680060828e-15,-4.227392226339495029e-16,4.231046255036137912e-14,-5.645742432623328213e-15,2.385876304743649771e-14,2.209488742341859268e-14,-8.837461721565451395e-15,-1.753127064092612633e-15,-1.801423102024271896e-14,1.640853356618044610e-14,-1.451379863470918597e-14,-1.329519374982929357e-14,-2.926809760020271327e-15,-4.775886560998895136e-16]

fig = plt.figure(figsize=(9,4))
ax = plt.subplot(111)
ax.plot(ev)
plt.savefig("eVectors.png")