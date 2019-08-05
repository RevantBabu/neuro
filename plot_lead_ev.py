import matplotlib.pyplot as plt

ev = [-2.062432852050939333e-02,2.694479412546955249e-02,1.164033978898088538e-02,-1.207876052263838311e-02,-3.231605108916917740e-02,-8.664535026673180276e-03,-1.132626691631962064e-02,-5.318562916424799530e-03,-2.550963488391652483e-03,1.249204573156732648e-03,-4.583289558681888365e-02,5.375878147497581590e-03,-4.538973785612255879e-04,-2.973304026698148778e-02,6.556000054722212200e-03,1.493738560130435100e-02,-3.830599159311989799e-02,-5.927824910732035733e-03,-9.844373446972205354e-04,2.428605813059570538e-03,4.707023871724252961e-03,-8.587080683067837075e-03,-4.227141191056978629e-03,2.892977899673721681e-02,2.104796606541708970e-02,1.916789140321329549e-02,-2.459497270381650388e-03,4.765458500471718949e-03,-5.069847713736537476e-03,-4.163909281325616808e-03,3.228169368971793574e-02,1.034455713392815187e-03,1.575549813829779655e-02,-4.372846693135138546e-02,1.150879927446640631e-02,-2.296084443980479436e-02,1.678822062992574651e-02,4.291209859392266374e-03,-1.481928106988128491e-02,2.200930077129984244e-02,-3.105799629322021378e-03,1.120319946918633611e-02,-2.493798874732886320e-02,-4.199434005311450391e-02,9.562356686137587006e-04,-6.617358979780114080e-03,4.018122109055095870e-02,9.533902140022240679e-03,4.353759229531935573e-03,7.674280607565814837e-03,-1.253086124572862919e-02,-1.888480158073264220e-02,5.332992996087727866e-02,5.065517085408426925e-04,-4.266760156509558435e-03,-2.965178977511192734e-02,-6.029495317373159691e-02,-1.055577034895951657e-02,-3.495436195239477045e-02,-7.266358106502938952e-03,-1.662531555599818661e-02,9.840129449512777238e-03,-5.871970703834097915e-02,-5.147544396152211287e-03,5.857203757812427802e-02,-1.230307564312536732e-02,4.582786731796144666e-03,3.443124892745139110e-02,-2.855744111527130230e-02,2.642317318385454042e-02,-2.380185726025616649e-02,3.298209695588490836e-02,-2.964417681347823047e-02,2.083218848741031845e-02,-1.125996034806343304e-01,1.817530429330821429e-02,-1.743646223063618356e-02,-5.796846973656277768e-02,-1.488068134393975492e-02,-1.563476679360230673e-03,-3.273400438198094398e-02,-4.733605974237366926e-02,-3.776144818819637122e-02,1.427963993286917796e-02,-1.885104715987879305e-03,7.798316945694793281e-07,4.441151356467246125e-02,4.179824554596902643e-04,-4.438566553377081003e-02,-2.344593961927316644e-02,1.710840892424011703e-02,1.095392978277159521e-03,-2.017957242730415105e-03,8.884530240761271888e-03,-1.028646284173929211e-03,1.143168819480862818e-02,4.472829290030581884e-02,-3.026859462762925435e-03,4.845083951915717807e-02,7.634946047476711892e-03,4.253007414000071346e-02,4.101644328739235262e-02,4.673619610391931134e-02,-5.562152168708130173e-02,-4.099057581324611760e-02,3.421663774917145517e-02,-2.963066984538970626e-03,1.506264478361070695e-04,2.467125802562656137e-02,-3.283477012502030151e-03,-2.244206918468092879e-02,2.042247941973689834e-02,-3.748397270280656723e-02,-1.451062498444495238e-02,1.807638020443199170e-02,2.625356489168897620e-02,-3.243367836386047004e-02,2.772629227359639514e-02,3.297300257942591822e-02,-3.449299666716762469e-02,6.268423139442938496e-03,-2.202298155772661539e-02,2.068030723360723272e-02,4.565265540117180443e-02,5.704208838799304862e-03,3.303529476454319241e-02,-9.463702117597094440e-03,6.794003127935419051e-03,7.167464434174007637e-03,-5.171256765960981217e-02,-9.130987398146611297e-03,1.964270503460943326e-02,2.761391384588730846e-02,-5.753412751626324484e-02,5.499335247949137251e-02,6.776456990556333285e-03,3.551715352180589980e-02,8.148665441283040739e-03,6.686120080124319243e-02,-2.564202914570008762e-02,6.971447609110911769e-02,-7.969271396858568224e-02,6.370107213099022656e-03,-4.376209453255137244e-02,2.542378490045343366e-03,1.984833237526642882e-02,3.323139004744994629e-02,-2.577058490090925261e-02,-1.035071406689586949e-02,-4.357753457798977520e-02,1.160341936891721575e-04,1.718640809356488872e-02,1.571967074181260596e-02,3.577908203398673381e-02,4.210028797494868441e-02,4.799236205894664986e-02,3.201249503071303820e-02,9.685710296745609141e-03,-3.528105516002893322e-02,-2.340334527333083267e-02,1.478828181089603643e-02,-5.930722626108663603e-02,-3.359322046910249993e-02,-2.272488316743187867e-02,-2.083624417464194009e-02,2.367815086306792466e-02,2.254214665224015673e-02,1.169161297355806803e-02,7.993960656686179000e-02,2.695797166994076677e-02,-2.746395332792319136e-02,-4.086432500367372100e-02,8.549513857277353177e-03,2.994601343824418796e-02,2.416011946343022895e-02,-1.421010532567041143e-02,4.100030599532370618e-02,-3.341135482301722803e-02,2.928304184586560596e-02,-1.411823677879175259e-02,-2.812939115578928784e-02,4.693920212686163163e-02,2.866487239925193803e-02,3.162299549792298159e-02,-1.811337134008409290e-03,3.993767718976435482e-02,3.778120517942665929e-02,1.168942967569540185e-02,3.299609036899603387e-02,6.921521455052365157e-02,9.298695044736578208e-03,2.848434583041262527e-02,4.514974062440400837e-02,3.213269785096144193e-02,2.774140930917789322e-02,2.085109299809289468e-02,-1.598238568403761647e-02,2.120366686520049754e-02,1.269300518702702781e-02,3.608032789594068507e-02,-6.801631575618057035e-02,-4.961026642375269274e-02,-1.443772812560145148e-02,-4.151081614327949143e-02,1.006286988090205649e-02,-1.482493681551202503e-04,3.429241929836254060e-02,5.358889323804853777e-02,3.847223931090114346e-02,-2.063072537021984690e-02,2.620957250306875722e-02,2.851305081037836670e-02,-2.717306576767842402e-02,-2.055841857335750662e-03,2.735988581300044520e-02,-2.797574060943138624e-02,-3.713504530818489274e-02,-4.572954380633845878e-02,3.864135600103635066e-03,-1.554749367961490158e-02,-2.326500488465454292e-02,4.340621842690225995e-02,-1.820487423123227921e-02,5.614861485064261831e-03,7.283162804136457218e-03,-6.840026861210310449e-03,-5.108128462838566058e-02,-1.312136653443712192e-02,-3.603624196074051850e-02,6.823778719120324882e-03,1.642248228897081469e-02,-4.496202353956848391e-02,-9.336787130238286339e-03,5.853512007366572928e-02,-4.148448173637054454e-02,3.395062645606847923e-02,1.534511969350237440e-02,-7.699002567024226806e-02,1.483711066259305218e-02,-9.293053017550045522e-03,-1.622088304083808483e-02,1.857596733157453398e-02,-4.654717127743932675e-03,-1.835863018363865021e-02,-4.340750616783974752e-02,2.374530903767619813e-02,7.671218038028311537e-02,4.516501195328039703e-02,-3.192203460342945415e-02,-6.465428044515077188e-02,1.846701564576868834e-02,-6.704207770710788813e-03,-5.371370352447661645e-02,5.211302155214890541e-02,9.351855237897336443e-03,3.113828359112663993e-02,3.605336198229797118e-02,-6.674214519254486125e-03,-2.949903220291339931e-02,2.117059174196299701e-02,7.987887684918859588e-02,1.819502549057553861e-02,3.483766505621081061e-02,-4.847411082089275042e-02,-3.020594950831675257e-03,2.016992920445581997e-02,3.589749359861935801e-02,-2.493981427810816956e-02,2.346023881855137036e-02,4.328108115682063189e-02,5.308925206548703417e-03,2.520520605686748031e-02,4.724503909341440377e-02,-4.626747378607855288e-02,4.964953177825569275e-02,1.281949529264678200e-02,7.192563974634960753e-04,1.327642826699528857e-02,-3.973361170502220929e-02,2.727537576759255997e-02,-3.348772307759710631e-02,3.642498002491956904e-02,2.471922162468886963e-02,8.217862108639973143e-03,-2.420290813237892594e-02,-1.015219039698462070e-02,3.891376386286886369e-02,-4.514516739542741991e-02,2.434275084331323502e-02,-2.036889693450478697e-02,-5.490463164606935835e-03,-2.866696136518187554e-02,4.534841385049642737e-02,5.787148655750201307e-03,5.525001273457789269e-02,2.889814950981734951e-02,1.880446300189757974e-02,-5.548692848677285600e-03,-1.186589116265024391e-02,2.498336988090977401e-02,-2.995464946678699433e-02,-1.466288197057641352e-02,-3.288135086222014093e-03,-2.359714171173208502e-02,1.443020947102906237e-02,1.673131892246801714e-02,1.917183340315281939e-02,-4.030563580226081272e-02,5.555449856284179477e-03,-2.651431018477547197e-02,1.480596017186910397e-02,-1.221463809427942443e-02,-8.097701620165256506e-03,-6.288568039895420757e-03,-6.639092898613927277e-03,-4.352453151880632254e-02,6.693441965457902487e-02,-8.350361316063738271e-03,-5.124540368203379936e-02,7.079773488814752880e-02,-1.516955451167586490e-02,-3.639079403887917480e-02,-4.703719286419874232e-03,5.146551357052694259e-02,-6.146786327740385615e-03,3.675689592330720623e-02,5.580064565253241987e-02,-4.962509163485058494e-02,1.188573454492252227e-02,1.104087744650891854e-03,3.697099637775319581e-02,3.785760650820707562e-02,2.218518631766001545e-02,2.412883612547813555e-02,-2.460273901292080179e-02,-3.954660997349015690e-04,-2.761748039941539987e-02,-5.183901051410267496e-02,2.301769711995565321e-02,4.832288399909672599e-02,8.189619022115878985e-03,1.638286541861499329e-02,-1.534397025624590662e-02,-7.590999214244361151e-03,-1.293879829370032063e-02,-3.905372302626759860e-03,7.597351130167973032e-02,-1.628237654273405333e-02,2.489600472154414323e-02,7.174980628233055928e-04,-1.306712464966932642e-02,-6.521175703705014981e-02,2.855520791016076879e-02,-4.731942333021178088e-02,1.164227804380277981e-02,1.107648929933675516e-02,-4.849205057127094209e-02,-1.261681754129756992e-02,8.269426255459086036e-03,-3.910907593315801623e-02,-5.165471069407932825e-02,-3.338988280423312721e-02,3.919888670581894718e-02,-3.305299466541122139e-02,-5.478662688188661728e-02,-2.643029220060371873e-02,2.458477281418350573e-03,1.126843160024225236e-02,1.520373819649116845e-02,2.274416938729254684e-02,4.077821249300230683e-02,-3.752341414354809501e-02,3.452674556538413292e-02,-1.177880961626180667e-02,2.645124054827376579e-03,5.459060979901195730e-03,6.321232045360037320e-03,4.535856554189631254e-03,-1.690152758581930882e-03,-5.886628877404082028e-02,-2.221203823222337934e-02,2.802489584061824968e-02,7.481375355783682207e-03,-5.440672140440221821e-02,-5.427711069727662180e-02,-2.616488486775665062e-02,2.665195124189537537e-02,-4.185339474744600996e-03,-2.165159420349510588e-02,-1.015202257726930193e-02,8.555789054264649474e-03,-1.100905061424637408e-03,-1.036774602803715827e-02,1.205893166869945188e-02,-8.826275993105500359e-03,4.339530855182474611e-02,3.514976410440374954e-02,-1.957289546199518851e-02,2.342757714331344596e-02,-2.609093072392861673e-02,-6.079888073534957943e-03,4.445658645358914474e-02,7.413595555156334135e-04,-5.226360496587460769e-02,1.857131314945437844e-02,5.179960646405643715e-02,-2.466647142489164848e-02,1.933111908732867285e-02,1.250783453435296184e-02,-2.713510128260603407e-02,2.456594239259990778e-02,-5.407592295402952054e-02,2.520672187118375152e-02,-3.283668971881804205e-02,1.463073128673885587e-02,-4.029039848657425360e-04,2.993895082441254060e-02,-1.001826177664504915e-02,3.083946713918428104e-02,-2.547747375580060314e-02,8.608928249085961992e-03,-3.441807860878160624e-02,7.701993563505057580e-03,2.471569237197458052e-02,9.473010276769576465e-03,-3.566215022590738925e-03,5.536829501443847439e-03,2.109469831225369019e-02,2.212180545408025736e-02,-9.171329286069554096e-03,5.384042014232501977e-02,2.268467472657190176e-02,3.313129098348623763e-02,1.537053938951158825e-03,2.634505332741762448e-02,3.009349178439796671e-02,3.310834648879197595e-02,1.479791458206747290e-02,-1.459584451959417689e-02,2.349431524346831321e-02,-1.986474447888936668e-03,4.668409950423692972e-03,3.028893167843287049e-02,-2.413528596982438337e-02,-4.552658179864976546e-04,6.135012407658856776e-03,2.063617289789457937e-02,1.517994251519474286e-02,-2.146822279140544673e-02,3.832485236872837375e-02,3.041895410461971719e-02,-1.424293266629217229e-02,-7.495937985009782333e-03,-9.791767215105417685e-03,-1.623039535851318127e-03,4.601108621983661211e-03,-1.748458173865565651e-02,6.491821468632845427e-02,1.998891150690490850e-02,2.046436835384331156e-03,-3.191351464964528595e-02,-6.733476912140357561e-03,-7.249879921423334206e-02,-6.233786965675979647e-02,2.073474666727784591e-02,1.798364648910643487e-02,1.066015650325244368e-02,-4.430305392389998626e-02,1.934085632867540636e-02,1.121972352369790538e-02,-1.386377468776047936e-02,4.569890539552606823e-02,-6.495167672181328955e-02,2.461574939605984391e-02,1.039498213378217163e-02,1.851224148330280275e-02,-2.093497725885349464e-02,-8.488656222436878618e-03,-3.142610772504229530e-03,-3.982344190439254111e-02,-7.458906262185682409e-05,1.010179910922339927e-02,-4.172054854596555368e-02,3.197765083300721511e-02,-2.030892575245987763e-02,9.130550894009185989e-04,-1.135854088554263952e-02,4.324410379470769450e-02,1.819046132635942711e-02,5.306192607229654953e-03,2.279244560202900449e-02,3.386041837746327828e-03,9.671214278472339831e-03,-2.985839711215077658e-02,4.354160759359004124e-02,2.938414274943523113e-03,-1.766024241837650666e-02,-1.814341259578746215e-02,-1.192029297095045272e-02,1.559171215957389292e-02,-5.434542640175888534e-02,-1.832119441873689136e-02,-4.409157309896050841e-02,-4.471299852131652153e-02,5.325876784414096399e-03,8.141309009831791677e-02,-2.578126899400551286e-02,-1.922391101393652532e-02,5.168408323988254831e-03,-2.776849705231565144e-02,-4.057209203097886241e-02,-9.070682193984810904e-03,-1.898026605188090840e-02,-5.033324697449450234e-03,-2.453644624413373748e-02,-1.472502124051643796e-02,-1.048600657276817921e-02,-2.033643681792361019e-02,-2.678577250538918819e-02,1.806936544757511282e-02,5.278530711315346929e-02,-3.749292207680317290e-02,2.585721942699502340e-02,1.541016390905454621e-02,-2.432964596057497764e-02,3.152128713089063367e-02,2.924774673924745300e-02,2.912772470531743013e-02,2.168397493242527063e-02,-1.591348822103520397e-02,-4.564083862382988660e-02,-1.706321312220292555e-02,-8.485291801477034754e-03,5.588458261187102816e-02,-9.586334342148946502e-03,8.408571320315199812e-03,-1.704852036314541061e-02,-1.832836386285994351e-02,9.365140457673290855e-03,-1.001860718735918471e-03,1.144960938233860123e-02,-2.081374215252669233e-02,-1.090106834001829117e-02,-7.462719984306242019e-03,8.965890189832088214e-03,-1.137137483258056359e-02,-3.818854371053027885e-02,-6.645630801263071978e-03,1.819618823797714002e-02,-2.035674112018154291e-02,2.379630303522094897e-02,-2.109881511450253586e-02,6.202874184751460546e-02,2.861257879567884882e-02,-4.452668634655497504e-02,-3.372836021949089397e-03,3.244176676419123495e-02,8.161859414961267212e-03,-3.756960711712176160e-02,8.857033004379424868e-02,4.386860138982688617e-02,-2.010346195953469084e-02,-1.656896494859855587e-02,3.553650675565775408e-02,2.612705281368515875e-02,-2.325094401873993230e-02,1.352567618892010562e-02,-8.772160483748146775e-03,-2.459562350780137782e-02,-9.888548687870868381e-03,-3.146979029830847263e-02,3.305196130637639423e-02,-1.667571328079555174e-02,1.049729940626825501e-02,-2.922522751414441834e-03,2.298099842180332739e-02,1.507989754080066823e-02,4.971628376120386210e-03,1.905547007092949288e-02,-4.124949358221439294e-02,-4.031940790152827025e-02,-3.999204182137090086e-02,-9.135346496101716049e-03,-1.741313625813529359e-02,1.232096431460102427e-02,3.923163794551320590e-04,2.119310389552278226e-02,-7.785281873740348968e-03,-5.395708740291619383e-04,-3.008082840413134687e-02,-3.856237957728010819e-03,-2.299442498192658113e-02,2.851393659997532651e-02,9.022595095342077556e-03,3.247279091951082303e-02,-6.873141257232799443e-04,-3.203598041553043507e-02,-4.283948716825060343e-02,-9.007014966065249317e-03,-4.137321964181805284e-02,-2.358679717040775004e-02,-3.668064446784129184e-02,-1.190081319244536140e-01,4.567747878469131245e-02,-3.225386738758437462e-03,-4.532609515568994385e-02,-1.219025994241436026e-03,1.622822031611611052e-02,1.452202866226768446e-02,-1.299303994568009810e-02,-1.159864178000873797e-02,5.571923738314579072e-03,-7.767998902646676071e-03,3.143767007308499034e-02,-1.584061247962520805e-02,5.373325344730311287e-02,-1.017131221566327029e-02,-1.593261182395628098e-02,3.167479421360424457e-02,4.750999329039172318e-03,-6.167559613219229797e-02,4.258306615228763664e-02,2.869108475244647877e-02,7.736009292037918095e-02,6.832572344669470346e-03,-1.283396675003335144e-03,-1.863026340472383885e-02,6.968882203250943014e-03,-4.625486057475428070e-02,2.141798997414260525e-02,-1.376346496573378070e-02,-3.365631966458017960e-02,-2.879493285418494031e-02,-4.563968457030703058e-02,-3.675752527414224285e-02,-2.332045373156133635e-03,-3.077659753179259883e-02,4.013448990070739124e-03,2.062839183409559147e-03,-1.740116325865801892e-03,6.890433616056516192e-03,-2.334446044854104202e-02,-1.236065194633626137e-02,-3.517300916980972171e-03,-7.105184167721593190e-03,8.301615793043521513e-03,1.043182250061761712e-02,-1.969253045742382080e-02,4.583802757770352732e-02,7.938586106452968916e-03,6.540090061949668798e-02,1.972691489428475553e-02,-5.229555698027141958e-02,5.251226151180587998e-02,-3.230626670778766196e-02,3.394159739880749788e-02,-9.441716374150983804e-03,-2.019969777453951149e-02,2.586792611338069661e-02,-6.582453581962144362e-02,8.939631996490218432e-03,4.461672110101572164e-02,-1.349245731473071828e-02,-2.819585703298698592e-02,-1.850519307912939712e-02,-4.113643704687437036e-02,-1.425533454025290289e-02,-2.464400049445470212e-02,-3.508471391818284400e-03,-2.391166188612606908e-02,-7.799509977996671971e-03,3.354796145269244717e-02,1.110612119570233633e-02,2.713889626591062254e-02,2.187305337132614425e-03,3.403175493929822860e-03,-5.591770468089765980e-03,3.627425552556235583e-02,5.638839323158600231e-02,-2.779629564739944866e-02,1.780209566616826680e-02,-1.248461344256583325e-02,-5.863344172965354734e-02,3.611349896174409491e-02,2.900910008502630491e-02,3.143759198103619756e-03,9.945933073029470176e-03,-5.300220332280779906e-02,2.275256676583456428e-02,2.589736729137528601e-02,-8.678712778710968856e-02,1.727411418620519029e-02,6.873591773159529184e-02,-2.368545929182088242e-02,2.434355290621357040e-02,3.286593908446517470e-02,5.908269651390953697e-02,3.991351732212192194e-02,-1.831413480331034807e-02,3.368753513379669356e-02,-1.067755847425127559e-02,-1.755932011515424227e-03,-2.834462692656414262e-02,1.300476483200358087e-02,3.729572672166586288e-03,-2.960445365963674733e-02,-1.789658573229303135e-02,-7.989881973216022421e-03,-1.430770596215589704e-02,-1.151612631216697956e-02,3.322192072613860958e-02,1.794534718374744819e-02,-4.411065669915931360e-03,-5.496655132288064821e-02,-1.361590952041463569e-02,3.387832597956267743e-03,6.127346310240058130e-02,-5.254702190398886918e-02,-1.772162719529520730e-02,4.733122156249039425e-02,-3.147400175589928906e-02,8.491809996809679406e-03,3.672707264743266253e-02,9.373944603385834726e-03,2.634093027253384817e-02,-2.459966142353432490e-03,-9.721583160700817891e-03,4.270923431544208781e-02,4.290331638750606580e-02,5.251689198120600144e-03,2.525979805115190213e-02,1.679841623891768429e-02,-1.574753024563198267e-02,2.287979835761752567e-02,8.115759765904078174e-03,-2.844687232635036145e-02,2.167123986284583918e-03,-4.078061992088916066e-02,4.332911802505770571e-02,2.626872433592889952e-02,-1.369944698124337355e-02,1.151479798596320540e-03,-3.163823873001880144e-02,2.674962214230370769e-02,-9.731479741543891740e-03,4.280067134534636109e-02,3.890667717394029161e-03,8.031701441530879337e-02,-3.990698700047752567e-02,1.108493360729744318e-02,2.732787244847981536e-02,-7.602153926487776638e-03,-6.395807397931984987e-03,-2.356235518234145107e-02,2.291716553230552927e-02,-3.121034689845457802e-02,-1.309492402979643179e-02,3.215448779886360964e-02,3.699699856290865341e-02,6.205228379631862884e-02,2.509633400872396738e-03,8.105082658518517058e-02,1.331736176308709503e-02,-1.201036646992410632e-02,1.806490517143997596e-02,-3.241962641180819865e-02,-7.835970585587518841e-03,3.472600462597467963e-02,3.379756506781863429e-02,-2.671046509906435055e-03,4.710094108365166926e-02,-3.716016190499985949e-03,-2.410365211347831674e-02,-2.241185000192534929e-02,-1.566299697526335683e-03,1.598482010197673983e-02,1.461363920706827864e-02,1.154834597546776018e-02,3.637794026688665611e-02,-2.391384271316680452e-02,-4.431706115499245424e-02,6.569347446744443209e-03,2.246100116904268390e-02,-4.217793195420838082e-02,-3.119276243071122251e-02,-2.124418423579879298e-02,4.970478056028608538e-02,2.176054163764897659e-02,3.844703407050684141e-02,-6.005062188947667655e-03,-4.150529252604974288e-03,9.082646935003921285e-03,-1.886024778163121430e-03,1.321893482363468812e-02,-5.236392098163965281e-02,1.756726560518803021e-02,2.628293616225053572e-02,1.677519057113249779e-02,-1.076218099970989439e-02,-4.757795865927243878e-02,-7.445876734317665412e-03,-2.907938659592310127e-02,-1.260974315662148214e-04,-1.057497503109352220e-02,3.730082871700195202e-02,2.157798525590472194e-02,3.382411142196977555e-02,-6.379220241105046200e-03,-5.901514560311807434e-02,-2.489544306681398377e-03,-2.451336292732351693e-02,1.362548732452867513e-02,-9.591746084648151288e-03,-3.352830617382181189e-02,1.113312605371594632e-03,-1.374909077504693489e-02,2.918769152093956057e-02,-4.240691896018656398e-02,3.632715294052438551e-03,-5.302402370222036865e-02,3.038547852745119085e-02,-8.376373144435176818e-04,6.808034745537860921e-02,6.672254998458927375e-03,2.613822619055774718e-02,-7.229306077861549773e-02,-4.901298844276831990e-05,-1.140486648210344012e-02,-2.273718596156509494e-02,-4.351023845252282966e-03,-2.211759818130587876e-02,-3.428546920601133197e-02,1.427790420237910057e-02,-1.517632542177304797e-02,-1.400143426175046689e-02,-1.626545776450248962e-02,-5.822937782647228527e-03,-1.223168703012531867e-02,1.559544623080473882e-03,-2.436563031397210102e-02,-2.546312234669341132e-02,4.431476496253761166e-02,-4.402063842826933575e-03,2.001613754600214956e-02,-1.462127328308806748e-02,-1.468791998822817531e-03,3.320897867990774827e-02,-1.059843424512000448e-02,3.166224100214296705e-02,7.467923044030416041e-03,-2.707760296420650900e-02,-5.300778226537170706e-02,2.669687138733486259e-02,-3.593192901887853289e-03,3.048943643488393265e-02,-7.582218510070024009e-02,-1.230849576204452104e-04,3.773181816198398382e-03,2.013386534515845469e-02,-1.681960519783640834e-02,1.872238829374895525e-02,3.002764359892872987e-04,4.470443961492239632e-02,-2.177949250672105846e-02,-7.544337007306602290e-03,-4.207489896492123613e-03,3.640377352353706131e-02,1.094182028858136334e-02,9.203967845774310361e-03,-4.293459854474834803e-02,-4.947642948486728059e-02,-3.951650093214512799e-02,-4.483813045119805496e-02,-5.988233880066954479e-02,-2.706300736298441686e-02,-4.010201762636356540e-03,2.099098094655147198e-02,-7.987475759835351713e-03,-3.117793090266760686e-02,-2.926750300967430329e-02,-4.523433427089393333e-02,-7.449778530743514024e-03,6.545123375965573864e-02,2.221461898389477663e-02,9.440246598415897791e-03,4.057142287038827816e-02,-1.300400037386809440e-02,-1.929375065087655244e-02,1.014025515534697913e-02,-7.807899460208767885e-03,-2.700533771880220604e-02,-6.321287211118239990e-02,-7.017987091209475572e-03,2.792905188846789635e-02,-6.484530447121007735e-02,2.207955380279339949e-02,-2.313591996190165340e-02,3.504773486827063300e-02,2.961903477813208896e-02,-6.191641419330317503e-02,-3.181754773092672524e-03,-2.995800967967339381e-03,1.551516077382821338e-02,3.225406304414590863e-02,-1.160973008551944088e-02,7.152037463389084027e-03,-1.503666101682746628e-02,3.169732695417388363e-02,-2.331102588834735659e-02,3.048592631905459177e-02,-1.495585039837956515e-02,-2.988107806341811987e-02,-7.024302892707372237e-02,-5.162311410935937345e-02,-1.073127512005162855e-02,1.693387094946649692e-03,1.329296490557344522e-02,-8.750307484279273504e-03,-2.652189189400715272e-03,5.765052884583226483e-02,1.746103029775594381e-02,-2.935791680952234972e-02,-6.084520993674842615e-02,-1.656744865127931371e-02,1.373475220812830737e-02,1.915899487685912561e-02,2.291552306771929559e-02,3.170395117739815277e-02,-2.406780052994039049e-02,7.681127907150928080e-02,3.106743931334360245e-03,-2.920900461079532773e-03,-3.907807319039262317e-02,2.673875344896591792e-03,-3.709599131526806429e-03,2.742689962202468634e-02]

fig = plt.figure(figsize=(9,4))
ax = plt.subplot(111)
ax.plot(ev, 'o')
plt.savefig("leadingVector.png")