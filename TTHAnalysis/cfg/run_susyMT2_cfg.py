import PhysicsTools.HeppyCore.framework.config as cfg


#Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

# Comment this line if you want the diagnostic folders produced along with the output root file
cfg.Analyzer.nosubdir = True


##------------------------------------------
## Redefine what I need
##------------------------------------------

### jet pt treshold for mt2 calculation
mt2JPt = 30.0

#JSON
jsonAna.useLumiBlocks = True

#Vertex
vertexAna.keepFailingEvents = True # keep events with no good vertices

#Lepton
lepAna.loose_muon_dxy = 0.2
lepAna.loose_muon_dz  = 0.5
lepAna.loose_muon_relIso  = 0.15
lepAna.loose_muon_isoCut = lambda muon :muon.miniRelIso < 0.2

lepAna.loose_electron_pt  = 5
lepAna.loose_electron_eta    = 2.4
lepAna.loose_electron_relIso = 0.15
lepAna.loose_electron_isoCut = lambda electron : electron.miniRelIso < 0.1

lepAna.loose_electron_id  = "POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto_full5x5"
lepAna.loose_electron_lostHits = 999. # no cut
lepAna.loose_electron_dxy    = 999.
lepAna.loose_electron_dz     = 999.

lepAna.inclusive_electron_id  = "POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto_full5x5"
lepAna.inclusive_electron_lostHits = 999. # no cut since embedded in ID
lepAna.inclusive_electron_dxy    = 999. # no cut since embedded in ID
lepAna.inclusive_electron_dz     = 999. # no cut since embedded in ID

lepAna.mu_isoCorr = "deltaBeta"
lepAna.ele_isoCorr = "deltaBeta"
# lepAna.ele_tightId = "Cuts_PHYS14_25ns_v1_ConvVetoDxyDz"
lepAna.ele_tightId = "Cuts_SPRING15_25ns_v1_ConvVetoDxyDz"
lepAna.notCleaningElectrons = True
lepAna.doMiniIsolation = True
lepAna.miniIsolationPUCorr = 'rhoArea'
#lepAna.ele_effectiveAreas = 'Phys14_25ns_v1'              #what we used with SnT       
#lepAna.mu_effectiveAreas = 'Phys14_25ns_v1'               #what we used with SnT
lepAna.ele_effectiveAreas = 'Spring15_25ns_v1'             #new default 
lepAna.mu_effectiveAreas = 'Spring15_25ns_v1'              #new default
#lepAna.rhoMuon= 'fixedGridRhoFastjetAll',                  #what we used with SnT       
#lepAna.rhoElectron = 'fixedGridRhoFastjetAll',             #what we used with SnT   
lepAna.rhoMuon= 'fixedGridRhoFastjetCentralNeutral',      #new default
lepAna.rhoElectron = 'fixedGridRhoFastjetCentralNeutral', #new default


lepAna.doIsoAnnulus = True

# JET (for event variables do apply the jetID and not PUID yet)
jetAna.relaxJetId = False
jetAna.doPuId = False
jetAna.doQG = True
jetAna.jetEta = 4.7
jetAna.jetEtaCentral = 2.5
jetAna.jetPt = 20. #was 10
jetAna.mcGT     = "Spring16_25nsV1_MC" # jec corrections
jetAna.dataGT   = "Spring16_25nsV1_MC" # jec corrections
jetAna.recalibrateJets = True # True or False
jetAna.applyL2L3Residual = True # 'Data'
jetAna.calculateSeparateCorrections = True
jetAna.calculateType1METCorrection = True
jetAna.jetLepDR = 0.4
jetAna.smearJets = False
jetAna.jetGammaDR = 0.4
jetAna.cleanFromLepAndGammaSimultaneously = True
jetAna.jetGammaLepDR = 0.4
jetAna.minGammaPt = 20.
jetAna.gammaEtaCentral = 2.4
jetAna.cleanJetsFromFirstPhoton = True
jetAna.cleanJetsFromIsoTracks = False ## added for Dominick
jetAna.doJetCleaning = False

### For Jet Cleaning AFTER MET analyzer
from PhysicsTools.Heppy.analyzers.objects.JetCleaner import JetCleaner
jetCleanAna = cfg.Analyzer(
    JetCleaner, name = 'JetCleaner',

    jetPt = 20.,
    jetEta = 4.7,
    jetEtaCentral = 2.5,

    relaxJetId = False,
    doPuId = False,

    minLepPt = 10,
    jetLepDR = 0.4,
    cleanSelectedLeptons = True,
    jetLepArbitration = (lambda jet,lepton : lepton),

    jetGammaDR = 0.4,
    minGammaPt = 20.,
    gammaEtaCentral = 2.4,

    cleanFromLepAndGammaSimultaneously = True,
    jetGammaLepDR = 0.4,

    alwaysCleanPhotons = False,
    cleanGenJetsFromPhoton = False,
    cleanJetsFromFirstPhoton = True,

    cleanJetsFromIsoTracks = True,
    cleanJetsFromTaus = False,

    do_mc_match = True,
    collectionPostFix = "",

    )


# TAU 
tauAna.inclusive_ptMin = 20.0
tauAna.inclusive_etaMax = 2.3
tauAna.inclusive_dxyMax = 99999.
tauAna.inclusive_dzMax = 99999.
tauAna.inclusive_vetoLeptons = False
tauAna.inclusive_vetoLeptonsPOG = False
#tauAna.inclusive_decayModeID = "byLooseCombinedIsolationDeltaBetaCorr3Hits" # ignored if not set or ""

tauAna.loose_ptMin = 20.0
tauAna.loose_etaMax = 2.3
tauAna.loose_dxyMax = 99999.
tauAna.loose_dzMax = 99999.
tauAna.loose_vetoLeptons = False
tauAna.loose_vetoLeptonsPOG = False
#tauAna.loose_decayModeID = "byLooseCombinedIsolationDeltaBetaCorr3Hits" # ignored if not set or ""

# Photon
photonAna.etaCentral = 2.5
photonAna.ptMin = 20
photonAna.gammaID = "POG_SPRING15_50ns_Loose_looseSieie_NoIso"
photonAna.do_randomCone = True
photonAna.do_mc_match = True

# Isolated Track
isoTrackAna.setOff=False
isoTrackAna.doIsoAnnulus = True

# recalibrate MET
metAna.recalibrate = 'type1' # 'type1' or False
metAna.old74XMiniAODs = False # get right Raw MET on old 74X MiniAODs

# store all taus by default
genAna.allGenTaus = True

# Core Analyzer
ttHCoreEventAna.mhtForBiasedDPhi = "mhtJetXjvec"
ttHCoreEventAna.jetPt = mt2JPt ### jet pt 30: this will change ht and mht

# switch off the SV and MC matching
#ttHSVAna.do_mc_match = False

##------------------------------------------ 
##  CONTROL VARIABLES
##------------------------------------------ 

from CMGTools.TTHAnalysis.analyzers.ttHMT2Control import ttHMT2Control

ttHMT2Control = cfg.Analyzer(
            ttHMT2Control, name = 'ttHMT2Control',
            jetPt = mt2JPt, ### this will change control variables (gamma_ and zll_)
            )

##------------------------------------------
##  TOPOLOGICAL VARIABLES: minMT, MT2
##------------------------------------------

from CMGTools.TTHAnalysis.analyzers.ttHTopoVarAnalyzer import ttHTopoVarAnalyzer

ttHTopoJetAna = cfg.Analyzer(
            ttHTopoVarAnalyzer, name = 'ttHTopoVarAnalyzer',
            doOnlyDefault = True,
            jetPt = mt2JPt, ### this will change diffMetMht and deltaPhiMin
            )

from PhysicsTools.Heppy.analyzers.eventtopology.MT2Analyzer import MT2Analyzer

MT2Ana = cfg.Analyzer(
    MT2Analyzer, name = 'MT2Analyzer',
    metCollection     = "slimmedMETs",
    doOnlyDefault = True,
    #    jetPt = 40.,
    jetPt = mt2JPt, ### jet pt 30: this will change MT2 and pseudo-jets
    collectionPostFix = "",
    )

MT2AnaNoHF = cfg.Analyzer(
    MT2Analyzer, name = 'MT2Analyzer',
    metCollection     = "slimmedMETsNoHF",
    doOnlyDefault = True,
    jetPt = mt2JPt, ### this will change MT2 and pseudo-jets
    collectionPostFix = "NoHF",
    )

##------------------------------------------
##  Z skim
##------------------------------------------

from CMGTools.TTHAnalysis.analyzers.ttHmllSkimmer import ttHmllSkimmer
# Tree Producer                                                                                                                                                                         
ttHZskim = cfg.Analyzer(
            ttHmllSkimmer, name='ttHmllSkimmer',
            lepId=[13],
            maxLeps=3,
            massMin=60,
            massMax=120,
            doZGen = False,
            doZReco = True
            )

from CMGTools.TTHAnalysis.analyzers.hbheAnalyzer import hbheAnalyzer
hbheFilterAna = cfg.Analyzer(
    hbheAnalyzer, name = 'hbheAnalyzer',
    IgnoreTS4TS5ifJetInLowBVRegion=False,
)


##------------------------------------------
##  PRODUCER
##------------------------------------------


from CMGTools.RootTools.samples.triggers_13TeV_Spring16 import triggers_HT900, triggers_HT800, triggers_AllMET170, triggers_HT350_MET100, triggers_HT350_MET120
from CMGTools.RootTools.samples.triggers_13TeV_Spring16 import triggers_MT2_mumu, triggers_MT2_ee, triggers_MT2_e, triggers_MT2_mu, triggers_MT2_emu, triggers_MT2_mue 
from CMGTools.RootTools.samples.triggers_13TeV_Spring16 import triggers_dijet, triggers_dijet70met120, triggers_dijet55met110, triggers_HT350, triggers_HT475,  triggers_HT600, triggers_HT125
from CMGTools.RootTools.samples.triggers_13TeV_Spring16 import triggers_photon75, triggers_photon90, triggers_photon120, triggers_photon75ps 
from CMGTools.RootTools.samples.triggers_13TeV_Spring16 import triggers_photon90ps, triggers_photon120ps, triggers_photon155, triggers_photon165_HE10, triggers_photon175
from CMGTools.RootTools.samples.triggers_13TeV_Spring16 import triggers_met90_mht90, triggers_metNoMu90_mhtNoMu90, triggers_metNoMu120_mhtNoMu120, triggers_Jet80MET90, triggers_met100_mht100, triggers_met110_mht110, triggers_met120_mht120
from CMGTools.RootTools.samples.triggers_13TeV_Spring16 import triggers_doubleele33, triggers_mumu_noniso

triggerFlagsAna.triggerBits = {
'PFHT900' : triggers_HT900,
'PFHT800' : triggers_HT800,
'PFMET170' : triggers_AllMET170,
'PFHT350_PFMET100' : triggers_HT350_MET100,
'PFHT350_PFMET120' : triggers_HT350_MET120,
'SingleMu' : triggers_MT2_mu,
'SingleEl' : triggers_MT2_e,
'DoubleMu' : triggers_MT2_mumu,
'DoubleEl' : triggers_MT2_ee,
'MuX_Ele12' : triggers_MT2_emu,
'Mu8_EleX'  : triggers_MT2_mue,
#'MuEG' : triggers_MT2_mue,
'DiCentralPFJet70_PFMET120' : triggers_dijet70met120,
'DiCentralPFJet55_PFMET110' : triggers_dijet55met110,
##
'PFHT125_Prescale' : triggers_HT125,
'PFHT350_Prescale' : triggers_HT350,
'PFHT475_Prescale' : triggers_HT475,
'PFHT600_Prescale'  : triggers_HT600,
'DiJet' : triggers_dijet,
'Photon75_R9Id90_HE10_IsoM' : triggers_photon75,
'Photon90_R9Id90_HE10_IsoM' : triggers_photon90,
'Photon120_R9Id90_HE10_IsoM' : triggers_photon120,
'Photon75' : triggers_photon75ps,
'Photon90' : triggers_photon90ps,
'Photon120' : triggers_photon120ps,
'Photon155' : triggers_photon155,
'Photon165_HE10' : triggers_photon165_HE10,
'Photon175' : triggers_photon175,
## monojet triggers
'PFMET90_PFMHT90' : triggers_met90_mht90,
'PFMET100_PFMHT100' : triggers_met100_mht100,
'PFMET110_PFMHT110' : triggers_met110_mht110,
'PFMET120_PFMHT120' : triggers_met120_mht120,
'PFMETNoMu90_PFMHTNoMu90' : triggers_metNoMu90_mhtNoMu90,
'PFMETNoMu120_PFMHTNoMu120' : triggers_metNoMu120_mhtNoMu120,
'MonoCentralPFJet80_PFMETNoMu90_PFMHTNoMu90' : triggers_Jet80MET90,
### ZGamma triggers
'DoubleEle33' : triggers_doubleele33,
'Mu30_TkMu11' : triggers_mumu_noniso,
}

### Temporary replacement for hbheFilter
eventFlagsAna.triggerBits = {
    "HBHENoiseFilter" : [ "Flag_HBHENoiseFilter" ], ### hbheFilter temporary replaced
    "HBHENoiseIsoFilter" : [ "Flag_HBHENoiseIsoFilter" ], ### hbheFilter temporary replaced
    "CSCTightHalo2015Filter" : [ "Flag_CSCTightHalo2015Filter" ],
    "EcalDeadCellTriggerPrimitiveFilter" : [ "Flag_EcalDeadCellTriggerPrimitiveFilter" ],
    "goodVertices" : [ "Flag_goodVertices" ],
    "eeBadScFilter" : [ "Flag_eeBadScFilter" ],
    "globalTightHalo2016Filter" : [ "Flag_globalTightHalo2016Filter" ],
    "hcalLaserEventFilter" : [ "Flag_hcalLaserEventFilter" ],
    "trackingFailureFilter" : [ "Flag_trackingFailureFilter" ],
    "ecalLaserCorrFilter" : [ "Flag_ecalLaserCorrFilter" ],
    "trkPOGFilters" : [ "Flag_trkPOGFilters" ],
    "trkPOG_manystripclus53X" : [ "Flag_trkPOG_manystripclus53X" ],
    "trkPOG_toomanystripclus53X" : [ "Flag_trkPOG_toomanystripclus53X" ],
    "trkPOG_logErrorTooManyClusters" : [ "Flag_trkPOG_logErrorTooManyClusters" ],
    "chargedHadronTrackResolutionFilter" : [ "Flag_chargedHadronTrackResolutionFilter" ],
    "muonBadTrackFilter" : [ "Flag_muonBadTrackFilter" ],
    "METFilters" : [ "Flag_METFilters" ],
}


#-------- SEQUENCE

from CMGTools.TTHAnalysis.analyzers.treeProducerSusyFullHad import *

treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerSusyFullHad',
##     AutoFillTreeProducer, name='treeProducerSusyCore',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     PDFWeights = PDFWeights,
     globalVariables = susyFullHad_globalVariables,
     globalObjects = susyFullHad_globalObjects,
     collections = susyFullHad_collections,
     defaultFloatType = 'F',
     treename = 'mt2'
)

susyCoreSequence.insert(susyCoreSequence.index(skimAnalyzer),
                        susyCounter)

#susyCoreSequence.insert(susyCoreSequence.index(ttHLepSkim),
#                        ttHZskim)

#susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
#                        ttHSVAna)


sequence = cfg.Sequence([
    lheWeightAna,
    skimAnalyzer,
    susyCounter,
   #eventSelector,
    jsonAna,
    triggerAna,
    pileUpAna,
    genAna,
    genHiggsAna,
    genHFAna,
    pdfwAna,
    susyScanAna,
    vertexAna,
    lepAna,
    ttHLepSkim,
    #ttHLepMCAna,
    photonAna,
    tauAna,
    jetAna,
    metAna,
    isoTrackAna,
    jetCleanAna,
    ttHCoreEventAna,
    triggerFlagsAna,
    eventFlagsAna,
    ttHMT2Control,
    MT2Ana,
    ttHTopoJetAna,
    ttHFatJetAna,
    treeProducer,
    ])

#sequence = cfg.Sequence(
#    susyCoreSequence+[
#    ttHMT2Control,
#    MT2Ana,
#    ttHTopoJetAna,
#    ttHFatJetAna,
#    # hbheFilterAna,
#    treeProducer,
#    ])

## NoHF add on
#sequence.insert(sequence.index(metAna),
#                metNoHFAna)
#sequence.insert(sequence.index(MT2Ana),
#                MT2AnaNoHF)


###---- to switch off the compression
#treeProducer.isCompressed = 0





from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption

#-------- HOW TO RUN
# choose 0 for quick validations tests. It doesn't require to load the sample files
# choose 2 for full mc production
# choose 3 for data production
# choose 4 for signal production
test = int(getHeppyOption('test',0))
#test = 0
isData = False # will be changed accordingly if chosen to run on data
doSpecialSettingsForMECCA = 1 # set to 1 for comparisons with americans
runPreprocessor = False

if test==0:
    # ------------------------------------------------------------------------------------------- #
    # --- all this lines taken from CMGTools.RootTools.samples.samples_13TeV_PHYS14
    # --- They may not be in synch anymore 
    from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
    kreator = ComponentCreator()
    # testComponent = kreator.makeMCComponent("testComponent", "/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_v3-v2/MINIAODSIM", "CMS", ".*root",489.9)
    testComponent = kreator.makeMCComponent("testComponent", "/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1/MINIAODSIM", "CMS", ".*root",489.9)
    samples=[testComponent]

    json='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/DCSOnly/json_DCSONLY.txt'

    dataDir = os.environ['CMSSW_BASE']+"/src/CMGTools/TTHAnalysis/data"

    from CMGTools.TTHAnalysis.setup.Efficiencies import *

    for comp in samples:
#        comp.isMC = True
#        comp.isData = False
        comp.splitFactor = 250 
        comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
        comp.puFileData=dataDir+"/puProfile_Data12.root"
        comp.efficiency = eff2012
        comp.json = json
    # ------------------------------------------------------------------------------------------- #

    #eventSelector.toSelect = [ 442430994 ]
    #sequence = cfg.Sequence([eventSelector] + sequence)
    comp=testComponent
    # 80X TTJets SingleLeptFromT for synch with SnT
    comp.files = ['file:/afs/cern.ch/user/m/mangano/public/MECCA/dataset/80X/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_109B2CAB-1205-E611-A9BE-0CC47A0AD6C4.root']
    #comp.files = ['root://xrootd.unl.edu//store/mc/RunIISpring16MiniAODv1/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1/00000/109B2CAB-1205-E611-A9BE-0CC47A0AD6C4.root']
    
    # 80X TTJets TuneCUETP8M1 for comparison with 76X
    # comp.files = ['root://xrootd.unl.edu//store/mc/RunIISpring16MiniAODv1/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_v3-v2/30000/00C07411-470D-E611-9A70-001E67E6F4C2.root']
    
    # 76X TTJets
    # comp.files = ['root://xrootd.unl.edu//store/mc/RunIIFall15MiniAODv2/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/00000/002253C9-DFB8-E511-8B0A-001A648F1C42.root']

    # 74X GJets
    #comp.files = ['root://xrootd.unl.edu//store/mc/RunIISpring15DR74/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/16E31BE7-7C18-E511-A551-00266CF2454C.root']

    # 747 Data
    #comp.files = ['/afs/cern.ch/user/m/mangano/public/MECCA/dataset/74X/data/JetHT_promptReco_Run2015B.root']
    #comp.files = ['/afs/cern.ch/work/m/mmasciov/CMSSW_7_4_7_MT2/src/CMGTools/TTHAnalysis/cfg/pickevents.root']

    # 7_4_12 data
    #isData = True
    #comp.files = ['/afs/cern.ch/user/c/casal/public/synch/86ACFECD-3C5F-E511-B8F2-02163E014374.root']

    selectedComponents = [comp]
#    comp.splitFactor = 10
#    comp.fineSplitFactor = 100

elif test==1:
    # Uncomment the two following lines to run on a specific event
    #eventSelector.toSelect = [ 84142401 ]
    #sequence = cfg.Sequence([eventSelector] + sequence)
    
#    from CMGTools.RootTools.samples.samples_13TeV_PHYS14 import *
#    from CMGTools.RootTools.samples.samples_13TeV_74X import *
    from CMGTools.RootTools.samples.samples_13TeV_RunIIFall15MiniAODv2 import *
#    from CMGTools.RootTools.samples.samples_8TeVReReco_74X import *
    # from CMGTools.RootTools.samples.samples_13TeV_DATA2015 import *

#    comp=GJets_HT200to400
#    comp.files = ['/afs/cern.ch/user/d/dalfonso/public/TESTfilesPHY14/gjets_ht200to400_miniaodsim_fix.root']

#    comp=TTJets
#    #comp.files = ['/afs/cern.ch/user/d/dalfonso/public/TESTfilesPHY14/TTJets_miniAOD_fixPhoton_forSynch.root']
#    comp.files = ['/afs/cern.ch/user/d/dalfonso/public/TESTspring/ttbar25nsmad_1ECE44F9-5F02-E511-9A65-02163E00EA1F.root']
#    #comp.files = ['/afs/cern.ch/user/d/dalfonso/public/74samples/JetHT_GR_R_74_V12_19May_RelVal/1294BDDB-B7FE-E411-8028-002590596490.root']
#    comp.files = ['/afs/cern.ch/user/m/mangano/public/MECCA/dataset/74X/data/JetHT_promptReco_Run2015B.root']

#    #synche file MC (v1 of the miniAOD)
#    comp=comp=TTJets_LO_50ns
#    comp.files = ['/afs/cern.ch/user/d/dalfonso/public/SYNCHfiles/0066F143-F8FD-E411-9A0B-D4AE526A0D2E.root']

    #synche file MC (v2 of the miniAOD)
#    comp=TTJets_LO
#    comp.files = ['/afs/cern.ch/work/d/dalfonso/public/001F4F14-786E-E511-804F-0025905A60FE.root']
   
    # comp=JetHT_Run2015D_Promptv4
    # comp.files = ['/afs/cern.ch/work/d/dalfonso/public/8ED4BA45-706D-E511-8D36-02163E014418.root']
    # comp.json = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/DCSOnly/json_DCSONLY.txt'

    selectedComponents = [TTJets_LO]
    for comp in selectedComponents:
        comp.files = ['root://xrootd.unl.edu//store/mc/RunIIFall15MiniAODv2/TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/00000/00D010B5-1EB9-E511-B950-02163E014965.root']
        comp.splitFactor = 1200

#    comp.triggers = triggers_HT900 + triggers_HTMET + triggers_photon155 + triggers_1mu_isolow + triggers_MT2_mumu + triggers_MT2_ee + triggers_MT2_mue # to apply trigger skimming

elif test==2:

    #from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14 import *
    # full production
#    selectedComponents = [ 
#TTJets, # TTJets
#TToLeptons_tch, TToLeptons_sch, TBarToLeptons_tch, TBarToLeptons_sch, TBar_tWch, T_tWch, #singleTop
#TTWJets, TTZJets, TTH, #TT+boson
#ZJetsToNuNu_HT100to200, ZJetsToNuNu_HT200to400, ZJetsToNuNu_HT400to600, ZJetsToNuNu_HT600toInf, # ZJetsToNuNu_HT
#WJetsToLNu_HT100to200, WJetsToLNu_HT200to400, WJetsToLNu_HT400to600, WJetsToLNu_HT600toInf, # WJetsToLNu_HT
#GJets_HT100to200_fixPhoton, GJets_HT200to400_fixPhoton, GJets_HT400to600_fixPhoton, GJets_HT600toInf_fixPhoton, # GJets_HT
#QCD_HT_100To250_fixPhoton, QCD_HT_250To500_fixPhoton, QCD_HT_500To1000_fixPhoton, QCD_HT_1000ToInf_fixPhoton, QCD_HT_250To500_ext1_fixPhoton, QCD_HT_500To1000_ext1_fixPhoton,QCD_HT_1000ToInf_ext1_fixPhoton, # QCD_HT
#QCD_Pt170to300_fixPhoton, QCD_Pt300to470_fixPhoton, QCD_Pt470to600_fixPhoton, QCD_Pt600to800_fixPhoton, QCD_Pt800to1000_fixPhoton, QCD_Pt1000to1400_fixPhoton, QCD_Pt1400to1800_fixPhoton, QCD_Pt1800to2400_fixPhoton, QCD_Pt2400to3200_fixPhoton, QCD_Pt3200_fixPhoton, # QCD_Pt
#QCD_Pt50to80, QCD_Pt80to120, QCD_Pt120to170, #For QCD Estimate
#SMS_T2tt_2J_mStop850_mLSP100, SMS_T2tt_2J_mStop650_mLSP325, SMS_T2tt_2J_mStop500_mLSP325, SMS_T2tt_2J_mStop425_mLSP325, SMS_T2qq_2J_mStop600_mLSP550, SMS_T2qq_2J_mStop1200_mLSP100, SMS_T2bb_2J_mStop900_mLSP100, SMS_T2bb_2J_mStop600_mLSP580, SMS_T1tttt_2J_mGl1500_mLSP100, SMS_T1tttt_2J_mGl1200_mLSP800, SMS_T1qqqq_2J_mGl1400_mLSP100, SMS_T1qqqq_2J_mGl1000_mLSP800, SMS_T1bbbb_2J_mGl1500_mLSP100, SMS_T1bbbb_2J_mGl1000_mLSP900, # SMS
#DYJetsToLL_M50_HT100to200, DYJetsToLL_M50_HT200to400, DYJetsToLL_M50_HT400to600, DYJetsToLL_M50_HT600toInf # DYJetsToLL_M50_HT
#]

#     from CMGTools.RootTools.samples.samples_13TeV_74X import *
# ### 25 ns
# #    selectedComponents = [ 
# #TTJets, TTJets_LO, # TTJets
# #QCD_Pt80to120, QCD_Pt120to170, QCD_Pt300to470, QCD_Pt470to600, QCD_Pt1000to1400, QCD_Pt1400to1800, QCD_Pt1800to2400, QCD_Pt2400to3200, QCD_Pt3200toInf, # QCD_Pt
# #]
# 
# ### 25    
# #    selectedComponents = [DYJetsToLL_M50_Zpt150toInf_LO]
# 
#     selectedComponents = ZJetsToNuNuHT + DYJetsM50HT + QCDPt + QCDHT + [
# TTJets_SingleLeptonFromT, TTJets_SingleLeptonFromTbar, TTJets_DiLepton,
# TTV, TToLeptons_tch, TbarToLeptons_tch, 
# TTJets_LO,
# #                                                                                                                                                                      
# GJets_HT100to200,
# GJets_HT200to400,
# GJets_HT400to600,
# GJets_HT600toInf,
# #
# WJetsToLNu_HT100to200,
# WJetsToLNu_HT200to400,
# WJetsToLNu_HT400to600,
# WJetsToLNu_HT600toInf,
# ] ### Full SM BG Spring15

    # test all components (1 thread per component).
    from CMGTools.RootTools.samples.samples_13TeV_RunIIFall15MiniAODv2 import ZGammaSig
### 25 ns
    selectedComponents = ZGammaSig

    for comp in selectedComponents:
        comp.splitFactor = 1200
        #comp.fineSplitFactor = 2 # to run two jobs per file
        comp.files = comp.files[:]
        #comp.files = comp.files[:1]
        #comp.files = comp.files[57:58]  # to process only file [57]  
        # triggers on MC
        #comp.triggers = triggers_HT900 + triggers_HTMET + triggers_photon155 + triggers_1mu_isolow + triggers_MT2_mumu + triggers_MT2_ee + triggers_MT2_mue # to apply trigger skimming

elif test==3:
    # run on data
    isData = True
    from CMGTools.RootTools.samples.samples_13TeV_DATA2015 import *

    dataDir = os.environ['CMSSW_BASE']+"/src/CMGTools/TTHAnalysis/data"
    json=dataDir+'/json/json_DCSONLY.txt'
    #synche file DATA
    #comp = JetHT_Run2015B_PromptReco
    #comp.files = ['/afs/cern.ch/user/m/mangano/public/MECCA/dataset/74X/data/JetHT_promptReco_Run2015B.root']
    #comp.files = ['root://eoscms.cern.ch//eos/cms/store/data/Run2015B/JetHT/MINIAOD/PromptReco-v1/000/251/643/00000/0AF95D60-992C-E511-8D36-02163E0146A4.root']
    #selectedComponents = [comp]

    ##selectedComponents = [JetHT_Run2015B, HTMHT_Run2015B, MET_Run2015B, SingleElectron_Run2015B, SingleMuon_Run2015B, SinglePhoton_Run2015B, DoubleEG_Run2015B, DoubleMuon_Run2015B, MuonEG_Run2015B]
    #selectedComponents = [JetHT_Run2015B_17Jul2015, HTMHT_Run2015B_17Jul2015, MET_Run2015B_17Jul2015, SingleElectron_Run2015B_17Jul2015, SingleMuon_Run2015B_17Jul2015, SinglePhoton_Run2015B_17Jul2015, DoubleEG_Run2015B_17Jul2015, MuonEG_Run2015B_17Jul2015, DoubleMuon_Run2015B_17Jul2015, JetHT_Run2015B_PromptReco, HTMHT_Run2015B_PromptReco, MET_Run2015B_PromptReco, SingleElectron_Run2015B_PromptReco, SingleMuon_Run2015B_PromptReco, SinglePhoton_Run2015B_PromptReco, DoubleEG_Run2015B_PromptReco, MuonEG_Run2015B_PromptReco, DoubleMuon_Run2015B_PromptReco]

    # selectedComponents = [JetHT_Run2015D, HTMHT_Run2015D, MET_Run2015D, SingleElectron_Run2015D, SingleMuon_Run2015D, SinglePhoton_Run2015D, DoubleEG_Run2015D, MuonEG_Run2015D, DoubleMuon_Run2015D]
    selectedComponents  = [ SinglePhoton_Run2015C_16Dec, SinglePhoton_Run2015D_16Dec ]
    
    for comp in selectedComponents:
        comp.json=json
        comp.files=comp.files[:]
        

elif test==4:

    from CMGTools.RootTools.samples.samples_13TeV_signals import *

### 25
    selectedComponents = + SignalSUSY + SignalEXO #+ SignalSUSYFullScan ###Signal Spring15
    
    # test all components (1 thread per component).
    for comp in selectedComponents:
        comp.splitFactor = 1200
        #comp.fineSplitFactor = 2 # to run two jobs per file
        comp.files = comp.files[:]
        # triggers on MC
        #comp.triggers = triggers_HT900 + triggers_HTMET + triggers_photon155 + triggers_1mu_isolow + triggers_MT2_mumu + triggers_MT2_ee + triggers_MT2_mue # to apply trigger skimming

# ------------------------------------------------------------------------------------------- #


if doSpecialSettingsForMECCA:
    jetAna.doQG = False
    # photonAna.do_randomCone = False
    # Below slow things note: it will in any case try it only on MC, not on data
    # photonAna.do_mc_match = False
    # jetAna.do_mc_match = False
    lepAna.do_mc_match = False
    isoTrackAna.do_mc_match = False
    genAna.makeLHEweights = False

if isData:
    for comp in samples:
        comp.isMC = False
        comp.isData = True
        #comp.files = ['/afs/cern.ch/user/d/dalfonso/public/74samples/JetHT_GR_R_74_V12_19May_RelVal/1294BDDB-B7FE-E411-8028-002590596490.root']



# ------------------------------------------------------------------------------------------- #


from PhysicsTools.HeppyCore.framework.services.tfile import TFileService 
output_service = cfg.Service(
      TFileService,
      'outputfile',
      name="outputfile",
      fname='mt2.root',
      option='recreate'
    )

# -------------------- Running Download from EOS

# the following is declared in case this cfg is used in input to the heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
from CMGTools.TTHAnalysis.tools.EOSEventsWithDownload import EOSEventsWithDownload
event_class = EOSEventsWithDownload
if getHeppyOption("nofetch"):
    event_class = Events


if runPreprocessor:
    removeResiduals = False
    # -------------------- Running pre-processor
    import subprocess

    if isData:
        #    uncFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_50nsV4_DATA_UncertaintySources_AK4PFchs.txt'
        #    jecDBFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_50nsV4_DATA.db'
        #    jecEra    = 'Summer15_50nsV4_DATA'
        uncFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_25nsV6_DATA_UncertaintySources_AK4PFchs.txt'
        jecDBFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_25nsV6_DATA.db'
        jecEra    = 'Summer15_25nsV6_DATA'
    else:
        #    uncFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_50nsV4_DATA_UncertaintySources_AK4PFchs.txt'
        #    jecDBFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_50nsV4_MC.db'
        #    jecEra    = 'Summer15_50nsV4_MC'
        uncFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_25nsV6_MC_UncertaintySources_AK4PFchs.txt'
        jecDBFile = '$CMSSW_BASE/src/CMGTools/RootTools/data/jec/Summer15_25nsV6_MC.db'
        jecEra    = 'Summer15_25nsV6_MC'
    preprocessorFile = "$CMSSW_BASE/tmp/MetType1_jec_%s.py"%(jecEra)
    extraArgs=[]
    if isData:
        extraArgs.append('--isData')
        GT= '74X_dataRun2_Prompt_v1'
    else:
        GT= 'MCRUN2_74_V9A'
    if removeResiduals:extraArgs.append('--removeResiduals')
    args = ['python',
            os.path.expandvars('$CMSSW_BASE/python/CMGTools/ObjectStudies/corMETMiniAOD_cfgCreator.py'),\
                '--GT='+GT,
            '--outputFile='+preprocessorFile,
            '--jecDBFile='+jecDBFile,
            '--uncFile='+uncFile,
            '--jecEra='+jecEra
            ] + extraArgs
    #print "Making pre-processorfile:"
    #print " ".join(args)
    subprocess.call(args)
    from PhysicsTools.Heppy.utils.cmsswPreprocessor import CmsswPreprocessor
    preprocessor = CmsswPreprocessor(preprocessorFile)


    config = cfg.Config( components = selectedComponents,
                         sequence = sequence,
                         services = [output_service],
                         preprocessor=preprocessor, # comment if pre-processor non needed
                         #                     events_class = event_class)
                         events_class = Events)
else:
    config = cfg.Config( components = selectedComponents,
                         sequence = sequence,
                         services = [output_service],
                         #                     events_class = event_class)
                         events_class = Events)


#printComps(config.components, True)
