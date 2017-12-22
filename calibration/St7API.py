import ctypes

kMaxStrLen = 255

## Array Limits
kMaxEntityTotals = 4
kMaxElementNode = 20
kMaxBeamResult = 4096
kNumBeamSectionData = 20
kNumMaterialData = 3
kMaxAttributeDoubles = 12
kMaxAttributeLogicals = 6
kMaxAttributeLongint = 6
kLastUnit = 6

## Unit Positions
ipLENGTHU = 0
ipFORCEU = 1
ipSTRESSU = 2
ipMASSU = 3
ipTEMPERU = 4
ipENERGYU = 5

## Unit Types - LENGTH
luMETRE = 0
luCENTIMETRE = 1
luMILLIMETRE = 2
luFOOT = 3
luINCH = 4

## Unit Types - FORCE
fuNEWTON = 0
fuKILONEWTON = 1
fuMEGANEWTON = 2
fuKILOFORCE = 3
fuPOUNDFORCE = 4
fuTONNEFORCE = 5
fuKIPFORCE = 6

## Unit Types - STRESS
suPASCAL = 0
suKILOPASCAL = 1
suMEGAPASCAL = 2
suKSCm = 3
suPSI = 4
suKSI = 5
suPSF = 6

## Unit Types - MASS
muKILOGRAM = 0
muTONNE = 1
muGRAM = 2
muPOUND = 3
muSLUG = 4

## Unit Types - TEMPERATURE
tuCELSIUS = 0
tuFAHRENHEIT = 1
tuKELVIN = 2

## Unit Types - ENERGY
euJOULE = 0
euBTU = 1
euFTLBF = 2
euCALORIE = 3

## Unit Types - TIME
tuMilliSec = 0
tuSec = 1
tuMin = 2
tuHour = 3
tuDay = 4

## Entity Types
tyNULL = -1
tyNODE = 0
tyBEAM = 1
tyPLATE = 2
tyBRICK = 3
tyLINK = 4
tyVERTEX = 5
tyGEOMETRYEDGE = 6
tyGEOMETRYFACE = 7
tyLOADPATH = 8

## Link Types
ilMasterSlaveLink = 1
ilSectorSymmetryLink = 2
ilCouplingLink = 3
ilPinnedLink = 4
ilRigidLink = 5
ilShrinkLink = 6
ilTwoPointLink = 7
ilAttachmentLink = 8
ilMultiPointLink = 9

## Master-Slave Link
msFree = 0
msFix = 1
msFixNegate = -1

## Coupling, Attachment and Multi-Point Links
cpTranslational = 1
cpRotational = 2
cpBoth = 3

## Rigid Link
rgPlaneXYZ = 0
rgPlaneXY = 1
rgPlaneYZ = 2
rgPlaneZX = 3

## 2-Point Link
ipTwoPointDOF1 = 0
ipTwoPointDOF2 = 1
ipTwoPointUCS1 = 2
ipTwoPointUCS2 = 3
ipTwoPointC0 = 0
ipTwoPointC1 = 1
ipTwoPointC2 = 2

## Attachment Link
ipAttachmentElType = 0
ipAttachmentElNum = 1
ipAttachmentBrickFaceNum = 2
ipAttachmentCouple = 3

## Multi-Point Link
mpInterpolatedFactors = 1
mpUserFactors = 2

## Node Temperature Types
tReferenceTemperature = 0
tFixedTemperature = 1
tInitialTemperature = 2
tTableTemperature = 3

## Beam End Release Constants
kBeamEndRelReleased = 0
kBeamEndRelFixed = 1
kBeamEndRelPartial = 2

## Property Types
ptBEAMPROP = 1
ptPLATEPROP = 2
ptBRICKPROP = 3
ptPLYPROP = 4

## Property Totals
ipBeamPropTotal = 0
ipPlatePropTotal = 1
ipBrickPropTotal = 2
ipPlyPropTotal = 3

## Alpha Temperature Types
kIntegratedAlpha = 0
kInstantAlpha = 1

## Sampling Positions
AtCentroid = 0
AtGaussPoints = 1
AtNodesAverageNever = 2
AtNodesAverageAll = 3
AtNodesAverageSame = 4

## Beam Types
kBeamTypeNull = 0
kBeamTypeSpring = 1
kBeamTypeCable = 2
kBeamTypeTruss = 3
kBeamTypeCutoff = 4
kBeamTypeContact = 5
kBeamTypeBeam = 6
kBeamTypeUser = 7
kBeamTypePipe = 8
kBeamTypeConnection = 9

## Contact Types
kZeroGapContact = 0
kNormalContact = 1
kTensionContact = 2
kTakeupContact = 3

## Contact Sub Types
kTensionTakeup = 0
kCompressionTakeup = 1

## Cutoff Types
kBrittleGap = 0
kDuctileGap = 1

## Contact Parameters Positions - Integers
ipContactType = 0
ipDynamicStiffness = 1
ipUseInFirstIteration = 2
ipUpdateDirection = 3
ipContactSubType = 4
ipFrictionYieldType = 5
ipFrictionModel = 6
ipTensionLateralStiffness = 7

## Contact Parameters Positions - Doubles
ipContactStiffness = 0
ipFrictionC1 = 1
ipFrictionC2 = 2
ipContactMaxTension = 3

## CutoffBar Parameter Positions
ipCutoffType = 0
ipKeepMass = 1

## Library Types
lbMaterial = 0
lbBeamSection = 1
lbComposite = 2
lbReinforcementLayout = 3
lbCreepDefinition = 4
lbLoadPathTemplate = 5

## Beam Section Types
kNullSection = 0
kCircularSolid = 1
kCircularHollow = 2
kSquareSolid = 3
kSquareHollow = 4
kLipChannel = 5
kTopHatChannel = 6
kISection = 7
kTSection = 8
kLSection = 9
kZSection = 10
kUserSection = 11
kTrapezoidSolid = 12
kTrapezoidHollow = 13
kTriangleSolid = 14
kTriangleHollow = 15
kCruciform = 16

## Beam Mirror Types
kMirrorNone = 0
kMirrorTop = 1
kMirrorBot = 2
kMirrorLeft = 3
kMirrorRight = 4
kMirrorLeftAndTop = 5
kMirrorLeftAndBot = 6
kMirrorRightAndTop = 7
kMirrorRightAndBot = 8
kMirrorLeftTopOnly = 9
kMirrorLeftBotOnly = 10
kMirrorRightTopOnly = 11
kMirrorRightBotOnly = 12

## Beam Section Positions
ipAREA = 0
ipI11 = 1
ipI22 = 2
ipJ = 3
ipSL1 = 4
ipSL2 = 5
ipSA1 = 6
ipSA2 = 7
ipXBAR = 8
ipYBAR = 9
ipANGLE = 10
ipD1 = 11
ipD2 = 12
ipD3 = 13
ipT1 = 14
ipT2 = 15
ipT3 = 16
ipGapA = 17
ipGapB = 18

## Beam Load Types
kMaxDLPerBeam = 64
kConstantDL = 0
kLinearDL = 1
kTriangularDL = 2
kThreePoint0DL = 3
kThreePoint1DL = 4
kTrapezoidalDL = 5

## Plate Load Patch Types
ptAuto4 = 0
ptAuto3 = 1
ptAuto2 = 2
ptAuto1 = 3
ptAngleSplit = 4
ptManual = 5

## Plate Types
kPlateTypeNull = 0
kPlateTypePlaneStress = 1
kPlateTypePlaneStrain = 2
kPlateTypeAxisymmetric = 3
kPlateTypePlateShell = 4
kPlateTypeShearPanel = 5
kPlateTypeMembrane = 6
kPlateTypeLoadPatch = 7

## Geometry Surface Types
suPlane = 0
suSphere = 1
suTorus = 2
suCone = 3
suBSpline = 4
suRotSur = 5
suPipeSur = 6
suSumSur = 7
suTabCyl = 8
suRuleSur = 9
suCubicSpline = 10

## Plate Section Positions
ipTHICKM = 0
ipTHICKB = 1

## Material Types
kMaterialTypeNull = 0
kMaterialTypeIsotropic = 1
kMaterialTypeOrthotropic = 2
kMaterialTypeAnisotropic = 3
kMaterialTypeRubber = 4
kMaterialTypeSoil = 5
kMaterialTypeLaminate = 6
kMaterialTypeUserDefined = 7
kMaterialTypePly = 8
kMaterialTypeFluid = 10

## Yield Criteria
ycTresca = 0
ycVonMises = 1
ycMaxStress = 2
ycMohrCoulomb = 3
ycDruckerPrager = 4

## Nonlinear Types
ntNonlinElastic = 0
ntElastoPlastic = 1

## Rubber Types
kNeoHookean = 1
kMooneyRivlin = 2
kGeneralisedMooneyRivlin = 3
kOgden = 4

## Material Positions
ipModulus = 0
ipPoisson = 1
ipDensity = 2

## Node Result Types - Old convention
kNodeDisp = 1
kNodeVel = 2
kNodeAcc = 3
kNodePhase = 4
kNodeReact = 5
kNodeTemp = 6
kNodeFlux = 7
kNodeInfluence = 1

## Node Result Types
rtNodeDisp = 1
rtNodeVel = 2
rtNodeAcc = 3
rtNodePhase = 4
rtNodeReact = 5
rtNodeTemp = 6
rtNodeFlux = 7
rtNodeInfluence = 1

## Beam Result Types
rtBeamForce = 1
rtBeamStrain = 2
rtBeamStress = 3
rtBeamTRelease = 4
rtBeamRRelease = 5
rtBeamCableXYZ = 6
rtBeamFlux = 8
rtBeamGradient = 9
rtBeamCreepStrain = 10
rtBeamEnergy = 11
rtBeamDisp = 12
rtBeamNodeReact = 13

## Beam Result Quantities - BEAMFORCE - Local and Principal
ipBeamSF1 = 0
ipBeamBM1 = 1
ipBeamSF2 = 2
ipBeamBM2 = 3
ipBeamAxialF = 4
ipBeamTorque = 5

## Beam Result Quantities - BEAMFORCE - Global
ipBeamFX = 0
ipBeamMX = 1
ipBeamFY = 2
ipBeamMY = 3
ipBeamFZ = 4
ipBeamMZ = 5

## Beam Result Quantities - BEAMSTRESS
ipMinFibreStress = 0
ipMaxFibreStress = 1
ipMaxShearStress1 = 2
ipMaxShearStress2 = 3
ipAvShearStress1 = 4
ipAvShearStress2 = 5
ipTorqueStress = 6
ipMinPrincipalStress = 7
ipMaxPrincipalStress = 8
ipMinPipeHoopStress = 9
ipMaxPipeHoopStress = 10
ipMinAxialStress = 11
ipMaxAxialStress = 12
ipMinBendingStress1 = 13
ipMaxBendingStress1 = 14
ipMinBendingStress2 = 15
ipMaxBendingStress2 = 16
ipYieldRatio = 17

## Beam Result Quantities - BEAMFLUXGRAD
ipBeamFlux = 0
ipBeamTempGradient = 1

## Beam Result Quantities - BEAMSTRAIN
ipAxialStrain = 0
ipCurvature1 = 1
ipCurvature2 = 2
ipTwist = 3

## Beam Result Quantities - BEAMRELEASE
ipRelEnd1Dir1 = 0
ipRelEnd1Dir2 = 1
ipRelEnd1Dir3 = 2
ipRelEnd2Dir1 = 3
ipRelEnd2Dir2 = 4
ipRelEnd2Dir3 = 5

## Beam Result Quantities - BEAMENERGY
ipBeamEnergyStored = 0
ipBeamEnergySpent = 1

## Plate Result Types
rtPlateStress = 1
rtPlateStrain = 2
rtPlateEnergy = 3
rtPlateForce = 4
rtPlateMoment = 5
rtPlateCurvature = 6
rtPlatePlyStress = 7
rtPlatePlyStrain = 8
rtPlatePlyReserve = 9
rtPlateFlux = 10
rtPlateGradient = 11
rtPlateReoDesign = 12
rtPlateCreepStrain = 13
rtPlateSoil = 14
rtPlateUser = 15
rtPlateNodeReact = 16
rtPlateNodeDisp = 17

## Plate Surface Definition
psPlateMidPlane = 0
psPlateZMinus = 1
psPlateZPlus = 2

## Brick Result Types
rtBrickStress = 1
rtBrickStrain = 2
rtBrickEnergy = 3
rtBrickFlux = 4
rtBrickGradient = 5
rtBrickCreepStrain = 6
rtBrickSoil = 7
rtBrickUser = 8
rtBrickNodeReact = 9
rtBrickNodeDisp = 10

## Beam Result Sub Types
stBeamLocal = 0
stBeamPrincipal = -1
stBeamGlobal = -2

## Plate Result Sub Types
stPlateLocal = 0
stPlateGlobal = -1
stPlateCombined = -2
stPlateSupport = -3
stPlateDevLocal = -4
stPlateDevGlobal = -5
stPlateDevCombined = -6

## Brick Result Sub Types
stBrickLocal = 0
stBrickGlobal = -1
stBrickCombined = -2
stBrickSupport = -3
stBrickDevLocal = -4
stBrickDevGlobal = -5
stBrickDevCombined = -6

## Plate/Brick Result Sub Types (Undocumented)
stLOCAL = 0
stGLOBAL = 1
stUCS = 2
stCOMBINED = 3

## PLATESTRESS, PLATESTRAIN, PLATECREEPSTRAIN, PLATEMOMENT, PLATECURVATURE, PLATEFORCE results for STLOCAL
ipPlateLocalxx = 0
ipPlateLocalyy = 1
ipPlateLocalzz = 2
ipPlateLocalxy = 3
ipPlateLocalyz = 4
ipPlateLocalzx = 5
ipPlateLocalxz = 5
ipPlateLocalMean = 0
ipPlateLocalDevxx = 1
ipPlateLocalDevyy = 2
ipPlateEdgeSupport = 0
ipPlateFaceSupport = 1

## PLATESTRESS, PLATESTRAIN, PLATECREEPSTRAIN, PLATEMOMENT, PLATECURVATURE, PLATEFORCE results for STGLOBAL (NOT AXISYMMETRIC)
ipPlateGlobalXX = 0
ipPlateGlobalYY = 1
ipPlateGlobalZZ = 2
ipPlateGlobalXY = 3
ipPlateGlobalYZ = 4
ipPlateGlobalZX = 5
ipPlateGlobalMean = 0
ipPlateGlobalDevXX = 1
ipPlateGlobalDevYY = 2
ipPlateGlobalDevZZ = 3

## PLATESTRESS, PLATESTRAIN, PLATECREEPSTRAIN, PLATEMOMENT, PLATECURVATURE, PLATEFORCE results for STUCS
ipPlateUCSXX = 0
ipPlateUCSYY = 1
ipPlateUCSZZ = 2
ipPlateUCSXY = 3
ipPlateUCSYZ = 4
ipPlateUCSZX = 5

## PLATESTRESS, PLATESTRAIN, PLATECREEPSTRAIN, PLATEFORCE, PLATEMOMENT, PLATECURVATURE results for STCOMBINED (NOT AXISYMMETRIC)
ipPlateCombPrincipal11 = 0
ipPlateCombPrincipal22 = 1
ipPlateCombPrincipalAngle = 3
ipPlateCombVonMises = 4
ipPlateCombTresca = 5
ipPlateCombMohrCoulomb = 6
ipPlateCombDruckerPrager = 7
ipPlateCombPlasticStrain = 6
ipPlateCombCreepEffRate = 6
ipPlateCombCreepShrinkage = 7
ipPlateCombYieldIndex = 8
ipPlateCombMean = 0
ipPlateCombDev11 = 1
ipPlateCombDev22 = 2

## PLATESTRESS, PLATESTRAIN, PLATECREEPSTRAIN results for STGLOBAL (AXISYMMETRIC)
ipPlateAxiGlobalRR = 0
ipPlateAxiGlobalZZ = 1
ipPlateAxiGlobalTT = 2
ipPlateAxiGlobalRZ = 3
ipPlateAxiGlobalMean = 0
ipPlateAxiGlobalDevRR = 1
ipPlateAxiGlobalDevZZ = 2
ipPlateAxiGlobalDevTT = 3

## PLATESTRESS, PLATESTRAIN, PLATECREEPSTRAIN results for STCOMBINED (AXISYMMETRIC)
ipPlateAxiCombPrincipal11 = 0
ipPlateAxiCombPrincipal22 = 1
ipPlateAxiCombPrincipal33 = 2
ipPlateAxiCombVonMises = 4
ipPlateAxiCombTresca = 5
ipPlateAxiCombMohrCoulomb = 6
ipPlateAxiCombDruckerPrager = 7
ipPlateAxiCombPlasticStrain = 6
ipPlateAxiCombCreepEffRate = 5
ipPlateAxiCombCreepShrinkage = 7
ipPlateAxiCombYieldIndex = 8
ipPlateAxiCombMean = 0
ipPlateAxiCombDev11 = 1
ipPlateAxiCombDev22 = 2
ipPlateAxiCombDev33 = 3

## PLATEPLYSTRESS
ipPlyStress11 = 0
ipPlyStress22 = 1
ipPlyStress12 = 3
ipPlyILSx = 4
ipPlyILSy = 5

## PLATEPLYSTRAIN
ipPlyStrain11 = 0
ipPlyStrain22 = 1
ipPlyStrain12 = 3

## PLATEPLYRESERVE
ipPlyMaxStress = 0
ipPlyMaxStrain = 1
ipPlyTsaiHill = 2
ipPlyModTsaiWu = 3
ipPlyHoffman = 4
ipPlyInterlam = 5

## PLATESOIL
ipPlateSoilTotalPorePressure = 0
ipPlateSoilExcessPorePressure = 1
ipPlateSoilOCRIndex = 2
ipPlateSoilStateIndex = 3
ipPlateSoilVoidRatio = 4

## PLATEFLUX, PLATEGRADIENT results for STLOCAL
ipPlateFluxLocalx = 0
ipPlateFluxLocaly = 1
ipPlateFluxLocalxy = 2

## PLATEFLUX, PLATEGRADIENT results for STGLOBAL
ipPlateFluxGlobalX = 0
ipPlateFluxGlobalY = 1
ipPlateFluxGlobalZ = 2
ipPlateFluxGlobalXY = 3
ipPlateFluxGlobalYZ = 4
ipPlateFluxGlobalZX = 5
ipPlateFluxGlobalSRSS = 6

## PLATEFLUX, PLATEGRADIENT results for STUCS
ipPlateFluxUCSX = 0
ipPlateFluxUCSY = 1
ipPlateFluxUCSZ = 2
ipPlateFluxUCSXY = 3
ipPlateFluxUCSYZ = 4
ipPlateFluxUCSZX = 5
ipPlateFluxUCSSRSS = 6

## PLATEREODESIGN
ipPlateRCWoodArmerMoment = 0
ipPlateRCWoodArmerForce = 1
ipPlateRCSteelArea = 2
ipPlateRCSteelAreaLessBase = 3
ipPlateRCSteelStress = 4
ipPlateRCConcreteStrain = 5
ipPlateRCBlockRatio = 6

## PLATENODEREACT
ipPlateNodeReactFX = 0
ipPlateNodeReactFY = 1
ipPlateNodeReactFZ = 2
ipPlateNodeReactMX = 3
ipPlateNodeReactMY = 4
ipPlateNodeReactMZ = 5

## PLATEENERGY
ipPlateEnergyStored = 0
ipPlateEnergySpent = 1

## BRICKSTRESS, BRICKSTRAIN, BRICKCREEPSTRAIN results for STLOCAL
ipBrickLocalxx = 0
ipBrickLocalyy = 1
ipBrickLocalzz = 2
ipBrickLocalxy = 3
ipBrickLocalyz = 4
ipBrickLocalzx = 5
ipBrickLocalMean = 0
ipBrickLocalDevxx = 1
ipBrickLocalDevyy = 2
ipBrickLocalDevzz = 3
ipBrickFaceSupport = 0

## BRICKSTRESS, BRICKSTRAIN, BRICKCREEPSTRAIN results for STGLOBAL
ipBrickGlobalXX = 0
ipBrickGlobalYY = 1
ipBrickGlobalZZ = 2
ipBrickGlobalXY = 3
ipBrickGlobalYZ = 4
ipBrickGlobalZX = 5
ipBrickGlobalMean = 0
ipBrickGlobalDevXX = 1
ipBrickGlobalDevYY = 2
ipBrickGlobalDevZZ = 3

## BRICKSTRESS, BRICKSTRAIN, BRICKCREEPSTRAIN results for STUCS
ipBrickUCSXX = 0
ipBrickUCSYY = 1
ipBrickUCSZZ = 2
ipBrickUCSXY = 3
ipBrickUCSYZ = 4
ipBrickUCSZX = 5

## BRICKSTRESS, BRICKSTRAIN, BRICKCREEPSTRAIN results for STCOMBINED
ipBrickCombPrincipal11 = 0
ipBrickCombPrincipal22 = 1
ipBrickCombPrincipal33 = 2
ipBrickCombVonMises = 3
ipBrickCombTresca = 4
ipBrickCombMohrCoulomb = 5
ipBrickCombDruckerPrager = 6
ipBrickCombPlasticStrain = 6
ipBrickCombCreepEffRate = 6
ipBrickCombCreepShrinkage = 7
ipBrickCombYieldIndex = 8
ipBrickCombMean = 0
ipBrickCombDev11 = 1
ipBrickCombDev22 = 2
ipBrickCombDev33 = 3

## BRICKSOIL
ipBrickSoilTotalPorePressure = 0
ipBrickSoilExcessPorePressure = 1
ipBrickSoilOCRIndex = 2
ipBrickSoilStateIndex = 3
ipBrickSoilVoidRatio = 4

## BRICKFLUX, BRICKGRADIENT results for STLOCAL
ipBrickFluxLocalx = 0
ipBrickFluxLocaly = 1
ipBrickFluxLocalz = 2
ipBrickFluxLocalxy = 3
ipBrickFluxLocalyz = 4
ipBrickFluxLocalzx = 5
ipBrickFluxLocalRMS = 6

## BRICKFLUX, BRICKGRADIENT results for STGLOBAL
ipBrickFluxGlobalX = 0
ipBrickFluxGlobalY = 1
ipBrickFluxGlobalZ = 2
ipBrickFluxGlobalXY = 3
ipBrickFluxGlobalYZ = 4
ipBrickFluxGlobalZX = 5
ipBrickFluxGlobalRMS = 6

## BRICKFLUX, BRICKGRADIENT results for STUCS
ipBrickFluxUCSX = 0
ipBrickFluxUCSY = 1
ipBrickFluxUCSZ = 2
ipBrickFluxUCSXY = 3
ipBrickFluxUCSYZ = 4
ipBrickFluxUCSZX = 5
ipBrickFluxUCSRMS = 6

## BRICKNODEREACT
ipBrickNodeReactFX = 0
ipBrickNodeReactFY = 1
ipBrickNodeReactFZ = 2

## BRICKENERGY
ipBrickEnergyStored = 0
ipBrickEnergySpent = 1

## MODAL RESULTS NFA
ipFrequencyNFA = 0
ipModalMassNFA = 1
ipModalStiffNFA = 2
ipModalDampNFA = 3
ipModalTMassP1 = 4
ipModalTMassP2 = 5
ipModalTMassP3 = 6
ipModalRMassP1 = 7
ipModalRMassP2 = 8
ipModalRMassP3 = 9

## INERTIA RELIEF RESULTS
ipMassXIRA = 0
ipMassYIRA = 1
ipMassZIRA = 2
ipXcIRA = 3
ipYcIRA = 4
ipZcIRA = 5
ipAccXIRA = 6
ipAccYIRA = 7
ipAccZIRA = 8
ipAngAccXIRA = 9
ipAngAccYIRA = 10
ipAngAccZIRA = 11

## UCS Types
UCSCartesian = 0
UCSCylindrical = 1
UCSSpherical = 2
UCSToroidal = 3

## Matrix Types
mtCompliance = 1
mtStiffness = 2

## Node/Vertex Attribute Types
ATTRFreedom = 1
ATTRForce = 2
ATTRMoment = 3
ATTRTemperature = 4
ATTRMTranslation = 5
ATTRMRotation = 6
ATTRKTranslation = 7
ATTRKRotation = 8
ATTRDamping = 9
ATTRNSMass = 10
ATTRNodeInfluence = 11
ATTRNodeHeatSource = 12
ATTRNodeVelocity = 13
ATTRNodeAcceleration = 14

## Vertex Types
vtFree = 1
vtFixed = 2

## Beam Attribute Types
ATTRBeamAngle = 21
ATTRBeamOffset = 22
ATTRBeamTEndRelease = 23
ATTRBeamREndRelease = 24
ATTRBeamSupport = 25
ATTRBeamPreTension = 26
ATTRCableFreeLength = 27
ATTRBeamDLL = 28
ATTRBeamDLG = 29
ATTRBeamCFL = 30
ATTRBeamCFG = 31
ATTRBeamCML = 32
ATTRBeamCMG = 33
ATTRBeamTempGradient = 34
ATTRBeamConvection = 35
ATTRBeamRadiation = 36
ATTRBeamFlux = 37
ATTRBeamHeatSource = 38
ATTRBeamRadius = 39
ATTRPipePressure = 40
ATTRBeamNSMass = 41
ATTRPipeTemperature = 42
ATTRBeamDML = 44
ATTRBeamStringGroup = 45
ATTRBeamTaper = 92
ATTRBeamInfluence = 93
ATTRBeamSectionFactor = 94
ATTRBeamCreepLoadingAge = 95
ATTRBeamEndAttachment = 96
ATTRBeamConnectionUCS = 97
ATTRBeamStageProperty = 98

## Plate/Edge/Face Attribute Types
ATTRPlateAngle = 51
ATTRPlateOffset = 52
ATTRPlatePreLoad = 53
ATTRPlateFacePressure = 54
ATTRPlateFaceShear = 55
ATTRPlateEdgePressure = 56
ATTRPlateEdgeShear = 57
ATTRPlateEdgeNormalShear = 58
ATTRPlateTempGradient = 59
ATTRPlateEdgeSupport = 60
ATTRPlateFaceSupport = 61
ATTRPlateEdgeConvection = 62
ATTRPlateEdgeRadiation = 63
ATTRPlateFlux = 64
ATTRPlateHeatSource = 65
ATTRPlateGlobalPressure = 66
ATTRPlateEdgeRelease = 67
ATTRPlateThickness = 69
ATTRPlateNSMass = 70
ATTRLoadPatch = 71
ATTRPlatePointForce = 99
ATTRPlatePointMoment = 100
ATTRPlateFaceConvection = 101
ATTRPlateFaceRadiation = 102
ATTRPlateInfluence = 103
ATTRPlateSoilStress = 104
ATTRPlateSoilRatio = 105
ATTRPlateCreepLoadingAge = 106
ATTRPlateEdgeAttachment = 107
ATTRPlateFaceAttachment = 108
ATTRPlateStageProperty = 109

## Edge Types
etInterpolated = 0
etNonInterpolated = 1

## Plate/Face Global Pressure Projection Options
pfNone = 0
pfProjResultant = 1
pfProjComponents = 2

## Brick Attribute Types
ATTRBrickPressure = 81
ATTRBrickShear = 82
ATTRBrickFaceFoundation = 83
ATTRBrickConvection = 84
ATTRBrickRadiation = 85
ATTRBrickFlux = 86
ATTRBrickHeatSource = 87
ATTRBrickGlobalPressure = 88
ATTRBrickNSMass = 89
ATTRBrickLocalAxes = 90
ATTRBrickPreLoad = 91
ATTRBrickPointForce = 110
ATTRBrickInfluence = 111
ATTRBrickSoilStress = 112
ATTRBrickSoilRatio = 113
ATTRBrickCreepLoadingAge = 114
ATTRBrickFaceAttachment = 115
ATTRBrickStageProperty = 116

## Titles
TITLEModel = 0
TITLEProject = 1
TITLEReference = 2
TITLEAuthor = 3
TITLECreated = 4
TITLEModified = 5

## Table Types
ttVsTime = 1
ttVsTemperature = 2
ttVsFrequency = 3
ttStressStrain = 4
ttForceDisplacement = 5
ttMomentCurvature = 6
ttMomentRotation = 8
ttAccVsTime = 9
ttForceVelocity = 10
ttVsPosition = 11
ttStrainTime = 12

## Frequency Table Types
tyPeriod = 0
tyFrequency = 1

## Beam Prop Table Entries
ptBeamStiffModVsTemp = 1001
ptBeamAlphaVsTemp = 1002
ptBeamConductVsTemp = 1003
ptBeamCpVsTemp = 1004
ptBeamStiffModVsTime = 1005
ptBeamConductVsTime = 1006
ptSpringAxialVsDisp = 1007
ptSpringTorqueVsTwist = 1008
ptSpringAxialVsVelocity = 1009
ptTrussAxialStressVsStrain = 1010
ptBeamAxialStressVsStrain = 1011
ptBeamMomentK1 = 1012
ptBeamMomentK2 = 1013
ptConnectionShear1 = 1014
ptConnectionShear2 = 1015
ptConnectionAxial = 1016
ptConnectionBend1 = 1017
ptConnectionBend2 = 1018
ptConnectionTorque = 1019
ptBeamYieldVsTemp = 1020

## Plate Prop Table Entries
ptPlateModVsTemp = 2001
ptPlateAlphaVsTemp = 2002
ptPlateConductVsTemp = 2003
ptPlateCpVsTemp = 2004
ptPlateModVsTime = 2005
ptPlateConductVsTime = 2006
ptPlateStressVsStrain = 2007
ptPlateYieldVsTemp = 2008

## Brick Prop Table Entries
ptBrickModVsTemp = 3001
ptBrickAlphaVsTemp = 3002
ptBrickConductVsTemp = 3003
ptBrickCpVsTemp = 3004
ptBrickModVsTime = 3005
ptBrickConductVsTime = 3006
ptBrickStressVsStrain = 3007
ptBrickYieldVsTemp = 3008

## Creep Laws
clConcreteHyperbolic = 0
clConcreteViscoChain = 1
clConcreteUserDefined = 2
clPrimaryPower = 3
clSecondaryPower = 4
clPrimarySecondaryPower = 5
clSecondaryHyperbolic = 6
clSecondaryExponential = 7
clThetaProjection = 8
clGenGraham = 9
clGenBlackburn = 10
clUserDefined = 11

## Load Case Types
kNoInertia = 0
kGravity = 1
kAccelerations = 2

## Freedom Case Types
kNormalFreedom = 0
kFreeBodyInertiaRelief = 1
kSingleSymmetryInertiaXY = 2
kSingleSymmetryInertiaYZ = 3
kSingleSymmetryInertiaZX = 4
kDoubleSymmetryInertiaX = 5
kDoubleSymmetryInertiaY = 6
kDoubleSymmetryInertiaZ = 7

## Global Load and Freedom Cases
ipRefTemp = 0
ipGlobOrigX = 1
ipGlobOrigY = 2
ipGlobOrigZ = 3
ipGlobAccX = 4
ipGlobAccY = 5
ipGlobAccZ = 6
ipGlobAngVelX = 7
ipGlobAngVelY = 8
ipGlobAngVelZ = 9
ipGlobAngAccX = 10
ipGlobAngAccY = 11
ipGlobAngAccZ = 12

## Damping Types
dtNoDamping = 0
dtRayleighDamping = 1
dtModalDamping = 2
dtViscousDamping = 3

## Rayleigh Modes
rmSetFrequencies = 0
rmSetAlphaBeta = 1

## Entity Solver Result Types - HEAT
hrNodeFlux = 1
hrBeamFlux = 2
hrPlateFlux = 3
hrBrickFlux = 4

## Entity Solver Result Types - FREQUENCY
frBeamForcePattern = 5
frBeamStrainPattern = 6
frPlateStressPattern = 7
frPlateStrainPattern = 8
frBrickStressPattern = 9
frBrickStrainPattern = 10

## Entity Solver Result Types - STRUCTURAL
srNodeReaction = 11
srNodeVelocity = 12
srNodeAcceleration = 13
srBeamForce = 14
srBeamMNLStress = 15
srBeamStrain = 16
srPlateStress = 17
srPlateStrain = 18
srBrickStress = 19
srBrickStrain = 20
srElementNodeForce = 21

## Solver Defaults - LOGICALS
spDoSturm = 1
spNonlinearMaterial = 2
spNonlinearGeometry = 4
spAddKg = 6
spCalcDampingRatios = 8
spIncludeLinkReactions = 9
spFullSystemTransient = 10
spNonlinearHeat = 11
spLumpedLoadBeam = 12
spLumpedLoadPlate = 13
spLumpedLoadBrick = 14
spLumpedMassBeam = 15
spLumpedMassPlate = 16
spLumpedMassBrick = 17
spForceDrillCheck = 18
spSaveRestartFile = 20
spSaveIntermediate = 21
spExcludeMassX = 22
spExcludeMassY = 23
spExcludeMassZ = 24
spSaveSRSSSpectral = 25
spSaveCQCSpectral = 26
spDoResidualsCheck = 27
spSuppressAllSingularities = 28
spSaveModalResults = 29
spSpectralReactionAsInertia = 30
spReducedLogFile = 31
spIncludeRotationalMass = 32
spIgnoreCompressiveBeamKg = 33
spAutoScaleKg = 34
spScaleSupports = 36
spAutoShift = 37
spSaveTableInsertedSteps = 38
spSaveLastRestartStep = 39
spAutoAssignPathDivisions = 40
spDoInstantNTA = 41
spAllowExtraIterations = 42
spPredictImpact = 43

## Solver Defaults - INTEGERS
spTreeStartNumber = 1
spNumFrequency = 2
spNumBucklingModes = 3
spMaxIterationEig = 4
spMaxIterationNonlin = 5
spNumBeamSlicesSpectral = 6
spMaxConjugateGradientIter = 7
spMaxNumWarnings = 8
spFiniteStrainDefinition = 9
spBeamLength = 10
spFormStiffMatrix = 11
spMaxUpdateInterval = 12
spFormNonlinHeatStiffMatrix = 13
spExpandWorkingSet = 14
spMinNumViscoUnits = 15
spMaxNumViscoUnits = 16
spCurveFitTimeUnit = 17
spStaticAutoStepping = 18
spBeamKgType = 19
spDynamicAutoStepping = 20

## Solver Defaults - DOUBLES
spEigenTolerance = 1
spFrequencyShift = 2
spBucklingShift = 3
spNonlinDispTolerance = 4
spNonlinResidualTolerance = 5
spTransientReferenceTemperature = 6
spRelaxationFactor = 7
spNonlinHeatTolerance = 8
spMinimumTimeStep = 9
spWilsonTheta = 10
spNewmarkBeta = 11
spGlobalZeroDiagonal = 12
spConjugateGradientTol = 13
spMinimumDimension = 14
spMinimumInternalAngle = 15
spZeroForce = 16
spZeroDiagonal = 17
spZeroContactFactor = 18
spFrictionCutoffStrain = 19
spZeroTranslation = 20
spZeroRotation = 21
spDrillStiffFactor = 22
spMaxNormalsAngle = 24
spMaximumRotation = 26
spZeroDisplacement = 27
spMaximumDispRatio = 28
spMinimumLoadReductionFactor = 29
spMaxDispChange = 30
spMaxResidualChange = 31
spZeroFrequency = 32
spZeroBucklingEigen = 33
spCurveFitTime = 34
spSpacingBias = 35
spTimeStepParam = 36
spSlidingFrictionFactor = 37
spMNLTangentRatio = 38
spStickingFrictionFactor = 39
spMinArcLengthFactor = 40
spMaxFibreStrainInc = 41

## Modal Load Types
mtBaseAcc = 0
mtBaseVel = 1
mtBaseDisp = 2
mtAppliedLoad = 3

## Solver Types
stSkyline = 0
stSparse = 1
stIterativePCG = 3

## Solver Temperature Types
tdNone = 0
tdCombined = 1

## Harmonic Load Types
htVsFrequency = 0
htVsTime = 1

## Sort Types
rnNone = 0
rnTree = 1
rnGeometry = 2
rnAMD = 3

## Utility
ztAbsolute = 0
ztRelative = 1

## Boolean Types
btFalse = 0
btTrue = 1

## Error Codes
ERR7_InvalidRegionalSettings = -6
ERR7_InvalidDLLsPresent = -5
ERR7_APINotInitialised = -4
ERR7_InvalidErrorCode = -3
ERR7_APINotLicensed = -2
ERR7_UnknownError = -1
ERR7_NoError = 0
ERR7_FileAlreadyOpen = 1
ERR7_FileNotFound = 2
ERR7_FileNotSt7 = 3
ERR7_InvalidFileName = 4
ERR7_FileIsNewer = 5
ERR7_CannotReadFile = 6
ERR7_InvalidScratchPath = 7
ERR7_FileNotOpen = 8
ERR7_ExceededTotal = 9
ERR7_DataNotFound = 10
ERR7_InvalidResultFile = 11
ERR7_ResultFileNotOpen = 12
ERR7_ExceededResultCase = 13
ERR7_UnknownResultType = 14
ERR7_UnknownResultLocation = 15
ERR7_UnknownSurfaceLocation = 16
ERR7_UnknownProperty = 17
ERR7_InvalidEntity = 18
ERR7_InvalidBeamPosition = 19
ERR7_InvalidLoadCase = 20
ERR7_InvalidFreedomCase = 21
ERR7_UnknownTitle = 22
ERR7_UnknownUCS = 23
ERR7_TooManyBeamStations = 24
ERR7_UnknownSubType = 25
ERR7_GroupIdDoesNotExist = 26
ERR7_InvalidFileUnit = 27
ERR7_CannotSaveFile = 28
ERR7_ResultFileIsOpen = 29
ERR7_InvalidUnits = 30
ERR7_InvalidEntityNodes = 31
ERR7_InvalidUCSType = 32
ERR7_InvalidUCSID = 33
ERR7_UCSIDAlreadyExists = 34
ERR7_CaseNameAlreadyExists = 35
ERR7_InvalidEntityNumber = 36
ERR7_InvalidBeamEnd = 37
ERR7_InvalidBeamDir = 38
ERR7_InvalidPlateEdge = 39
ERR7_InvalidBrickFace = 40
ERR7_InvalidBeamType = 41
ERR7_InvalidPlateType = 42
ERR7_InvalidMaterialType = 43
ERR7_PropertyAlreadyExists = 44
ERR7_InvalidBeamSectionType = 45
ERR7_PropertyNotSpring = 46
ERR7_PropertyNotCable = 47
ERR7_PropertyNotTruss = 48
ERR7_PropertyNotCutOffBar = 49
ERR7_PropertyNotPointContact = 50
ERR7_PropertyNotBeam = 51
ERR7_PropertyNotPipe = 52
ERR7_PropertyNotConnectionBeam = 53
ERR7_InvalidSectionParameters = 54
ERR7_PropertyNotUserDefinedBeam = 55
ERR7_MaterialIsUserDefined = 56
ERR7_MaterialNotIsotropic = 57
ERR7_MaterialNotOrthotropic = 58
ERR7_InvalidRubberModel = 59
ERR7_MaterialNotRubber = 60
ERR7_InvalidSectionProperties = 61
ERR7_PlateDoesNotHaveThickness = 62
ERR7_IncompatibleMaterialCombination = 63
ERR7_UnknownSolver = 64
ERR7_InvalidSolverMode = 65
ERR7_InvalidMirrorOption = 66
ERR7_SectionCannotBeMirrored = 67
ERR7_InvalidTableType = 68
ERR7_InvalidTableName = 69
ERR7_TableNameAlreadyExists = 70
ERR7_InvalidNumberOfEntries = 71
ERR7_InvalidZipType = 72
ERR7_TableDoesNotExist = 73
ERR7_NotFrequencyTable = 74
ERR7_InvalidFrequencyType = 75
ERR7_InvalidTableSetting = 76
ERR7_IncompatibleTableType = 77
ERR7_IncompatibleCriterionCombination = 78
ERR7_InvalidModalFile = 79
ERR7_InvalidCombinationCaseNumber = 80
ERR7_InvalidInitialCaseNumber = 81
ERR7_InvalidInitialFile = 82
ERR7_InvalidModeNumber = 83
ERR7_BeamIsNotBXS = 84
ERR7_InvalidDampingType = 85
ERR7_InvalidRayleighMode = 86
ERR7_CannotReadBXS = 87
ERR7_InvalidResultType = 88
ERR7_InvalidSolverParameter = 89
ERR7_InvalidModalLoadType = 90
ERR7_InvalidTimeRow = 91
ERR7_SparseSolverNotLicenced = 92
ERR7_InvalidSolverScheme = 93
ERR7_InvalidSortOption = 94
ERR7_IncompatibleResultFile = 95
ERR7_InvalidLinkType = 96
ERR7_InvalidLinkData = 97
ERR7_OnlyOneLoadCase = 98
ERR7_OnlyOneFreedomCase = 99
ERR7_InvalidLoadID = 100
ERR7_InvalidBeamLoadType = 101
ERR7_InvalidStringID = 102
ERR7_InvalidPatchType = 103
ERR7_IncrementDoesNotExist = 104
ERR7_InvalidLoadCaseType = 105
ERR7_InvalidFreedomCaseType = 106
ERR7_InvalidHarmonicLoadType = 107
ERR7_InvalidTemperatureType = 108
ERR7_InvalidPatchTypeForPlate = 109
ERR7_InvalidAttributeType = 110
ERR7_MaterialNotAnisotropic = 111
ERR7_InvalidMatrixType = 112
ERR7_MaterialNotUserDefined = 113
ERR7_InvalidIndex = 114
ERR7_InvalidContactType = 115
ERR7_InvalidContactSubType = 116
ERR7_InvalidCutoffType = 117
ERR7_ResultQuantityNotAvailable = 118
ERR7_YieldNotMCDP = 119
ERR7_CombinationDoesNotExist = 120
ERR7_InvalidSeismicCase = 121
ERR7_InvalidImportExportMode = 122
ERR7_CannotReadImportFile = 123
ERR7_InvalidAnsysImportFormat = 124
ERR7_InvalidAnsysArrayStatus = 125
ERR7_CannotWriteExportFile = 126
ERR7_InvalidAnsysExportFormat = 127
ERR7_InvalidAnsysEndReleaseOption = 128
ERR7_InvalidAnsysExportUnits = 129
ERR7_InvalidSt7ExportFormat = 130
ERR7_InvalidUVPos = 131
ERR7_InvalidResponseType = 132
ERR7_InvalidLayoutID = 133
ERR7_InvalidPlateSurface = 134
ERR7_MeshingErrors = 135
ERR7_InvalidZipTolerance = 136
ERR7_InvalidTaperAxis = 137
ERR7_InvalidTaperType = 138
ERR7_InvalidTaperRatio = 139
ERR7_InvalidPositionType = 140
ERR7_InvalidPreLoadType = 141
ERR7_InvalidVertexType = 142
ERR7_InvalidVertexMeshSize = 143
ERR7_InvalidGeometryEdgeType = 144
ERR7_InvalidPropertyNumber = 145
ERR7_InvalidFaceSurface = 146
ERR7_InvalidModType = 147
ERR7_MaterialNotSoil = 148
ERR7_MaterialNotFluid = 149
ERR7_SoilTypeNotDC = 150
ERR7_SoilTypeNotCC = 151
ERR7_MaterialNotLaminate = 152
ERR7_InvalidLaminateID = 153
ERR7_LaminateNameAlreadyExists = 154
ERR7_LaminateIDAlreadyExists = 155
ERR7_PlyDoesNotExist = 156
ERR7_ExceededMaxNumPlies = 157
ERR7_LayoutIDAlreadyExists = 158
ERR7_InvalidNumModes = 159
ERR7_InvalidLTAMethod = 160
ERR7_InvalidLTASolutionType = 161
ERR7_ExceededMaxNumStages = 162
ERR7_StageDoesNotExist = 163
ERR7_ExceededMaxNumSpectralCases = 164
ERR7_InvalidSpectralCase = 165
ERR7_InvalidSpectrumType = 166
ERR7_InvalidResultsSign = 167
ERR7_InvalidPositionTableAxis = 168
ERR7_InvalidInitialConditionsType = 169
ERR7_ExceededMaxNumNodeHistory = 170
ERR7_NodeHistoryDoesNotExist = 171
ERR7_InvalidTransientTempType = 172
ERR7_InvalidTimeUnit = 173
ERR7_InvalidLoadPath = 174
ERR7_InvalidTempDependenceType = 175
ERR7_InvalidTrigType = 176
ERR7_InvalidUserEquation = 177
ERR7_InvalidCreepID = 178
ERR7_CreepIDAlreadyExists = 179
ERR7_InvalidCreepLaw = 180
ERR7_InvalidCreepHardeningLaw = 181
ERR7_InvalidCreepViscoChainRow = 182
ERR7_InvalidCreepFunctionType = 183
ERR7_InvalidCreepShrinkageType = 184
ERR7_InvalidTableRow = 185
ERR7_ExceededMaxNumRows = 186
ERR7_InvalidLoadPathTemplateID = 187
ERR7_LoadPathTemplateIDAlreadyExists = 188
ERR7_InvalidLoadPathLane = 189
ERR7_ExceededMaxNumLoadPathTemplates = 190
ERR7_ExceededMaxNumLoadPathVehicles = 191
ERR7_InvalidLoadPathVehicle = 192
ERR7_InvalidMobilityType = 193
ERR7_InvalidAxisSystem = 194
ERR7_InvalidLoadPathID = 195
ERR7_LoadPathIDAlreadyExists = 196
ERR7_InvalidPathDefinition = 197
ERR7_InvalidLoadPathShape = 198
ERR7_InvalidLoadPathSurface = 199
ERR7_InvalidNumPathDivs = 200
ERR7_InvalidGeometryCavityLoop = 201
ERR7_InvalidLimitEnvelope = 202
ERR7_ExceededMaxNumLimitEnvelopes = 203
ERR7_InvalidCombEnvelope = 204
ERR7_ExceededMaxNumCombEnvelopes = 205
ERR7_InvalidFactorsEnvelope = 206
ERR7_ExceededMaxNumFactorsEnvelopes = 207
ERR7_InvalidLimitEnvelopeType = 208
ERR7_InvalidCombEnvelopeType = 209
ERR7_InvalidFactorsEnvelopeType = 210
ERR7_InvalidCombEnvelopeAccType = 211
ERR7_InvalidEnvelopeSet = 212
ERR7_ExceededMaxNumEnvelopeSets = 213
ERR7_InvalidEnvelopeSetType = 214
ERR7_InvalidCombResFile = 215
ERR7_ExceededMaxNumCombResFiles = 216
ERR7_CannotCombResFiles = 217
ERR7_InvalidStartEndTimes = 218
ERR7_InvalidNumSteps = 219
ERR7_InvalidLibraryPath = 220
ERR7_InvalidLibraryType = 221
ERR7_InvalidLibraryID = 222
ERR7_InvalidLibraryName = 223
ERR7_InvalidLibraryItemID = 224
ERR7_InvalidLibraryItemName = 225
ERR7_InvalidDisplayOptionsPath = 226
ERR7_InvalidSolverPath = 227
ERR7_InvalidCementHardeningType = 228
ERR7_ZeroPlateElements = 229
ERR7_CannotMakeBXS = 230
ERR7_CannotCalculateBXSData = 231
ERR7_InvalidSurfaceMeshTargetType = 232
ERR7_InvalidModalNodeReactType = 233
ERR7_InvalidAxis = 234
ERR7_InvalidBeamAxisType = 235
ERR7_InvalidStaadCountryCodeOption = 236
ERR7_InvalidGeometryFormatProtocol = 237
ERR7_InvalidDXFBeamOption = 238
ERR7_InvalidDXFPlateOption = 239
ERR7_InvalidLoadPathLaneFactorType = 240
ERR7_InvalidLoadPathVehicleInstance = 241
ERR7_InvalidNumBeamStations = 242
ERR7_ResFileUnsupportedType = 243
ERR7_ResFileAlreadyOpen = 244
ERR7_ResFileInvalidNumCases = 245
ERR7_ResFileNotOpen = 246
ERR7_ResFileInvalidCase = 247
ERR7_ResFileDoesNotHaveEntity = 248
ERR7_ResFileInvalidQuantity = 249
ERR7_ResFileQuantityNotExist = 250
ERR7_ResFileCantSave = 251
ERR7_ResFileCantClearQuantity = 252
ERR7_ResFileContainsNoElements = 253
ERR7_ResFileContainsNoNodes = 254
ERR7_ResFileInvalidName = 255
ERR7_ResFileAssociationNotAllowed = 256
ERR7_ResFileIncompatibleQuantity = 257
ERR7_CannotEditSolverFiles = 258
ERR7_CannotOpenResultFile = 259
ERR7_CouldNotShowModelWindow = 260
ERR7_ModelWindowWasNotShowing = 261
ERR7_CantDoWithModalWindows = 262
ERR7_InvalidSelectionEndEdgeFace = 263
ERR7_CouldNotCreateModelWindow = 264
ERR7_ModelWindowWasNotCreated = 265
ERR7_InvalidImageType = 266
ERR7_InvalidImageDimensions = 267
ERR7_InsufficientRamToCreateImage = 268
ERR7_CannotSaveImageFile = 269
ERR7_InvalidWindowDimensions = 270
ERR7_InvalidResultQuantity = 271
ERR7_InvalidResultSubQuantity = 272
ERR7_InvalidComponent = 273
ERR7_ResultIsNotAvailable = 274
ERR7_InvalidUCSIndex = 275
ERR7_InvalidDiagramAxis = 276
ERR7_InvalidVectorComponents = 277
ERR7_TableTypeIsNotTimeBased = 278
ERR7_InvalidTableID = 279
ERR7_LinkNotMasterSlave = 280
ERR7_LinkNotSectorSymmetry = 281
ERR7_LinkNotCoupling = 282
ERR7_LinkNotPinned = 283
ERR7_LinkNotRigid = 284
ERR7_LinkNotShrink = 285
ERR7_LinkNotTwoPoint = 286
ERR7_LinkNotAttachment = 287
ERR7_LinkNotMultiPoint = 288
ERR7_InvalidCoupleType = 289
ERR7_InvalidRigidPlane = 290
ERR7_InvalidMultiPointFactorsType = 291
ERR7_InvalidMultiPointLink = 292
ERR7_InvalidAttachmentType = 293
ERR7_ExceededMaxNumColumns = 294
ERR7_CouldNotDestroyModelWindow = 295
ERR7_CannotSetWindowParent = 296
ERR7_InvalidLoadCaseFilePath = 297
ERR7_InvalidStaadLengthUnit = 298
ERR7_InvalidStaadForceUnit = 299
ERR7_InvalidDuplicateFaceType = 300
ERR7_InvalidNodeCoordinateKeepType = 301
ERR7_CommentDoesNotExist = 302
ERR7_InvalidFilePath = 303
ERR7_InvalidContactYieldType = 304
ERR7_InvalidNumMeshingLoops = 305
ERR7_InvalidMeshPositionOnUCS = 306
ERR7_InvalidK0Expression = 307
ERR7_InvalidK1Expression = 308
ERR7_NoPatchLoadsCreated = 309
ERR7_InvalidResOptsBeamEnvelope = 310
ERR7_InvalidResOptsRotationUnit = 311
ERR7_InvalidResOptsHRASetting = 312
ERR7_InvalidResOptsStageDisplacement = 313
ERR7_InvalidToolOptsZipOptions = 314
ERR7_InvalidToolOptsSubdivideOptions = 315
ERR7_InvalidToolOptsCopyOptions = 316
ERR7_InvalidToleranceType = 317
ERR7_InvalidAttachPartsParams = 318
ERR7_InvalidDrawParameters = 319
ERR7_FilesStillOpen = 320
ERR7_SolverStillRunning = 321
ERR7_InvalidPolygonToFaceParameters = 322
ERR7_InvalidResOptsStrainUnit = 323
ERR7_FunctionNotSupported = 324
ERR7_SoilTypeNotMC = 325
ERR7_SoilTypeNotDP = 326
ERR7_TooManyAnimations = 327
ERR7_InvalidAnimationFile = 328
ERR7_InvalidAnimationMode = 329
ERR7_InsufficientFrames = 330
ERR7_AnimationDimensionsTooSmall = 331
ERR7_AnimationDimensionsTooLarge = 332
ERR7_ReducedAnimation = 333
ERR7_InvalidAnimationType = 334
ERR7_CannotFindStubFile = 335
ERR7_CouldNotSaveAnimationFile = 336
ERR7_AnimationHandleOutOfRange = 337
ERR7_AnimationNotRunning = 338
ERR7_SoilTypeNotLS = 339
ERR7_NoPolygonWasConverted = 340
ERR7_InvalidAlphaTempType = 341
ERR7_InvalidGravityDirection = 342
ERR7_InvalidAttachmentDirection = 343
ERR7_InvalidHardeningType = 344
ERR7_ResultCaseNotInertiaRelief = 345
ERR7_InvalidNumLayers = 346
ERR7_PlateDoesNotHaveLayers = 347
ERR7_ToolOperationFailed = 348

## Solver Error Codes
SE_NoLoadCaseSelected = 1001
SE_IncompatibleRestartFile = 1002
SE_ElementUsesInvalidProperty = 1003
SE_InvalidElement = 1004
SE_NeedNonlinearHeatSolver = 1005
SE_TableNotFound = 1006
SE_InvalidRestartFile = 1007
SE_InvalidInitialFile = 1008
SE_InvalidSolverResultFile = 1009
SE_InvalidLink = 1010
SE_InvalidPlateCohesionValue = 1011
SE_InvalidBrickCohesionValue = 1012
SE_NonlinearSolverRequired = 1013
SE_NoLoadTablesDefined = 1014
SE_NoVelocityDataInInitialFile = 1015
SE_NoModesIncluded = 1016
SE_InvalidTimeStep = 1017
SE_LoadIncrementsNotDefined = 1018
SE_NoFreedomCaseInIncrements = 1019
SE_InvalidInitialTemperatureFile = 1020
SE_InvalidFrequencyRange = 1021
SE_ModelMixesAxiNonAxi = 1022
SE_CompositeModuleNotAvailable = 1023
SE_CannotFindSolver = 1024
SE_UnknownException = 1025
SE_DuplicateLinks = 1026
SE_CannotAppendToFile = 1027
SE_CannotOverwriteFile = 1028
SE_CannotWriteToResultFile = 1029
SE_CannotWriteToLogFile = 1030
SE_CannotReadRestartFile = 1031
SE_InitialConditionsNotValid = 1032
SE_InvalidRayleighFactors = 1033
SE_ShearPanelMustBeQuad4 = 1035
SE_SingularPlateMatrix = 1036
SE_SingularBrickMatrix = 1037
SE_NoBeamProperties = 1038
SE_NoPlateProperties = 1039
SE_NoBrickProperties = 1040
SE_MoreLoadIncrementsNeeded = 1041
SE_RubberRequiresGNL = 1042
SE_NoFreedomCaseSelected = 1043
SE_InvalidSpectralVectors = 1044
SE_NoSpectralResultsSelected = 1045
SE_SpectralFactorsNotDefined = 1046
SE_SpectralFactorsAllZero = 1047
SE_NoTimeStepsSaved = 1048
SE_InvalidDirectionVector = 1049
SE_HarmonicFactorsAllZero = 1050
SE_TemperatureDependenceCaseNotSet = 1051
SE_ZeroLengthRigidLinkGenerated = 1052
SE_InvalidStringGroupDefinition = 1053
SE_InvalidPreTensionOnString = 1054
SE_StringOrderHasChanged = 1055
SE_BadTaperData = 1056
SE_TaperedPlasticBeams = 1057
SE_NoMovingLoadPathsInCases = 1058
SE_NoResponseVariablesDefined = 1059
SE_InvalidPlateVariableRequested = 1060
SE_InvalidGravityCase = 1061
SE_InvalidUserPlateCreepDefinition = 1062
SE_InvalidUserBrickCreepDefinition = 1063
SE_InvalidPlateShrinkageDefinition = 1064
SE_InvalidBrickShrinkageDefinition = 1065
SE_InvalidLaminateID = 1066
SE_CannotReadWriteScratchPath = 1067
SE_CannotConvertAttachmentLink = 1068
SE_SoilRequiresMNL = 1069
SE_ActiveStageHasNoIncrements = 1070
SE_ConcreteCreepMNL = 1071
SE_CannotConvertInterpMultiPoint = 1072
SE_MissingInsituStress = 1073
SE_InvalidMaterialNonlinearString = 1074
SE_TensileInsituPlateStress = 1075
SE_TensileInsituBrickStress = 1076
SE_IncompatibleRestartUnits = 1077
SE_CreepTimeTooShort = 1078
SE_InvalidElements = 1079
SE_InsufficientRestartFileSteps = 1080
SE_NeedNodeTempNTASolver = 1081
SE_SingleShotRestartFile = 1082
SE_SkylineUsesBadSort = 1083
SE_StagedSolutionFileNotFound = 1084
SE_NeedTemperatureTables = 1085
SE_AttachmentsInWrongGroup = 1086
SE_StagingHasChanged = 1087
SE_NoNodes = 1088
SE_CQCRequiresDamping = 1089

## Other Constants
kMaxPlateResult = 1024
kMaxBrickResult = 1024
kMaxBeamRelease = 12
kMaxDisp = 6
kAllStations = 20

## UCS
kMaxUCSDoubles = 10

## Solvers
stLinearStaticSolver = 1
stLinearBucklingSolver = 2
stNonlinearStaticSolver = 3
stNaturalFrequencySolver = 4
stHarmonicResponseSolver = 5
stSpectralResponseSolver = 6
stLinearTransientDynamicSolver = 7
stNonlinearTransientDynamicSolver = 8
stSteadyHeatSolver = 9
stTransientHeatSolver = 10
stLoadInfluenceSolver = 11
stQuasiStaticSolver = 12

## Solver Modes
smNormalRun = 1
smProgressRun = 2
smBackgroundRun = 3
smNormalCloseRun = 4

## Primary Load Case
ipLoadCaseDefRefTemp = 0
ipLoadCaseDefOriginX = 1
ipLoadCaseDefOriginY = 2
ipLoadCaseDefOriginZ = 3
ipLoadCaseDefLinAccX = 4
ipLoadCaseDefLinAccY = 5
ipLoadCaseDefLinAccZ = 6
ipLoadCaseDefAngVelX = 7
ipLoadCaseDefAngVelY = 8
ipLoadCaseDefAngVelZ = 9
ipLoadCaseDefAngAccX = 10
ipLoadCaseDefAngAccY = 11
ipLoadCaseDefAngAccZ = 12

## Seismic Load Case
ipSeismicCaseDefAlpha = 0
ipSeismicCaseDefPhi = 1
ipSeismicCaseDefBeta = 2
ipSeismicCaseDefK = 3
ipSeismicCaseDefh0 = 4
ipSeismicCaseDefDir = 5
ipSeismicCaseDefLinAcc = 6
ipSeismicCaseDefV1 = 7
ipSeismicCaseDefV2 = 8

## Import/Export Modes
ieQuietRun = 0
ieProgressRun = 1

## NASTRAN
ipNASTRANImportUnits = 0
ipNASTRANFreedomCase = 0
ipNASTRANLoadCase = 1
ipNASTRANSolver = 2
ipNASTRANExportUnits = 3
ipNASTRANBeamStressSections = 4
ipNASTRANBeamSectionGeometry = 5
ipNASTRANExportHeatTransfer = 6
ipNASTRANExportNSMass = 7
ipNASTRANExportUnusedProps = 8
ipNASTRANTemperatureCase = 9
ipNASTRANExportZeroFields = 0
ieNASTRANSolverLSA = 0
ieNASTRANSolverNFA = 1
ieNASTRANSolverLBA = 2
ieNASTRANExportGeometryProps = 0
ieNASTRANExportPropsOnly = 1
naUnits_kg_N_m = 0
naUnits_T_N_mm = 1
naUnits_sl_lbf_ft = 2
naUnits_lbm_lbf_in = 3
naUnits_sl_lbf_in = 4
naUnits_NoUnits = 5

## ANSYS
ipANSYSImportFormat = 0
ipANSYSArrayParameters = 1
ipANSYSImportLoadCaseFiles = 2
ipANSYSImportIGESEntities = 3
ipANSYSFixElementConnectivity = 4
ipANSYSRemoveDuplicateProps = 5
ipANSYSExportFormat = 0
ipANSYSFreedomCase = 1
ipANSYSLoadCase = 2
ipANSYSUnits = 3
ipANSYSEndRelease = 4
ipANSYSExportNonlinearMat = 5
ipANSYSExportHeatTransfer = 6
ipANSYSExportPreLoadNSMass = 7
ipANSYSExportTetraOption = 8
ieANSYSBatchImport = 0
ieANSYSCDBImport = 1
ieANSYSBatchCDBImport = 2
ieANSYSBatch1Export = 0
ieANSYSBatch3Export = 1
ieANSYSBlockedCDBExport = 2
ieANSYSUnblockedCDBExport = 3
ieANSYSArrayOverwrite = 0
ieANSYSArrayIgnore = 1
ieANSYSArrayPrompt = 2
ieANSYSEndReleaseFixed = 0
ieANSYSEndReleaseFull = 1
anUnits_NoUnits = 0
anUnits_kg_m_C = 1
anUnits_g_cm_C = 2
anUnits_T_mm_C = 3
anUnits_sl_ft_F = 4
anUnits_lbm_in_F = 5

## STAAD
ipSTAADCountryType = 0
ipSTAADIncludeSectionLibrary = 1
ipSTAADStripUnderscore = 2
ipSTAADStripSectionSpaces = 3
ipSTAADLengthUnit = 4
ipSTAADForceUnit = 5
ieSTAADAmericanCode = 0
ieSTAADAustralianCode = 1
ieSTAADBritishCode = 2
sdLengthUnit_in = 0
sdLengthUnit_ft = 1
sdLengthUnit_cm = 2
sdLengthUnit_m = 3
sdLengthUnit_mm = 4
sdLengthUnit_dm = 5
sdLengthUnit_km = 6
sdForceUnit_kip = 0
sdForceUnit_lbf = 1
sdForceUnit_kgf = 2
sdForceUnit_MTf = 3
sdForceUnit_N = 4
sdForceUnit_kN = 5
sdForceUnit_MN = 6
sdForceUnit_dN = 7

## SAP2000
ipSAP2000ConvertBlackTo = 0
ipSAP2000DecimalSeparator = 1
ipSAP2000ThousandSeparator = 2
ipSAP2000MergeDuplicateFreedomSets = 3
ieSAP2000Period = 0
ieSAP2000Comma = 1
ieSAP2000Space = 2
ieSAP2000None = 3

## ST7
ieSt7ExportCurrent = 0
ieSt7Export106 = 1
ieSt7Export21x = 2
ieSt7Export22x = 3
ieSt7Export23x = 4

## GEOMETRY
ipImportGeomProp = 0
ipImportGeomCurvesToBeams = 1
ipImportGeomGroupsAs = 2
ipImportGeomColourAsProperty = 3
ipImportGeomBlackReplacement = 4
ipImportGeomACISBodiesAsGroups = 5
ipImportGeomLengthUnit = 6
ipExportGeomColour = 0
ipExportGeomGroupsAsLevels = 1
ipExportGeomFullGroupPath = 2
ipExportGeomFormatProtocol = 3
ipExportGeomCurve = 4
ipExportGeomPeriodicFace = 5
ipExportGeomKeepAnalytic = 6
ipImportGeomTol = 0
luGeomNONE = -1
luGeomINCH = 0
luGeomMILLIMETRE = 1
luGeomFEET = 2
luGeomMILES = 3
luGeomMETRE = 4
luGeomKILOMETRE = 5
luGeomMIL = 6
luGeomMICRON = 7
luGeomCENTIMETRE = 8
luGeomMICROINCH = 9
luGeomUNSPECIFIED = 10

## Geometry Groups
ggNone = 0
ggAuto = 1
ggSubfigures = 2
ggLevels = 3
ggAssemblies = 1

## IGES Formats
ifBoundedSurface = 0
ifTrimmedParametricSurface = 1
ifOpenShell = 2
ifManifoldSolidBRep = 3

## STEP Protocols
spConfigControlDesign = 0
spAutomotiveDesign = 1

## GEOMETRY Export Format Options
ieModelOnly = 0
ieParameterOnly = 1
ieModelPreferred = 2
ieParameterPreferred = 3
ieSeamOnlyAsRequired = 0
ieSplitOnFaceBoundary = 1
ieSplitIntoHalves = 2
ieColourNone = 0
ieFaceColour = 1
ieGroupColour = 2
iePropertyColour = 3

## DXF Options
ipDXFImportFrozenLayers = 0
ipDXFImportLayersAsGroups = 1
ipDXFImportColoursAsProps = 2
ipDXFImportPolylineAsPlates = 3
ipDXFImportPolygonAsBricks = 4
ipDXFImportSegmentsPerCircle = 5
ipDXFExportPlatesBricks3DFaces = 0
ipDXFExportGroupsAsLayers = 1
ipDXFExportPropColoursAsEntityColours = 2
ipDXFExportBeamsAs = 3
ipDXFExportPlatesAs = 4
bmLine = 0
bmSection = 1
bmSolid = 2
plSurface = 0
plSolid = 1

## Geometry Groups Settings
grNone = 0
grAuto = 1
grSubfigures = 2
grLevels = 3
grAssembly = 1

## BXS
ipBXSXBar = 0
ipBXSYBar = 1
ipBXSArea = 2
ipBXSI11 = 3
ipBXSI22 = 4
ipBXSAngle = 5
ipBXSZ11Plus = 6
ipBXSZ11Minus = 7
ipBXSZ22Plus = 8
ipBXSZ22Minus = 9
ipBXSS11 = 10
ipBXSS22 = 11
ipBXSr1 = 12
ipBXSr2 = 13
ipBXSSA1 = 14
ipBXSSA2 = 15
ipBXSSL1 = 16
ipBXSSL2 = 17
ipBXSIXX = 18
ipBXSIYY = 19
ipBXSIXY = 20
ipBXSIxxL = 21
ipBXSIyyL = 22
ipBXSIxyL = 23
ipBXSZxxPlus = 24
ipBXSZxxMinus = 25
ipBXSZyyPlus = 26
ipBXSZyyMinus = 27
ipBXSSxx = 28
ipBXSSyy = 29
ipBXSrx = 30
ipBXSry = 31
ipBXSJ = 32
ipBXSIw = 33

## GEOMETRY CLEAN - DOUBLES
ipGeometryAccuracy = 0
ipGeometryFeatureLength = 1
ipGeometryEdgeMergeAngle = 2

## GEOMETRY CLEAN - INTEGERS
ipGeometryAccuracyType = 0
ipGeometryFeatureType = 1
ipGeometryActOnWholeModel = 2
ipGeometryFreeEdgesOnly = 3
ipGeometryDuplicateFaces = 4
dfGeometryLeave = 0
dfGeometryDeleteOne = 1
dfGeometryDeleteBoth = 2

## MESH CLEAN - DOUBLES
ipMeshTolerance = 0

## MESH CLEAN - INTEGERS
ipMeshToleranceType = 0
ipZipNodes = 1
ipRemoveDuplicateElements = 2
ipFixElementConnectivity = 3
ipDeleteFreeNodes = 4
ipDoBeams = 5
ipDoPlates = 6
ipDoBricks = 7
ipDoLinks = 8
ipZeroLengthLinks = 9
ipZeroLengthBeams = 10
ipNodeAttributeKeep = 11
ipNodeCoordinates = 12
ipAllowDifferentProps = 13
ipActOnWholeModel = 14
dfLeaveAll = 0
dfLeaveOne = 1
dfLeaveNone = 2

## Attribute keep
naLower = 0
naHigher = 1
naAccumulate = 2

## Node coordinates
ncAverage = 0
ncLowerNode = 1
ncHigherNode = 2
ncSelectedNode = 3

## SURFACE MESHING - INTEGERS
ipSurfaceMeshMode = 0
ipSurfaceMeshSizeMode = 1
ipSurfaceMeshTargetNodes = 2
ipSurfaceMeshTargetPropertyID = 3
ipSurfaceMeshAutoCreateProperties = 4
ipSurfaceMeshMinEdgesPerCircle = 5
ipSurfaceMeshApplyTransitioning = 6
ipSurfaceMeshAllowUserStop = 7
ipSurfaceMeshConsiderNearVertex = 8
mmAuto = 0
mmCustom = 1
smPercentage = 0
smAbsolute = 1

## SURFACE MESHING - DOUBLES
ipSurfaceMeshSize = 0
ipSurfaceMeshLengthRatio = 1
ipSurfaceMeshMaximumIncrease = 2
ipSurfaceMeshOnEdgesLongerThan = 3

## TETRA MESHING
ipTetraMeshSize = 0
ipTetraMeshProperty = 1
ipTetraMeshInc = 2
ipTetraMesh10 = 3
ipTetraMeshGroupsAsSolids = 4
ipTetraMeshSmooth = 5
ipTetraMeshAutoCreateProperties = 7
ipTetraMeshDeletePlates = 8
ipTetraMeshMultiBodyOption = 9
ipTetraMeshAllowUserStop = 10
ipTetraMeshCheckSelfIntersect = 11
msFine = 1
msMedium = 2
msCoarse = 3
mbCancelMeshing = 0
mbCavity = 1
mbSeparateSolids = 2

## Polygon Meshing
ipMeshTargetNodes = 0
ipMeshTargetPropertyID = 1
ipMeshUCSID = 2
ipMeshGroupID = 3
ipMeshPositionUCS = 0

## IMAGE TYPES
itBitmap8Bit = 1
itBitmap16Bit = 2
itBitmap24Bit = 3
itJPEG = 4

## WINDOW POPUP MENU GROUPS
imView = 1
imDisplay = 2
imShow = 3
imSelect = 4
imResults = 5

## WINDOW STATE
wsModelWindowNotCreated = 0
wsModelWindowVisible = 1
wsModelWindowMaximised = 2
wsModelWindowMinimised = 3
wsModelWindowHidden = 4

## Entity Display Settings - Node
ipNodeSelectedColour = 0
ipNodeUnselectedColour = 1
ipNodeShowFree = 2
ipNodeNumberMode = 3
ipNodeSymbol = 4

## Entity Display Settings - Beam
ipBeamDisplay = 0
ipBeamShowRefNode = 1
ipBeamShowOffset = 2
ipBeamMoveToOffset = 3
ipBeamLightShade = 4
ipBeamGlobalColour = 5
ipBeamOutlineColour = 6
ipBeamEnd1Colour = 7
ipBeamEnd2Colour = 8
ipBeamRefNodeColour = 9
ipBeamFilledMode = 10
ipBeamContour = 11
ipBeamShrink = 12
ipBeamRoundFacets = 13
ipBeamSpringCoils = 14
ipBeamSpringAspect = 15
ipBeamThickness = 16
ipBeamSections = 17
ipBeamOutlines = 18
ipBeamShowAxes = 19
ipBeamNumberMode = 20

## Entity Display Settings - Plate
ipPlateDisplay = 0
ipPlateLightShade = 1
ipPlateGlobalColour = 2
ipPlateOutlineColour = 3
ipPlateZPlusColour = 4
ipPlateZMinusColour = 5
ipPlateOffsetColour = 6
ipPlateFilledMode = 7
ipPlateContour = 8
ipPlateShrink = 9
ipPlateOutlines = 10
ipPlateOutlineThickness = 11
ipPlateShowAxes = 12
ipPlateAxisOnPly = 13
ipPlateOffset = 14
ipPlateMoveToOffset = 15
ipPlateNumberMode = 16

## Entity Display Settings - Brick
ipBrickLightShade = 0
ipBrickGlobalColour = 1
ipBrickOutlineColour = 2
ipBrickFilledMode = 3
ipBrickContour = 4
ipBrickShrink = 5
ipBrickOutlines = 6
ipBrickOutlineThickness = 7
ipBrickShowFreeFaces = 8
ipBrickAxes1 = 9
ipBrickAxes2 = 10
ipBrickAxes3 = 11
ipBrickNumberMode = 12
ipBrickShowAllFaces = 13

## Entity Display Settings - Link
ipLinkGlobalColour = 0
ipLinkMasterSlaveColour = 1
ipLinkSectorSymmColour = 2
ipLinkCouplingColour = 3
ipLinkPinnedColour = 4
ipLinkRigidColour = 5
ipLinkShrinkColour = 6
ipLinkTwoPointColour = 7
ipLinkAttachmentColour = 8
ipLinkMultiPointColour = 9
ipLinkFilledMode = 10
ipLinkNumberMode = 11

## Entity Display Settings - Load Path
ipLoadPathColour = 0
ipLoadPathColourMode = 1
ipLoadPathNumberMode = 2
ipLoadPathShowDivisions = 3
ipLoadPathThickness = 4

## Entity Display Settings - Vertex
ipVertexFreeColour = 0
ipVertexFixedColour = 1
ipVertexSelectedColour = 2
ipVertextNumberMode = 3
ipVertexSymbol = 4

## Entity Display Settings - Geometry Edge
ipEdgeShow = 0
ipEdgeShowNonInterp = 1
ipEdgeStyle = 2
ipEdgeColourMode = 3
ipEdgeColour = 4
ipEdgeNonInterpColour = 5

## Entity Display Settings - Geometry Face
ipFaceWireframeColour = 0
ipFaceShowWireframes = 1
ipFaceShowControlPoints = 2
ipFaceShowNormals = 3
ipFaceWireframeStyle = 4
ipFaceWireframeColourMode = 5
ipFaceWireframeDensity = 6

## Entity Display Settings - Number Modes
nmNone = 0
nmByElement = 1
nmByProperty = 2
nmByPropertyName = 3
nmByID = 4

## Entity Display Settings - Display Modes
dmLine = 0
dmSection = 1
dmSolid = 2
dmSlice = 3

## Entity Display Settings - Outline Modes
omOutlineOn = 0
omOutlineOff = 1
omOutlineFacet = 2

## Entity Display Settings - Filled Modes
fmPropertyColour = 1
fmGroupColour = 2
fmGlobalColour = 3
fmPropertyWireframe = 4
fmGroupWireframe = 5
fmOutlineWireframe = 6
fmOrientation = 7

## Entity Display Settings - Colour Modes
cmPropertyColour = 0
cmGroupColour = 1
cmFaceColour = 2
cmFixedColour = 3

## Entity Display Settings - Load Path Colour Modes
cmLoadPathTemplateColour = 0
cmLoadPathGroupColour = 1
cmLoadPathColour = 2
cmLoadPathGlobalColour = 3

## Entity Display Settings - Edge Styles
esThinEdge = 0
esThickEdge = 1

## Entity Display Settings - Wireframe Styles
wsDepthShaded = 0
wsConstantColour = 1

## Entity Display Settings - Node/Vertex Symbols
syDot1 = 0
syDot2 = 1
syDot3 = 2
syDot4 = 3
sySquare1 = 4
sySquare2 = 5
syDisk1 = 6
syDisk2 = 7
syCircle1 = 8
syCircle2 = 9
syCircle3 = 10
sy3D1 = 11
sy3D2 = 12
sy3D3 = 13

## Entity Display Settings - Beam Contour Types
ctBeamNone = 0
ctBeamLength = 1
ctBeamAxis1 = 2
ctBeamAxis2 = 3
ctBeamAxis3 = 4
ctBeamEA = 5
ctBeamEI11 = 6
ctBeamEI22 = 7
ctBeamGJ = 8
ctBeamEAFactor = 9
ctBeamEI11Factor = 10
ctBeamEI22Factor = 11
ctBeamGJFactor = 12
ctBeamOffset1 = 13
ctBeamOffset2 = 14
ctBeamStiffnessFactor1 = 15
ctBeamStiffnessFactor2 = 16
ctBeamStiffnessFactor3 = 17
ctBeamStiffnessFactor4 = 18
ctBeamStiffnessFactor5 = 19
ctBeamStiffnessFactor6 = 20
ctBeamMassFactor = 21
ctBeamSupport1 = 22
ctBeamSupport2 = 23
ctBeamTemperature = 24
ctBeamPreTension = 25
ctBeamPreStrain = 26
ctBeamTempGradient1 = 27
ctBeamTempGradient2 = 28
ctBeamPipePressureIn = 29
ctBeamPipePressureOut = 30
ctBeamPipeTempIn = 31
ctBeamPipeTempOut = 32
ctBeamConvectionCoeff = 33
ctBeamConvectionAmbient = 34
ctBeamRadiationCoeff = 35
ctBeamRadiationAmbient = 36
ctBeamHeatFlux = 37
ctBeamHeatSource = 38
ctBeamAgeAtFirstLoading = 39

## Entity Display Settings - Plate Contour Types
ctPlateNone = 0
ctPlateAspectRatioMin = 1
ctPlateAspectRatioMax = 2
ctPlateWarping = 3
ctPlateInternalAngle = 4
ctPlateInternalAngleRatio = 5
ctPlateDiscreteThicknessM = 6
ctPlateContinuousThicknessM = 7
ctPlateDiscreteThicknessB = 8
ctPlateContinuousThicknessB = 9
ctPlateOffset = 10
ctPlateArea = 11
ctPlateAxis1 = 12
ctPlateAxis2 = 13
ctPlateAxis3 = 14
ctPlateTemperature = 15
ctPlateEdgeSupport = 16
ctPlateFaceSupport = 17
ctPlatePreStressX = 18
ctPlatePreStressY = 19
ctPlatePresStressZ = 20
ctPlatePreStressMagnitude = 21
ctPlatePreStrainX = 22
ctPlatePreStrainY = 23
ctPlatePreStrainZ = 24
ctPlatePreStrainMagnitude = 25
ctPlateTempGradient = 26
ctPlateEdgePressure = 27
ctPlateEdgeShear = 28
ctPlateEdgeNormalShear = 29
ctPlatePressureNormal = 30
ctPlatePressureGlobal = 31
ctPlatePressureGlobalX = 32
ctPlatePressureGlobalY = 33
ctPlatePressureGlobalZ = 34
ctPlateFaceShearX = 35
ctPlateFaceShearY = 36
ctPlateFaceShearMagnitude = 37
ctPlateNSMass = 38
ctPlateDynamicFactor = 39
ctPlateConvectionCoeff = 40
ctPlateConvectionAmbient = 41
ctPlateRadiationCoeff = 42
ctPlateRadiationAmbient = 43
ctPlateHeatFlux = 44
ctPlateConvectionCoeffZPlus = 45
ctPlateConvectionCoeffZMinus = 46
ctPlateConvectionAmbientZPlus = 47
ctPlateConvectionAmbientZMinus = 48
ctPlateRadiationCoeffZPlus = 49
ctPlateRadiationCoeffZMinus = 50
ctPlateRadiationAmbientZPlus = 51
ctPlateRadiationAmbientZMinus = 52
ctPlateHeatSource = 53
ctPlateSoilStressSV = 54
ctPlateSoilStressKO = 55
ctPlateSoilStressSH = 56
ctPlateSoilRatioOCR = 57
ctPlateSoilRatioEO = 58
ctPlateAgeAtFirstLoading = 59

## Entity Display Settings - Brick Contour Types
ctBrickNone = 0
ctBrickAspectRatioMin = 1
ctBrickAspectRatioMax = 2
ctBrickVolume = 3
ctBrickDeterminant = 4
ctBrickInternalAngle = 5
ctBrickMixedProduct = 6
ctBrickDihedral = 7
ctBrickAxis1 = 8
ctBrickAxis2 = 9
ctBrickAxis3 = 10
ctBrickTemperature = 11
ctBrickSupport = 12
ctBrickPreStressX = 13
ctBrickPreStressY = 14
ctBrickPreStressZ = 15
ctBrickPreStressMagnitude = 16
ctBrickPreStrainX = 17
ctBrickPreStrainY = 18
ctBrickPreStrainZ = 19
ctBrickPreStrainMagnitude = 20
ctBrickNormalPressure = 21
ctBrickGlobalPressure = 22
ctBrickGlobalPressureX = 23
ctBrickGlobalPressureY = 24
ctBrickGlobalPressureZ = 25
ctBrickShearX = 26
ctBrickShearY = 27
ctBrickShearMagnitude = 28
ctBrickNSMass = 29
ctBrickDynamicFactor = 30
ctBrickConvectionCoeff = 31
ctBrickConvectionAmbient = 32
ctBrickRaditionCoeff = 33
ctBrickRadiationAmbient = 34
ctBrickHeatFlux = 35
ctBrickHeatSource = 36
ctBrickSoilStressSV = 37
ctBrickSoilStressKO = 38
ctBrickSoilStressSH = 39
ctBrickSoilRatioOCR = 40
ctBrickSoilRatioEO = 41
ctBrickAgeAtFirstLoading = 42

## Beam/Plate/Brick Result Display Type - INDEXED BY ipResultType
rtAsNone = 0
rtAsContour = 1
rtAsDiagram = 2
rtAsVector = 3

## Node Output Display Quantity - Indexed by ipResultQuantity
icDispC = 101
icVelC = 102
icAccC = 103
icPhaseC = 104
icReactC = 105
icTempC = 106
icNodeForceC = 107
icNodeFluxC = 108

## Beam Output Display Quantity - Indexed by ipResultQuantity
icBeamForceC = 201
icBeamStrainC = 202
icBeamStressC = 203
icBeamCreepStrainC = 204
icBeamEnergyC = 205
icBeamFluxC = 206
icBeamTGradC = 207

## Plate Output Display Quantity - Indexed by ipResultQuantity
icPlateForceC = 301
icPlateMomentC = 302
icPlateStressC = 303
icPlateStrainC = 304
icPlateCurvatureC = 305
icPlateCreepStrainC = 306
icPlateEnergyC = 307
icPlateFluxC = 308
icPlateTGradC = 309

## Brick Output Display Quantity - Indexed by ipResultQuantity
icBrickStressC = 401
icBrickStrainC = 402
icBrickCreepStrainC = 403
icBrickEnergyC = 404
icBrickFluxC = 405
icBrickTGradC = 406

## Vector Styles - Indexed by ipVectorStyle
vtVectorComponent = 0
vtVectorTranslationMag = 1
vtVectorRotationMag = 2

## Result Display Indexes
ipResultType = 0
ipResultQuantity = 1
ipResultAxis = 2
ipResultComponent = 3
ipResultSurface = 4
ipVectorStyle = 5
ipDiagram1 = 7
ipDiagram2 = 8
ipDiagram3 = 9
ipDiagram4 = 10
ipDiagram5 = 11
ipDiagram6 = 12
ipVector1 = 7
ipVector2 = 8
ipVector3 = 9
ipVector4 = 10
ipVector5 = 11
ipVector6 = 12

## Displacement Scales
dsPercent = 0
dsAbsolute = 1

## User Contour File Types
ucNode = 0
ucElement = 1

## Utility
ipRadian = 0
ipDegree = 1

## Result Options
ipResOptsBeamEnvelope = 0
ipResOptsRotationUnit = 1
ipResOptsHRADisplacement = 2
ipResOptsHRAVelocity = 3
ipResOptsHRAAcceleration = 4
ipResOptsStageDisplacement = 5
ipResOptsStrainUnit = 6

## Result Options - Strain Units
suUnit = 0
suPercent = 1
suMicro = 2

## Result Options - HRA
hrRelative = 0
hrTotal = 1

## Result Options - Staging
sdBirthStage = 0
sdInitial = 1

## Result Options - Beam Envelopes
bePrincipal = 0
beLocal = 1

## Tool Options - Doubles
ipToolOptsElementTol = 0
ipToolOptsGeometryAccuracy = 1
ipToolOptsGeometryFeatureLength = 2

## Tool Options - Integers
ipToolOptsElementTolType = 0
ipToolOptsGeometryAccuracyType = 1
ipToolOptsGeometryFeatureType = 2
ipToolOptsZipMesh = 3
ipToolOptsNodeCoordinate = 4
ipToolOptsNodeAttributeKeep = 5
ipToolOptsAllowZeroLengthLinks = 6
ipToolOptsAllowZeroLengthBeams = 7
ipToolOptsAllowSameProperty = 8
ipToolOptsCompatibleTriangle = 9
ipToolOptsSubdivideBeams = 10
ipToolOptsPlateAxisAlign = 11
ipToolOptsCopyMode = 12
ipToolOptsAutoCreateProperties = 13

## Tool Options - Mesh Zipping
zmAsNeeded = 0
zmOnSave = 1
zmOnRequest = 2

## Tool Options - Copy Mode
cmRoot = 0
cmSibling = 1

## Tool Options - Axis Alignment
paCentroid = 0
paCurvilinear = 1

## Axis Definitions
axLocalX = 1
axLocalY = 2
axPrincipal1 = 1
axPrincipal2 = 2
axBeamPrincipal = 0
axBeamLocal = 1

## Beam Taper
btSymm = 0
btTop = 1
btBottom = 2

## Pre-load
plBeamPreTension = 0
plBeamPreStrain = 1
plPlatePreStress = 0
plPlatePreStrain = 1
plBrickPreStress = 0
plBrickPreStrain = 1

## Attachment Attribute
alRigid = 0
alFlexible = 1
alDirect = 2
alMoment = 0
alPinned = 1

## Thermal
ipConvection = 0
ipRadiation = 0
ipAmbient = 1

## LTA Methods
ltWilson = 0
ltNewmark = 1

## Spectral
stResponse = 0
stPSD = 1

## Spectral Results Sign
rsAuto = 0
rsAbsolute = 1

## LTA
stFullSystem = 0
stSuperposition = 1

## Attach Parts
ipDoEnds = 0
ipDoEdges = 1
ipDoFaces = 2
ipSelectedOnly = 3
ipDeleteExisting = 4
ipAllBrickFaces = 5
ipAngleDelta = 0

## Modal Reactions
mrElementForce = 0
mrInertiaForce = 1

## Transient Initial Conditions
icAppliedVectors = 0
icNodalVelocity = 1
icFromFile = 2

## Transient-Quasi Temperature
ttNodalTemp = 0
ttFromFile = 1

## Envelopes
etLimitEnvelopeMin = 0
etLimitEnvelopeMax = 1
etLimitEnvelopeAbs = 2
etCombEnvelopeMin = 3
etCombEnvelopeMax = 4
etFactEnvelopeMin = 5
etFactEnvelopeMax = 6
esCombEnvelopeOn = 0
esCombEnvelopeOff = 1
esCombEnvelopeCheck = 2
stExclusiveOR = 0
stExclusiveAND = 1

## Frequency Table Units
fuNone = 0
fuDispResponse = 1
fuVelResponse = 2
fuAccelResponse = 3
fuDispPSD = 4
fuVelPSD = 5
fuAccelPSD = 6

## Temp/Time Types
mtElastic = 0
mtPlastic = 1

## Material Hardening Types
htIsotropic = 0
htKinematic = 1
htTakeda = 2

## Spring-damper
ipSpringAxialStiff = 0
ipSpringLateralStiff = 1
ipSpringTorsionStiff = 2
ipSpringAxialDamp = 3
ipSpringLateralDamp = 4
ipSpringTorsionDamp = 5
ipSpringMass = 6

## Truss
ipTrussIncludeTorsion = 0

## Cable
ipCableSegments = 0

## Cutoff Bar
ipCutoffTension = 0
ipCutoffCompression = 1

## Contact
cfElastic = 0
cfPlastic = 1
cyRectangular = 0
cyElliptical = 1

## Ply Material - Integers
ipPlyWeaveType = 0
wtPlyUniDirectional = 0
wtPlyBiDirectional = 1
wtPlyTriDirectional = 2
wtPlyQuasiIsotropic = 3

## Ply Material - Doubles
ipPlyModulus1 = 0
ipPlyModulus2 = 1
ipPlyPoisson = 2
ipPlyShear12 = 3
ipPlyShear13 = 4
ipPlyShear23 = 5
ipPlyAlpha1 = 6
ipPlyAlpha2 = 7
ipPlyDensity = 8
ipPlyThickness = 9
ipPlyS1Tension = 10
ipPlyS2Tension = 11
ipPlyS1Compression = 12
ipPlyS2Compression = 13
ipPlySShear = 14
ipPlyE1Tension = 15
ipPlyE2Tension = 16
ipPlyE1Compression = 17
ipPlyE2Compression = 18
ipPlyEShear = 19
ipPlyInterLaminaShear = 20

## Laminate Material
ipLaminateViscosity = 0
ipLaminateDampingRatio = 1
ipLaminateConductivity1 = 2
ipLaminateConductivity2 = 3
ipLaminateSpecificHeat = 4
ipLaminateDensity = 5
ipLaminateAlphax = 6
ipLaminateAlphay = 7
ipLaminateAlphaxy = 8
ipLaminateBetax = 9
ipLaminateBetay = 10
ipLaminateBetaxy = 11
ipLaminateModulusx = 12
ipLaminateModulusy = 13
ipLaminateShearxy = 14
ipLaminatePoissonxy = 15
ipLaminatePoissonyx = 16
ipLaminateThickness = 17

## Laminate Plies
ipLaminatePlyAngle = 0
ipLaminatePlyThickness = 1

## Laminate Matrices
ipLaminateIgnoreCoupling = 0
ipLaminateAutoTransverseShear = 1

## Concrete Reinforcement Layouts - Integers
ipReoLayoutType = 0
ipReoColour13 = 1
ipReoColour24 = 2
ipReoCalcMethod = 3
ipReoConsiderMembrane = 4
ipReoAllowCompressionReo = 5
ipReoCode = 6
ipReoLimitConcreteStrain = 7
crReoSymmetric = 0
crReoAntiSymmetric = 1
crReoSimplified = 0
crReoElastoPlasticIter = 1

## Concrete Reinforcement Layouts - Doubles
ipReoDiam1 = 0
ipReoDiam2 = 1
ipReoDiam3 = 2
ipReoDiam4 = 3
ipReoCover1 = 4
ipReoCover2 = 5
ipReoSpacing1 = 6
ipReoSpacing2 = 7
ipReoSpacing3 = 8
ipReoSpacing4 = 9
ipReoConcreteModulus = 10
ipReoConcreteStrain = 11
ipReoConcreteStress = 12
ipReoConcretePhi = 13
ipReoConcreteGamma = 14
ipReoSteelModulus = 15
ipReoSteelStress = 16
ipReoSteelGamma = 17
ipReoSteelMinArea = 18

## Creep Hardening
ipCreepHardeningType = 0
ipCreepHardeningCyclic = 1
crHardeningTime = 0
crHardeningStrain = 1

## Hyperbolic Creep - Doubles
ipCreepHyberbolicAlpha = 0
ipCreepHyperbolicBeta = 1
ipCreepHyperbolicDelta = 2
ipCreepHyperbolicPhi = 3

## Hyperbolic Creep - Integers
ipCreepHyperbolicTimeTable = 0
ipCreepHyperbolicConstModulus = 1

## Visco-elastic Creep - Integers
ipCreepViscoTimeTable = 0
ipCreepViscoTempTable = 1

## Visco-elastic Creep - Doubles
ipCreepViscoDamper = 0
ipCreepViscoStiffness = 1

## Creep Concrete Functions
cfCreepFunction = 0
cfRelaxationFunction = 1

## Creep Shrinkage
crCreepShrinkageTable = 0
crCreepShrinkageFormula = 1
ipCreepShrinkageAlpha = 0
ipCreepShrinkageBeta = 1
ipCreepShrinkageDelta = 2
ipCreepShrinkageStrain = 3

## Creep Temperature - Integers
ipIncludeCreepTemperature = 0
ipIncludeRateTemperature = 1
ipIncludeShrinkageTemperature = 2

## Creep Temperature - Doubles
ipCreepCAAge = 0
ipCreepTRefAge = 1
ipCreepCCCreep = 2
ipCreepTRefCreep = 3
ipCreepCAShrink = 4
ipCreepTRefShrink = 5

## Cement Curing - Integers
ipCreepIncludeCuring = 0
ipCreepCuringTimeTable = 1
ipCreepCuringType = 2
ctCuringRapid = 0
ctCuringNormal = 1
ctCuringSlow = 2

## Cement Curing - Doubles
ipCreepCuringCT = 0
ipCreepCuringTRef = 1
ipCreepCuringT0 = 2

## Stage Data
ipStageMorph = 0
ipStageMovedFixedNodes = 1
ipStageRotateClusters = 2

## Node Response Variables
reNodeDisplacement = 0
reNodeReaction = 1

## Beam Response Variables
ipBeamResponseSF1 = 0
ipBeamResponseSF2 = 1
ipBeamResponseAxial = 2
ipBeamResponseBM1 = 3
ipBeamResponseBM2 = 4
ipBeamResponseTorque = 5

## Plate Response Variables
rePlateForce = 0
rePlateMoment = 1

## Pipe Properties
ipPipeFlexibility = 0
ipPipeFluidDensity = 1
ipPipeOuterDiameter = 2
ipPipeThickness = 3

## Connection Properties
ipConnectionShear1 = 0
ipConnectionShear2 = 1
ipConnectionAxial = 2
ipConnectionBend1 = 3
ipConnectionBend2 = 4
ipConnectionTorque = 5

## Beam Materials
ipBeamModulus = 0
ipBeamShear = 1
ipBeamPoisson = 2
ipBeamDensity = 3
ipBeamAlpha = 4
ipBeamViscosity = 5
ipBeamDampingRatio = 6
ipBeamConductivity = 7
ipBeamSpecificHeat = 8

## Plate Isotropic Materials
ipPlateIsoModulus = 0
ipPlateIsoPoisson = 1
ipPlateIsoDensity = 2
ipPlateIsoAlpha = 3
ipPlateIsoViscosity = 4
ipPlateIsoDampingRatio = 5
ipPlateIsoConductivity = 6
ipPlateIsoSpecificHeat = 7

## Brick Isotropic Materials
ipBrickIsoModulus = 0
ipBrickIsoPoisson = 1
ipBrickIsoDensity = 2
ipBrickIsoAlpha = 3
ipBrickIsoViscosity = 4
ipBrickIsoDampingRatio = 5
ipBrickIsoConductivity = 6
ipBrickIsoSpecificHeat = 7

## Plate Orthotropic Materials
ipPlateOrthoModulus1 = 0
ipPlateOrthoModulus2 = 1
ipPlateOrthoModulus3 = 2
ipPlateOrthoShear12 = 3
ipPlateOrthoShear23 = 4
ipPlateOrthoShear31 = 5
ipPlateOrthoPoisson12 = 6
ipPlateOrthoPoisson23 = 7
ipPlateOrthoPoisson31 = 8
ipPlateOrthoDensity = 9
ipPlateOrthoAlpha1 = 10
ipPlateOrthoAlpha2 = 11
ipPlateOrthoAlpha3 = 12
ipPlateOrthoViscosity = 13
ipPlateOrthoDampingRatio = 14
ipPlateOrthoConductivity1 = 15
ipPlateOrthoConductivity2 = 16
ipPlateOrthoSpecificHeat = 17

## Brick Orthotropic Materials
ipBrickOrthoModulus1 = 0
ipBrickOrthoModulus2 = 1
ipBrickOrthoModulus3 = 2
ipBrickOrthoShear12 = 3
ipBrickOrthoShear23 = 4
ipBrickOrthoShear31 = 5
ipBrickOrthoPoisson12 = 6
ipBrickOrthoPoisson23 = 7
ipBrickOrthoPoisson31 = 8
ipBrickOrthoDensity = 9
ipBrickOrthoAlpha1 = 10
ipBrickOrthoAlpha2 = 11
ipBrickOrthoAlpha3 = 12
ipBrickOrthoViscosity = 13
ipBrickOrthoDampingRatio = 14
ipBrickOrthoConductivity1 = 15
ipBrickOrthoConductivity2 = 16
ipBrickOrthoConductivity3 = 17
ipBrickOrthoSpecificHeat = 18

## Plate Anisotropic Materials

## 0..9 ansi matrix
ipPlateAnisoTransShear1 = 10
ipPlateAnisoTransShear2 = 11
ipPlateAnisoTransShear3 = 12
ipPlateAnisoDensity = 13
ipPlateAnisoAlpha1 = 14
ipPlateAnisoAlpha2 = 15
ipPlateAnisoAlpha3 = 16
ipPlateAnisoAlpha12 = 17
ipPlateAnisoViscosity = 18
ipPlateAnisoDampingRatio = 19
ipPlateAnisoConductivity1 = 20
ipPlateAnisoConductivity2 = 21
ipPlateAnisoSpecificHeat = 22

## Plate User Defined Materials

## 0..20 user matrix
ipPlateUserTransShearxz = 21
ipPlateUserTransShearyz = 22
ipPlateUserTransShearcz = 23
ipPlateUserDensity = 24
ipPlateUserAlphax = 25
ipPlateUserAlphay = 26
ipPlateUserAlphaxy = 27
ipPlateUserBetax = 28
ipPlateUserBetay = 29
ipPlateUserBetaxy = 30
ipPlateUserViscosity = 31
ipPlateUserDampingRatio = 32
ipPlateUserConductivity1 = 33
ipPlateUserConductivity2 = 34
ipPlateUserSpecificHeat = 35

## Brick Anisotropic Materials

## 0..20 user matrix
ipBrickUserDensity = 21
ipBrickUserAlpha1 = 22
ipBrickUserAlpha2 = 23
ipBrickUserAlpha3 = 24
ipBrickUserAlpha12 = 25
ipBrickUserAlpha23 = 26
ipBrickUserAlpha31 = 27
ipBrickUserViscosity = 28
ipBrickUserDampingRatio = 29
ipBrickUserConductivity1 = 30
ipBrickUserConductivity2 = 31
ipBrickUserConductivity3 = 32
ipBrickUserSpecificHeat = 33

## Duncan-Chang Soil Materials - Integers
ipSoilDCUsePoisson = 0
ipSoilDCSetLevel = 1

## Duncan-Chang Soil Materials - Doubles
ipSoilDCModulusK = 0
ipSoilDCModulusKUR = 1
ipSoilDCModulusN = 2
ipSoilDCPoisson = 3
ipSoilDCBulkK = 4
ipSoilDCBulkM = 5
ipSoilDCFrictionAngle = 6
ipSoilDCDeltaAngle = 7
ipSoilDCCohesion = 8
ipSoilDCFailureRatio = 9
ipSoilDCFailureMod = 10
ipSoilDCReferenceP = 11
ipSoilDCDensity = 12
ipSoilDCHorizontalRatio = 13
ipSoilDCConductivity = 14
ipSoilDCSpecificHeat = 15
ipSoilDCFluidLevel = 16

## Cam-Clay Soil Materials - Integers
ipSoilCCUsePoisson = 0
ipSoilCCDrainedState = 1
ipSoilCCUseOCR = 2
ipSoilCCSetLevel = 3

## Cam-Clay Soil Materials - Doubles
ipSoilCCCriticalStateLine = 0
ipSoilCCConsolidationLine = 1
ipSoilCCSwellingLine = 2
ipSoilCCDensity = 3
ipSoilCCPoisson = 4
ipSoilCCModulusG = 5
ipSoilCCModulusB = 6
ipSoilCCHorizontalRatio = 7
ipSoilCCER = 8
ipSoilCCPR = 9
ipSoilCCPC0 = 10
ipSoilCCOCR = 11
ipSoilCCConductivity = 12
ipSoilCCSpecificHeat = 13
ipSoilCCFluidLevel = 14

## Mohr-Coulomb Soil Materials - Integers
ipSoilMCSetLevel = 0

## Mohr-Coulomb Soil Materials - Doubles
ipSoilMCModulus = 0
ipSoilMCPoisson = 1
ipSoilMCDensity = 2
ipSoilMCHorizontalRatio = 3
ipSoilMCER = 4
ipSoilMCConductivity = 5
ipSoilMCSpecificHeat = 6
ipSoilMCFluidLevel = 7
ipSoilMCCohesion = 8
ipSoilMCFrictionAngle = 9

## Drucker-Prager Soil Materials - Integers
ipSoilDPSetLevel = 0

## Drucker-Prager Soil Materials - Doubles
ipSoilDPModulus = 0
ipSoilDPPoisson = 1
ipSoilDPDensity = 2
ipSoilDPHorizontalRatio = 3
ipSoilDPER = 4
ipSoilDPConductivity = 5
ipSoilDPSpecificHeat = 6
ipSoilDPFluidLevel = 7
ipSoilDPCohesion = 8
ipSoilDPFrictionAngle = 9

## Linear Elastic Soil Materials - Integers
ipSoilLSSetLevel = 0

## Linear Elastic Soil Materials - Doubles
ipSoilLSModulus = 0
ipSoilLSPoisson = 1
ipSoilLSDensity = 2
ipSoilLSHorizontalRatio = 3
ipSoilLSER = 4
ipSoilLSConductivity = 5
ipSoilLSSpecificHeat = 6
ipSoilLSFluidLevel = 7

## Fluid Materials
ipFluidModulus = 0
ipFluidPenaltyParam = 1
ipFluidDensity = 2
ipFluidAlpha = 3
ipFluidViscosity = 4
ipFluidDampingRatio = 5
ipFluidConductivity = 6
ipFluidSpecificHeat = 7

## Mohr-Coulomb, Drucker-Prager
ipFrictionAngle = 0
ipCohesion = 1

## Rubber Materials
ipRubberBulk = 0
ipRubberDensity = 1
ipRubberAlpha = 2
ipRubberViscosity = 3
ipRubberDampingRatio = 4
ipRubberConductivity = 5
ipRubberSpecificHeat = 6
ipRubberConstC1 = 7

## Load Case Types
ltLoadCase = 0
ltSeismicCase = 1
ltSpectralCase = 2

## Polygon to Face - Doubles
ipPolyToFaceEdgeTolerance = 0

## Polygon to Face - Integers
ipPolyToFaceFaceID = 0
ipPolyToFaceGroupIndex = 1
ipPolyToFacePropertyNumber = 2
ipPolyToFaceDeleteBeams = 3
ipPolyToFaceKeepSelected = 4

## Beam Property
ipBeamPropBeamType = 0
ipBeamPropSectionType = 1
ipBeamPropMirrorType = 2
ipBeamPropCompatibleTwist = 3

## Element Axis Types
axUCS = 0
axLocal = 1

## Load Path Template - Integers
ipLPTColour = 0
ipLPTNumLanes = 1
ipLPTMultiLaneType = 2
lpAllSameFactors = 0
lpAllDifferentFactors = 1

## Load Path Template - Doubles
ipLPTTolerance = 0
ipLPTMinLaneWidth = 1

## Load Path Vehicle - Integers
ipLPTVehicleInstance = 0
ipLPTVehicleDirection = 1
lpVehicleSingleLane = 0
lpVehicleDoubleLane = 1
lpVehicleForward = 0
lpVehicleBackward = 1

## Load Path Vehicle - Doubles
ipLPTVehicleVelocity = 0
ipLPTVehicleStartTime = 1

## Load Path Template Forces - Integers
ipLPTMobility = 0
ipLPTAxisSystem = 1
ipLPTAdjacency = 2
ipLPTCentrifugal = 3
lpPointForceMobilityGrouped = 0
lpPointForceMobilityFloating = 1
lpDistrForceMobilityGrouped = 0
lpDistrForceMobilityLeading = 1
lpDistrForceMobilityTrailing = 2
lpDistrForceMobilityFullLength = 3
lpDistrForceMobilityFloating = 4
lpAxisLocal = 0
lpAxisGlobal = 1

## Load Path Templates - Integers
ipLPTLimitK1 = 0
ipLPTLengthUnit = 1
ipLPTForceUnit = 2

## Load Path Templates - Doubles
ipLPTMinK1 = 0
ipLPTMaxK1 = 1

## Combined Result Files
rfCombFactors = 0
rfCombSRSS = 1

## Load Path
ipLoadPathCase = 0
ipLoadPathTemplate = 1
ipLoadPathShape = 2
ipLoadPathSurface = 3
ipLoadPathTarget = 4
ipLoadPathDivisions = 5
lpShapeStraight = 0
lpShapeCurved = 1
lpShapeQuadratic = 2
lpSurfaceFlat = 0
lpSurfaceCurved = 1

## Animation
ipAniParentHandle = 0
ipAniCase = 1
ipNumFrames = 2
ipAniWidth = 3
ipAniHeight = 4
ipAniType = 5
kAniSAF = 0
kAniEXE = 1
kAniAVI = 2

## Custom Result Files - NODEDISP, NODEREACT
ipNodeResFileDX = 0
ipNodeResFileDY = 1
ipNodeResFileDZ = 2
ipNodeResFileRX = 3
ipNodeResFileRY = 4
ipNodeResFileRZ = 5

## Custom Result Files - NODETEMP, NODEFLUX
ipNodeResTemp = 0

## Custom Result Files - BEAMFORCE
ipBeamResFileSF1 = 0
ipBeamResFileSF2 = 1
ipBeamResFileAxial = 2
ipBeamResFileBM1 = 3
ipBeamResFileBM2 = 4
ipBeamResFileTorque = 5
kBeamResFileForceSize = 6

## Custom Result Files - BEAMSTRAIN
ipBeamResFileAxialStrain = 2
ipBeamResFileCurvature1 = 3
ipBeamResFileCurvature2 = 4
ipBeamResFileTwist = 5
kBeamResFileStrainSize = 6

## Custom Result Files - BEAMNODEREACT
ipBeamResFileFX = 0
ipBeamResFileFY = 1
ipBeamResFileFZ = 2
ipBeamResFileMX = 3
ipBeamResFileMY = 4
ipBeamResFileMZ = 5
kBeamResFileReactSize = 6

## Custom Result Files - BEAMFLUX
ipBeamResFileF = 0
ipBeamResFileG = 1
kBeamResFileFluxSize = 2

## Custom Result Files - PLATESTRESS for PlateShell - Local system
ipPlateShellResFileNxx = 0
ipPlateShellResFileNyy = 1
ipPlateShellResFileNxy = 2
ipPlateShellResFileMxx = 3
ipPlateShellResFileMyy = 4
ipPlateShellResFileMxy = 5
ipPlateShellResFileQxz = 6
ipPlateShellResFileQyz = 7
ipPlateShellResFileZMinusSxx = 8
ipPlateShellResFileZMinusSyy = 9
ipPlateShellResFileZMinusSxy = 10
ipPlateShellResFileMidPlaneSxx = 11
ipPlateShellResFileMidPlaneSyy = 12
ipPlateShellResFileMidPlaneSxy = 13
ipPlateShellResFileZPlusSxx = 14
ipPlateShellResFileZPlusSyy = 15
ipPlateShellResFileZPlusSxy = 16
kPlateShellResFileStressSize = 17

## Custom Result Files - PLATESTRAIN for PlateShell - Local system
ipPlateShellResFileExx = 0
ipPlateShellResFileEyy = 1
ipPlateShellResFileExy = 2
ipPlateShellResFileEzz = 3
ipPlateShellResFileKxx = 4
ipPlateShellResFileKyy = 5
ipPlateShellResFileKxy = 6
ipPlateShellResFileTxz = 7
ipPlateShellResFileTyz = 8
ipPlateShellResFileStoredE = 9
ipPlateShellResFileSpentE = 10
kPlateShellResFileStrainSize = 11

## Custom Result Files - PLATESTRESS for 2D Plates - Global system
ipPlate2DResFileSXX = 0
ipPlate2DResFileSYY = 1
ipPlate2DResFileSXY = 2
ipPlate2DResFileSZZ = 3
kPlate2DResFileStressSize = 4

## Custom Result Files - PLATESTRAIN for 2D Plates - Global system
ipPlate2DResFileEXX = 0
ipPlate2DResFileEYY = 1
ipPlate2DResFileEXY = 2
ipPlate2DResFileEZZ = 3
ipPlate2DResFileStoredE = 4
ipPlate2DResFileSpentE = 5
kPlate2DResFileStrainSize = 6

## Custom Result Files - PLATESTRESS for Axi Plates - Axisymmetric system
ipPlateAxiResFileSRR = 0
ipPlateAxiResFileSZZ = 1
ipPlateAxiResFileSTT = 2
ipPlateAxiResFileSRT = 3
kPlateAxiResFileStressSize = 4

## Custom Result Files - PLATESTRAIN for Axi Plates - Axisymmetric system
ipPlateAxiResFileERR = 0
ipPlateAxiResFileEZZ = 1
ipPlateAxiResFileETT = 2
ipPlateAxiResFileERT = 3
ipPlateAxiResFileStoredE = 4
ipPlateAxiResFileSpentE = 5
kPlateAxiResFileStrainSize = 6

## Custom Result Files - PLATENODEREACT
ipPlateResFileFX = 0
ipPlateResFileFY = 1
ipPlateResFileFZ = 2
ipPlateResFileMX = 3
ipPlateResFileMY = 4
ipPlateResFileMZ = 5
kPlateResFileReactSize = 6

## Custom Result Files - PLATEFLUX
ipPlateResFileFxx = 0
ipPlateResFileFyy = 1
ipPlateResFileGxx = 2
ipPlateResFileGyy = 3
kPlateResFileFluxSize = 4

## Custom Result Files - BRICKSTRESS
ipBrickResFileSXX = 0
ipBrickResFileSYY = 1
ipBrickResFileSZZ = 2
ipBrickResFileSXY = 3
ipBrickResFileSYZ = 4
ipBrickResFileSZX = 5
kBrickResFileStressSize = 6

## Custom Result Files - BRICKSTRAIN
ipBrickResFileExx = 0
ipBrickResFileEyy = 1
ipBrickResFileEzz = 2
ipBrickResFileExy = 3
ipBrickResFileEyz = 4
ipBrickResFileEzx = 5
ipBrickResFileStoredE = 6
ipBrickResFileSpentE = 7
kBrickResFileStrainSize = 8

## Custom Result Files - BRICKNODEREACT
ipBrickResFileFX = 0
ipBrickResFileFY = 1
ipBrickResFileFZ = 2
kBrickResFileReactSize = 3

## Custom Result Files - BRICKFLUX
ipBrickResFileFXX = 0
ipBrickResFileFYY = 1
ipBrickResFileFZZ = 2
ipBrickResFileGXX = 3
ipBrickResFileGYY = 4
ipBrickResFileGZZ = 5
kBrickResFileFluxSize = 6

## Edge Attachment Direction
adPlanar = 0
adPlusZ = 1
adMinusZ = 2

_ST7API = ctypes.windll.LoadLibrary('St7API.dll')

c_char = ctypes.c_char
c_char_p = ctypes.c_char_p
c_bool = ctypes.c_bool
c_long = ctypes.c_long
c_double = ctypes.c_double
create_string_buffer = ctypes.create_string_buffer

St7Init = _ST7API.St7Init
St7Init.argtypes = []
St7Release = _ST7API.St7Release
St7Release.argtypes = []
St7APIVersion = _ST7API.St7APIVersion
St7APIVersion.argtypes = [ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7OpenFile = _ST7API.St7OpenFile
St7OpenFile.argtypes = [c_long, c_char_p, c_char_p]
St7CloseFile = _ST7API.St7CloseFile
St7CloseFile.argtypes = [c_long]
St7NewFile = _ST7API.St7NewFile
St7NewFile.argtypes = [c_long, c_char_p, c_char_p]
St7SaveFile = _ST7API.St7SaveFile
St7SaveFile.argtypes = [c_long]
St7SaveFileTo = _ST7API.St7SaveFileTo
St7SaveFileTo.argtypes = [c_long, c_char_p]
St7OpenResultFile = _ST7API.St7OpenResultFile
St7OpenResultFile.argtypes = [c_long, c_char_p, c_char_p, c_bool, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7GenerateLSACombinations = _ST7API.St7GenerateLSACombinations
St7GenerateLSACombinations.argtypes = [c_long, ctypes.POINTER(c_long)]
St7GenerateEnvelopes = _ST7API.St7GenerateEnvelopes
St7GenerateEnvelopes.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7CloseResultFile = _ST7API.St7CloseResultFile
St7CloseResultFile.argtypes = [c_long]
St7GetDisplayOptionsPath = _ST7API.St7GetDisplayOptionsPath
St7GetDisplayOptionsPath.argtypes = [c_char_p, c_long]
St7SetDisplayOptionsPath = _ST7API.St7SetDisplayOptionsPath
St7SetDisplayOptionsPath.argtypes = [c_char_p]
St7GetLibraryPath = _ST7API.St7GetLibraryPath
St7GetLibraryPath.argtypes = [c_char_p, c_long]
St7SetLibraryPath = _ST7API.St7SetLibraryPath
St7SetLibraryPath.argtypes = [c_char_p]
St7GetPath = _ST7API.St7GetPath
St7GetPath.argtypes = [c_char_p, c_long]
St7GetLastError = _ST7API.St7GetLastError
St7GetLastError.argtypes = []
St7GetAPIErrorString = _ST7API.St7GetAPIErrorString
St7GetAPIErrorString.argtypes = [c_long, c_char_p, c_long]
St7GetSolverErrorString = _ST7API.St7GetSolverErrorString
St7GetSolverErrorString.argtypes = [c_long, c_char_p, c_long]
St7TransformToUCS = _ST7API.St7TransformToUCS
St7TransformToUCS.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7TransformToXYZ = _ST7API.St7TransformToXYZ
St7TransformToXYZ.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7VectorTransformToUCS = _ST7API.St7VectorTransformToUCS
St7VectorTransformToUCS.argtypes = [c_long, c_long, ctypes.POINTER(c_double), ctypes.POINTER(c_double)]
St7VectorTransformToXYZ = _ST7API.St7VectorTransformToXYZ
St7VectorTransformToXYZ.argtypes = [c_long, c_long, ctypes.POINTER(c_double), ctypes.POINTER(c_double)]
St7GetCleanMeshData = _ST7API.St7GetCleanMeshData
St7GetCleanMeshData.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetCleanMeshData = _ST7API.St7SetCleanMeshData
St7SetCleanMeshData.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7CleanMesh = _ST7API.St7CleanMesh
St7CleanMesh.argtypes = [c_long]
St7DeleteUnusedNodes = _ST7API.St7DeleteUnusedNodes
St7DeleteUnusedNodes.argtypes = [c_long, ctypes.POINTER(c_long)]
St7InvalidateElement = _ST7API.St7InvalidateElement
St7InvalidateElement.argtypes = [c_long, c_long, c_long]
St7DeleteInvalidElements = _ST7API.St7DeleteInvalidElements
St7DeleteInvalidElements.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetPlateUV = _ST7API.St7GetPlateUV
St7GetPlateUV.argtypes = [c_long, c_long, ctypes.POINTER(c_double), ctypes.POINTER(c_double)]
St7GetBrickUVW = _ST7API.St7GetBrickUVW
St7GetBrickUVW.argtypes = [c_long, c_long, ctypes.POINTER(c_double), ctypes.POINTER(c_double)]
St7GetNumElementResultGaussPoints = _ST7API.St7GetNumElementResultGaussPoints
St7GetNumElementResultGaussPoints.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7ConvertElementResultNodeToGaussPoint = _ST7API.St7ConvertElementResultNodeToGaussPoint
St7ConvertElementResultNodeToGaussPoint.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetResultOptions = _ST7API.St7SetResultOptions
St7SetResultOptions.argtypes = [c_long, ctypes.POINTER(c_long)]
St7GetResultOptions = _ST7API.St7GetResultOptions
St7GetResultOptions.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetToolOptions = _ST7API.St7SetToolOptions
St7SetToolOptions.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetToolOptions = _ST7API.St7GetToolOptions
St7GetToolOptions.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7EnableModelStrainUnit = _ST7API.St7EnableModelStrainUnit
St7EnableModelStrainUnit.argtypes = [c_long]
St7DisableModelStrainUnit = _ST7API.St7DisableModelStrainUnit
St7DisableModelStrainUnit.argtypes = [c_long]
St7EnableModelRotationUnit = _ST7API.St7EnableModelRotationUnit
St7EnableModelRotationUnit.argtypes = [c_long]
St7DisableModelRotationUnit = _ST7API.St7DisableModelRotationUnit
St7DisableModelRotationUnit.argtypes = [c_long]
St7EnableModelRCUnit = _ST7API.St7EnableModelRCUnit
St7EnableModelRCUnit.argtypes = [c_long]
St7DisableModelRCUnit = _ST7API.St7DisableModelRCUnit
St7DisableModelRCUnit.argtypes = [c_long]
St7SetEntitySelectState = _ST7API.St7SetEntitySelectState
St7SetEntitySelectState.argtypes = [c_long, c_long, c_long, c_long, c_bool]
St7GetEntitySelectState = _ST7API.St7GetEntitySelectState
St7GetEntitySelectState.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_bool)]
St7CreateModelWindow = _ST7API.St7CreateModelWindow
St7CreateModelWindow.argtypes = [c_long]
St7DestroyModelWindow = _ST7API.St7DestroyModelWindow
St7DestroyModelWindow.argtypes = [c_long]
St7GetModelWindowState = _ST7API.St7GetModelWindowState
St7GetModelWindowState.argtypes = [c_long, ctypes.POINTER(c_long)]
St7GetModelWindowHandle = _ST7API.St7GetModelWindowHandle
St7GetModelWindowHandle.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetModelWindowParent = _ST7API.St7SetModelWindowParent
St7SetModelWindowParent.argtypes = [c_long, c_long]
St7ShowModelWindow = _ST7API.St7ShowModelWindow
St7ShowModelWindow.argtypes = [c_long]
St7HideModelWindow = _ST7API.St7HideModelWindow
St7HideModelWindow.argtypes = [c_long]
St7RedrawModel = _ST7API.St7RedrawModel
St7RedrawModel.argtypes = [c_long, c_bool]
St7ClearModelWindow = _ST7API.St7ClearModelWindow
St7ClearModelWindow.argtypes = [c_long]
St7ShowWindowPopUp = _ST7API.St7ShowWindowPopUp
St7ShowWindowPopUp.argtypes = [c_long, c_long]
St7HideWindowPopUp = _ST7API.St7HideWindowPopUp
St7HideWindowPopUp.argtypes = [c_long, c_long]
St7ShowWindowTopPanel = _ST7API.St7ShowWindowTopPanel
St7ShowWindowTopPanel.argtypes = [c_long]
St7HideWindowTopPanel = _ST7API.St7HideWindowTopPanel
St7HideWindowTopPanel.argtypes = [c_long]
St7ShowWindowToolbar = _ST7API.St7ShowWindowToolbar
St7ShowWindowToolbar.argtypes = [c_long]
St7HideWindowToolbar = _ST7API.St7HideWindowToolbar
St7HideWindowToolbar.argtypes = [c_long]
St7ShowWindowStatusBar = _ST7API.St7ShowWindowStatusBar
St7ShowWindowStatusBar.argtypes = [c_long]
St7HideWindowStatusBar = _ST7API.St7HideWindowStatusBar
St7HideWindowStatusBar.argtypes = [c_long]
St7ShowSelectionToolBar = _ST7API.St7ShowSelectionToolBar
St7ShowSelectionToolBar.argtypes = [c_long]
St7HideSelectionToolBar = _ST7API.St7HideSelectionToolBar
St7HideSelectionToolBar.argtypes = [c_long]
St7SetSelectionToolBarPosition = _ST7API.St7SetSelectionToolBarPosition
St7SetSelectionToolBarPosition.argtypes = [c_long, c_long, c_long]
St7GetSelectionToolBarPosition = _ST7API.St7GetSelectionToolBarPosition
St7GetSelectionToolBarPosition.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7RotateModel = _ST7API.St7RotateModel
St7RotateModel.argtypes = [c_long, c_double, c_double, c_double]
St7ShowEntity = _ST7API.St7ShowEntity
St7ShowEntity.argtypes = [c_long, c_long]
St7HideEntity = _ST7API.St7HideEntity
St7HideEntity.argtypes = [c_long, c_long]
St7SetEntityDisplay = _ST7API.St7SetEntityDisplay
St7SetEntityDisplay.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetEntityDisplay = _ST7API.St7GetEntityDisplay
St7GetEntityDisplay.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7ShowPointAttributes = _ST7API.St7ShowPointAttributes
St7ShowPointAttributes.argtypes = [c_long]
St7HidePointAttributes = _ST7API.St7HidePointAttributes
St7HidePointAttributes.argtypes = [c_long]
St7ShowEntityAttributes = _ST7API.St7ShowEntityAttributes
St7ShowEntityAttributes.argtypes = [c_long]
St7HideEntityAttributes = _ST7API.St7HideEntityAttributes
St7HideEntityAttributes.argtypes = [c_long]
St7PositionModelWindow = _ST7API.St7PositionModelWindow
St7PositionModelWindow.argtypes = [c_long, c_long, c_long, c_long, c_long]
St7GetModelWindowPosition = _ST7API.St7GetModelWindowPosition
St7GetModelWindowPosition.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7GetDrawAreaSize = _ST7API.St7GetDrawAreaSize
St7GetDrawAreaSize.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7ShowProperty = _ST7API.St7ShowProperty
St7ShowProperty.argtypes = [c_long, c_long, c_long]
St7HideProperty = _ST7API.St7HideProperty
St7HideProperty.argtypes = [c_long, c_long, c_long]
St7ShowGroup = _ST7API.St7ShowGroup
St7ShowGroup.argtypes = [c_long, c_long]
St7HideGroup = _ST7API.St7HideGroup
St7HideGroup.argtypes = [c_long, c_long]
St7SetBeamResultDisplay = _ST7API.St7SetBeamResultDisplay
St7SetBeamResultDisplay.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetPlateResultDisplay = _ST7API.St7SetPlateResultDisplay
St7SetPlateResultDisplay.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetBrickResultDisplay = _ST7API.St7SetBrickResultDisplay
St7SetBrickResultDisplay.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetWindowResultCase = _ST7API.St7SetWindowResultCase
St7SetWindowResultCase.argtypes = [c_long, c_long]
St7SetWindowLoadCase = _ST7API.St7SetWindowLoadCase
St7SetWindowLoadCase.argtypes = [c_long, c_long]
St7SetWindowFreedomCase = _ST7API.St7SetWindowFreedomCase
St7SetWindowFreedomCase.argtypes = [c_long, c_long]
St7SetWindowUCSCase = _ST7API.St7SetWindowUCSCase
St7SetWindowUCSCase.argtypes = [c_long, c_long]
St7SetEntityContourFile = _ST7API.St7SetEntityContourFile
St7SetEntityContourFile.argtypes = [c_long, c_long, c_long, c_char_p]
St7GetEntityContourFile = _ST7API.St7GetEntityContourFile
St7GetEntityContourFile.argtypes = [c_long, c_long, ctypes.POINTER(c_long), c_char_p, c_long]
St7SetDisplacementScale = _ST7API.St7SetDisplacementScale
St7SetDisplacementScale.argtypes = [c_long, c_double, c_long]
St7GetDisplacementScale = _ST7API.St7GetDisplacementScale
St7GetDisplacementScale.argtypes = [c_long, ctypes.POINTER(c_double), ctypes.POINTER(c_long)]
St7ImportST7File = _ST7API.St7ImportST7File
St7ImportST7File.argtypes = [c_long, c_char_p, c_long]
St7ImportIGESFile = _ST7API.St7ImportIGESFile
St7ImportIGESFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), ctypes.POINTER(c_double), c_long]
St7ImportACISFile = _ST7API.St7ImportACISFile
St7ImportACISFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), ctypes.POINTER(c_double), c_long]
St7ImportSTEPFile = _ST7API.St7ImportSTEPFile
St7ImportSTEPFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), ctypes.POINTER(c_double), c_long]
St7ImportST6BinaryFile = _ST7API.St7ImportST6BinaryFile
St7ImportST6BinaryFile.argtypes = [c_long, c_char_p, c_long]
St7ImportST6TextFile = _ST7API.St7ImportST6TextFile
St7ImportST6TextFile.argtypes = [c_long, c_char_p, c_long]
St7ImportDXFFile = _ST7API.St7ImportDXFFile
St7ImportDXFFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7ImportSTLFile = _ST7API.St7ImportSTLFile
St7ImportSTLFile.argtypes = [c_long, c_char_p, c_long]
St7ImportNASTRANFile = _ST7API.St7ImportNASTRANFile
St7ImportNASTRANFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7ImportANSYSFile = _ST7API.St7ImportANSYSFile
St7ImportANSYSFile.argtypes = [c_long, c_char_p, c_char_p, ctypes.POINTER(c_long), c_long]
St7ImportSTAADFile = _ST7API.St7ImportSTAADFile
St7ImportSTAADFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7ImportSAP2000File = _ST7API.St7ImportSAP2000File
St7ImportSAP2000File.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7ExportImageFile = _ST7API.St7ExportImageFile
St7ExportImageFile.argtypes = [c_long, c_char_p, c_long, c_long, c_long]
St7ExportST7File = _ST7API.St7ExportST7File
St7ExportST7File.argtypes = [c_long, c_char_p, c_long, c_long]
St7ExportIGESFile = _ST7API.St7ExportIGESFile
St7ExportIGESFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7ExportSTEPFile = _ST7API.St7ExportSTEPFile
St7ExportSTEPFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7ExportDXFFile = _ST7API.St7ExportDXFFile
St7ExportDXFFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7ExportNASTRANFile = _ST7API.St7ExportNASTRANFile
St7ExportNASTRANFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), ctypes.POINTER(c_double), c_long]
St7ExportANSYSFile = _ST7API.St7ExportANSYSFile
St7ExportANSYSFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7PlayAnimationFile = _ST7API.St7PlayAnimationFile
St7PlayAnimationFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long)]
St7CreateAnimation = _ST7API.St7CreateAnimation
St7CreateAnimation.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7CreateAnimationFile = _ST7API.St7CreateAnimationFile
St7CreateAnimationFile.argtypes = [c_long, ctypes.POINTER(c_long), c_char_p]
St7CloseAnimation = _ST7API.St7CloseAnimation
St7CloseAnimation.argtypes = [c_long]
St7SetAnimationCase = _ST7API.St7SetAnimationCase
St7SetAnimationCase.argtypes = [c_long, c_long, c_bool]
St7GetAnimationCase = _ST7API.St7GetAnimationCase
St7GetAnimationCase.argtypes = [c_long, c_long, ctypes.POINTER(c_bool)]
St7GetTotal = _ST7API.St7GetTotal
St7GetTotal.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetTitle = _ST7API.St7GetTitle
St7GetTitle.argtypes = [c_long, c_long, c_char_p, c_long]
St7SetTitle = _ST7API.St7SetTitle
St7SetTitle.argtypes = [c_long, c_long, c_char_p]
St7AddComment = _ST7API.St7AddComment
St7AddComment.argtypes = [c_long, c_char_p]
St7GetNumComments = _ST7API.St7GetNumComments
St7GetNumComments.argtypes = [c_long, ctypes.POINTER(c_long)]
St7GetComment = _ST7API.St7GetComment
St7GetComment.argtypes = [c_long, c_long, c_char_p, c_long]
St7SetComment = _ST7API.St7SetComment
St7SetComment.argtypes = [c_long, c_long, c_char_p]
St7DeleteComment = _ST7API.St7DeleteComment
St7DeleteComment.argtypes = [c_long, c_long]
St7GetBeamAxisSystem = _ST7API.St7GetBeamAxisSystem
St7GetBeamAxisSystem.argtypes = [c_long, c_long, c_bool, ctypes.POINTER(c_double)]
St7GetPlateAxisSystem = _ST7API.St7GetPlateAxisSystem
St7GetPlateAxisSystem.argtypes = [c_long, c_long, c_bool, ctypes.POINTER(c_double)]
St7GetBrickFaceAxisSystem = _ST7API.St7GetBrickFaceAxisSystem
St7GetBrickFaceAxisSystem.argtypes = [c_long, c_long, c_long, c_bool, ctypes.POINTER(c_double)]
St7GetPlateNumPlies = _ST7API.St7GetPlateNumPlies
St7GetPlateNumPlies.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetNumBXSLoopsAndPlates = _ST7API.St7GetNumBXSLoopsAndPlates
St7GetNumBXSLoopsAndPlates.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7GetNumBXSLoopPoints = _ST7API.St7GetNumBXSLoopPoints
St7GetNumBXSLoopPoints.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetBXSLoop = _ST7API.St7GetBXSLoop
St7GetBXSLoop.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GenerateBXS = _ST7API.St7GenerateBXS
St7GenerateBXS.argtypes = [c_long, c_char_p, ctypes.POINTER(c_double)]
St7NewLoadCase = _ST7API.St7NewLoadCase
St7NewLoadCase.argtypes = [c_long, c_char_p]
St7NewSeismicCase = _ST7API.St7NewSeismicCase
St7NewSeismicCase.argtypes = [c_long, c_char_p]
St7NewFreedomCase = _ST7API.St7NewFreedomCase
St7NewFreedomCase.argtypes = [c_long, c_char_p]
St7GetNumLoadCase = _ST7API.St7GetNumLoadCase
St7GetNumLoadCase.argtypes = [c_long, ctypes.POINTER(c_long)]
St7GetNumSeismicCase = _ST7API.St7GetNumSeismicCase
St7GetNumSeismicCase.argtypes = [c_long, ctypes.POINTER(c_long)]
St7GetNumFreedomCase = _ST7API.St7GetNumFreedomCase
St7GetNumFreedomCase.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetLoadCaseName = _ST7API.St7SetLoadCaseName
St7SetLoadCaseName.argtypes = [c_long, c_long, c_char_p]
St7GetLoadCaseName = _ST7API.St7GetLoadCaseName
St7GetLoadCaseName.argtypes = [c_long, c_long, c_char_p, c_long]
St7SetSeismicCaseName = _ST7API.St7SetSeismicCaseName
St7SetSeismicCaseName.argtypes = [c_long, c_long, c_char_p]
St7GetSeismicCaseName = _ST7API.St7GetSeismicCaseName
St7GetSeismicCaseName.argtypes = [c_long, c_long, c_char_p, c_long]
St7SetFreedomCaseName = _ST7API.St7SetFreedomCaseName
St7SetFreedomCaseName.argtypes = [c_long, c_long, c_char_p]
St7GetFreedomCaseName = _ST7API.St7GetFreedomCaseName
St7GetFreedomCaseName.argtypes = [c_long, c_long, c_char_p, c_long]
St7SetLoadCaseDefaults = _ST7API.St7SetLoadCaseDefaults
St7SetLoadCaseDefaults.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetLoadCaseDefaults = _ST7API.St7GetLoadCaseDefaults
St7GetLoadCaseDefaults.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetSeismicCaseDefaults = _ST7API.St7SetSeismicCaseDefaults
St7SetSeismicCaseDefaults.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetSeismicCaseDefaults = _ST7API.St7GetSeismicCaseDefaults
St7GetSeismicCaseDefaults.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetFreedomCaseDefaults = _ST7API.St7SetFreedomCaseDefaults
St7SetFreedomCaseDefaults.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetFreedomCaseDefaults = _ST7API.St7GetFreedomCaseDefaults
St7GetFreedomCaseDefaults.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetLoadCaseType = _ST7API.St7SetLoadCaseType
St7SetLoadCaseType.argtypes = [c_long, c_long, c_long]
St7GetLoadCaseType = _ST7API.St7GetLoadCaseType
St7GetLoadCaseType.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetLoadCaseGravityDir = _ST7API.St7SetLoadCaseGravityDir
St7SetLoadCaseGravityDir.argtypes = [c_long, c_long, c_long]
St7GetLoadCaseGravityDir = _ST7API.St7GetLoadCaseGravityDir
St7GetLoadCaseGravityDir.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetFreedomCaseType = _ST7API.St7SetFreedomCaseType
St7SetFreedomCaseType.argtypes = [c_long, c_long, c_long]
St7GetFreedomCaseType = _ST7API.St7GetFreedomCaseType
St7GetFreedomCaseType.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetLoadCaseMassOption = _ST7API.St7SetLoadCaseMassOption
St7SetLoadCaseMassOption.argtypes = [c_long, c_long, c_bool, c_bool]
St7GetLoadCaseMassOption = _ST7API.St7GetLoadCaseMassOption
St7GetLoadCaseMassOption.argtypes = [c_long, c_long, ctypes.POINTER(c_bool), ctypes.POINTER(c_bool)]
St7EnableSeismicNSMassCase = _ST7API.St7EnableSeismicNSMassCase
St7EnableSeismicNSMassCase.argtypes = [c_long, c_long, c_long]
St7DisableSeismicNSMassCase = _ST7API.St7DisableSeismicNSMassCase
St7DisableSeismicNSMassCase.argtypes = [c_long, c_long, c_long]
St7GetSeismicNSMassCaseState = _ST7API.St7GetSeismicNSMassCaseState
St7GetSeismicNSMassCaseState.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_bool)]
St7DeleteLoadCase = _ST7API.St7DeleteLoadCase
St7DeleteLoadCase.argtypes = [c_long, c_long]
St7DeleteSeismicCase = _ST7API.St7DeleteSeismicCase
St7DeleteSeismicCase.argtypes = [c_long, c_long]
St7DeleteFreedomCase = _ST7API.St7DeleteFreedomCase
St7DeleteFreedomCase.argtypes = [c_long, c_long]
St7SetUCS = _ST7API.St7SetUCS
St7SetUCS.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetUCS = _ST7API.St7GetUCS
St7GetUCS.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetUCSName = _ST7API.St7SetUCSName
St7SetUCSName.argtypes = [c_long, c_long, c_char_p]
St7GetUCSName = _ST7API.St7GetUCSName
St7GetUCSName.argtypes = [c_long, c_long, c_char_p, c_long]
St7GetUCSID = _ST7API.St7GetUCSID
St7GetUCSID.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetNumUCS = _ST7API.St7GetNumUCS
St7GetNumUCS.argtypes = [c_long, ctypes.POINTER(c_long)]
St7GetGroupIDName = _ST7API.St7GetGroupIDName
St7GetGroupIDName.argtypes = [c_long, c_long, c_char_p, c_long]
St7GetNumGroups = _ST7API.St7GetNumGroups
St7GetNumGroups.argtypes = [c_long, ctypes.POINTER(c_long)]
St7GetGroupByIndex = _ST7API.St7GetGroupByIndex
St7GetGroupByIndex.argtypes = [c_long, c_long, c_char_p, c_long, ctypes.POINTER(c_long)]
St7NewChildGroup = _ST7API.St7NewChildGroup
St7NewChildGroup.argtypes = [c_long, c_long, c_char_p, ctypes.POINTER(c_long)]
St7GetGroupParent = _ST7API.St7GetGroupParent
St7GetGroupParent.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetGroupChild = _ST7API.St7GetGroupChild
St7GetGroupChild.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetGroupSibling = _ST7API.St7GetGroupSibling
St7GetGroupSibling.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7DeleteGroup = _ST7API.St7DeleteGroup
St7DeleteGroup.argtypes = [c_long, c_long]
St7SetGroupColour = _ST7API.St7SetGroupColour
St7SetGroupColour.argtypes = [c_long, c_long, c_long]
St7GetGroupColour = _ST7API.St7GetGroupColour
St7GetGroupColour.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7AddStage = _ST7API.St7AddStage
St7AddStage.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long)]
St7InsertStage = _ST7API.St7InsertStage
St7InsertStage.argtypes = [c_long, c_long, c_char_p, ctypes.POINTER(c_long)]
St7DeleteStage = _ST7API.St7DeleteStage
St7DeleteStage.argtypes = [c_long, c_long]
St7GetNumStages = _ST7API.St7GetNumStages
St7GetNumStages.argtypes = [c_long, ctypes.POINTER(c_long)]
St7GetStageName = _ST7API.St7GetStageName
St7GetStageName.argtypes = [c_long, c_long, c_char_p, c_long]
St7SetStageName = _ST7API.St7SetStageName
St7SetStageName.argtypes = [c_long, c_long, c_char_p]
St7GetStageData = _ST7API.St7GetStageData
St7GetStageData.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetStageData = _ST7API.St7SetStageData
St7SetStageData.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7EnableStageGroup = _ST7API.St7EnableStageGroup
St7EnableStageGroup.argtypes = [c_long, c_long, c_long]
St7DisableStageGroup = _ST7API.St7DisableStageGroup
St7DisableStageGroup.argtypes = [c_long, c_long, c_long]
St7GetStageGroupState = _ST7API.St7GetStageGroupState
St7GetStageGroupState.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_bool)]
St7GetUnits = _ST7API.St7GetUnits
St7GetUnits.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetUnits = _ST7API.St7SetUnits
St7SetUnits.argtypes = [c_long, ctypes.POINTER(c_long)]
St7GetRCUnits = _ST7API.St7GetRCUnits
St7GetRCUnits.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7SetRCUnits = _ST7API.St7SetRCUnits
St7SetRCUnits.argtypes = [c_long, c_long, c_long]
St7ConvertUnits = _ST7API.St7ConvertUnits
St7ConvertUnits.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetNodeXYZ = _ST7API.St7SetNodeXYZ
St7SetNodeXYZ.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetNodeXYZ = _ST7API.St7GetNodeXYZ
St7GetNodeXYZ.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetNodeUCS = _ST7API.St7GetNodeUCS
St7GetNodeUCS.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetNodeUCS = _ST7API.St7SetNodeUCS
St7SetNodeUCS.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetElementConnection = _ST7API.St7SetElementConnection
St7SetElementConnection.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetElementConnection = _ST7API.St7GetElementConnection
St7GetElementConnection.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetElementData = _ST7API.St7GetElementData
St7GetElementData.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetElementCentroid = _ST7API.St7GetElementCentroid
St7GetElementCentroid.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetMasterSlaveLink = _ST7API.St7SetMasterSlaveLink
St7SetMasterSlaveLink.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7GetMasterSlaveLink = _ST7API.St7GetMasterSlaveLink
St7GetMasterSlaveLink.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7SetSectorSymmetryLink = _ST7API.St7SetSectorSymmetryLink
St7SetSectorSymmetryLink.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetSectorSymmetryLink = _ST7API.St7GetSectorSymmetryLink
St7GetSectorSymmetryLink.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7SetCouplingLink = _ST7API.St7SetCouplingLink
St7SetCouplingLink.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetCouplingLink = _ST7API.St7GetCouplingLink
St7GetCouplingLink.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7SetPinnedLink = _ST7API.St7SetPinnedLink
St7SetPinnedLink.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetPinnedLink = _ST7API.St7GetPinnedLink
St7GetPinnedLink.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetRigidLink = _ST7API.St7SetRigidLink
St7SetRigidLink.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetRigidLink = _ST7API.St7GetRigidLink
St7GetRigidLink.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7SetShrinkLink = _ST7API.St7SetShrinkLink
St7SetShrinkLink.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7GetShrinkLink = _ST7API.St7GetShrinkLink
St7GetShrinkLink.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7SetTwoPointLink = _ST7API.St7SetTwoPointLink
St7SetTwoPointLink.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetTwoPointLink = _ST7API.St7GetTwoPointLink
St7GetTwoPointLink.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetAttachmentLink = _ST7API.St7SetAttachmentLink
St7SetAttachmentLink.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetAttachmentLink = _ST7API.St7GetAttachmentLink
St7GetAttachmentLink.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetMultiPointLink = _ST7API.St7SetMultiPointLink
St7SetMultiPointLink.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetNumMultiPointLinkNodes = _ST7API.St7GetNumMultiPointLinkNodes
St7GetNumMultiPointLinkNodes.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetMultiPointLink = _ST7API.St7GetMultiPointLink
St7GetMultiPointLink.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetLinkType = _ST7API.St7GetLinkType
St7GetLinkType.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetVertexXYZ = _ST7API.St7GetVertexXYZ
St7GetVertexXYZ.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetGeometryFaceOuterLoops = _ST7API.St7GetGeometryFaceOuterLoops
St7GetGeometryFaceOuterLoops.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetNumGeometryFaceCavityLoops = _ST7API.St7GetNumGeometryFaceCavityLoops
St7GetNumGeometryFaceCavityLoops.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetGeometryFaceCavityLoops = _ST7API.St7GetGeometryFaceCavityLoops
St7GetGeometryFaceCavityLoops.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetNumGeometryFaceEdges = _ST7API.St7GetNumGeometryFaceEdges
St7GetNumGeometryFaceEdges.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetGeometryFaceEdges = _ST7API.St7GetGeometryFaceEdges
St7GetGeometryFaceEdges.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetGeometryEdgeLength = _ST7API.St7GetGeometryEdgeLength
St7GetGeometryEdgeLength.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetNumGeometryFaceVertices = _ST7API.St7GetNumGeometryFaceVertices
St7GetNumGeometryFaceVertices.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetGeometryFaceVertices = _ST7API.St7GetGeometryFaceVertices
St7GetGeometryFaceVertices.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetGeometryEdgeVertices = _ST7API.St7GetGeometryEdgeVertices
St7GetGeometryEdgeVertices.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetGeometryFaceSurface = _ST7API.St7GetGeometryFaceSurface
St7GetGeometryFaceSurface.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetGeometrySurfaceType = _ST7API.St7GetGeometrySurfaceType
St7GetGeometrySurfaceType.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7InvalidateGeometryFace = _ST7API.St7InvalidateGeometryFace
St7InvalidateGeometryFace.argtypes = [c_long, c_long]
St7InvalidateGeometryFaceCavityLoopID = _ST7API.St7InvalidateGeometryFaceCavityLoopID
St7InvalidateGeometryFaceCavityLoopID.argtypes = [c_long, c_long, c_long]
St7InvalidateGeometryFaceCavityLoopIndex = _ST7API.St7InvalidateGeometryFaceCavityLoopIndex
St7InvalidateGeometryFaceCavityLoopIndex.argtypes = [c_long, c_long, c_long]
St7DeleteInvalidGeometryFaces = _ST7API.St7DeleteInvalidGeometryFaces
St7DeleteInvalidGeometryFaces.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7GetCleanGeometryData = _ST7API.St7GetCleanGeometryData
St7GetCleanGeometryData.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetCleanGeometryData = _ST7API.St7SetCleanGeometryData
St7SetCleanGeometryData.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7CleanGeometry = _ST7API.St7CleanGeometry
St7CleanGeometry.argtypes = [c_long, ctypes.POINTER(c_long), c_long]
St7GetGeometrySize = _ST7API.St7GetGeometrySize
St7GetGeometrySize.argtypes = [c_long, ctypes.POINTER(c_double)]
St7SurfaceMesh = _ST7API.St7SurfaceMesh
St7SurfaceMesh.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double), c_long]
St7SolidTetMesh = _ST7API.St7SolidTetMesh
St7SolidTetMesh.argtypes = [c_long, ctypes.POINTER(c_long), c_long]
St7MeshFromLoops = _ST7API.St7MeshFromLoops
St7MeshFromLoops.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double), ctypes.POINTER(c_long), ctypes.POINTER(c_double), c_long]
St7SetLoadPath = _ST7API.St7SetLoadPath
St7SetLoadPath.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetLoadPath = _ST7API.St7GetLoadPath
St7GetLoadPath.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7DeleteLoadPath = _ST7API.St7DeleteLoadPath
St7DeleteLoadPath.argtypes = [c_long, c_long]
St7SetNodeID = _ST7API.St7SetNodeID
St7SetNodeID.argtypes = [c_long, c_long, c_long]
St7SetNodeRestraint6 = _ST7API.St7SetNodeRestraint6
St7SetNodeRestraint6.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetNodeForce3 = _ST7API.St7SetNodeForce3
St7SetNodeForce3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetNodeMoment3 = _ST7API.St7SetNodeMoment3
St7SetNodeMoment3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetNodeTemperature1 = _ST7API.St7SetNodeTemperature1
St7SetNodeTemperature1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetNodeTemperatureType1 = _ST7API.St7SetNodeTemperatureType1
St7SetNodeTemperatureType1.argtypes = [c_long, c_long, c_long, c_long]
St7SetNodeTemperatureTable = _ST7API.St7SetNodeTemperatureTable
St7SetNodeTemperatureTable.argtypes = [c_long, c_long, c_long, c_long]
St7SetNodeKTranslation3F = _ST7API.St7SetNodeKTranslation3F
St7SetNodeKTranslation3F.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetNodeKRotation3F = _ST7API.St7SetNodeKRotation3F
St7SetNodeKRotation3F.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetNodeTMass3 = _ST7API.St7SetNodeTMass3
St7SetNodeTMass3.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetNodeRMass3 = _ST7API.St7SetNodeRMass3
St7SetNodeRMass3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetNodeNSMass5 = _ST7API.St7SetNodeNSMass5
St7SetNodeNSMass5.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetNodeKDamping3F = _ST7API.St7SetNodeKDamping3F
St7SetNodeKDamping3F.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetNodeHeatSource1 = _ST7API.St7SetNodeHeatSource1
St7SetNodeHeatSource1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetNodeHeatSourceTables = _ST7API.St7SetNodeHeatSourceTables
St7SetNodeHeatSourceTables.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetNodeInitialVelocity3 = _ST7API.St7SetNodeInitialVelocity3
St7SetNodeInitialVelocity3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetNodeAcceleration3 = _ST7API.St7SetNodeAcceleration3
St7SetNodeAcceleration3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetNodeResponse = _ST7API.St7SetNodeResponse
St7SetNodeResponse.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetNodeID = _ST7API.St7GetNodeID
St7GetNodeID.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetNodeRestraint6 = _ST7API.St7GetNodeRestraint6
St7GetNodeRestraint6.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetNodeForce3 = _ST7API.St7GetNodeForce3
St7GetNodeForce3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetNodeMoment3 = _ST7API.St7GetNodeMoment3
St7GetNodeMoment3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetNodeTemperature1 = _ST7API.St7GetNodeTemperature1
St7GetNodeTemperature1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetNodeTemperatureType1 = _ST7API.St7GetNodeTemperatureType1
St7GetNodeTemperatureType1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetNodeTemperatureTable = _ST7API.St7GetNodeTemperatureTable
St7GetNodeTemperatureTable.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetNodeTMass3 = _ST7API.St7GetNodeTMass3
St7GetNodeTMass3.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetNodeRMass3 = _ST7API.St7GetNodeRMass3
St7GetNodeRMass3.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetNodeKTranslation3F = _ST7API.St7GetNodeKTranslation3F
St7GetNodeKTranslation3F.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetNodeKRotation3F = _ST7API.St7GetNodeKRotation3F
St7GetNodeKRotation3F.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetNodeNSMass5 = _ST7API.St7GetNodeNSMass5
St7GetNodeNSMass5.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetNodeKDamping3F = _ST7API.St7GetNodeKDamping3F
St7GetNodeKDamping3F.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetNodeHeatSource1 = _ST7API.St7GetNodeHeatSource1
St7GetNodeHeatSource1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetNodeHeatSourceTables = _ST7API.St7GetNodeHeatSourceTables
St7GetNodeHeatSourceTables.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetNodeInitialVelocity3 = _ST7API.St7GetNodeInitialVelocity3
St7GetNodeInitialVelocity3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetNodeAcceleration3 = _ST7API.St7GetNodeAcceleration3
St7GetNodeAcceleration3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetNodeResponse = _ST7API.St7GetNodeResponse
St7GetNodeResponse.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7SetBeamID = _ST7API.St7SetBeamID
St7SetBeamID.argtypes = [c_long, c_long, c_long]
St7SetBeamReferenceAngle1 = _ST7API.St7SetBeamReferenceAngle1
St7SetBeamReferenceAngle1.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamConnectionUCS = _ST7API.St7SetBeamConnectionUCS
St7SetBeamConnectionUCS.argtypes = [c_long, c_long, c_long, c_long]
St7SetBeamTaper2 = _ST7API.St7SetBeamTaper2
St7SetBeamTaper2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamOffset2 = _ST7API.St7SetBeamOffset2
St7SetBeamOffset2.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamSupport2F = _ST7API.St7SetBeamSupport2F
St7SetBeamSupport2F.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamSectionFactor7 = _ST7API.St7SetBeamSectionFactor7
St7SetBeamSectionFactor7.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamTRelease3 = _ST7API.St7SetBeamTRelease3
St7SetBeamTRelease3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetBeamRRelease3 = _ST7API.St7SetBeamRRelease3
St7SetBeamRRelease3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetBeamCableFreeLength1 = _ST7API.St7SetBeamCableFreeLength1
St7SetBeamCableFreeLength1.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamRadius1 = _ST7API.St7SetBeamRadius1
St7SetBeamRadius1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPipePressure2AF = _ST7API.St7SetPipePressure2AF
St7SetPipePressure2AF.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPipeTemperature2OT = _ST7API.St7SetPipeTemperature2OT
St7SetPipeTemperature2OT.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamStringGroup1 = _ST7API.St7SetBeamStringGroup1
St7SetBeamStringGroup1.argtypes = [c_long, c_long, c_long]
St7SetBeamPreLoad1 = _ST7API.St7SetBeamPreLoad1
St7SetBeamPreLoad1.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamTempGradient2 = _ST7API.St7SetBeamTempGradient2
St7SetBeamTempGradient2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamCFL4ID = _ST7API.St7SetBeamCFL4ID
St7SetBeamCFL4ID.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamCFG4ID = _ST7API.St7SetBeamCFG4ID
St7SetBeamCFG4ID.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamCML4ID = _ST7API.St7SetBeamCML4ID
St7SetBeamCML4ID.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamCMG4ID = _ST7API.St7SetBeamCMG4ID
St7SetBeamCMG4ID.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamDLL6ID = _ST7API.St7SetBeamDLL6ID
St7SetBeamDLL6ID.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamDML6ID = _ST7API.St7SetBeamDML6ID
St7SetBeamDML6ID.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamDLG6ID = _ST7API.St7SetBeamDLG6ID
St7SetBeamDLG6ID.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamNSMass10ID = _ST7API.St7SetBeamNSMass10ID
St7SetBeamNSMass10ID.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamConvection2 = _ST7API.St7SetBeamConvection2
St7SetBeamConvection2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamConvectionTables = _ST7API.St7SetBeamConvectionTables
St7SetBeamConvectionTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetBeamRadiation2 = _ST7API.St7SetBeamRadiation2
St7SetBeamRadiation2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamRadiationTables = _ST7API.St7SetBeamRadiationTables
St7SetBeamRadiationTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetBeamFlux1 = _ST7API.St7SetBeamFlux1
St7SetBeamFlux1.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamFluxTables = _ST7API.St7SetBeamFluxTables
St7SetBeamFluxTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetBeamHeatSource1 = _ST7API.St7SetBeamHeatSource1
St7SetBeamHeatSource1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamHeatSourceTables = _ST7API.St7SetBeamHeatSourceTables
St7SetBeamHeatSourceTables.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetBeamResponse = _ST7API.St7SetBeamResponse
St7SetBeamResponse.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetBeamCreepLoadingAge1 = _ST7API.St7SetBeamCreepLoadingAge1
St7SetBeamCreepLoadingAge1.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamEndAttachment1 = _ST7API.St7SetBeamEndAttachment1
St7SetBeamEndAttachment1.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBeamID = _ST7API.St7GetBeamID
St7GetBeamID.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetBeamReferenceAngle1 = _ST7API.St7GetBeamReferenceAngle1
St7GetBeamReferenceAngle1.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetBeamConnectionUCS = _ST7API.St7GetBeamConnectionUCS
St7GetBeamConnectionUCS.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetBeamTaper2 = _ST7API.St7GetBeamTaper2
St7GetBeamTaper2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBeamOffset2 = _ST7API.St7GetBeamOffset2
St7GetBeamOffset2.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetBeamSupport2F = _ST7API.St7GetBeamSupport2F
St7GetBeamSupport2F.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBeamSectionFactor7 = _ST7API.St7GetBeamSectionFactor7
St7GetBeamSectionFactor7.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetBeamTRelease3 = _ST7API.St7GetBeamTRelease3
St7GetBeamTRelease3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBeamRRelease3 = _ST7API.St7GetBeamRRelease3
St7GetBeamRRelease3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBeamCableFreeLength1 = _ST7API.St7GetBeamCableFreeLength1
St7GetBeamCableFreeLength1.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetBeamRadius1 = _ST7API.St7GetBeamRadius1
St7GetBeamRadius1.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetPipePressure2AF = _ST7API.St7GetPipePressure2AF
St7GetPipePressure2AF.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetPipeTemperature2OT = _ST7API.St7GetPipeTemperature2OT
St7GetPipeTemperature2OT.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBeamStringGroup1 = _ST7API.St7GetBeamStringGroup1
St7GetBeamStringGroup1.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetBeamPreLoad1 = _ST7API.St7GetBeamPreLoad1
St7GetBeamPreLoad1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBeamTempGradient2 = _ST7API.St7GetBeamTempGradient2
St7GetBeamTempGradient2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBeamCFL4ID = _ST7API.St7GetBeamCFL4ID
St7GetBeamCFL4ID.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBeamCFG4ID = _ST7API.St7GetBeamCFG4ID
St7GetBeamCFG4ID.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBeamCML4ID = _ST7API.St7GetBeamCML4ID
St7GetBeamCML4ID.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBeamCMG4ID = _ST7API.St7GetBeamCMG4ID
St7GetBeamCMG4ID.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBeamDLL6ID = _ST7API.St7GetBeamDLL6ID
St7GetBeamDLL6ID.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBeamDML6ID = _ST7API.St7GetBeamDML6ID
St7GetBeamDML6ID.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBeamDLG6ID = _ST7API.St7GetBeamDLG6ID
St7GetBeamDLG6ID.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBeamNSMass10ID = _ST7API.St7GetBeamNSMass10ID
St7GetBeamNSMass10ID.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBeamConvection2 = _ST7API.St7GetBeamConvection2
St7GetBeamConvection2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBeamConvectionTables = _ST7API.St7GetBeamConvectionTables
St7GetBeamConvectionTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetBeamRadiation2 = _ST7API.St7GetBeamRadiation2
St7GetBeamRadiation2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBeamRadiationTables = _ST7API.St7GetBeamRadiationTables
St7GetBeamRadiationTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetBeamFlux1 = _ST7API.St7GetBeamFlux1
St7GetBeamFlux1.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBeamFluxTables = _ST7API.St7GetBeamFluxTables
St7GetBeamFluxTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetBeamHeatSource1 = _ST7API.St7GetBeamHeatSource1
St7GetBeamHeatSource1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBeamHeatSourceTables = _ST7API.St7GetBeamHeatSourceTables
St7GetBeamHeatSourceTables.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetBeamResponse = _ST7API.St7GetBeamResponse
St7GetBeamResponse.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetBeamCreepLoadingAge1 = _ST7API.St7GetBeamCreepLoadingAge1
St7GetBeamCreepLoadingAge1.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetBeamEndAttachment1 = _ST7API.St7GetBeamEndAttachment1
St7GetBeamEndAttachment1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetPlateID = _ST7API.St7SetPlateID
St7SetPlateID.argtypes = [c_long, c_long, c_long]
St7SetPlateXAngle1 = _ST7API.St7SetPlateXAngle1
St7SetPlateXAngle1.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateThickness2 = _ST7API.St7SetPlateThickness2
St7SetPlateThickness2.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateOffset1 = _ST7API.St7SetPlateOffset1
St7SetPlateOffset1.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateEdgeSupport1F = _ST7API.St7SetPlateEdgeSupport1F
St7SetPlateEdgeSupport1F.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateFaceSupport1F = _ST7API.St7SetPlateFaceSupport1F
St7SetPlateFaceSupport1F.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateEdgeRelease1 = _ST7API.St7SetPlateEdgeRelease1
St7SetPlateEdgeRelease1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetPlatePreLoad3 = _ST7API.St7SetPlatePreLoad3
St7SetPlatePreLoad3.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateTempGradient1 = _ST7API.St7SetPlateTempGradient1
St7SetPlateTempGradient1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlatePointForce6 = _ST7API.St7SetPlatePointForce6
St7SetPlatePointForce6.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlatePointMoment6 = _ST7API.St7SetPlatePointMoment6
St7SetPlatePointMoment6.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateEdgePressure1 = _ST7API.St7SetPlateEdgePressure1
St7SetPlateEdgePressure1.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateEdgeShear1 = _ST7API.St7SetPlateEdgeShear1
St7SetPlateEdgeShear1.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateEdgeNormalShear1 = _ST7API.St7SetPlateEdgeNormalShear1
St7SetPlateEdgeNormalShear1.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateNormalPressure1 = _ST7API.St7SetPlateNormalPressure1
St7SetPlateNormalPressure1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateGlobalPressure3 = _ST7API.St7SetPlateGlobalPressure3
St7SetPlateGlobalPressure3.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateShear2 = _ST7API.St7SetPlateShear2
St7SetPlateShear2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateNSMass5 = _ST7API.St7SetPlateNSMass5
St7SetPlateNSMass5.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateEdgeConvection2 = _ST7API.St7SetPlateEdgeConvection2
St7SetPlateEdgeConvection2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateEdgeConvectionTables = _ST7API.St7SetPlateEdgeConvectionTables
St7SetPlateEdgeConvectionTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetPlateEdgeRadiation2 = _ST7API.St7SetPlateEdgeRadiation2
St7SetPlateEdgeRadiation2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateEdgeRadiationTables = _ST7API.St7SetPlateEdgeRadiationTables
St7SetPlateEdgeRadiationTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetPlateFlux1 = _ST7API.St7SetPlateFlux1
St7SetPlateFlux1.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateFluxTables = _ST7API.St7SetPlateFluxTables
St7SetPlateFluxTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetPlateFaceConvection2 = _ST7API.St7SetPlateFaceConvection2
St7SetPlateFaceConvection2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateFaceConvectionTables = _ST7API.St7SetPlateFaceConvectionTables
St7SetPlateFaceConvectionTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetPlateFaceRadiation2 = _ST7API.St7SetPlateFaceRadiation2
St7SetPlateFaceRadiation2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateFaceRadiationTables = _ST7API.St7SetPlateFaceRadiationTables
St7SetPlateFaceRadiationTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetPlateHeatSource1 = _ST7API.St7SetPlateHeatSource1
St7SetPlateHeatSource1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateHeatSourceTables = _ST7API.St7SetPlateHeatSourceTables
St7SetPlateHeatSourceTables.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetPlateSoilStress2 = _ST7API.St7SetPlateSoilStress2
St7SetPlateSoilStress2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateSoilRatio2 = _ST7API.St7SetPlateSoilRatio2
St7SetPlateSoilRatio2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateResponse = _ST7API.St7SetPlateResponse
St7SetPlateResponse.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetPlateLoadPatch4 = _ST7API.St7SetPlateLoadPatch4
St7SetPlateLoadPatch4.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateReinforcement2 = _ST7API.St7SetPlateReinforcement2
St7SetPlateReinforcement2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateCreepLoadingAge1 = _ST7API.St7SetPlateCreepLoadingAge1
St7SetPlateCreepLoadingAge1.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateEdgeAttachment1 = _ST7API.St7SetPlateEdgeAttachment1
St7SetPlateEdgeAttachment1.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateFaceAttachment1 = _ST7API.St7SetPlateFaceAttachment1
St7SetPlateFaceAttachment1.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateID = _ST7API.St7GetPlateID
St7GetPlateID.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetPlateXAngle1 = _ST7API.St7GetPlateXAngle1
St7GetPlateXAngle1.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateThickness2 = _ST7API.St7GetPlateThickness2
St7GetPlateThickness2.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateOffset1 = _ST7API.St7GetPlateOffset1
St7GetPlateOffset1.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateEdgeSupport1F = _ST7API.St7GetPlateEdgeSupport1F
St7GetPlateEdgeSupport1F.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetPlateFaceSupport1F = _ST7API.St7GetPlateFaceSupport1F
St7GetPlateFaceSupport1F.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetPlateEdgeRelease1 = _ST7API.St7GetPlateEdgeRelease1
St7GetPlateEdgeRelease1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetPlatePreLoad3 = _ST7API.St7GetPlatePreLoad3
St7GetPlatePreLoad3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetPlateTempGradient1 = _ST7API.St7GetPlateTempGradient1
St7GetPlateTempGradient1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlatePointForce6 = _ST7API.St7GetPlatePointForce6
St7GetPlatePointForce6.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlatePointMoment6 = _ST7API.St7GetPlatePointMoment6
St7GetPlatePointMoment6.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateEdgePressure1 = _ST7API.St7GetPlateEdgePressure1
St7GetPlateEdgePressure1.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateEdgeShear1 = _ST7API.St7GetPlateEdgeShear1
St7GetPlateEdgeShear1.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateEdgeNormalShear1 = _ST7API.St7GetPlateEdgeNormalShear1
St7GetPlateEdgeNormalShear1.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateNormalPressure1 = _ST7API.St7GetPlateNormalPressure1
St7GetPlateNormalPressure1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateGlobalPressure3 = _ST7API.St7GetPlateGlobalPressure3
St7GetPlateGlobalPressure3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetPlateShear2 = _ST7API.St7GetPlateShear2
St7GetPlateShear2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateNSMass5 = _ST7API.St7GetPlateNSMass5
St7GetPlateNSMass5.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateEdgeConvection2 = _ST7API.St7GetPlateEdgeConvection2
St7GetPlateEdgeConvection2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateEdgeConvectionTables = _ST7API.St7GetPlateEdgeConvectionTables
St7GetPlateEdgeConvectionTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetPlateEdgeRadiation2 = _ST7API.St7GetPlateEdgeRadiation2
St7GetPlateEdgeRadiation2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateEdgeRadiationTables = _ST7API.St7GetPlateEdgeRadiationTables
St7GetPlateEdgeRadiationTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetPlateFlux1 = _ST7API.St7GetPlateFlux1
St7GetPlateFlux1.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateFluxTables = _ST7API.St7GetPlateFluxTables
St7GetPlateFluxTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetPlateFaceConvection2 = _ST7API.St7GetPlateFaceConvection2
St7GetPlateFaceConvection2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateFaceConvectionTables = _ST7API.St7GetPlateFaceConvectionTables
St7GetPlateFaceConvectionTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetPlateFaceRadiation2 = _ST7API.St7GetPlateFaceRadiation2
St7GetPlateFaceRadiation2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateFaceRadiationTables = _ST7API.St7GetPlateFaceRadiationTables
St7GetPlateFaceRadiationTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetPlateHeatSource1 = _ST7API.St7GetPlateHeatSource1
St7GetPlateHeatSource1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateHeatSourceTables = _ST7API.St7GetPlateHeatSourceTables
St7GetPlateHeatSourceTables.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetPlateSoilStress2 = _ST7API.St7GetPlateSoilStress2
St7GetPlateSoilStress2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateSoilRatio2 = _ST7API.St7GetPlateSoilRatio2
St7GetPlateSoilRatio2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateResponse = _ST7API.St7GetPlateResponse
St7GetPlateResponse.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7GetPlateLoadPatch4 = _ST7API.St7GetPlateLoadPatch4
St7GetPlateLoadPatch4.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetPlateReinforcement2 = _ST7API.St7GetPlateReinforcement2
St7GetPlateReinforcement2.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetPlateCreepLoadingAge1 = _ST7API.St7GetPlateCreepLoadingAge1
St7GetPlateCreepLoadingAge1.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateEdgeAttachment1 = _ST7API.St7GetPlateEdgeAttachment1
St7GetPlateEdgeAttachment1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetPlateFaceAttachment1 = _ST7API.St7GetPlateFaceAttachment1
St7GetPlateFaceAttachment1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetBrickID = _ST7API.St7SetBrickID
St7SetBrickID.argtypes = [c_long, c_long, c_long]
St7SetBrickLocalAxes1 = _ST7API.St7SetBrickLocalAxes1
St7SetBrickLocalAxes1.argtypes = [c_long, c_long, c_long]
St7SetBrickSupport1F = _ST7API.St7SetBrickSupport1F
St7SetBrickSupport1F.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBrickPreLoad3 = _ST7API.St7SetBrickPreLoad3
St7SetBrickPreLoad3.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBrickPointForce6 = _ST7API.St7SetBrickPointForce6
St7SetBrickPointForce6.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBrickNormalPressure1 = _ST7API.St7SetBrickNormalPressure1
St7SetBrickNormalPressure1.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBrickGlobalPressure3 = _ST7API.St7SetBrickGlobalPressure3
St7SetBrickGlobalPressure3.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBrickShear2 = _ST7API.St7SetBrickShear2
St7SetBrickShear2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBrickNSMass5 = _ST7API.St7SetBrickNSMass5
St7SetBrickNSMass5.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBrickConvection2 = _ST7API.St7SetBrickConvection2
St7SetBrickConvection2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBrickConvectionTables = _ST7API.St7SetBrickConvectionTables
St7SetBrickConvectionTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetBrickRadiation2 = _ST7API.St7SetBrickRadiation2
St7SetBrickRadiation2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBrickRadiationTables = _ST7API.St7SetBrickRadiationTables
St7SetBrickRadiationTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetBrickFlux1 = _ST7API.St7SetBrickFlux1
St7SetBrickFlux1.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBrickFluxTables = _ST7API.St7SetBrickFluxTables
St7SetBrickFluxTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetBrickHeatSource1 = _ST7API.St7SetBrickHeatSource1
St7SetBrickHeatSource1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBrickHeatSourceTables = _ST7API.St7SetBrickHeatSourceTables
St7SetBrickHeatSourceTables.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetBrickSoilStress2 = _ST7API.St7SetBrickSoilStress2
St7SetBrickSoilStress2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBrickSoilRatio2 = _ST7API.St7SetBrickSoilRatio2
St7SetBrickSoilRatio2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBrickResponse = _ST7API.St7SetBrickResponse
St7SetBrickResponse.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetBrickCreepLoadingAge1 = _ST7API.St7SetBrickCreepLoadingAge1
St7SetBrickCreepLoadingAge1.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetBrickFaceAttachment1 = _ST7API.St7SetBrickFaceAttachment1
St7SetBrickFaceAttachment1.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBrickID = _ST7API.St7GetBrickID
St7GetBrickID.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetBrickLocalAxes1 = _ST7API.St7GetBrickLocalAxes1
St7GetBrickLocalAxes1.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetBrickSupport1F = _ST7API.St7GetBrickSupport1F
St7GetBrickSupport1F.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBrickPreLoad3 = _ST7API.St7GetBrickPreLoad3
St7GetBrickPreLoad3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBrickPointForce6 = _ST7API.St7GetBrickPointForce6
St7GetBrickPointForce6.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBrickNormalPressure1 = _ST7API.St7GetBrickNormalPressure1
St7GetBrickNormalPressure1.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBrickGlobalPressure3 = _ST7API.St7GetBrickGlobalPressure3
St7GetBrickGlobalPressure3.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBrickShear2 = _ST7API.St7GetBrickShear2
St7GetBrickShear2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBrickNSMass5 = _ST7API.St7GetBrickNSMass5
St7GetBrickNSMass5.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBrickConvection2 = _ST7API.St7GetBrickConvection2
St7GetBrickConvection2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBrickConvectionTables = _ST7API.St7GetBrickConvectionTables
St7GetBrickConvectionTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetBrickRadiation2 = _ST7API.St7GetBrickRadiation2
St7GetBrickRadiation2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBrickRadiationTables = _ST7API.St7GetBrickRadiationTables
St7GetBrickRadiationTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetBrickFlux1 = _ST7API.St7GetBrickFlux1
St7GetBrickFlux1.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBrickFluxTables = _ST7API.St7GetBrickFluxTables
St7GetBrickFluxTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetBrickHeatSource1 = _ST7API.St7GetBrickHeatSource1
St7GetBrickHeatSource1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBrickHeatSourceTables = _ST7API.St7GetBrickHeatSourceTables
St7GetBrickHeatSourceTables.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetBrickSoilStress2 = _ST7API.St7GetBrickSoilStress2
St7GetBrickSoilStress2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBrickSoilRatio2 = _ST7API.St7GetBrickSoilRatio2
St7GetBrickSoilRatio2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBrickResponse = _ST7API.St7GetBrickResponse
St7GetBrickResponse.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7GetBrickCreepLoadingAge1 = _ST7API.St7GetBrickCreepLoadingAge1
St7GetBrickCreepLoadingAge1.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetBrickFaceAttachment1 = _ST7API.St7GetBrickFaceAttachment1
St7GetBrickFaceAttachment1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetVertexType = _ST7API.St7SetVertexType
St7SetVertexType.argtypes = [c_long, c_long, c_long]
St7SetVertexID = _ST7API.St7SetVertexID
St7SetVertexID.argtypes = [c_long, c_long, c_long]
St7SetVertexMeshSize1 = _ST7API.St7SetVertexMeshSize1
St7SetVertexMeshSize1.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetVertexRestraint6 = _ST7API.St7SetVertexRestraint6
St7SetVertexRestraint6.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetVertexForce3 = _ST7API.St7SetVertexForce3
St7SetVertexForce3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetVertexMoment3 = _ST7API.St7SetVertexMoment3
St7SetVertexMoment3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetVertexTemperature1 = _ST7API.St7SetVertexTemperature1
St7SetVertexTemperature1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetVertexTemperatureType1 = _ST7API.St7SetVertexTemperatureType1
St7SetVertexTemperatureType1.argtypes = [c_long, c_long, c_long, c_long]
St7SetVertexTemperatureTable = _ST7API.St7SetVertexTemperatureTable
St7SetVertexTemperatureTable.argtypes = [c_long, c_long, c_long, c_long]
St7SetVertexKTranslation3F = _ST7API.St7SetVertexKTranslation3F
St7SetVertexKTranslation3F.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetVertexKRotation3F = _ST7API.St7SetVertexKRotation3F
St7SetVertexKRotation3F.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetVertexTMass3 = _ST7API.St7SetVertexTMass3
St7SetVertexTMass3.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetVertexRMass3 = _ST7API.St7SetVertexRMass3
St7SetVertexRMass3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetVertexNSMass5 = _ST7API.St7SetVertexNSMass5
St7SetVertexNSMass5.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetVertexKDamping3F = _ST7API.St7SetVertexKDamping3F
St7SetVertexKDamping3F.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetVertexHeatSource1 = _ST7API.St7SetVertexHeatSource1
St7SetVertexHeatSource1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetVertexHeatSourceTables = _ST7API.St7SetVertexHeatSourceTables
St7SetVertexHeatSourceTables.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetVertexType = _ST7API.St7GetVertexType
St7GetVertexType.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetVertexID = _ST7API.St7GetVertexID
St7GetVertexID.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetVertexMeshSize1 = _ST7API.St7GetVertexMeshSize1
St7GetVertexMeshSize1.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetVertexRestraint6 = _ST7API.St7GetVertexRestraint6
St7GetVertexRestraint6.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetVertexForce3 = _ST7API.St7GetVertexForce3
St7GetVertexForce3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetVertexMoment3 = _ST7API.St7GetVertexMoment3
St7GetVertexMoment3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetVertexTemperature1 = _ST7API.St7GetVertexTemperature1
St7GetVertexTemperature1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetVertexTemperatureType1 = _ST7API.St7GetVertexTemperatureType1
St7GetVertexTemperatureType1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetVertexTemperatureTable = _ST7API.St7GetVertexTemperatureTable
St7GetVertexTemperatureTable.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetVertexKTranslation3F = _ST7API.St7GetVertexKTranslation3F
St7GetVertexKTranslation3F.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetVertexKRotation3F = _ST7API.St7GetVertexKRotation3F
St7GetVertexKRotation3F.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetVertexTMass3 = _ST7API.St7GetVertexTMass3
St7GetVertexTMass3.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetVertexRMass3 = _ST7API.St7GetVertexRMass3
St7GetVertexRMass3.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetVertexNSMass5 = _ST7API.St7GetVertexNSMass5
St7GetVertexNSMass5.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetVertexKDamping3F = _ST7API.St7GetVertexKDamping3F
St7GetVertexKDamping3F.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetVertexHeatSource1 = _ST7API.St7GetVertexHeatSource1
St7GetVertexHeatSource1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetVertexHeatSourceTables = _ST7API.St7GetVertexHeatSourceTables
St7GetVertexHeatSourceTables.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetGeometryEdgeType = _ST7API.St7SetGeometryEdgeType
St7SetGeometryEdgeType.argtypes = [c_long, c_long, c_long]
St7SetGeometryEdgeRelease1 = _ST7API.St7SetGeometryEdgeRelease1
St7SetGeometryEdgeRelease1.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetGeometryEdgeSupport1F = _ST7API.St7SetGeometryEdgeSupport1F
St7SetGeometryEdgeSupport1F.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetGeometryEdgePressure1 = _ST7API.St7SetGeometryEdgePressure1
St7SetGeometryEdgePressure1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetGeometryEdgeShear1 = _ST7API.St7SetGeometryEdgeShear1
St7SetGeometryEdgeShear1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetGeometryEdgeNormalShear1 = _ST7API.St7SetGeometryEdgeNormalShear1
St7SetGeometryEdgeNormalShear1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetGeometryEdgeConvection2 = _ST7API.St7SetGeometryEdgeConvection2
St7SetGeometryEdgeConvection2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetGeometryEdgeConvectionTables = _ST7API.St7SetGeometryEdgeConvectionTables
St7SetGeometryEdgeConvectionTables.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetGeometryEdgeRadiation2 = _ST7API.St7SetGeometryEdgeRadiation2
St7SetGeometryEdgeRadiation2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetGeometryEdgeRadiationTables = _ST7API.St7SetGeometryEdgeRadiationTables
St7SetGeometryEdgeRadiationTables.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetGeometryEdgeFlux1 = _ST7API.St7SetGeometryEdgeFlux1
St7SetGeometryEdgeFlux1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetGeometryEdgeFluxTables = _ST7API.St7SetGeometryEdgeFluxTables
St7SetGeometryEdgeFluxTables.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetGeometryEdgeAttachment1 = _ST7API.St7SetGeometryEdgeAttachment1
St7SetGeometryEdgeAttachment1.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetGeometryEdgeType = _ST7API.St7GetGeometryEdgeType
St7GetGeometryEdgeType.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetGeometryEdgeRelease1 = _ST7API.St7GetGeometryEdgeRelease1
St7GetGeometryEdgeRelease1.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetGeometryEdgeSupport1F = _ST7API.St7GetGeometryEdgeSupport1F
St7GetGeometryEdgeSupport1F.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetGeometryEdgePressure1 = _ST7API.St7GetGeometryEdgePressure1
St7GetGeometryEdgePressure1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetGeometryEdgeShear1 = _ST7API.St7GetGeometryEdgeShear1
St7GetGeometryEdgeShear1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetGeometryEdgeNormalShear1 = _ST7API.St7GetGeometryEdgeNormalShear1
St7GetGeometryEdgeNormalShear1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetGeometryEdgeConvection2 = _ST7API.St7GetGeometryEdgeConvection2
St7GetGeometryEdgeConvection2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetGeometryEdgeConvectionTables = _ST7API.St7GetGeometryEdgeConvectionTables
St7GetGeometryEdgeConvectionTables.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetGeometryEdgeRadiation2 = _ST7API.St7GetGeometryEdgeRadiation2
St7GetGeometryEdgeRadiation2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetGeometryEdgeRadiationTables = _ST7API.St7GetGeometryEdgeRadiationTables
St7GetGeometryEdgeRadiationTables.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetGeometryEdgeFlux1 = _ST7API.St7GetGeometryEdgeFlux1
St7GetGeometryEdgeFlux1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetGeometryEdgeFluxTables = _ST7API.St7GetGeometryEdgeFluxTables
St7GetGeometryEdgeFluxTables.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetGeometryEdgeAttachment1 = _ST7API.St7GetGeometryEdgeAttachment1
St7GetGeometryEdgeAttachment1.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetGeometryFaceProperty = _ST7API.St7SetGeometryFaceProperty
St7SetGeometryFaceProperty.argtypes = [c_long, c_long, c_long]
St7SetGeometryFaceID = _ST7API.St7SetGeometryFaceID
St7SetGeometryFaceID.argtypes = [c_long, c_long, c_long]
St7SetGeometryFaceOffset1 = _ST7API.St7SetGeometryFaceOffset1
St7SetGeometryFaceOffset1.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetGeometryFaceSupport1F = _ST7API.St7SetGeometryFaceSupport1F
St7SetGeometryFaceSupport1F.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetGeometryFaceTempGradient1 = _ST7API.St7SetGeometryFaceTempGradient1
St7SetGeometryFaceTempGradient1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetGeometryFaceNormalPressure1 = _ST7API.St7SetGeometryFaceNormalPressure1
St7SetGeometryFaceNormalPressure1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetGeometryFaceGlobalPressure3 = _ST7API.St7SetGeometryFaceGlobalPressure3
St7SetGeometryFaceGlobalPressure3.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetGeometryFaceNSMass5 = _ST7API.St7SetGeometryFaceNSMass5
St7SetGeometryFaceNSMass5.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetGeometryFaceConvection2 = _ST7API.St7SetGeometryFaceConvection2
St7SetGeometryFaceConvection2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetGeometryFaceConvectionTables = _ST7API.St7SetGeometryFaceConvectionTables
St7SetGeometryFaceConvectionTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetGeometryFaceRadiation2 = _ST7API.St7SetGeometryFaceRadiation2
St7SetGeometryFaceRadiation2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetGeometryFaceRadiationTables = _ST7API.St7SetGeometryFaceRadiationTables
St7SetGeometryFaceRadiationTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetGeometryFaceHeatSource1 = _ST7API.St7SetGeometryFaceHeatSource1
St7SetGeometryFaceHeatSource1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetGeometryFaceHeatSourceTables = _ST7API.St7SetGeometryFaceHeatSourceTables
St7SetGeometryFaceHeatSourceTables.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetGeometryFaceAttachment1 = _ST7API.St7SetGeometryFaceAttachment1
St7SetGeometryFaceAttachment1.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetGeometryFaceProperty = _ST7API.St7GetGeometryFaceProperty
St7GetGeometryFaceProperty.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetGeometryFaceID = _ST7API.St7GetGeometryFaceID
St7GetGeometryFaceID.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetGeometryFaceOffset1 = _ST7API.St7GetGeometryFaceOffset1
St7GetGeometryFaceOffset1.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetGeometryFaceSupport1F = _ST7API.St7GetGeometryFaceSupport1F
St7GetGeometryFaceSupport1F.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetGeometryFaceTempGradient1 = _ST7API.St7GetGeometryFaceTempGradient1
St7GetGeometryFaceTempGradient1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetGeometryFaceNormalPressure1 = _ST7API.St7GetGeometryFaceNormalPressure1
St7GetGeometryFaceNormalPressure1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetGeometryFaceGlobalPressure3 = _ST7API.St7GetGeometryFaceGlobalPressure3
St7GetGeometryFaceGlobalPressure3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetGeometryFaceNSMass5 = _ST7API.St7GetGeometryFaceNSMass5
St7GetGeometryFaceNSMass5.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetGeometryFaceConvection2 = _ST7API.St7GetGeometryFaceConvection2
St7GetGeometryFaceConvection2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetGeometryFaceConvectionTables = _ST7API.St7GetGeometryFaceConvectionTables
St7GetGeometryFaceConvectionTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetGeometryFaceRadiation2 = _ST7API.St7GetGeometryFaceRadiation2
St7GetGeometryFaceRadiation2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetGeometryFaceRadiationTables = _ST7API.St7GetGeometryFaceRadiationTables
St7GetGeometryFaceRadiationTables.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetGeometryFaceHeatSource1 = _ST7API.St7GetGeometryFaceHeatSource1
St7GetGeometryFaceHeatSource1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetGeometryFaceHeatSourceTables = _ST7API.St7GetGeometryFaceHeatSourceTables
St7GetGeometryFaceHeatSourceTables.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetGeometryFaceAttachment1 = _ST7API.St7GetGeometryFaceAttachment1
St7GetGeometryFaceAttachment1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetElementProperty = _ST7API.St7GetElementProperty
St7GetElementProperty.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetElementPropertySequence = _ST7API.St7GetElementPropertySequence
St7GetElementPropertySequence.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7SetElementProperty = _ST7API.St7SetElementProperty
St7SetElementProperty.argtypes = [c_long, c_long, c_long, c_long]
St7SetElementPropertySwitch = _ST7API.St7SetElementPropertySwitch
St7SetElementPropertySwitch.argtypes = [c_long, c_long, c_long, c_long, c_long]
St7DeleteAttribute = _ST7API.St7DeleteAttribute
St7DeleteAttribute.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetEntityGroup = _ST7API.St7SetEntityGroup
St7SetEntityGroup.argtypes = [c_long, c_long, c_long, c_long]
St7GetEntityGroup = _ST7API.St7GetEntityGroup
St7GetEntityGroup.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetTotalProperties = _ST7API.St7GetTotalProperties
St7GetTotalProperties.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7GetTotalCreepDefinitions = _ST7API.St7GetTotalCreepDefinitions
St7GetTotalCreepDefinitions.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7GetTotalLaminateStacks = _ST7API.St7GetTotalLaminateStacks
St7GetTotalLaminateStacks.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7GetTotalLoadPathTemplates = _ST7API.St7GetTotalLoadPathTemplates
St7GetTotalLoadPathTemplates.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7GetTotalReinforcementLayouts = _ST7API.St7GetTotalReinforcementLayouts
St7GetTotalReinforcementLayouts.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7GetPropertyNumByIndex = _ST7API.St7GetPropertyNumByIndex
St7GetPropertyNumByIndex.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetCreepDefinitionNumByIndex = _ST7API.St7GetCreepDefinitionNumByIndex
St7GetCreepDefinitionNumByIndex.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetLaminateStackNumByIndex = _ST7API.St7GetLaminateStackNumByIndex
St7GetLaminateStackNumByIndex.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetLoadPathTemplateNumByIndex = _ST7API.St7GetLoadPathTemplateNumByIndex
St7GetLoadPathTemplateNumByIndex.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetReinforcementLayoutNumByIndex = _ST7API.St7GetReinforcementLayoutNumByIndex
St7GetReinforcementLayoutNumByIndex.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetPropertyName = _ST7API.St7SetPropertyName
St7SetPropertyName.argtypes = [c_long, c_long, c_long, c_char_p]
St7GetPropertyName = _ST7API.St7GetPropertyName
St7GetPropertyName.argtypes = [c_long, c_long, c_long, c_char_p, c_long]
St7SetPropertyColour = _ST7API.St7SetPropertyColour
St7SetPropertyColour.argtypes = [c_long, c_long, c_long, c_long]
St7GetPropertyColour = _ST7API.St7GetPropertyColour
St7GetPropertyColour.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetPropertyTable = _ST7API.St7SetPropertyTable
St7SetPropertyTable.argtypes = [c_long, c_long, c_long, c_long]
St7GetPropertyTable = _ST7API.St7GetPropertyTable
St7GetPropertyTable.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetPropertyCreepID = _ST7API.St7SetPropertyCreepID
St7SetPropertyCreepID.argtypes = [c_long, c_long, c_long, c_long]
St7GetPropertyCreepID = _ST7API.St7GetPropertyCreepID
St7GetPropertyCreepID.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetMaterialName = _ST7API.St7SetMaterialName
St7SetMaterialName.argtypes = [c_long, c_long, c_long, c_char_p]
St7GetMaterialName = _ST7API.St7GetMaterialName
St7GetMaterialName.argtypes = [c_long, c_long, c_long, c_char_p, c_long]
St7SetTimeDependentModType = _ST7API.St7SetTimeDependentModType
St7SetTimeDependentModType.argtypes = [c_long, c_long, c_long, c_long]
St7GetTimeDependentModType = _ST7API.St7GetTimeDependentModType
St7GetTimeDependentModType.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetHardeningType = _ST7API.St7SetHardeningType
St7SetHardeningType.argtypes = [c_long, c_long, c_long, c_long]
St7GetHardeningType = _ST7API.St7GetHardeningType
St7GetHardeningType.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetAlphaTempType = _ST7API.St7GetAlphaTempType
St7GetAlphaTempType.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetAlphaTempType = _ST7API.St7SetAlphaTempType
St7SetAlphaTempType.argtypes = [c_long, c_long, c_long, c_long]
St7NewBeamProperty = _ST7API.St7NewBeamProperty
St7NewBeamProperty.argtypes = [c_long, c_long, c_long, c_char_p]
St7GetBeamPropertyData = _ST7API.St7GetBeamPropertyData
St7GetBeamPropertyData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double), ctypes.POINTER(c_double)]
St7GetBeamSectionName = _ST7API.St7GetBeamSectionName
St7GetBeamSectionName.argtypes = [c_long, c_long, c_char_p, c_long]
St7SetBeamSectionName = _ST7API.St7SetBeamSectionName
St7SetBeamSectionName.argtypes = [c_long, c_long, c_char_p]
St7SetBeamPropertyType = _ST7API.St7SetBeamPropertyType
St7SetBeamPropertyType.argtypes = [c_long, c_long, c_long]
St7SetBeamMirrorOption = _ST7API.St7SetBeamMirrorOption
St7SetBeamMirrorOption.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamNonlinearType = _ST7API.St7SetBeamNonlinearType
St7SetBeamNonlinearType.argtypes = [c_long, c_long, c_long]
St7GetBeamNonlinearType = _ST7API.St7GetBeamNonlinearType
St7GetBeamNonlinearType.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetBeamSectionPropertyData = _ST7API.St7SetBeamSectionPropertyData
St7SetBeamSectionPropertyData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBeamSectionPropertyData = _ST7API.St7GetBeamSectionPropertyData
St7GetBeamSectionPropertyData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetBeamSectionGeometry = _ST7API.St7SetBeamSectionGeometry
St7SetBeamSectionGeometry.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBeamSectionGeometry = _ST7API.St7GetBeamSectionGeometry
St7GetBeamSectionGeometry.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetBeamSectionNominalDiscretisation = _ST7API.St7SetBeamSectionNominalDiscretisation
St7SetBeamSectionNominalDiscretisation.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetBeamSectionNominalDiscretisation = _ST7API.St7GetBeamSectionNominalDiscretisation
St7GetBeamSectionNominalDiscretisation.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetBeamSectionCircularDiscretisation = _ST7API.St7SetBeamSectionCircularDiscretisation
St7SetBeamSectionCircularDiscretisation.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetBeamSectionCircularDiscretisation = _ST7API.St7GetBeamSectionCircularDiscretisation
St7GetBeamSectionCircularDiscretisation.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7CalculateBeamSectionProperties = _ST7API.St7CalculateBeamSectionProperties
St7CalculateBeamSectionProperties.argtypes = [c_long, c_long, c_bool, c_bool]
St7AssignBXS = _ST7API.St7AssignBXS
St7AssignBXS.argtypes = [c_long, c_long, c_char_p]
St7SetSpringDamperData = _ST7API.St7SetSpringDamperData
St7SetSpringDamperData.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetSpringDamperData = _ST7API.St7GetSpringDamperData
St7GetSpringDamperData.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetTrussData = _ST7API.St7SetTrussData
St7SetTrussData.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetTrussData = _ST7API.St7GetTrussData
St7GetTrussData.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetCableData = _ST7API.St7SetCableData
St7SetCableData.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetCableData = _ST7API.St7GetCableData
St7GetCableData.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetCutoffBarData = _ST7API.St7SetCutoffBarData
St7SetCutoffBarData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetCutoffBarData = _ST7API.St7GetCutoffBarData
St7GetCutoffBarData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetPointContactData = _ST7API.St7SetPointContactData
St7SetPointContactData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetPointContactData = _ST7API.St7GetPointContactData
St7GetPointContactData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetPipeData = _ST7API.St7SetPipeData
St7SetPipeData.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetPipeData = _ST7API.St7GetPipeData
St7GetPipeData.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetConnectionData = _ST7API.St7SetConnectionData
St7SetConnectionData.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetConnectionData = _ST7API.St7GetConnectionData
St7GetConnectionData.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetUserBeamData = _ST7API.St7SetUserBeamData
St7SetUserBeamData.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetUserBeamData = _ST7API.St7GetUserBeamData
St7GetUserBeamData.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamMaterialData = _ST7API.St7SetBeamMaterialData
St7SetBeamMaterialData.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetBeamMaterialData = _ST7API.St7GetBeamMaterialData
St7GetBeamMaterialData.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamUsePoisson = _ST7API.St7SetBeamUsePoisson
St7SetBeamUsePoisson.argtypes = [c_long, c_long]
St7SetBeamUseShearMod = _ST7API.St7SetBeamUseShearMod
St7SetBeamUseShearMod.argtypes = [c_long, c_long]
St7GetBeamUseMomCurv = _ST7API.St7GetBeamUseMomCurv
St7GetBeamUseMomCurv.argtypes = [c_long, c_long, ctypes.POINTER(c_bool)]
St7SetBeamUseMomCurv = _ST7API.St7SetBeamUseMomCurv
St7SetBeamUseMomCurv.argtypes = [c_long, c_long, c_bool]
St7NewPlateProperty = _ST7API.St7NewPlateProperty
St7NewPlateProperty.argtypes = [c_long, c_long, c_long, c_long, c_char_p]
St7GetPlatePropertyData = _ST7API.St7GetPlatePropertyData
St7GetPlatePropertyData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double), ctypes.POINTER(c_double)]
St7SetPlatePropertyType = _ST7API.St7SetPlatePropertyType
St7SetPlatePropertyType.argtypes = [c_long, c_long, c_long, c_long]
St7GetPlatePropertyType = _ST7API.St7GetPlatePropertyType
St7GetPlatePropertyType.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7SetPlateNonlinearType = _ST7API.St7SetPlateNonlinearType
St7SetPlateNonlinearType.argtypes = [c_long, c_long, c_long, c_long]
St7GetPlateNonlinearType = _ST7API.St7GetPlateNonlinearType
St7GetPlateNonlinearType.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7SetPlateThickness = _ST7API.St7SetPlateThickness
St7SetPlateThickness.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateThickness = _ST7API.St7GetPlateThickness
St7GetPlateThickness.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateLayers = _ST7API.St7SetPlateLayers
St7SetPlateLayers.argtypes = [c_long, c_long, c_long]
St7GetPlateLayers = _ST7API.St7GetPlateLayers
St7GetPlateLayers.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetPlateIsotropicMaterial = _ST7API.St7SetPlateIsotropicMaterial
St7SetPlateIsotropicMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateIsotropicMaterial = _ST7API.St7GetPlateIsotropicMaterial
St7GetPlateIsotropicMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateOrthotropicMaterial = _ST7API.St7SetPlateOrthotropicMaterial
St7SetPlateOrthotropicMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateOrthotropicMaterial = _ST7API.St7GetPlateOrthotropicMaterial
St7GetPlateOrthotropicMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateRubberMaterial = _ST7API.St7SetPlateRubberMaterial
St7SetPlateRubberMaterial.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateRubberMaterial = _ST7API.St7GetPlateRubberMaterial
St7GetPlateRubberMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetPlateAnisotropicMaterial = _ST7API.St7SetPlateAnisotropicMaterial
St7SetPlateAnisotropicMaterial.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateAnisotropicMaterial = _ST7API.St7GetPlateAnisotropicMaterial
St7GetPlateAnisotropicMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetPlateUserDefinedMaterial = _ST7API.St7SetPlateUserDefinedMaterial
St7SetPlateUserDefinedMaterial.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateUserDefinedMaterial = _ST7API.St7GetPlateUserDefinedMaterial
St7GetPlateUserDefinedMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetPlateMCDPMaterial = _ST7API.St7SetPlateMCDPMaterial
St7SetPlateMCDPMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateMCDPMaterial = _ST7API.St7GetPlateMCDPMaterial
St7GetPlateMCDPMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateSoilDCMaterial = _ST7API.St7SetPlateSoilDCMaterial
St7SetPlateSoilDCMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetPlateSoilDCMaterial = _ST7API.St7GetPlateSoilDCMaterial
St7GetPlateSoilDCMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetPlateSoilCCMaterial = _ST7API.St7SetPlateSoilCCMaterial
St7SetPlateSoilCCMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetPlateSoilCCMaterial = _ST7API.St7GetPlateSoilCCMaterial
St7GetPlateSoilCCMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetPlateSoilMCMaterial = _ST7API.St7SetPlateSoilMCMaterial
St7SetPlateSoilMCMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetPlateSoilMCMaterial = _ST7API.St7GetPlateSoilMCMaterial
St7GetPlateSoilMCMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetPlateSoilDPMaterial = _ST7API.St7SetPlateSoilDPMaterial
St7SetPlateSoilDPMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetPlateSoilDPMaterial = _ST7API.St7GetPlateSoilDPMaterial
St7GetPlateSoilDPMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetPlateSoilLSMaterial = _ST7API.St7SetPlateSoilLSMaterial
St7SetPlateSoilLSMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetPlateSoilLSMaterial = _ST7API.St7GetPlateSoilLSMaterial
St7GetPlateSoilLSMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetPlateFluidMaterial = _ST7API.St7SetPlateFluidMaterial
St7SetPlateFluidMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateFluidMaterial = _ST7API.St7GetPlateFluidMaterial
St7GetPlateFluidMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetPlateUseReducedInt = _ST7API.St7GetPlateUseReducedInt
St7GetPlateUseReducedInt.argtypes = [c_long, c_long, ctypes.POINTER(c_bool)]
St7SetPlateUseReducedInt = _ST7API.St7SetPlateUseReducedInt
St7SetPlateUseReducedInt.argtypes = [c_long, c_long, c_bool]
St7NewBrickProperty = _ST7API.St7NewBrickProperty
St7NewBrickProperty.argtypes = [c_long, c_long, c_long, c_char_p]
St7GetBrickPropertyData = _ST7API.St7GetBrickPropertyData
St7GetBrickPropertyData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetBrickPropertyType = _ST7API.St7SetBrickPropertyType
St7SetBrickPropertyType.argtypes = [c_long, c_long, c_long]
St7GetBrickPropertyType = _ST7API.St7GetBrickPropertyType
St7GetBrickPropertyType.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetBrickNonlinearType = _ST7API.St7SetBrickNonlinearType
St7SetBrickNonlinearType.argtypes = [c_long, c_long, c_long, c_long]
St7GetBrickNonlinearType = _ST7API.St7GetBrickNonlinearType
St7GetBrickNonlinearType.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7SetBrickIsotropicMaterial = _ST7API.St7SetBrickIsotropicMaterial
St7SetBrickIsotropicMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetBrickIsotropicMaterial = _ST7API.St7GetBrickIsotropicMaterial
St7GetBrickIsotropicMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetBrickOrthotropicMaterial = _ST7API.St7SetBrickOrthotropicMaterial
St7SetBrickOrthotropicMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetBrickOrthotropicMaterial = _ST7API.St7GetBrickOrthotropicMaterial
St7GetBrickOrthotropicMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetBrickAnisotropicMaterial = _ST7API.St7SetBrickAnisotropicMaterial
St7SetBrickAnisotropicMaterial.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBrickAnisotropicMaterial = _ST7API.St7GetBrickAnisotropicMaterial
St7GetBrickAnisotropicMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetBrickRubberMaterial = _ST7API.St7SetBrickRubberMaterial
St7SetBrickRubberMaterial.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBrickRubberMaterial = _ST7API.St7GetBrickRubberMaterial
St7GetBrickRubberMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetBrickMCDPMaterial = _ST7API.St7SetBrickMCDPMaterial
St7SetBrickMCDPMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetBrickMCDPMaterial = _ST7API.St7GetBrickMCDPMaterial
St7GetBrickMCDPMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetBrickSoilDCMaterial = _ST7API.St7SetBrickSoilDCMaterial
St7SetBrickSoilDCMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBrickSoilDCMaterial = _ST7API.St7GetBrickSoilDCMaterial
St7GetBrickSoilDCMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetBrickSoilCCMaterial = _ST7API.St7SetBrickSoilCCMaterial
St7SetBrickSoilCCMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBrickSoilCCMaterial = _ST7API.St7GetBrickSoilCCMaterial
St7GetBrickSoilCCMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetBrickSoilMCMaterial = _ST7API.St7SetBrickSoilMCMaterial
St7SetBrickSoilMCMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBrickSoilMCMaterial = _ST7API.St7GetBrickSoilMCMaterial
St7GetBrickSoilMCMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetBrickSoilDPMaterial = _ST7API.St7SetBrickSoilDPMaterial
St7SetBrickSoilDPMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBrickSoilDPMaterial = _ST7API.St7GetBrickSoilDPMaterial
St7GetBrickSoilDPMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetBrickSoilLSMaterial = _ST7API.St7SetBrickSoilLSMaterial
St7SetBrickSoilLSMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBrickSoilLSMaterial = _ST7API.St7GetBrickSoilLSMaterial
St7GetBrickSoilLSMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetBrickFluidMaterial = _ST7API.St7SetBrickFluidMaterial
St7SetBrickFluidMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetBrickFluidMaterial = _ST7API.St7GetBrickFluidMaterial
St7GetBrickFluidMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetBrickAddBubbleFunction = _ST7API.St7GetBrickAddBubbleFunction
St7GetBrickAddBubbleFunction.argtypes = [c_long, c_long, ctypes.POINTER(c_bool)]
St7SetBrickAddBubbleFunction = _ST7API.St7SetBrickAddBubbleFunction
St7SetBrickAddBubbleFunction.argtypes = [c_long, c_long, c_bool]
St7DeleteProperty = _ST7API.St7DeleteProperty
St7DeleteProperty.argtypes = [c_long, c_long, c_long]
St7DeleteUnusedProperties = _ST7API.St7DeleteUnusedProperties
St7DeleteUnusedProperties.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7UpdateElementPropertyData = _ST7API.St7UpdateElementPropertyData
St7UpdateElementPropertyData.argtypes = [c_long, c_long, c_long]
St7NewPlyProperty = _ST7API.St7NewPlyProperty
St7NewPlyProperty.argtypes = [c_long, c_long, c_char_p]
St7GetPlyMaterial = _ST7API.St7GetPlyMaterial
St7GetPlyMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetPlyMaterial = _ST7API.St7SetPlyMaterial
St7SetPlyMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetPlateLaminateMaterial = _ST7API.St7GetPlateLaminateMaterial
St7GetPlateLaminateMaterial.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetPlateLaminateMaterial = _ST7API.St7SetPlateLaminateMaterial
St7SetPlateLaminateMaterial.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7NewLaminate = _ST7API.St7NewLaminate
St7NewLaminate.argtypes = [c_long, c_long, c_char_p]
St7GetLaminateName = _ST7API.St7GetLaminateName
St7GetLaminateName.argtypes = [c_long, c_long, c_char_p, c_long]
St7SetLaminateName = _ST7API.St7SetLaminateName
St7SetLaminateName.argtypes = [c_long, c_long, c_char_p]
St7GetLaminateNumPlies = _ST7API.St7GetLaminateNumPlies
St7GetLaminateNumPlies.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetLaminatePly = _ST7API.St7GetLaminatePly
St7GetLaminatePly.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetLaminatePly = _ST7API.St7SetLaminatePly
St7SetLaminatePly.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7AddLaminatePly = _ST7API.St7AddLaminatePly
St7AddLaminatePly.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7DeleteLaminatePly = _ST7API.St7DeleteLaminatePly
St7DeleteLaminatePly.argtypes = [c_long, c_long, c_long]
St7InsertLaminatePly = _ST7API.St7InsertLaminatePly
St7InsertLaminatePly.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetLaminateMatrices = _ST7API.St7GetLaminateMatrices
St7GetLaminateMatrices.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetLaminateMatrices = _ST7API.St7SetLaminateMatrices
St7SetLaminateMatrices.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7DeleteLaminate = _ST7API.St7DeleteLaminate
St7DeleteLaminate.argtypes = [c_long, c_long]
St7DeleteUnusedLaminates = _ST7API.St7DeleteUnusedLaminates
St7DeleteUnusedLaminates.argtypes = [c_long, ctypes.POINTER(c_long)]
St7NewReinforcementLayout = _ST7API.St7NewReinforcementLayout
St7NewReinforcementLayout.argtypes = [c_long, c_long, c_char_p]
St7GetReinforcementName = _ST7API.St7GetReinforcementName
St7GetReinforcementName.argtypes = [c_long, c_long, c_char_p, c_long]
St7SetReinforcementName = _ST7API.St7SetReinforcementName
St7SetReinforcementName.argtypes = [c_long, c_long, c_char_p]
St7GetReinforcementData = _ST7API.St7GetReinforcementData
St7GetReinforcementData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetReinforcementData = _ST7API.St7SetReinforcementData
St7SetReinforcementData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7DeleteReinforcementLayout = _ST7API.St7DeleteReinforcementLayout
St7DeleteReinforcementLayout.argtypes = [c_long, c_long]
St7NewCreepDefinition = _ST7API.St7NewCreepDefinition
St7NewCreepDefinition.argtypes = [c_long, c_long, c_char_p]
St7GetCreepDefinitionName = _ST7API.St7GetCreepDefinitionName
St7GetCreepDefinitionName.argtypes = [c_long, c_long, c_char_p, c_long]
St7SetCreepDefinitionName = _ST7API.St7SetCreepDefinitionName
St7SetCreepDefinitionName.argtypes = [c_long, c_long, c_char_p]
St7GetCreepLaw = _ST7API.St7GetCreepLaw
St7GetCreepLaw.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetCreepLaw = _ST7API.St7SetCreepLaw
St7SetCreepLaw.argtypes = [c_long, c_long, c_long]
St7GetCreepBasicData = _ST7API.St7GetCreepBasicData
St7GetCreepBasicData.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetCreepBasicData = _ST7API.St7SetCreepBasicData
St7SetCreepBasicData.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7EnableCreepUserTable = _ST7API.St7EnableCreepUserTable
St7EnableCreepUserTable.argtypes = [c_long, c_long, c_long]
St7DisableCreepUserTable = _ST7API.St7DisableCreepUserTable
St7DisableCreepUserTable.argtypes = [c_long, c_long, c_long]
St7GetCreepUserTableState = _ST7API.St7GetCreepUserTableState
St7GetCreepUserTableState.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_bool)]
St7GetCreepUserTableData = _ST7API.St7GetCreepUserTableData
St7GetCreepUserTableData.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetCreepUserTableData = _ST7API.St7SetCreepUserTableData
St7SetCreepUserTableData.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetCreepHardeningType = _ST7API.St7GetCreepHardeningType
St7GetCreepHardeningType.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetCreepHardeningType = _ST7API.St7SetCreepHardeningType
St7SetCreepHardeningType.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetCreepTimeUnit = _ST7API.St7GetCreepTimeUnit
St7GetCreepTimeUnit.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetCreepTimeUnit = _ST7API.St7SetCreepTimeUnit
St7SetCreepTimeUnit.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetCreepTemperatureInclude = _ST7API.St7GetCreepTemperatureInclude
St7GetCreepTemperatureInclude.argtypes = [c_long, c_long, ctypes.POINTER(c_bool)]
St7SetCreepTemperatureInclude = _ST7API.St7SetCreepTemperatureInclude
St7SetCreepTemperatureInclude.argtypes = [c_long, c_long, c_bool]
St7GetCreepConcreteHyperbolicData = _ST7API.St7GetCreepConcreteHyperbolicData
St7GetCreepConcreteHyperbolicData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetCreepConcreteHyperbolicData = _ST7API.St7SetCreepConcreteHyperbolicData
St7SetCreepConcreteHyperbolicData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetCreepConcreteViscoChainData = _ST7API.St7GetCreepConcreteViscoChainData
St7GetCreepConcreteViscoChainData.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetCreepConcreteViscoChainData = _ST7API.St7SetCreepConcreteViscoChainData
St7SetCreepConcreteViscoChainData.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7EnableCreepConcreteUserTable = _ST7API.St7EnableCreepConcreteUserTable
St7EnableCreepConcreteUserTable.argtypes = [c_long, c_long, c_long]
St7DisableCreepConcreteUserTable = _ST7API.St7DisableCreepConcreteUserTable
St7DisableCreepConcreteUserTable.argtypes = [c_long, c_long, c_long]
St7GetCreepConcreteUserTableState = _ST7API.St7GetCreepConcreteUserTableState
St7GetCreepConcreteUserTableState.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_bool)]
St7GetCreepConcreteUserTableData = _ST7API.St7GetCreepConcreteUserTableData
St7GetCreepConcreteUserTableData.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetCreepConcreteUserTableData = _ST7API.St7SetCreepConcreteUserTableData
St7SetCreepConcreteUserTableData.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetCreepConcreteFunctionType = _ST7API.St7GetCreepConcreteFunctionType
St7GetCreepConcreteFunctionType.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetCreepConcreteFunctionType = _ST7API.St7SetCreepConcreteFunctionType
St7SetCreepConcreteFunctionType.argtypes = [c_long, c_long, c_long]
St7GetCreepConcreteLoadingAge = _ST7API.St7GetCreepConcreteLoadingAge
St7GetCreepConcreteLoadingAge.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetCreepConcreteLoadingAge = _ST7API.St7SetCreepConcreteLoadingAge
St7SetCreepConcreteLoadingAge.argtypes = [c_long, c_long, c_double]
St7GetCreepConcreteLoadingTimeUnit = _ST7API.St7GetCreepConcreteLoadingTimeUnit
St7GetCreepConcreteLoadingTimeUnit.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetCreepConcreteLoadingTimeUnit = _ST7API.St7SetCreepConcreteLoadingTimeUnit
St7SetCreepConcreteLoadingTimeUnit.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetCreepConcreteShrinkageType = _ST7API.St7GetCreepConcreteShrinkageType
St7GetCreepConcreteShrinkageType.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetCreepConcreteShrinkageType = _ST7API.St7SetCreepConcreteShrinkageType
St7SetCreepConcreteShrinkageType.argtypes = [c_long, c_long, c_long]
St7GetCreepConcreteShrinkageFormulaData = _ST7API.St7GetCreepConcreteShrinkageFormulaData
St7GetCreepConcreteShrinkageFormulaData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetCreepConcreteShrinkageFormulaData = _ST7API.St7SetCreepConcreteShrinkageFormulaData
St7SetCreepConcreteShrinkageFormulaData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetCreepConcreteShrinkageTableData = _ST7API.St7GetCreepConcreteShrinkageTableData
St7GetCreepConcreteShrinkageTableData.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetCreepConcreteShrinkageTableData = _ST7API.St7SetCreepConcreteShrinkageTableData
St7SetCreepConcreteShrinkageTableData.argtypes = [c_long, c_long, c_long]
St7GetCreepConcreteTemperatureData = _ST7API.St7GetCreepConcreteTemperatureData
St7GetCreepConcreteTemperatureData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetCreepConcreteTemperatureData = _ST7API.St7SetCreepConcreteTemperatureData
St7SetCreepConcreteTemperatureData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetCreepConcreteCementCuringData = _ST7API.St7GetCreepConcreteCementCuringData
St7GetCreepConcreteCementCuringData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetCreepConcreteCementCuringData = _ST7API.St7SetCreepConcreteCementCuringData
St7SetCreepConcreteCementCuringData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7DeleteCreepDefinition = _ST7API.St7DeleteCreepDefinition
St7DeleteCreepDefinition.argtypes = [c_long, c_long]
St7NewLoadPathTemplate = _ST7API.St7NewLoadPathTemplate
St7NewLoadPathTemplate.argtypes = [c_long, c_long, c_char_p]
St7GetLoadPathTemplateName = _ST7API.St7GetLoadPathTemplateName
St7GetLoadPathTemplateName.argtypes = [c_long, c_long, c_char_p, c_long]
St7SetLoadPathTemplateName = _ST7API.St7SetLoadPathTemplateName
St7SetLoadPathTemplateName.argtypes = [c_long, c_long, c_char_p]
St7GetLoadPathTemplateParameters = _ST7API.St7GetLoadPathTemplateParameters
St7GetLoadPathTemplateParameters.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetLoadPathTemplateParameters = _ST7API.St7SetLoadPathTemplateParameters
St7SetLoadPathTemplateParameters.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetLoadPathTemplateLaneFactor = _ST7API.St7GetLoadPathTemplateLaneFactor
St7GetLoadPathTemplateLaneFactor.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetLoadPathTemplateLaneFactor = _ST7API.St7SetLoadPathTemplateLaneFactor
St7SetLoadPathTemplateLaneFactor.argtypes = [c_long, c_long, c_long, c_double]
St7AddLoadPathTemplateVehicle = _ST7API.St7AddLoadPathTemplateVehicle
St7AddLoadPathTemplateVehicle.argtypes = [c_long, c_long]
St7GetLoadPathTemplateVehicleName = _ST7API.St7GetLoadPathTemplateVehicleName
St7GetLoadPathTemplateVehicleName.argtypes = [c_long, c_long, c_long, c_char_p, c_long]
St7SetLoadPathTemplateVehicleName = _ST7API.St7SetLoadPathTemplateVehicleName
St7SetLoadPathTemplateVehicleName.argtypes = [c_long, c_long, c_long, c_char_p]
St7InsertLoadPathTemplateVehicle = _ST7API.St7InsertLoadPathTemplateVehicle
St7InsertLoadPathTemplateVehicle.argtypes = [c_long, c_long, c_long]
St7CloneLoadPathTemplateVehicle = _ST7API.St7CloneLoadPathTemplateVehicle
St7CloneLoadPathTemplateVehicle.argtypes = [c_long, c_long, c_long]
St7DeleteLoadPathTemplateVehicle = _ST7API.St7DeleteLoadPathTemplateVehicle
St7DeleteLoadPathTemplateVehicle.argtypes = [c_long, c_long, c_long]
St7GetNumLoadPathTemplateVehicles = _ST7API.St7GetNumLoadPathTemplateVehicles
St7GetNumLoadPathTemplateVehicles.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetLoadPathTemplateVehicleData = _ST7API.St7GetLoadPathTemplateVehicleData
St7GetLoadPathTemplateVehicleData.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetLoadPathTemplateVehicleData = _ST7API.St7SetLoadPathTemplateVehicleData
St7SetLoadPathTemplateVehicleData.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7EnableLoadPathTemplateVehicleLane = _ST7API.St7EnableLoadPathTemplateVehicleLane
St7EnableLoadPathTemplateVehicleLane.argtypes = [c_long, c_long, c_long, c_long]
St7DisableLoadPathTemplateVehicleLane = _ST7API.St7DisableLoadPathTemplateVehicleLane
St7DisableLoadPathTemplateVehicleLane.argtypes = [c_long, c_long, c_long, c_long]
St7GetLoadPathTemplateVehicleLaneState = _ST7API.St7GetLoadPathTemplateVehicleLaneState
St7GetLoadPathTemplateVehicleLaneState.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_bool)]
St7AddLoadPathTemplatePointForce = _ST7API.St7AddLoadPathTemplatePointForce
St7AddLoadPathTemplatePointForce.argtypes = [c_long, c_long, c_long]
St7InsertLoadPathTemplatePointForce = _ST7API.St7InsertLoadPathTemplatePointForce
St7InsertLoadPathTemplatePointForce.argtypes = [c_long, c_long, c_long, c_long]
St7DeleteLoadPathTemplatePointForce = _ST7API.St7DeleteLoadPathTemplatePointForce
St7DeleteLoadPathTemplatePointForce.argtypes = [c_long, c_long, c_long, c_long]
St7GetNumLoadPathTemplatePointForces = _ST7API.St7GetNumLoadPathTemplatePointForces
St7GetNumLoadPathTemplatePointForces.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetLoadPathTemplatePointForceData = _ST7API.St7GetLoadPathTemplatePointForceData
St7GetLoadPathTemplatePointForceData.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetLoadPathTemplatePointForceData = _ST7API.St7SetLoadPathTemplatePointForceData
St7SetLoadPathTemplatePointForceData.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7AddLoadPathTemplateDistributedForce = _ST7API.St7AddLoadPathTemplateDistributedForce
St7AddLoadPathTemplateDistributedForce.argtypes = [c_long, c_long, c_long]
St7InsertLoadPathTemplateDistributedForce = _ST7API.St7InsertLoadPathTemplateDistributedForce
St7InsertLoadPathTemplateDistributedForce.argtypes = [c_long, c_long, c_long, c_long]
St7DeleteLoadPathTemplateDistributedForce = _ST7API.St7DeleteLoadPathTemplateDistributedForce
St7DeleteLoadPathTemplateDistributedForce.argtypes = [c_long, c_long, c_long, c_long]
St7GetNumLoadPathTemplateDistributedForces = _ST7API.St7GetNumLoadPathTemplateDistributedForces
St7GetNumLoadPathTemplateDistributedForces.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetLoadPathTemplateDistributedForceData = _ST7API.St7GetLoadPathTemplateDistributedForceData
St7GetLoadPathTemplateDistributedForceData.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetLoadPathTemplateDistributedForceData = _ST7API.St7SetLoadPathTemplateDistributedForceData
St7SetLoadPathTemplateDistributedForceData.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7AddLoadPathTemplateHeatSource = _ST7API.St7AddLoadPathTemplateHeatSource
St7AddLoadPathTemplateHeatSource.argtypes = [c_long, c_long, c_long]
St7InsertLoadPathTemplateHeatSource = _ST7API.St7InsertLoadPathTemplateHeatSource
St7InsertLoadPathTemplateHeatSource.argtypes = [c_long, c_long, c_long, c_long]
St7DeleteLoadPathTemplateHeatSource = _ST7API.St7DeleteLoadPathTemplateHeatSource
St7DeleteLoadPathTemplateHeatSource.argtypes = [c_long, c_long, c_long, c_long]
St7GetNumLoadPathTemplateHeatSources = _ST7API.St7GetNumLoadPathTemplateHeatSources
St7GetNumLoadPathTemplateHeatSources.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetLoadPathTemplateHeatSourceData = _ST7API.St7GetLoadPathTemplateHeatSourceData
St7GetLoadPathTemplateHeatSourceData.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetLoadPathTemplateHeatSourceData = _ST7API.St7SetLoadPathTemplateHeatSourceData
St7SetLoadPathTemplateHeatSourceData.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetLoadPathTemplateVehicleSet = _ST7API.St7GetLoadPathTemplateVehicleSet
St7GetLoadPathTemplateVehicleSet.argtypes = [c_long, c_long, c_long, c_char_p, c_long]
St7SetLoadPathTemplateVehicleSet = _ST7API.St7SetLoadPathTemplateVehicleSet
St7SetLoadPathTemplateVehicleSet.argtypes = [c_long, c_long, c_long, c_char_p]
St7DeleteLoadPathTemplate = _ST7API.St7DeleteLoadPathTemplate
St7DeleteLoadPathTemplate.argtypes = [c_long, c_long]
St7SetLoadPathTemplateCentrifugalData = _ST7API.St7SetLoadPathTemplateCentrifugalData
St7SetLoadPathTemplateCentrifugalData.argtypes = [c_long, c_long, c_char_p, c_char_p, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetLoadPathTemplateCentrifugalData = _ST7API.St7GetLoadPathTemplateCentrifugalData
St7GetLoadPathTemplateCentrifugalData.argtypes = [c_long, c_long, c_char_p, c_char_p, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetNumLibraries = _ST7API.St7GetNumLibraries
St7GetNumLibraries.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetLibraryName = _ST7API.St7GetLibraryName
St7GetLibraryName.argtypes = [c_long, c_long, c_long, c_char_p, c_long]
St7GetLibraryID = _ST7API.St7GetLibraryID
St7GetLibraryID.argtypes = [c_long, c_long, c_char_p, ctypes.POINTER(c_long)]
St7GetNumLibraryItems = _ST7API.St7GetNumLibraryItems
St7GetNumLibraryItems.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetLibraryItemName = _ST7API.St7GetLibraryItemName
St7GetLibraryItemName.argtypes = [c_long, c_long, c_long, c_long, c_char_p, c_long]
St7GetLibraryItemID = _ST7API.St7GetLibraryItemID
St7GetLibraryItemID.argtypes = [c_long, c_long, c_long, c_char_p, ctypes.POINTER(c_long)]
St7AssignLibraryMaterial = _ST7API.St7AssignLibraryMaterial
St7AssignLibraryMaterial.argtypes = [c_long, c_long, c_long, c_long, c_long]
St7AssignLibraryComposite = _ST7API.St7AssignLibraryComposite
St7AssignLibraryComposite.argtypes = [c_long, c_long, c_long, c_long]
St7AssignLibraryBeamSection = _ST7API.St7AssignLibraryBeamSection
St7AssignLibraryBeamSection.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7AssignLibraryCreepDefinition = _ST7API.St7AssignLibraryCreepDefinition
St7AssignLibraryCreepDefinition.argtypes = [c_long, c_long, c_long, c_long]
St7AssignLibraryLoadPathTemplate = _ST7API.St7AssignLibraryLoadPathTemplate
St7AssignLibraryLoadPathTemplate.argtypes = [c_long, c_long, c_long, c_long]
St7AssignLibraryReinforcementLayout = _ST7API.St7AssignLibraryReinforcementLayout
St7AssignLibraryReinforcementLayout.argtypes = [c_long, c_long, c_long, c_long]
St7NewTableType = _ST7API.St7NewTableType
St7NewTableType.argtypes = [c_long, c_long, c_long, c_long, c_char_p, ctypes.POINTER(c_double)]
St7DeleteTableType = _ST7API.St7DeleteTableType
St7DeleteTableType.argtypes = [c_long, c_long, c_long]
St7GetTableTypeName = _ST7API.St7GetTableTypeName
St7GetTableTypeName.argtypes = [c_long, c_long, c_long, c_char_p, c_long]
St7GetTableID = _ST7API.St7GetTableID
St7GetTableID.argtypes = [c_long, c_char_p, c_long, ctypes.POINTER(c_long)]
St7GetNumTableTypeRows = _ST7API.St7GetNumTableTypeRows
St7GetNumTableTypeRows.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetTableTypeData = _ST7API.St7GetTableTypeData
St7GetTableTypeData.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetTableTypeData = _ST7API.St7SetTableTypeData
St7SetTableTypeData.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetFrequencyTable = _ST7API.St7GetFrequencyTable
St7GetFrequencyTable.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetFrequencyTable = _ST7API.St7SetFrequencyTable
St7SetFrequencyTable.argtypes = [c_long, c_long, c_long]
St7GetTimeTableUnits = _ST7API.St7GetTimeTableUnits
St7GetTimeTableUnits.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetTimeTableUnits = _ST7API.St7SetTimeTableUnits
St7SetTimeTableUnits.argtypes = [c_long, c_long, c_long, c_long]
St7ConvertTimeTableUnits = _ST7API.St7ConvertTimeTableUnits
St7ConvertTimeTableUnits.argtypes = [c_long, c_long, c_long, c_long]
St7GetFrequencyPeriodTableUnits = _ST7API.St7GetFrequencyPeriodTableUnits
St7GetFrequencyPeriodTableUnits.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetFrequencyPeriodTableUnits = _ST7API.St7SetFrequencyPeriodTableUnits
St7SetFrequencyPeriodTableUnits.argtypes = [c_long, c_long, c_long]
St7GetNumTables = _ST7API.St7GetNumTables
St7GetNumTables.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7GetTableInfoByIndex = _ST7API.St7GetTableInfoByIndex
St7GetTableInfoByIndex.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), c_char_p, c_long]
St7EnableLSALoadCase = _ST7API.St7EnableLSALoadCase
St7EnableLSALoadCase.argtypes = [c_long, c_long, c_long]
St7DisableLSALoadCase = _ST7API.St7DisableLSALoadCase
St7DisableLSALoadCase.argtypes = [c_long, c_long, c_long]
St7GetLSALoadCaseState = _ST7API.St7GetLSALoadCaseState
St7GetLSALoadCaseState.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_bool)]
St7EnableLSAInitialPCGFile = _ST7API.St7EnableLSAInitialPCGFile
St7EnableLSAInitialPCGFile.argtypes = [c_long]
St7DisableLSAInitialPCGFile = _ST7API.St7DisableLSAInitialPCGFile
St7DisableLSAInitialPCGFile.argtypes = [c_long]
St7GetLSAInitialPCGFileState = _ST7API.St7GetLSAInitialPCGFileState
St7GetLSAInitialPCGFileState.argtypes = [c_long, ctypes.POINTER(c_bool)]
St7SetLSAInitialPCGFile = _ST7API.St7SetLSAInitialPCGFile
St7SetLSAInitialPCGFile.argtypes = [c_long, c_char_p]
St7GetLSAInitialPCGFile = _ST7API.St7GetLSAInitialPCGFile
St7GetLSAInitialPCGFile.argtypes = [c_long, c_char_p, c_long]
St7SetLBAInitialFile = _ST7API.St7SetLBAInitialFile
St7SetLBAInitialFile.argtypes = [c_long, c_char_p, c_long]
St7GetLBAInitialFile = _ST7API.St7GetLBAInitialFile
St7GetLBAInitialFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7SetLBANumModes = _ST7API.St7SetLBANumModes
St7SetLBANumModes.argtypes = [c_long, c_long]
St7GetLBANumModes = _ST7API.St7GetLBANumModes
St7GetLBANumModes.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetLBAShift = _ST7API.St7SetLBAShift
St7SetLBAShift.argtypes = [c_long, c_double]
St7GetLBAShift = _ST7API.St7GetLBAShift
St7GetLBAShift.argtypes = [c_long, ctypes.POINTER(c_double)]
St7EnableLIALoadCase = _ST7API.St7EnableLIALoadCase
St7EnableLIALoadCase.argtypes = [c_long, c_long, c_long]
St7DisableLIALoadCase = _ST7API.St7DisableLIALoadCase
St7DisableLIALoadCase.argtypes = [c_long, c_long, c_long]
St7GetLIALoadCaseState = _ST7API.St7GetLIALoadCaseState
St7GetLIALoadCaseState.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_bool)]
St7SetNLAStagedAnalysis = _ST7API.St7SetNLAStagedAnalysis
St7SetNLAStagedAnalysis.argtypes = [c_long, c_bool]
St7GetNLAStagedAnalysis = _ST7API.St7GetNLAStagedAnalysis
St7GetNLAStagedAnalysis.argtypes = [c_long, ctypes.POINTER(c_bool)]
St7EnableNLAStage = _ST7API.St7EnableNLAStage
St7EnableNLAStage.argtypes = [c_long, c_long]
St7DisableNLAStage = _ST7API.St7DisableNLAStage
St7DisableNLAStage.argtypes = [c_long, c_long]
St7GetNLAStageState = _ST7API.St7GetNLAStageState
St7GetNLAStageState.argtypes = [c_long, c_long, ctypes.POINTER(c_bool)]
St7AddNLAIncrement = _ST7API.St7AddNLAIncrement
St7AddNLAIncrement.argtypes = [c_long, c_long, c_char_p]
St7InsertNLAIncrement = _ST7API.St7InsertNLAIncrement
St7InsertNLAIncrement.argtypes = [c_long, c_long, c_long, c_char_p]
St7DeleteNLAIncrement = _ST7API.St7DeleteNLAIncrement
St7DeleteNLAIncrement.argtypes = [c_long, c_long, c_long]
St7GetNumNLAIncrements = _ST7API.St7GetNumNLAIncrements
St7GetNumNLAIncrements.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetNLALoadIncrementFactor = _ST7API.St7SetNLALoadIncrementFactor
St7SetNLALoadIncrementFactor.argtypes = [c_long, c_long, c_long, c_long, c_double]
St7SetNLAFreedomIncrementFactor = _ST7API.St7SetNLAFreedomIncrementFactor
St7SetNLAFreedomIncrementFactor.argtypes = [c_long, c_long, c_long, c_long, c_double]
St7GetNLALoadIncrementFactor = _ST7API.St7GetNLALoadIncrementFactor
St7GetNLALoadIncrementFactor.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetNLAFreedomIncrementFactor = _ST7API.St7GetNLAFreedomIncrementFactor
St7GetNLAFreedomIncrementFactor.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7EnableNLALoadCase = _ST7API.St7EnableNLALoadCase
St7EnableNLALoadCase.argtypes = [c_long, c_long, c_long]
St7DisableNLALoadCase = _ST7API.St7DisableNLALoadCase
St7DisableNLALoadCase.argtypes = [c_long, c_long, c_long]
St7EnableNLAFreedomCase = _ST7API.St7EnableNLAFreedomCase
St7EnableNLAFreedomCase.argtypes = [c_long, c_long, c_long]
St7DisableNLAFreedomCase = _ST7API.St7DisableNLAFreedomCase
St7DisableNLAFreedomCase.argtypes = [c_long, c_long, c_long]
St7GetNLALoadCaseState = _ST7API.St7GetNLALoadCaseState
St7GetNLALoadCaseState.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_bool)]
St7GetNLAFreedomCaseState = _ST7API.St7GetNLAFreedomCaseState
St7GetNLAFreedomCaseState.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_bool)]
St7SetNLAInitialFile = _ST7API.St7SetNLAInitialFile
St7SetNLAInitialFile.argtypes = [c_long, c_char_p, c_long]
St7GetNLAInitialFile = _ST7API.St7GetNLAInitialFile
St7GetNLAInitialFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7SetQSAInitialFile = _ST7API.St7SetQSAInitialFile
St7SetQSAInitialFile.argtypes = [c_long, c_char_p, c_long]
St7GetQSAInitialFile = _ST7API.St7GetQSAInitialFile
St7GetQSAInitialFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7SetNFAInitialFile = _ST7API.St7SetNFAInitialFile
St7SetNFAInitialFile.argtypes = [c_long, c_char_p, c_long]
St7GetNFAInitialFile = _ST7API.St7GetNFAInitialFile
St7GetNFAInitialFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7EnableNFANonStructuralMassCase = _ST7API.St7EnableNFANonStructuralMassCase
St7EnableNFANonStructuralMassCase.argtypes = [c_long, c_long]
St7DisableNFANonStructuralMassCase = _ST7API.St7DisableNFANonStructuralMassCase
St7DisableNFANonStructuralMassCase.argtypes = [c_long, c_long]
St7GetNFANonStructuralMassCaseState = _ST7API.St7GetNFANonStructuralMassCaseState
St7GetNFANonStructuralMassCaseState.argtypes = [c_long, c_long, ctypes.POINTER(c_bool)]
St7SetNFANumModes = _ST7API.St7SetNFANumModes
St7SetNFANumModes.argtypes = [c_long, c_long]
St7GetNFANumModes = _ST7API.St7GetNFANumModes
St7GetNFANumModes.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetNFAShift = _ST7API.St7SetNFAShift
St7SetNFAShift.argtypes = [c_long, c_double]
St7GetNFAShift = _ST7API.St7GetNFAShift
St7GetNFAShift.argtypes = [c_long, ctypes.POINTER(c_double)]
St7SetNFAModeParticipationCalculate = _ST7API.St7SetNFAModeParticipationCalculate
St7SetNFAModeParticipationCalculate.argtypes = [c_long, c_bool]
St7GetNFAModeParticipationCalculate = _ST7API.St7GetNFAModeParticipationCalculate
St7GetNFAModeParticipationCalculate.argtypes = [c_long, ctypes.POINTER(c_bool)]
St7SetNFAModeParticipationVectors = _ST7API.St7SetNFAModeParticipationVectors
St7SetNFAModeParticipationVectors.argtypes = [c_long, ctypes.POINTER(c_double)]
St7GetNFAModeParticipationVectors = _ST7API.St7GetNFAModeParticipationVectors
St7GetNFAModeParticipationVectors.argtypes = [c_long, ctypes.POINTER(c_double)]
St7SetHRARange = _ST7API.St7SetHRARange
St7SetHRARange.argtypes = [c_long, c_long, c_double, c_double, c_bool]
St7GetHRARange = _ST7API.St7GetHRARange
St7GetHRARange.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double), ctypes.POINTER(c_double), ctypes.POINTER(c_bool)]
St7SetHRAResultType = _ST7API.St7SetHRAResultType
St7SetHRAResultType.argtypes = [c_long, c_long]
St7GetHRAResultType = _ST7API.St7GetHRAResultType
St7GetHRAResultType.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetHRABaseVector = _ST7API.St7SetHRABaseVector
St7SetHRABaseVector.argtypes = [c_long, ctypes.POINTER(c_double)]
St7GetHRABaseVector = _ST7API.St7GetHRABaseVector
St7GetHRABaseVector.argtypes = [c_long, ctypes.POINTER(c_double)]
St7SetHRALoadCase = _ST7API.St7SetHRALoadCase
St7SetHRALoadCase.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetHRALoadCase = _ST7API.St7GetHRALoadCase
St7GetHRALoadCase.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7AddSRALoadCase = _ST7API.St7AddSRALoadCase
St7AddSRALoadCase.argtypes = [c_long, c_char_p]
St7InsertSRALoadCase = _ST7API.St7InsertSRALoadCase
St7InsertSRALoadCase.argtypes = [c_long, c_long, c_char_p]
St7DeleteSRALoadCase = _ST7API.St7DeleteSRALoadCase
St7DeleteSRALoadCase.argtypes = [c_long, c_long]
St7GetNumSRALoadCases = _ST7API.St7GetNumSRALoadCases
St7GetNumSRALoadCases.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetSRALoadCaseTable = _ST7API.St7SetSRALoadCaseTable
St7SetSRALoadCaseTable.argtypes = [c_long, c_long, c_long, c_long]
St7GetSRALoadCaseTable = _ST7API.St7GetSRALoadCaseTable
St7GetSRALoadCaseTable.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7AddSRADirectionVector = _ST7API.St7AddSRADirectionVector
St7AddSRADirectionVector.argtypes = [c_long, c_char_p]
St7InsertSRADirectionVector = _ST7API.St7InsertSRADirectionVector
St7InsertSRADirectionVector.argtypes = [c_long, c_long, c_char_p]
St7DeleteSRADirectionVector = _ST7API.St7DeleteSRADirectionVector
St7DeleteSRADirectionVector.argtypes = [c_long, c_long]
St7GetNumSRADirectionVectors = _ST7API.St7GetNumSRADirectionVectors
St7GetNumSRADirectionVectors.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetSRADirectionVectorTable = _ST7API.St7SetSRADirectionVectorTable
St7SetSRADirectionVectorTable.argtypes = [c_long, c_long, c_long]
St7GetSRADirectionVectorTable = _ST7API.St7GetSRADirectionVectorTable
St7GetSRADirectionVectorTable.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetSRADirectionVectorFactors = _ST7API.St7SetSRADirectionVectorFactors
St7SetSRADirectionVectorFactors.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetSRADirectionVectorFactors = _ST7API.St7GetSRADirectionVectorFactors
St7GetSRADirectionVectorFactors.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetSRAResultModal = _ST7API.St7SetSRAResultModal
St7SetSRAResultModal.argtypes = [c_long, c_bool]
St7SetSRAResultSRSS = _ST7API.St7SetSRAResultSRSS
St7SetSRAResultSRSS.argtypes = [c_long, c_bool]
St7SetSRAResultCQC = _ST7API.St7SetSRAResultCQC
St7SetSRAResultCQC.argtypes = [c_long, c_bool]
St7SetSRAType = _ST7API.St7SetSRAType
St7SetSRAType.argtypes = [c_long, c_long]
St7SetSRAResultsSign = _ST7API.St7SetSRAResultsSign
St7SetSRAResultsSign.argtypes = [c_long, c_long]
St7SetLTAInitialFile = _ST7API.St7SetLTAInitialFile
St7SetLTAInitialFile.argtypes = [c_long, c_char_p, c_long]
St7GetLTAInitialFile = _ST7API.St7GetLTAInitialFile
St7GetLTAInitialFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7SetLTAMethod = _ST7API.St7SetLTAMethod
St7SetLTAMethod.argtypes = [c_long, c_long]
St7GetLTAMethod = _ST7API.St7GetLTAMethod
St7GetLTAMethod.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetLTASolutionType = _ST7API.St7SetLTASolutionType
St7SetLTASolutionType.argtypes = [c_long, c_long]
St7GetLTASolutionType = _ST7API.St7GetLTASolutionType
St7GetLTASolutionType.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetNTAInitialFile = _ST7API.St7SetNTAInitialFile
St7SetNTAInitialFile.argtypes = [c_long, c_char_p, c_long]
St7GetNTAInitialFile = _ST7API.St7GetNTAInitialFile
St7GetNTAInitialFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7SetNTALoadPositionTable = _ST7API.St7SetNTALoadPositionTable
St7SetNTALoadPositionTable.argtypes = [c_long, c_long, c_long, c_long, c_long]
St7GetNTALoadPositionTable = _ST7API.St7GetNTALoadPositionTable
St7GetNTALoadPositionTable.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7SetNTAFreedomPositionTable = _ST7API.St7SetNTAFreedomPositionTable
St7SetNTAFreedomPositionTable.argtypes = [c_long, c_long, c_long, c_long, c_long]
St7GetNTAFreedomPositionTable = _ST7API.St7GetNTAFreedomPositionTable
St7GetNTAFreedomPositionTable.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7EnableHeatLoadCase = _ST7API.St7EnableHeatLoadCase
St7EnableHeatLoadCase.argtypes = [c_long, c_long]
St7DisableHeatLoadCase = _ST7API.St7DisableHeatLoadCase
St7DisableHeatLoadCase.argtypes = [c_long, c_long]
St7GetHeatLoadCaseState = _ST7API.St7GetHeatLoadCaseState
St7GetHeatLoadCaseState.argtypes = [c_long, c_long, ctypes.POINTER(c_bool)]
St7SetTHAInitialFile = _ST7API.St7SetTHAInitialFile
St7SetTHAInitialFile.argtypes = [c_long, c_char_p, c_long]
St7GetTHAInitialFile = _ST7API.St7GetTHAInitialFile
St7GetTHAInitialFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7SetTHATemperatureLoadCase = _ST7API.St7SetTHATemperatureLoadCase
St7SetTHATemperatureLoadCase.argtypes = [c_long, c_long]
St7GetTHATemperatureLoadCase = _ST7API.St7GetTHATemperatureLoadCase
St7GetTHATemperatureLoadCase.argtypes = [c_long, ctypes.POINTER(c_long)]
St7GetModalLoadType = _ST7API.St7GetModalLoadType
St7GetModalLoadType.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetModalLoadType = _ST7API.St7SetModalLoadType
St7SetModalLoadType.argtypes = [c_long, c_long]
St7GetModalNodeReactionType = _ST7API.St7GetModalNodeReactionType
St7GetModalNodeReactionType.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetModalNodeReactionType = _ST7API.St7SetModalNodeReactionType
St7SetModalNodeReactionType.argtypes = [c_long, c_long]
St7SetModalSuperpositionFile = _ST7API.St7SetModalSuperpositionFile
St7SetModalSuperpositionFile.argtypes = [c_long, c_char_p]
St7GetModalSuperpositionFile = _ST7API.St7GetModalSuperpositionFile
St7GetModalSuperpositionFile.argtypes = [c_long, c_char_p, c_long]
St7GetNumModesInModalFile = _ST7API.St7GetNumModesInModalFile
St7GetNumModesInModalFile.argtypes = [c_long, ctypes.POINTER(c_long)]
St7EnableMode = _ST7API.St7EnableMode
St7EnableMode.argtypes = [c_long, c_long]
St7DisableMode = _ST7API.St7DisableMode
St7DisableMode.argtypes = [c_long, c_long]
St7SetModeDampingRatio = _ST7API.St7SetModeDampingRatio
St7SetModeDampingRatio.argtypes = [c_long, c_long, c_double]
St7GetModeDampingRatio = _ST7API.St7GetModeDampingRatio
St7GetModeDampingRatio.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetTransientInitialConditionsType = _ST7API.St7SetTransientInitialConditionsType
St7SetTransientInitialConditionsType.argtypes = [c_long, c_long]
St7GetTransientInitialConditionsType = _ST7API.St7GetTransientInitialConditionsType
St7GetTransientInitialConditionsType.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetTransientInitialConditionsVectors = _ST7API.St7SetTransientInitialConditionsVectors
St7SetTransientInitialConditionsVectors.argtypes = [c_long, ctypes.POINTER(c_double)]
St7GetTransientInitialConditionsVectors = _ST7API.St7GetTransientInitialConditionsVectors
St7GetTransientInitialConditionsVectors.argtypes = [c_long, ctypes.POINTER(c_double)]
St7SetTransientInitialConditionsNodalVelocity = _ST7API.St7SetTransientInitialConditionsNodalVelocity
St7SetTransientInitialConditionsNodalVelocity.argtypes = [c_long, c_long]
St7GetTransientInitialConditionsNodalVelocity = _ST7API.St7GetTransientInitialConditionsNodalVelocity
St7GetTransientInitialConditionsNodalVelocity.argtypes = [c_long, ctypes.POINTER(c_long)]
St7GetTransientBaseVector = _ST7API.St7GetTransientBaseVector
St7GetTransientBaseVector.argtypes = [c_long, ctypes.POINTER(c_double)]
St7SetTransientBaseVector = _ST7API.St7SetTransientBaseVector
St7SetTransientBaseVector.argtypes = [c_long, ctypes.POINTER(c_double)]
St7GetTransientBaseVelocity = _ST7API.St7GetTransientBaseVelocity
St7GetTransientBaseVelocity.argtypes = [c_long, ctypes.POINTER(c_double)]
St7SetTransientBaseVelocity = _ST7API.St7SetTransientBaseVelocity
St7SetTransientBaseVelocity.argtypes = [c_long, ctypes.POINTER(c_double)]
St7GetTransientBaseTables = _ST7API.St7GetTransientBaseTables
St7GetTransientBaseTables.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetTransientBaseTables = _ST7API.St7SetTransientBaseTables
St7SetTransientBaseTables.argtypes = [c_long, ctypes.POINTER(c_long)]
St7GetTransientBaseResults = _ST7API.St7GetTransientBaseResults
St7GetTransientBaseResults.argtypes = [c_long, ctypes.POINTER(c_bool)]
St7SetTransientBaseResults = _ST7API.St7SetTransientBaseResults
St7SetTransientBaseResults.argtypes = [c_long, ctypes.POINTER(c_bool)]
St7AddTransientNodeHistoryCase = _ST7API.St7AddTransientNodeHistoryCase
St7AddTransientNodeHistoryCase.argtypes = [c_long, c_long]
St7InsertTransientNodeHistoryCase = _ST7API.St7InsertTransientNodeHistoryCase
St7InsertTransientNodeHistoryCase.argtypes = [c_long, c_long, c_long]
St7DeleteTransientNodeHistoryCase = _ST7API.St7DeleteTransientNodeHistoryCase
St7DeleteTransientNodeHistoryCase.argtypes = [c_long, c_long]
St7GetNumTransientNodeHistoryCases = _ST7API.St7GetNumTransientNodeHistoryCases
St7GetNumTransientNodeHistoryCases.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetTransientNodeHistoryCaseData = _ST7API.St7SetTransientNodeHistoryCaseData
St7SetTransientNodeHistoryCaseData.argtypes = [c_long, c_long, ctypes.POINTER(c_bool)]
St7GetTransientNodeHistoryCaseData = _ST7API.St7GetTransientNodeHistoryCaseData
St7GetTransientNodeHistoryCaseData.argtypes = [c_long, c_long, ctypes.POINTER(c_bool)]
St7SetTransientTemperatureInputType = _ST7API.St7SetTransientTemperatureInputType
St7SetTransientTemperatureInputType.argtypes = [c_long, c_long]
St7SetTransientHeatFile = _ST7API.St7SetTransientHeatFile
St7SetTransientHeatFile.argtypes = [c_long, c_char_p, c_double]
St7GetTransientHeatFile = _ST7API.St7GetTransientHeatFile
St7GetTransientHeatFile.argtypes = [c_long, c_char_p, c_long, ctypes.POINTER(c_double)]
St7EnableTransientLoadCase = _ST7API.St7EnableTransientLoadCase
St7EnableTransientLoadCase.argtypes = [c_long, c_long]
St7EnableTransientFreedomCase = _ST7API.St7EnableTransientFreedomCase
St7EnableTransientFreedomCase.argtypes = [c_long, c_long]
St7DisableTransientLoadCase = _ST7API.St7DisableTransientLoadCase
St7DisableTransientLoadCase.argtypes = [c_long, c_long]
St7DisableTransientFreedomCase = _ST7API.St7DisableTransientFreedomCase
St7DisableTransientFreedomCase.argtypes = [c_long, c_long]
St7GetTransientLoadCaseState = _ST7API.St7GetTransientLoadCaseState
St7GetTransientLoadCaseState.argtypes = [c_long, c_long, ctypes.POINTER(c_bool)]
St7GetTransientFreedomCaseState = _ST7API.St7GetTransientFreedomCaseState
St7GetTransientFreedomCaseState.argtypes = [c_long, c_long, ctypes.POINTER(c_bool)]
St7SetTransientLoadTable = _ST7API.St7SetTransientLoadTable
St7SetTransientLoadTable.argtypes = [c_long, c_long, c_long]
St7GetTransientLoadTable = _ST7API.St7GetTransientLoadTable
St7GetTransientLoadTable.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetTransientFreedomTable = _ST7API.St7SetTransientFreedomTable
St7SetTransientFreedomTable.argtypes = [c_long, c_long, c_long]
St7GetTransientFreedomTable = _ST7API.St7GetTransientFreedomTable
St7GetTransientFreedomTable.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetNumTimeStepRows = _ST7API.St7GetNumTimeStepRows
St7GetNumTimeStepRows.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetNumTimeStepRows = _ST7API.St7SetNumTimeStepRows
St7SetNumTimeStepRows.argtypes = [c_long, c_long]
St7GetTimeStepData = _ST7API.St7GetTimeStepData
St7GetTimeStepData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetTimeStepData = _ST7API.St7SetTimeStepData
St7SetTimeStepData.argtypes = [c_long, c_long, c_long, c_long, c_double]
St7SetTimeStepUnit = _ST7API.St7SetTimeStepUnit
St7SetTimeStepUnit.argtypes = [c_long, c_long]
St7GetTimeStepUnit = _ST7API.St7GetTimeStepUnit
St7GetTimeStepUnit.argtypes = [c_long, ctypes.POINTER(c_long)]
St7EnableMovingLoad = _ST7API.St7EnableMovingLoad
St7EnableMovingLoad.argtypes = [c_long, c_long]
St7DisableMovingLoad = _ST7API.St7DisableMovingLoad
St7DisableMovingLoad.argtypes = [c_long, c_long]
St7GetMovingLoadState = _ST7API.St7GetMovingLoadState
St7GetMovingLoadState.argtypes = [c_long, c_long, ctypes.POINTER(c_bool)]
St7SetSolverHeatNonlinear = _ST7API.St7SetSolverHeatNonlinear
St7SetSolverHeatNonlinear.argtypes = [c_long, c_bool]
St7SetSolverScheme = _ST7API.St7SetSolverScheme
St7SetSolverScheme.argtypes = [c_long, c_long]
St7GetSolverScheme = _ST7API.St7GetSolverScheme
St7GetSolverScheme.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetSolverSort = _ST7API.St7SetSolverSort
St7SetSolverSort.argtypes = [c_long, c_long]
St7GetSolverSort = _ST7API.St7GetSolverSort
St7GetSolverSort.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetSolverTreeStartNumber = _ST7API.St7SetSolverTreeStartNumber
St7SetSolverTreeStartNumber.argtypes = [c_long, c_long]
St7GetSolverTreeStartNumber = _ST7API.St7GetSolverTreeStartNumber
St7GetSolverTreeStartNumber.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetSolverActiveStage = _ST7API.St7SetSolverActiveStage
St7SetSolverActiveStage.argtypes = [c_long, c_long]
St7GetSolverActiveStage = _ST7API.St7GetSolverActiveStage
St7GetSolverActiveStage.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetSolverTemperatureDependence = _ST7API.St7SetSolverTemperatureDependence
St7SetSolverTemperatureDependence.argtypes = [c_long, c_long]
St7GetSolverTemperatureDependence = _ST7API.St7GetSolverTemperatureDependence
St7GetSolverTemperatureDependence.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetSolverLoadCaseTemperatureDependence = _ST7API.St7SetSolverLoadCaseTemperatureDependence
St7SetSolverLoadCaseTemperatureDependence.argtypes = [c_long, c_long]
St7GetSolverLoadCaseTemperatureDependence = _ST7API.St7GetSolverLoadCaseTemperatureDependence
St7GetSolverLoadCaseTemperatureDependence.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetSolverFreedomCase = _ST7API.St7SetSolverFreedomCase
St7SetSolverFreedomCase.argtypes = [c_long, c_long]
St7GetSolverFreedomCase = _ST7API.St7GetSolverFreedomCase
St7GetSolverFreedomCase.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetDampingType = _ST7API.St7SetDampingType
St7SetDampingType.argtypes = [c_long, c_long]
St7GetDampingType = _ST7API.St7GetDampingType
St7GetDampingType.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetRayleighFactors = _ST7API.St7SetRayleighFactors
St7SetRayleighFactors.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetRayleighFactors = _ST7API.St7GetRayleighFactors
St7GetRayleighFactors.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetSoilFluidOptions = _ST7API.St7SetSoilFluidOptions
St7SetSoilFluidOptions.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetSoilFluidOptions = _ST7API.St7GetSoilFluidOptions
St7GetSoilFluidOptions.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetSturmCheck = _ST7API.St7SetSturmCheck
St7SetSturmCheck.argtypes = [c_long, c_bool]
St7GetSturmCheck = _ST7API.St7GetSturmCheck
St7GetSturmCheck.argtypes = [c_long, ctypes.POINTER(c_bool)]
St7SetSolverNonlinearGeometry = _ST7API.St7SetSolverNonlinearGeometry
St7SetSolverNonlinearGeometry.argtypes = [c_long, c_bool]
St7GetSolverNonlinearGeometry = _ST7API.St7GetSolverNonlinearGeometry
St7GetSolverNonlinearGeometry.argtypes = [c_long, ctypes.POINTER(c_bool)]
St7SetSolverNonlinearMaterial = _ST7API.St7SetSolverNonlinearMaterial
St7SetSolverNonlinearMaterial.argtypes = [c_long, c_bool]
St7GetSolverNonlinearMaterial = _ST7API.St7GetSolverNonlinearMaterial
St7GetSolverNonlinearMaterial.argtypes = [c_long, ctypes.POINTER(c_bool)]
St7SetSolverCreep = _ST7API.St7SetSolverCreep
St7SetSolverCreep.argtypes = [c_long, c_bool]
St7GetSolverCreep = _ST7API.St7GetSolverCreep
St7GetSolverCreep.argtypes = [c_long, ctypes.POINTER(c_bool)]
St7SetSolverIncludeKG = _ST7API.St7SetSolverIncludeKG
St7SetSolverIncludeKG.argtypes = [c_long, c_bool]
St7GetSolverIncludeKG = _ST7API.St7GetSolverIncludeKG
St7GetSolverIncludeKG.argtypes = [c_long, ctypes.POINTER(c_bool)]
St7SetSolverStressStiffening = _ST7API.St7SetSolverStressStiffening
St7SetSolverStressStiffening.argtypes = [c_long, c_bool]
St7GetSolverStressStiffening = _ST7API.St7GetSolverStressStiffening
St7GetSolverStressStiffening.argtypes = [c_long, ctypes.POINTER(c_bool)]
St7SetEntityResult = _ST7API.St7SetEntityResult
St7SetEntityResult.argtypes = [c_long, c_long, c_long]
St7GetEntityResult = _ST7API.St7GetEntityResult
St7GetEntityResult.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetResultSurfaceBricksOnly = _ST7API.St7SetResultSurfaceBricksOnly
St7SetResultSurfaceBricksOnly.argtypes = [c_long, c_long]
St7GetResultSurfaceBricksOnly = _ST7API.St7GetResultSurfaceBricksOnly
St7GetResultSurfaceBricksOnly.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetResultLimit = _ST7API.St7SetResultLimit
St7SetResultLimit.argtypes = [c_long, c_long, c_long, c_double]
St7GetResultLimit = _ST7API.St7GetResultLimit
St7GetResultLimit.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7EnableResultGroup = _ST7API.St7EnableResultGroup
St7EnableResultGroup.argtypes = [c_long, c_long]
St7DisableResultGroup = _ST7API.St7DisableResultGroup
St7DisableResultGroup.argtypes = [c_long, c_long]
St7GetResultGroupState = _ST7API.St7GetResultGroupState
St7GetResultGroupState.argtypes = [c_long, c_long, ctypes.POINTER(c_bool)]
St7EnableResultProperty = _ST7API.St7EnableResultProperty
St7EnableResultProperty.argtypes = [c_long, c_long, c_long]
St7DisableResultProperty = _ST7API.St7DisableResultProperty
St7DisableResultProperty.argtypes = [c_long, c_long, c_long]
St7GetResultPropertyState = _ST7API.St7GetResultPropertyState
St7GetResultPropertyState.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_bool)]
St7SetResultFileName = _ST7API.St7SetResultFileName
St7SetResultFileName.argtypes = [c_long, c_char_p]
St7SetResultLogFileName = _ST7API.St7SetResultLogFileName
St7SetResultLogFileName.argtypes = [c_long, c_char_p]
St7SetStaticRestartFile = _ST7API.St7SetStaticRestartFile
St7SetStaticRestartFile.argtypes = [c_long, c_char_p]
St7GetStaticRestartFile = _ST7API.St7GetStaticRestartFile
St7GetStaticRestartFile.argtypes = [c_long, c_char_p, c_long]
St7SetDynamicRestartFile = _ST7API.St7SetDynamicRestartFile
St7SetDynamicRestartFile.argtypes = [c_long, c_char_p]
St7GetDynamicRestartFile = _ST7API.St7GetDynamicRestartFile
St7GetDynamicRestartFile.argtypes = [c_long, c_char_p, c_long]
St7SetQuasiStaticRestartFile = _ST7API.St7SetQuasiStaticRestartFile
St7SetQuasiStaticRestartFile.argtypes = [c_long, c_char_p]
St7GetQuasiStaticRestartFile = _ST7API.St7GetQuasiStaticRestartFile
St7GetQuasiStaticRestartFile.argtypes = [c_long, c_char_p, c_long]
St7SetNodeHistoryFile = _ST7API.St7SetNodeHistoryFile
St7SetNodeHistoryFile.argtypes = [c_long, c_char_p]
St7GetNodeHistoryFile = _ST7API.St7GetNodeHistoryFile
St7GetNodeHistoryFile.argtypes = [c_long, c_char_p, c_long]
St7EnableSaveRestart = _ST7API.St7EnableSaveRestart
St7EnableSaveRestart.argtypes = [c_long]
St7DisableSaveRestart = _ST7API.St7DisableSaveRestart
St7DisableSaveRestart.argtypes = [c_long]
St7EnableSaveLastRestartStep = _ST7API.St7EnableSaveLastRestartStep
St7EnableSaveLastRestartStep.argtypes = [c_long]
St7DisableSaveLastRestartStep = _ST7API.St7DisableSaveLastRestartStep
St7DisableSaveLastRestartStep.argtypes = [c_long]
St7EnableAutoAssignPathDivisions = _ST7API.St7EnableAutoAssignPathDivisions
St7EnableAutoAssignPathDivisions.argtypes = [c_long]
St7DisableAutoAssignPathDivisions = _ST7API.St7DisableAutoAssignPathDivisions
St7DisableAutoAssignPathDivisions.argtypes = [c_long]
St7SetSolverDefaultsLogical = _ST7API.St7SetSolverDefaultsLogical
St7SetSolverDefaultsLogical.argtypes = [c_long, c_long, c_bool]
St7GetSolverDefaultsLogical = _ST7API.St7GetSolverDefaultsLogical
St7GetSolverDefaultsLogical.argtypes = [c_long, c_long, ctypes.POINTER(c_bool)]
St7SetSolverDefaultsInteger = _ST7API.St7SetSolverDefaultsInteger
St7SetSolverDefaultsInteger.argtypes = [c_long, c_long, c_long]
St7GetSolverDefaultsInteger = _ST7API.St7GetSolverDefaultsInteger
St7GetSolverDefaultsInteger.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetSolverDefaultsDouble = _ST7API.St7SetSolverDefaultsDouble
St7SetSolverDefaultsDouble.argtypes = [c_long, c_long, c_double]
St7GetSolverDefaultsDouble = _ST7API.St7GetSolverDefaultsDouble
St7GetSolverDefaultsDouble.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7RunSolver = _ST7API.St7RunSolver
St7RunSolver.argtypes = [c_long, c_long, c_long, c_long]
St7RunSolverProcess = _ST7API.St7RunSolverProcess
St7RunSolverProcess.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7CheckSolverRunning = _ST7API.St7CheckSolverRunning
St7CheckSolverRunning.argtypes = [c_long, ctypes.POINTER(c_bool)]
St7GetResultCaseName = _ST7API.St7GetResultCaseName
St7GetResultCaseName.argtypes = [c_long, c_long, c_char_p, c_long]
St7GetResultFreedomCaseName = _ST7API.St7GetResultFreedomCaseName
St7GetResultFreedomCaseName.argtypes = [c_long, c_char_p, c_long]
St7GetResultCaseConvergence = _ST7API.St7GetResultCaseConvergence
St7GetResultCaseConvergence.argtypes = [c_long, c_long, ctypes.POINTER(c_bool)]
St7GetResultCaseTime = _ST7API.St7GetResultCaseTime
St7GetResultCaseTime.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetResultCaseFactor = _ST7API.St7GetResultCaseFactor
St7GetResultCaseFactor.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetFrequency = _ST7API.St7GetFrequency
St7GetFrequency.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetModalResultsNFA = _ST7API.St7GetModalResultsNFA
St7GetModalResultsNFA.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetInertiaReliefResults = _ST7API.St7GetInertiaReliefResults
St7GetInertiaReliefResults.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetBuckFactor = _ST7API.St7GetBuckFactor
St7GetBuckFactor.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetNodeResult = _ST7API.St7GetNodeResult
St7GetNodeResult.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetNodeResultUCS = _ST7API.St7GetNodeResultUCS
St7GetNodeResultUCS.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetBeamResultArray = _ST7API.St7GetBeamResultArray
St7GetBeamResultArray.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double), ctypes.POINTER(c_double)]
St7GetBeamResultArrayPos = _ST7API.St7GetBeamResultArrayPos
St7GetBeamResultArrayPos.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBeamResultEndPos = _ST7API.St7GetBeamResultEndPos
St7GetBeamResultEndPos.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBeamResultSinglePos = _ST7API.St7GetBeamResultSinglePos
St7GetBeamResultSinglePos.argtypes = [c_long, c_long, c_long, c_long, c_long, c_double, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBeamReleaseResult = _ST7API.St7GetBeamReleaseResult
St7GetBeamReleaseResult.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_bool), ctypes.POINTER(c_double)]
St7GetPlateResultArray = _ST7API.St7GetPlateResultArray
St7GetPlateResultArray.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetPlateResultMaxJunctionAngle = _ST7API.St7SetPlateResultMaxJunctionAngle
St7SetPlateResultMaxJunctionAngle.argtypes = [c_long, c_double]
St7GetPlateResultMaxJunctionAngle = _ST7API.St7GetPlateResultMaxJunctionAngle
St7GetPlateResultMaxJunctionAngle.argtypes = [c_long, ctypes.POINTER(c_double)]
St7SetPlateResultUserEquation = _ST7API.St7SetPlateResultUserEquation
St7SetPlateResultUserEquation.argtypes = [c_long, c_char_p, c_long]
St7GetPlateResultUserEquation = _ST7API.St7GetPlateResultUserEquation
St7GetPlateResultUserEquation.argtypes = [c_long, c_char_p, c_long, ctypes.POINTER(c_long)]
St7GetPlateResultGaussPoints = _ST7API.St7GetPlateResultGaussPoints
St7GetPlateResultGaussPoints.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBrickResultArray = _ST7API.St7GetBrickResultArray
St7GetBrickResultArray.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetBrickResultUserEquation = _ST7API.St7SetBrickResultUserEquation
St7SetBrickResultUserEquation.argtypes = [c_long, c_char_p, c_long]
St7GetBrickResultUserEquation = _ST7API.St7GetBrickResultUserEquation
St7GetBrickResultUserEquation.argtypes = [c_long, c_char_p, c_long, ctypes.POINTER(c_long)]
St7GetBrickResultGaussPoints = _ST7API.St7GetBrickResultGaussPoints
St7GetBrickResultGaussPoints.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetNumLSACombinations = _ST7API.St7GetNumLSACombinations
St7GetNumLSACombinations.argtypes = [c_long, ctypes.POINTER(c_long)]
St7GetLSACombinationName = _ST7API.St7GetLSACombinationName
St7GetLSACombinationName.argtypes = [c_long, c_long, c_char_p, c_long]
St7SetLSACombinationName = _ST7API.St7SetLSACombinationName
St7SetLSACombinationName.argtypes = [c_long, c_long, c_char_p]
St7GetLSACombinationSpectralName = _ST7API.St7GetLSACombinationSpectralName
St7GetLSACombinationSpectralName.argtypes = [c_long, c_char_p, c_long]
St7SetLSACombinationSpectralName = _ST7API.St7SetLSACombinationSpectralName
St7SetLSACombinationSpectralName.argtypes = [c_long, c_char_p]
St7AddLSACombination = _ST7API.St7AddLSACombination
St7AddLSACombination.argtypes = [c_long, c_char_p]
St7InsertLSACombination = _ST7API.St7InsertLSACombination
St7InsertLSACombination.argtypes = [c_long, c_long, c_char_p]
St7DeleteLSACombination = _ST7API.St7DeleteLSACombination
St7DeleteLSACombination.argtypes = [c_long, c_long]
St7SetLSACombinationFactor = _ST7API.St7SetLSACombinationFactor
St7SetLSACombinationFactor.argtypes = [c_long, c_long, c_long, c_long, c_long, c_double]
St7GetLSACombinationFactor = _ST7API.St7GetLSACombinationFactor
St7GetLSACombinationFactor.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetNumEnvelopes = _ST7API.St7GetNumEnvelopes
St7GetNumEnvelopes.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7AddLimitEnvelope = _ST7API.St7AddLimitEnvelope
St7AddLimitEnvelope.argtypes = [c_long, c_long, c_char_p]
St7InsertLimitEnvelope = _ST7API.St7InsertLimitEnvelope
St7InsertLimitEnvelope.argtypes = [c_long, c_long, c_long, c_char_p]
St7DeleteLimitEnvelope = _ST7API.St7DeleteLimitEnvelope
St7DeleteLimitEnvelope.argtypes = [c_long, c_long]
St7EnableLimitEnvelopeCase = _ST7API.St7EnableLimitEnvelopeCase
St7EnableLimitEnvelopeCase.argtypes = [c_long, c_long, c_long]
St7DisableLimitEnvelopeCase = _ST7API.St7DisableLimitEnvelopeCase
St7DisableLimitEnvelopeCase.argtypes = [c_long, c_long, c_long]
St7GetLimitEnvelopeCaseState = _ST7API.St7GetLimitEnvelopeCaseState
St7GetLimitEnvelopeCaseState.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_bool)]
St7GetLimitEnvelopeData = _ST7API.St7GetLimitEnvelopeData
St7GetLimitEnvelopeData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), c_char_p, c_long]
St7SetLimitEnvelopeData = _ST7API.St7SetLimitEnvelopeData
St7SetLimitEnvelopeData.argtypes = [c_long, c_long, c_long, c_char_p]
St7AddCombinationEnvelope = _ST7API.St7AddCombinationEnvelope
St7AddCombinationEnvelope.argtypes = [c_long, c_long, c_char_p]
St7InsertCombinationEnvelope = _ST7API.St7InsertCombinationEnvelope
St7InsertCombinationEnvelope.argtypes = [c_long, c_long, c_long, c_char_p]
St7DeleteCombinationEnvelope = _ST7API.St7DeleteCombinationEnvelope
St7DeleteCombinationEnvelope.argtypes = [c_long, c_long]
St7GetCombinationEnvelopeCase = _ST7API.St7GetCombinationEnvelopeCase
St7GetCombinationEnvelopeCase.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetCombinationEnvelopeCase = _ST7API.St7SetCombinationEnvelopeCase
St7SetCombinationEnvelopeCase.argtypes = [c_long, c_long, c_long, c_long]
St7GetCombinationEnvelopeData = _ST7API.St7GetCombinationEnvelopeData
St7GetCombinationEnvelopeData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), c_char_p, c_long]
St7SetCombinationEnvelopeData = _ST7API.St7SetCombinationEnvelopeData
St7SetCombinationEnvelopeData.argtypes = [c_long, c_long, c_long, c_char_p]
St7AddFactorsEnvelope = _ST7API.St7AddFactorsEnvelope
St7AddFactorsEnvelope.argtypes = [c_long, c_long, c_char_p]
St7InsertFactorsEnvelope = _ST7API.St7InsertFactorsEnvelope
St7InsertFactorsEnvelope.argtypes = [c_long, c_long, c_long, c_char_p]
St7DeleteFactorsEnvelope = _ST7API.St7DeleteFactorsEnvelope
St7DeleteFactorsEnvelope.argtypes = [c_long, c_long]
St7GetFactorsEnvelopeData = _ST7API.St7GetFactorsEnvelopeData
St7GetFactorsEnvelopeData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), c_char_p, c_long]
St7SetFactorsEnvelopeData = _ST7API.St7SetFactorsEnvelopeData
St7SetFactorsEnvelopeData.argtypes = [c_long, c_long, c_long, c_char_p]
St7AddFactorsEnvelopeCase = _ST7API.St7AddFactorsEnvelopeCase
St7AddFactorsEnvelopeCase.argtypes = [c_long, c_long]
St7InsertFactorsEnvelopeCase = _ST7API.St7InsertFactorsEnvelopeCase
St7InsertFactorsEnvelopeCase.argtypes = [c_long, c_long, c_long]
St7DeleteFactorsEnvelopeCase = _ST7API.St7DeleteFactorsEnvelopeCase
St7DeleteFactorsEnvelopeCase.argtypes = [c_long, c_long, c_long]
St7GetFactorsEnvelopeCaseData = _ST7API.St7GetFactorsEnvelopeCaseData
St7GetFactorsEnvelopeCaseData.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetFactorsEnvelopeCaseData = _ST7API.St7SetFactorsEnvelopeCaseData
St7SetFactorsEnvelopeCaseData.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7AddFactorsEnvelopeSet = _ST7API.St7AddFactorsEnvelopeSet
St7AddFactorsEnvelopeSet.argtypes = [c_long]
St7InsertFactorsEnvelopeSet = _ST7API.St7InsertFactorsEnvelopeSet
St7InsertFactorsEnvelopeSet.argtypes = [c_long, c_long]
St7DeleteFactorsEnvelopeSet = _ST7API.St7DeleteFactorsEnvelopeSet
St7DeleteFactorsEnvelopeSet.argtypes = [c_long, c_long]
St7GetNumFactorsEnvelopeSets = _ST7API.St7GetNumFactorsEnvelopeSets
St7GetNumFactorsEnvelopeSets.argtypes = [c_long, ctypes.POINTER(c_long)]
St7GetFactorsEnvelopeSetData = _ST7API.St7GetFactorsEnvelopeSetData
St7GetFactorsEnvelopeSetData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), c_char_p, c_char_p, c_long]
St7SetFactorsEnvelopeSetData = _ST7API.St7SetFactorsEnvelopeSetData
St7SetFactorsEnvelopeSetData.argtypes = [c_long, c_long, c_long, c_char_p, c_char_p]
St7GetResultFileCombTargetFileName = _ST7API.St7GetResultFileCombTargetFileName
St7GetResultFileCombTargetFileName.argtypes = [c_long, c_char_p, c_long]
St7SetResultFileCombTargetFileName = _ST7API.St7SetResultFileCombTargetFileName
St7SetResultFileCombTargetFileName.argtypes = [c_long, c_char_p]
St7AddResultFileCombFileName = _ST7API.St7AddResultFileCombFileName
St7AddResultFileCombFileName.argtypes = [c_long, c_char_p]
St7DeleteResultFileCombFileName = _ST7API.St7DeleteResultFileCombFileName
St7DeleteResultFileCombFileName.argtypes = [c_long, c_long]
St7GetResultFileCombFileName = _ST7API.St7GetResultFileCombFileName
St7GetResultFileCombFileName.argtypes = [c_long, c_long, c_char_p, c_long]
St7SetResultFileCombFileName = _ST7API.St7SetResultFileCombFileName
St7SetResultFileCombFileName.argtypes = [c_long, c_long, c_char_p]
St7AddResultFileCombCase = _ST7API.St7AddResultFileCombCase
St7AddResultFileCombCase.argtypes = [c_long, c_char_p]
St7DeleteResultFileCombCase = _ST7API.St7DeleteResultFileCombCase
St7DeleteResultFileCombCase.argtypes = [c_long]
St7GetResultFileCombCaseData = _ST7API.St7GetResultFileCombCaseData
St7GetResultFileCombCaseData.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetResultFileCombCaseData = _ST7API.St7SetResultFileCombCaseData
St7SetResultFileCombCaseData.argtypes = [c_long, c_long, c_long, c_long, c_double]
St7GetResultFileCombCaseName = _ST7API.St7GetResultFileCombCaseName
St7GetResultFileCombCaseName.argtypes = [c_long, c_long, c_char_p, c_long]
St7SetResultFileCombCaseName = _ST7API.St7SetResultFileCombCaseName
St7SetResultFileCombCaseName.argtypes = [c_long, c_long, c_char_p]
St7GenerateResultFileComb = _ST7API.St7GenerateResultFileComb
St7GenerateResultFileComb.argtypes = [c_long, c_long]
St7UpdateResultFileComb = _ST7API.St7UpdateResultFileComb
St7UpdateResultFileComb.argtypes = [c_long, c_char_p]
St7GenerateHRATimeHistory = _ST7API.St7GenerateHRATimeHistory
St7GenerateHRATimeHistory.argtypes = [c_long, c_double, c_double, c_long]
St7NewResFile = _ST7API.St7NewResFile
St7NewResFile.argtypes = [c_long, c_char_p, c_long]
St7OpenResFile = _ST7API.St7OpenResFile
St7OpenResFile.argtypes = [c_long, c_char_p]
St7CloseResFile = _ST7API.St7CloseResFile
St7CloseResFile.argtypes = [c_long]
St7SetResFileDescription = _ST7API.St7SetResFileDescription
St7SetResFileDescription.argtypes = [c_long, c_char_p]
St7GetResFileDescription = _ST7API.St7GetResFileDescription
St7GetResFileDescription.argtypes = [c_long, c_char_p, c_long]
St7SetResFileNumCases = _ST7API.St7SetResFileNumCases
St7SetResFileNumCases.argtypes = [c_long, c_long]
St7SetResFileCaseName = _ST7API.St7SetResFileCaseName
St7SetResFileCaseName.argtypes = [c_long, c_long, c_char_p]
St7AssociateResFileCase = _ST7API.St7AssociateResFileCase
St7AssociateResFileCase.argtypes = [c_long, c_long, c_long, c_long]
St7AssociateResFileStage = _ST7API.St7AssociateResFileStage
St7AssociateResFileStage.argtypes = [c_long, c_long, c_long]
St7SetResFileMode = _ST7API.St7SetResFileMode
St7SetResFileMode.argtypes = [c_long, c_long, c_double]
St7GetResFileMode = _ST7API.St7GetResFileMode
St7GetResFileMode.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetResFileTime = _ST7API.St7SetResFileTime
St7SetResFileTime.argtypes = [c_long, c_long, c_double]
St7GetResFileTime = _ST7API.St7GetResFileTime
St7GetResFileTime.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetResFileTimeUnit = _ST7API.St7SetResFileTimeUnit
St7SetResFileTimeUnit.argtypes = [c_long, c_long]
St7GetResFileTimeUnit = _ST7API.St7GetResFileTimeUnit
St7GetResFileTimeUnit.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetResFileQuantity = _ST7API.St7SetResFileQuantity
St7SetResFileQuantity.argtypes = [c_long, c_long, c_long, c_long]
St7ClearResFileQuantity = _ST7API.St7ClearResFileQuantity
St7ClearResFileQuantity.argtypes = [c_long, c_long, c_long, c_long]
St7GetResFileQuantity = _ST7API.St7GetResFileQuantity
St7GetResFileQuantity.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_bool)]
St7SetResFileNodeResult = _ST7API.St7SetResFileNodeResult
St7SetResFileNodeResult.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetResFileNodeResult = _ST7API.St7GetResFileNodeResult
St7GetResFileNodeResult.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetResFileBeamResult = _ST7API.St7SetResFileBeamResult
St7SetResFileBeamResult.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetResFileBeamResult = _ST7API.St7GetResFileBeamResult
St7GetResFileBeamResult.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetResFileBeamStations = _ST7API.St7SetResFileBeamStations
St7SetResFileBeamStations.argtypes = [c_long, c_long, c_long]
St7GetResFileBeamStations = _ST7API.St7GetResFileBeamStations
St7GetResFileBeamStations.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetResFilePlateResult = _ST7API.St7SetResFilePlateResult
St7SetResFilePlateResult.argtypes = [c_long, c_long, c_long, c_long, c_bool, ctypes.POINTER(c_double)]
St7GetResFilePlateResult = _ST7API.St7GetResFilePlateResult
St7GetResFilePlateResult.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_bool), ctypes.POINTER(c_double)]
St7SetResFileBrickResult = _ST7API.St7SetResFileBrickResult
St7SetResFileBrickResult.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetResFileBrickResult = _ST7API.St7GetResFileBrickResult
St7GetResFileBrickResult.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7ToolAlignBeamAxes = _ST7API.St7ToolAlignBeamAxes
St7ToolAlignBeamAxes.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long]
St7ToolAlignPlateAxes = _ST7API.St7ToolAlignPlateAxes
St7ToolAlignPlateAxes.argtypes = [c_long, c_long, c_long, c_long, c_long]
St7ToolConvertPatchLoads = _ST7API.St7ToolConvertPatchLoads
St7ToolConvertPatchLoads.argtypes = [c_long, c_long, c_bool]
St7ToolAttachParts = _ST7API.St7ToolAttachParts
St7ToolAttachParts.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7ToolPolygonToFace = _ST7API.St7ToolPolygonToFace
St7ToolPolygonToFace.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7ZipMesh = _ST7API.St7ZipMesh
St7ZipMesh.argtypes = [c_long, c_double, c_long]
St7SetBeamSectionProperties = _ST7API.St7SetBeamSectionProperties
St7SetBeamSectionProperties.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7CalcBeamSectionProperties = _ST7API.St7CalcBeamSectionProperties
St7CalcBeamSectionProperties.argtypes = [c_long, c_long, c_long]
St7AddNonlinearIncrement = _ST7API.St7AddNonlinearIncrement
St7AddNonlinearIncrement.argtypes = [c_long, c_char_p]
St7InsertNonlinearIncrement = _ST7API.St7InsertNonlinearIncrement
St7InsertNonlinearIncrement.argtypes = [c_long, c_long, c_char_p]
St7DeleteNonlinearIncrement = _ST7API.St7DeleteNonlinearIncrement
St7DeleteNonlinearIncrement.argtypes = [c_long, c_long]
St7SetNonlinearLoadIncrementFactor = _ST7API.St7SetNonlinearLoadIncrementFactor
St7SetNonlinearLoadIncrementFactor.argtypes = [c_long, c_long, c_long, c_double]
St7SetNonlinearFreedomIncrementFactor = _ST7API.St7SetNonlinearFreedomIncrementFactor
St7SetNonlinearFreedomIncrementFactor.argtypes = [c_long, c_long, c_long, c_double]
St7GetNonlinearLoadIncrementFactor = _ST7API.St7GetNonlinearLoadIncrementFactor
St7GetNonlinearLoadIncrementFactor.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetNonlinearFreedomIncrementFactor = _ST7API.St7GetNonlinearFreedomIncrementFactor
St7GetNonlinearFreedomIncrementFactor.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7AddLoadCaseCombination = _ST7API.St7AddLoadCaseCombination
St7AddLoadCaseCombination.argtypes = [c_long, c_char_p]
St7InsertLoadCaseCombination = _ST7API.St7InsertLoadCaseCombination
St7InsertLoadCaseCombination.argtypes = [c_long, c_long, c_char_p]
St7DeleteLoadCaseCombination = _ST7API.St7DeleteLoadCaseCombination
St7DeleteLoadCaseCombination.argtypes = [c_long, c_long]
St7SetLoadCaseCombinationFactor = _ST7API.St7SetLoadCaseCombinationFactor
St7SetLoadCaseCombinationFactor.argtypes = [c_long, c_long, c_long, c_double]
St7GetLoadCaseCombinationFactor = _ST7API.St7GetLoadCaseCombinationFactor
St7GetLoadCaseCombinationFactor.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7EnableNonlinearLoadCase = _ST7API.St7EnableNonlinearLoadCase
St7EnableNonlinearLoadCase.argtypes = [c_long, c_long]
St7DisableNonlinearLoadCase = _ST7API.St7DisableNonlinearLoadCase
St7DisableNonlinearLoadCase.argtypes = [c_long, c_long]
St7EnableNonlinearFreedomCase = _ST7API.St7EnableNonlinearFreedomCase
St7EnableNonlinearFreedomCase.argtypes = [c_long, c_long]
St7DisableNonlinearFreedomCase = _ST7API.St7DisableNonlinearFreedomCase
St7DisableNonlinearFreedomCase.argtypes = [c_long, c_long]
St7GetNonlinearLoadCaseState = _ST7API.St7GetNonlinearLoadCaseState
St7GetNonlinearLoadCaseState.argtypes = [c_long, c_long, ctypes.POINTER(c_bool)]
St7GetNonlinearFreedomCaseState = _ST7API.St7GetNonlinearFreedomCaseState
St7GetNonlinearFreedomCaseState.argtypes = [c_long, c_long, ctypes.POINTER(c_bool)]
St7EnableFrequencyNSMassCase = _ST7API.St7EnableFrequencyNSMassCase
St7EnableFrequencyNSMassCase.argtypes = [c_long, c_long]
St7DisableFrequencyNSMassCase = _ST7API.St7DisableFrequencyNSMassCase
St7DisableFrequencyNSMassCase.argtypes = [c_long, c_long]
St7GetFrequencyNSMassCaseState = _ST7API.St7GetFrequencyNSMassCaseState
St7GetFrequencyNSMassCaseState.argtypes = [c_long, c_long, ctypes.POINTER(c_bool)]
St7GetBeamResult = _ST7API.St7GetBeamResult
St7GetBeamResult.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double), ctypes.POINTER(c_double)]
St7GetBeamForceResultPos = _ST7API.St7GetBeamForceResultPos
St7GetBeamForceResultPos.argtypes = [c_long, c_long, c_long, c_double, ctypes.POINTER(c_double)]
St7GetBeamResultPos = _ST7API.St7GetBeamResultPos
St7GetBeamResultPos.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBeamDispResultPos = _ST7API.St7GetBeamDispResultPos
St7GetBeamDispResultPos.argtypes = [c_long, c_long, c_long, c_double, ctypes.POINTER(c_double), ctypes.POINTER(c_double)]
St7GetPlateResult = _ST7API.St7GetPlateResult
St7GetPlateResult.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetPlateResultUCS = _ST7API.St7GetPlateResultUCS
St7GetPlateResultUCS.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBrickResult = _ST7API.St7GetBrickResult
St7GetBrickResult.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBrickResultUCS = _ST7API.St7GetBrickResultUCS
St7GetBrickResultUCS.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetUserSpectralName = _ST7API.St7GetUserSpectralName
St7GetUserSpectralName.argtypes = [c_long, c_char_p, c_long]
St7SetNodeKTranslation3 = _ST7API.St7SetNodeKTranslation3
St7SetNodeKTranslation3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetNodeKRotation3 = _ST7API.St7SetNodeKRotation3
St7SetNodeKRotation3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetNodeKDamping3 = _ST7API.St7SetNodeKDamping3
St7SetNodeKDamping3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetNodeNSMass2 = _ST7API.St7SetNodeNSMass2
St7SetNodeNSMass2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamSupport2 = _ST7API.St7SetBeamSupport2
St7SetBeamSupport2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamDLL4 = _ST7API.St7SetBeamDLL4
St7SetBeamDLL4.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamDML4 = _ST7API.St7SetBeamDML4
St7SetBeamDML4.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamDLG4 = _ST7API.St7SetBeamDLG4
St7SetBeamDLG4.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamCFL4 = _ST7API.St7SetBeamCFL4
St7SetBeamCFL4.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamCFG4 = _ST7API.St7SetBeamCFG4
St7SetBeamCFG4.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamCML4 = _ST7API.St7SetBeamCML4
St7SetBeamCML4.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamCMG4 = _ST7API.St7SetBeamCMG4
St7SetBeamCMG4.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamNSMass7ID = _ST7API.St7SetBeamNSMass7ID
St7SetBeamNSMass7ID.argtypes = [c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPipePressure2 = _ST7API.St7SetPipePressure2
St7SetPipePressure2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPipeTemperature2 = _ST7API.St7SetPipeTemperature2
St7SetPipeTemperature2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBeamPreTension1 = _ST7API.St7SetBeamPreTension1
St7SetBeamPreTension1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlatePreStress3 = _ST7API.St7SetPlatePreStress3
St7SetPlatePreStress3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateFaceSupport1 = _ST7API.St7SetPlateFaceSupport1
St7SetPlateFaceSupport1.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateEdgeSupport1 = _ST7API.St7SetPlateEdgeSupport1
St7SetPlateEdgeSupport1.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateNSMass2 = _ST7API.St7SetPlateNSMass2
St7SetPlateNSMass2.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateConvection2 = _ST7API.St7SetPlateConvection2
St7SetPlateConvection2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetPlateRadiation2 = _ST7API.St7SetPlateRadiation2
St7SetPlateRadiation2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBrickSupport1 = _ST7API.St7SetBrickSupport1
St7SetBrickSupport1.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBrickPreStress3 = _ST7API.St7SetBrickPreStress3
St7SetBrickPreStress3.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetBrickNSMass2 = _ST7API.St7SetBrickNSMass2
St7SetBrickNSMass2.argtypes = [c_long, c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7EnableLoadCase = _ST7API.St7EnableLoadCase
St7EnableLoadCase.argtypes = [c_long, c_long]
St7DisableLoadCase = _ST7API.St7DisableLoadCase
St7DisableLoadCase.argtypes = [c_long, c_long]
St7GetLoadCaseStatus = _ST7API.St7GetLoadCaseStatus
St7GetLoadCaseStatus.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetLinearBucklingInitialFile = _ST7API.St7SetLinearBucklingInitialFile
St7SetLinearBucklingInitialFile.argtypes = [c_long, c_char_p, c_long]
St7GetLinearBucklingInitialFile = _ST7API.St7GetLinearBucklingInitialFile
St7GetLinearBucklingInitialFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7SetNaturalFrequencyInitialFile = _ST7API.St7SetNaturalFrequencyInitialFile
St7SetNaturalFrequencyInitialFile.argtypes = [c_long, c_char_p, c_long]
St7GetNaturalFrequencyInitialFile = _ST7API.St7GetNaturalFrequencyInitialFile
St7GetNaturalFrequencyInitialFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7SetNonlinearStaticInitialFile = _ST7API.St7SetNonlinearStaticInitialFile
St7SetNonlinearStaticInitialFile.argtypes = [c_long, c_char_p, c_long]
St7GetNonlinearStaticInitialFile = _ST7API.St7GetNonlinearStaticInitialFile
St7GetNonlinearStaticInitialFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7SetNonlinearTransientInitialFile = _ST7API.St7SetNonlinearTransientInitialFile
St7SetNonlinearTransientInitialFile.argtypes = [c_long, c_char_p, c_long]
St7GetNonlinearTransientInitialFile = _ST7API.St7GetNonlinearTransientInitialFile
St7GetNonlinearTransientInitialFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7SetLinearTransientInitialFile = _ST7API.St7SetLinearTransientInitialFile
St7SetLinearTransientInitialFile.argtypes = [c_long, c_char_p, c_long]
St7GetLinearTransientInitialFile = _ST7API.St7GetLinearTransientInitialFile
St7GetLinearTransientInitialFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7SetTransientHeatInitialFile = _ST7API.St7SetTransientHeatInitialFile
St7SetTransientHeatInitialFile.argtypes = [c_long, c_char_p, c_long]
St7GetTransientHeatInitialFile = _ST7API.St7GetTransientHeatInitialFile
St7GetTransientHeatInitialFile.argtypes = [c_long, c_char_p, ctypes.POINTER(c_long), c_long]
St7SetModalDampingType = _ST7API.St7SetModalDampingType
St7SetModalDampingType.argtypes = [c_long, c_long]
St7GetModalDampingType = _ST7API.St7GetModalDampingType
St7GetModalDampingType.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetHarmonicRange = _ST7API.St7SetHarmonicRange
St7SetHarmonicRange.argtypes = [c_long, c_long, c_double, c_double]
St7GetHarmonicRange = _ST7API.St7GetHarmonicRange
St7GetHarmonicRange.argtypes = [c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double), ctypes.POINTER(c_double)]
St7SetHeatLoadCase = _ST7API.St7SetHeatLoadCase
St7SetHeatLoadCase.argtypes = [c_long, c_long]
St7GetHarmonicBaseVector = _ST7API.St7GetHarmonicBaseVector
St7GetHarmonicBaseVector.argtypes = [c_long, ctypes.POINTER(c_double)]
St7SetHarmonicBaseVector = _ST7API.St7SetHarmonicBaseVector
St7SetHarmonicBaseVector.argtypes = [c_long, ctypes.POINTER(c_double)]
St7SetHarmonicLoadType = _ST7API.St7SetHarmonicLoadType
St7SetHarmonicLoadType.argtypes = [c_long, c_long]
St7GetHarmonicLoadType = _ST7API.St7GetHarmonicLoadType
St7GetHarmonicLoadType.argtypes = [c_long, ctypes.POINTER(c_long)]
St7SetLSAFreedomCase = _ST7API.St7SetLSAFreedomCase
St7SetLSAFreedomCase.argtypes = [c_long, c_long]
St7SetSolverLogicalParameter = _ST7API.St7SetSolverLogicalParameter
St7SetSolverLogicalParameter.argtypes = [c_long, c_long, c_bool]
St7GetSolverLogicalParameter = _ST7API.St7GetSolverLogicalParameter
St7GetSolverLogicalParameter.argtypes = [c_long, c_long, ctypes.POINTER(c_bool)]
St7SetSolverIntegerParameter = _ST7API.St7SetSolverIntegerParameter
St7SetSolverIntegerParameter.argtypes = [c_long, c_long, c_long]
St7GetSolverIntegerParameter = _ST7API.St7GetSolverIntegerParameter
St7GetSolverIntegerParameter.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7SetSolverDoubleParameter = _ST7API.St7SetSolverDoubleParameter
St7SetSolverDoubleParameter.argtypes = [c_long, c_long, c_double]
St7GetSolverDoubleParameter = _ST7API.St7GetSolverDoubleParameter
St7GetSolverDoubleParameter.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7GetAttribute = _ST7API.St7GetAttribute
St7GetAttribute.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double), ctypes.POINTER(c_bool), ctypes.POINTER(c_long)]
St7GetAttributeID = _ST7API.St7GetAttributeID
St7GetAttributeID.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, c_long, ctypes.POINTER(c_double), ctypes.POINTER(c_bool), ctypes.POINTER(c_long)]
St7GetElementGroup = _ST7API.St7GetElementGroup
St7GetElementGroup.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7SetElementGroup = _ST7API.St7SetElementGroup
St7SetElementGroup.argtypes = [c_long, c_long, c_long, c_long]
St7DeleteAttributeID = _ST7API.St7DeleteAttributeID
St7DeleteAttributeID.argtypes = [c_long, c_long, c_long, c_long, c_long, c_long, c_long]
St7NewTable = _ST7API.St7NewTable
St7NewTable.argtypes = [c_long, c_char_p, c_long, c_long, ctypes.POINTER(c_double), ctypes.POINTER(c_long)]
St7DeleteTable = _ST7API.St7DeleteTable
St7DeleteTable.argtypes = [c_long, c_long]
St7GetTableType = _ST7API.St7GetTableType
St7GetTableType.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetTableName = _ST7API.St7GetTableName
St7GetTableName.argtypes = [c_long, c_long, c_char_p, c_long]
St7GetNumTableRows = _ST7API.St7GetNumTableRows
St7GetNumTableRows.argtypes = [c_long, c_long, ctypes.POINTER(c_long)]
St7GetTableData = _ST7API.St7GetTableData
St7GetTableData.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7SetTableData = _ST7API.St7SetTableData
St7SetTableData.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7SetLinkData = _ST7API.St7SetLinkData
St7SetLinkData.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_long)]
St7GetLinkData = _ST7API.St7GetLinkData
St7GetLinkData.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long)]
St7SetLinkDoubles = _ST7API.St7SetLinkDoubles
St7SetLinkDoubles.argtypes = [c_long, c_long, c_long, ctypes.POINTER(c_double)]
St7GetLinkDoubles = _ST7API.St7GetLinkDoubles
St7GetLinkDoubles.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_double)]
St7GetBeamProperty = _ST7API.St7GetBeamProperty
St7GetBeamProperty.argtypes = [c_long, c_long, ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_long), ctypes.POINTER(c_double), ctypes.POINTER(c_double)]
St7GetPlateProperty = _ST7API.St7GetPlateProperty
St7GetPlateProperty.argtypes = [c_long, c_long, ctypes.POINTER(c_double), ctypes.POINTER(c_double)]
St7GetBrickProperty = _ST7API.St7GetBrickProperty
St7GetBrickProperty.argtypes = [c_long, c_long, ctypes.POINTER(c_double)]
St7SetTransientInitialConditions = _ST7API.St7SetTransientInitialConditions
St7SetTransientInitialConditions.argtypes = [c_long, ctypes.POINTER(c_double)]
St7GetTransientInitialConditions = _ST7API.St7GetTransientInitialConditions
St7GetTransientInitialConditions.argtypes = [c_long, ctypes.POINTER(c_double)]
