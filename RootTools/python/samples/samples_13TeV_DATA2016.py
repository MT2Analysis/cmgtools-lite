import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

### ----------------------------- Zero Tesla run  ----------------------------------------

dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"  # use environmental variable, useful for instance to run on CRAB
json=dataDir+'/json/json_DCSONLY.txt'




JetHT_Run2016B_PromptReco_v1          = kreator.makeDataComponent("JetHT_Run2016B_PromptReco_v1"         , "/JetHT/Run2016B-PromptReco-v1/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016B_PromptReco_v1          = kreator.makeDataComponent("HTMHT_Run2016B_PromptReco_v1"         , "/HTMHT/Run2016B-PromptReco-v1/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016B_PromptReco_v1            = kreator.makeDataComponent("MET_Run2016B_PromptReco_v1"           , "/MET/Run2016B-PromptReco-v1/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016B_PromptReco_v1 = kreator.makeDataComponent("SingleElectron_Run2016B_PromptReco_v1", "/SingleElectron/Run2016B-PromptReco-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016B_PromptReco_v1     = kreator.makeDataComponent("SingleMuon_Run2016B_PromptReco_v1"    , "/SingleMuon/Run2016B-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016B_PromptReco_v1   = kreator.makeDataComponent("SinglePhoton_Run2016B_PromptReco_v1"  , "/SinglePhoton/Run2016B-PromptReco-v1/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016B_PromptReco_v1       = kreator.makeDataComponent("DoubleEG_Run2016B_PromptReco_v1"      , "/DoubleEG/Run2016B-PromptReco-v1/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016B_PromptReco_v1         = kreator.makeDataComponent("MuonEG_Run2016B_PromptReco_v1"        , "/MuonEG/Run2016B-PromptReco-v1/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016B_PromptReco_v1     = kreator.makeDataComponent("DoubleMuon_Run2016B_PromptReco_v1"    , "/DoubleMuon/Run2016B-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json)

JetHT_Run2016B_PromptReco_v2          = kreator.makeDataComponent("JetHT_Run2016B_PromptReco_v2"         , "/JetHT/Run2016B-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016B_PromptReco_v2          = kreator.makeDataComponent("HTMHT_Run2016B_PromptReco_v2"         , "/HTMHT/Run2016B-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016B_PromptReco_v2            = kreator.makeDataComponent("MET_Run2016B_PromptReco_v2"           , "/MET/Run2016B-PromptReco-v2/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016B_PromptReco_v2 = kreator.makeDataComponent("SingleElectron_Run2016B_PromptReco_v2", "/SingleElectron/Run2016B-PromptReco-v2/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016B_PromptReco_v2     = kreator.makeDataComponent("SingleMuon_Run2016B_PromptReco_v2"    , "/SingleMuon/Run2016B-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016B_PromptReco_v2   = kreator.makeDataComponent("SinglePhoton_Run2016B_PromptReco_v2"  , "/SinglePhoton/Run2016B-PromptReco-v2/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016B_PromptReco_v2       = kreator.makeDataComponent("DoubleEG_Run2016B_PromptReco_v2"      , "/DoubleEG/Run2016B-PromptReco-v2/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016B_PromptReco_v2         = kreator.makeDataComponent("MuonEG_Run2016B_PromptReco_v2"        , "/MuonEG/Run2016B-PromptReco-v2/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016B_PromptReco_v2     = kreator.makeDataComponent("DoubleMuon_Run2016B_PromptReco_v2"    , "/DoubleMuon/Run2016B-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)


#run_range = (275377, 276097)
JetHT_Run2016C_PromptReco_v2          = kreator.makeDataComponent("JetHT_Run2016C_PromptReco_v2"         , "/JetHT/Run2016C-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016C_PromptReco_v2          = kreator.makeDataComponent("HTMHT_Run2016C_PromptReco_v2"         , "/HTMHT/Run2016C-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016C_PromptReco_v2            = kreator.makeDataComponent("MET_Run2016C_PromptReco_v2"           , "/MET/Run2016C-PromptReco-v2/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016C_PromptReco_v2 = kreator.makeDataComponent("SingleElectron_Run2016C_PromptReco_v2", "/SingleElectron/Run2016C-PromptReco-v2/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016C_PromptReco_v2     = kreator.makeDataComponent("SingleMuon_Run2016C_PromptReco_v2"    , "/SingleMuon/Run2016C-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016C_PromptReco_v2   = kreator.makeDataComponent("SinglePhoton_Run2016C_PromptReco_v2"  , "/SinglePhoton/Run2016C-PromptReco-v2/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016C_PromptReco_v2       = kreator.makeDataComponent("DoubleEG_Run2016C_PromptReco_v2"      , "/DoubleEG/Run2016C-PromptReco-v2/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016C_PromptReco_v2         = kreator.makeDataComponent("MuonEG_Run2016C_PromptReco_v2"        , "/MuonEG/Run2016C-PromptReco-v2/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016C_PromptReco_v2     = kreator.makeDataComponent("DoubleMuon_Run2016C_PromptReco_v2"    , "/DoubleMuon/Run2016C-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)

run_rangeD = (276311 , 276811) #full runD range
JetHT_Run2016D_PromptReco_v2          = kreator.makeDataComponent("JetHT_Run2016D_PromptReco_v2"         , "/JetHT/Run2016D-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json, run_rangeD)
HTMHT_Run2016D_PromptReco_v2          = kreator.makeDataComponent("HTMHT_Run2016D_PromptReco_v2"         , "/HTMHT/Run2016D-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json, run_rangeD)
MET_Run2016D_PromptReco_v2            = kreator.makeDataComponent("MET_Run2016D_PromptReco_v2"           , "/MET/Run2016D-PromptReco-v2/MINIAOD"           , "CMS", ".*root", json, run_rangeD)
SingleElectron_Run2016D_PromptReco_v2 = kreator.makeDataComponent("SingleElectron_Run2016D_PromptReco_v2", "/SingleElectron/Run2016D-PromptReco-v2/MINIAOD", "CMS", ".*root", json, run_rangeD)
SingleMuon_Run2016D_PromptReco_v2     = kreator.makeDataComponent("SingleMuon_Run2016D_PromptReco_v2"    , "/SingleMuon/Run2016D-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json, run_rangeD)
SinglePhoton_Run2016D_PromptReco_v2   = kreator.makeDataComponent("SinglePhoton_Run2016D_PromptReco_v2"  , "/SinglePhoton/Run2016D-PromptReco-v2/MINIAOD"  , "CMS", ".*root", json, run_rangeD)
DoubleEG_Run2016D_PromptReco_v2       = kreator.makeDataComponent("DoubleEG_Run2016D_PromptReco_v2"      , "/DoubleEG/Run2016D-PromptReco-v2/MINIAOD"      , "CMS", ".*root", json, run_rangeD)
MuonEG_Run2016D_PromptReco_v2         = kreator.makeDataComponent("MuonEG_Run2016D_PromptReco_v2"        , "/MuonEG/Run2016D-PromptReco-v2/MINIAOD"        , "CMS", ".*root", json, run_rangeD)
DoubleMuon_Run2016D_PromptReco_v2     = kreator.makeDataComponent("DoubleMuon_Run2016D_PromptReco_v2"    , "/DoubleMuon/Run2016D-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json, run_rangeD)

#run_range = (276831, 277420) #full runE range
JetHT_Run2016E_PromptReco_v2          = kreator.makeDataComponent("JetHT_Run2016E_PromptReco_v2"         , "/JetHT/Run2016E-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json)
HTMHT_Run2016E_PromptReco_v2          = kreator.makeDataComponent("HTMHT_Run2016E_PromptReco_v2"         , "/HTMHT/Run2016E-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json)
MET_Run2016E_PromptReco_v2            = kreator.makeDataComponent("MET_Run2016E_PromptReco_v2"           , "/MET/Run2016E-PromptReco-v2/MINIAOD"           , "CMS", ".*root", json)
SingleElectron_Run2016E_PromptReco_v2 = kreator.makeDataComponent("SingleElectron_Run2016E_PromptReco_v2", "/SingleElectron/Run2016E-PromptReco-v2/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2016E_PromptReco_v2     = kreator.makeDataComponent("SingleMuon_Run2016E_PromptReco_v2"    , "/SingleMuon/Run2016E-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)
SinglePhoton_Run2016E_PromptReco_v2   = kreator.makeDataComponent("SinglePhoton_Run2016E_PromptReco_v2"  , "/SinglePhoton/Run2016E-PromptReco-v2/MINIAOD"  , "CMS", ".*root", json)
DoubleEG_Run2016E_PromptReco_v2       = kreator.makeDataComponent("DoubleEG_Run2016E_PromptReco_v2"      , "/DoubleEG/Run2016E-PromptReco-v2/MINIAOD"      , "CMS", ".*root", json)
MuonEG_Run2016E_PromptReco_v2         = kreator.makeDataComponent("MuonEG_Run2016E_PromptReco_v2"        , "/MuonEG/Run2016E-PromptReco-v2/MINIAOD"        , "CMS", ".*root", json)
DoubleMuon_Run2016E_PromptReco_v2     = kreator.makeDataComponent("DoubleMuon_Run2016E_PromptReco_v2"    , "/DoubleMuon/Run2016E-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json)

run_rangeF = ( 277772, 277933) #full runF range
JetHT_Run2016F_PromptReco_v2          = kreator.makeDataComponent("JetHT_Run2016F_PromptReco_v2"         , "/JetHT/Run2016F-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json, run_rangeF)
HTMHT_Run2016F_PromptReco_v2          = kreator.makeDataComponent("HTMHT_Run2016F_PromptReco_v2"         , "/HTMHT/Run2016F-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json, run_rangeF)
MET_Run2016F_PromptReco_v2            = kreator.makeDataComponent("MET_Run2016F_PromptReco_v2"           , "/MET/Run2016F-PromptReco-v2/MINIAOD"           , "CMS", ".*root", json, run_rangeF)
SingleElectron_Run2016F_PromptReco_v2 = kreator.makeDataComponent("SingleElectron_Run2016F_PromptReco_v2", "/SingleElectron/Run2016F-PromptReco-v2/MINIAOD", "CMS", ".*root", json, run_rangeF)
SingleMuon_Run2016F_PromptReco_v2     = kreator.makeDataComponent("SingleMuon_Run2016F_PromptReco_v2"    , "/SingleMuon/Run2016F-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json, run_rangeF)
SinglePhoton_Run2016F_PromptReco_v2   = kreator.makeDataComponent("SinglePhoton_Run2016F_PromptReco_v2"  , "/SinglePhoton/Run2016F-PromptReco-v2/MINIAOD"  , "CMS", ".*root", json, run_rangeF)
DoubleEG_Run2016F_PromptReco_v2       = kreator.makeDataComponent("DoubleEG_Run2016F_PromptReco_v2"      , "/DoubleEG/Run2016F-PromptReco-v2/MINIAOD"      , "CMS", ".*root", json, run_rangeF)
MuonEG_Run2016F_PromptReco_v2         = kreator.makeDataComponent("MuonEG_Run2016F_PromptReco_v2"        , "/MuonEG/Run2016F-PromptReco-v2/MINIAOD"        , "CMS", ".*root", json, run_rangeF)
DoubleMuon_Run2016F_PromptReco_v2     = kreator.makeDataComponent("DoubleMuon_Run2016F_PromptReco_v2"    , "/DoubleMuon/Run2016F-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json, run_rangeF)


# old bad data (unlikely a run will be certified as good from this period)
dataSamples_Run2016B_PromptV1 = [JetHT_Run2016B_PromptReco_v1, HTMHT_Run2016B_PromptReco_v1, MET_Run2016B_PromptReco_v1, SingleElectron_Run2016B_PromptReco_v1, SingleMuon_Run2016B_PromptReco_v1, SinglePhoton_Run2016B_PromptReco_v1, DoubleEG_Run2016B_PromptReco_v1, MuonEG_Run2016B_PromptReco_v1, DoubleMuon_Run2016B_PromptReco_v1] 

# runB
dataSamples_Run2016B_PromptV2 = [JetHT_Run2016B_PromptReco_v2, HTMHT_Run2016B_PromptReco_v2, MET_Run2016B_PromptReco_v2, SingleElectron_Run2016B_PromptReco_v2, SingleMuon_Run2016B_PromptReco_v2, SinglePhoton_Run2016B_PromptReco_v2, DoubleEG_Run2016B_PromptReco_v2, MuonEG_Run2016B_PromptReco_v2, DoubleMuon_Run2016B_PromptReco_v2]
dataSamples_Run2016B_PromptV2_forQCD = [JetHT_Run2016B_PromptReco_v2, MET_Run2016B_PromptReco_v2, SingleElectron_Run2016B_PromptReco_v2]

# runC
dataSamples_Run2016C_PromptV2 = [JetHT_Run2016C_PromptReco_v2, HTMHT_Run2016C_PromptReco_v2, MET_Run2016C_PromptReco_v2, SingleElectron_Run2016C_PromptReco_v2, SingleMuon_Run2016C_PromptReco_v2, SinglePhoton_Run2016C_PromptReco_v2, DoubleEG_Run2016C_PromptReco_v2, MuonEG_Run2016C_PromptReco_v2, DoubleMuon_Run2016C_PromptReco_v2]
dataSamples_Run2016C_PromptV2_forQCD = [JetHT_Run2016C_PromptReco_v2, MET_Run2016C_PromptReco_v2, SingleElectron_Run2016C_PromptReco_v2]

# runD
dataSamples_Run2016D_PromptV2 = [JetHT_Run2016D_PromptReco_v2, HTMHT_Run2016D_PromptReco_v2, MET_Run2016D_PromptReco_v2, SingleElectron_Run2016D_PromptReco_v2, SingleMuon_Run2016D_PromptReco_v2, SinglePhoton_Run2016D_PromptReco_v2, DoubleEG_Run2016D_PromptReco_v2, MuonEG_Run2016D_PromptReco_v2, DoubleMuon_Run2016D_PromptReco_v2]
dataSamples_Run2016D_PromptV2_forQCD = [JetHT_Run2016D_PromptReco_v2, MET_Run2016D_PromptReco_v2, SingleElectron_Run2016D_PromptReco_v2]

# runE
dataSamples_Run2016E_PromptV2 = [JetHT_Run2016E_PromptReco_v2, HTMHT_Run2016E_PromptReco_v2, MET_Run2016E_PromptReco_v2, SingleElectron_Run2016E_PromptReco_v2, SingleMuon_Run2016E_PromptReco_v2, SinglePhoton_Run2016E_PromptReco_v2, DoubleEG_Run2016E_PromptReco_v2, MuonEG_Run2016E_PromptReco_v2, DoubleMuon_Run2016E_PromptReco_v2]
dataSamples_Run2016E_PromptV2_forQCD = [JetHT_Run2016E_PromptReco_v2, MET_Run2016E_PromptReco_v2, SingleElectron_Run2016E_PromptReco_v2]

# runF
dataSamples_Run2016F_PromptV2 = [JetHT_Run2016F_PromptReco_v2, HTMHT_Run2016F_PromptReco_v2, MET_Run2016F_PromptReco_v2, SingleElectron_Run2016F_PromptReco_v2, SingleMuon_Run2016F_PromptReco_v2, SinglePhoton_Run2016F_PromptReco_v2, DoubleEG_Run2016F_PromptReco_v2, MuonEG_Run2016F_PromptReco_v2, DoubleMuon_Run2016F_PromptReco_v2]
dataSamples_Run2016F_PromptV2_forQCD = [JetHT_Run2016F_PromptReco_v2, MET_Run2016F_PromptReco_v2, SingleElectron_Run2016F_PromptReco_v2]



### ----------------------------- summary ----------------------------------------

dataSamplesB = dataSamples_Run2016B_PromptV1 + dataSamples_Run2016B_PromptV2 + dataSamples_Run2016B_PromptV2_forQCD
dataSamplesC = dataSamples_Run2016C_PromptV2 + dataSamples_Run2016C_PromptV2_forQCD
dataSamplesD = dataSamples_Run2016D_PromptV2 + dataSamples_Run2016D_PromptV2_forQCD
dataSamplesE = dataSamples_Run2016E_PromptV2 + dataSamples_Run2016E_PromptV2_forQCD
dataSamplesF = dataSamples_Run2016F_PromptV2 + dataSamples_Run2016F_PromptV2_forQCD
samples = dataSamplesB + dataSamplesC + dataSamplesD + dataSamplesE + dataSamplesF

### ---------------------------------------------------------------------

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"

for comp in samples:
    comp.splitFactor = 1000
#    comp.splitFactor = 400
    comp.isMC = False
    comp.isData = True

if __name__ == "__main__":
   import sys
   if "test" in sys.argv:
       from CMGTools.RootTools.samples.ComponentCreator import testSamples
       testSamples(samples)
