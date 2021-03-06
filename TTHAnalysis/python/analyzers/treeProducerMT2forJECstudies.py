from CMGTools.TTHAnalysis.analyzers.treeProducerSusyCore import *
from CMGTools.TTHAnalysis.analyzers.ntupleTypes import *

MT2forJECstudies_globalVariables = susyCore_globalVariables + [

    ##--------------------------------------------------
    ## Filters
    ##--------------------------------------------------
    NTupleVariable("Flag_badChargedHadronFilter", lambda ev: ev.badChargedHadron, int, help="bad charged hadron filter decision"),
    NTupleVariable("Flag_badMuonFilter"         , lambda ev: ev.badMuon         , int, help="bad muon filter decision"),
    
    ##--------------------------------------------------
    ## energy sums
    ##--------------------------------------------------
    NTupleVariable("ht", lambda ev : ev.htJetXj10l5t, help="H_{T} computed from jets (with |eta|<2.5, pt > 40 GeV) and leptons (electrons and muons with |eta|<2.5, pt > 10 GeV)"),
    NTupleVariable("mht_pt", lambda ev : ev.mhtJetXj10l5t, help="H_{T}^{miss} computed from jets (with |eta|<2.5, pt > 40 GeV) and leptons (electrons ans muons with |eta|<2.5, pt > 10 GeV)"),
    NTupleVariable("mht_phi", lambda ev : ev.mhtPhiJetXj10l5t, help="H_{T}^{miss} #phi computed from jets (with |eta|<2.5, pt > 40 GeV) and leptons (electrons ans muons with |eta|<2.5, pt > 10 GeV)"),
    NTupleVariable("diffMetMht", lambda ev : ev.diffMetMht_Xj, help="abs( vec(mht) - vec(met) ) - with jets and leptons"),
    NTupleVariable("deltaPhiMin", lambda ev : ev.deltaPhiMin_Xj, help="minimal deltaPhi between the MET and the four leading jets with pt>40 and eta<2.4 and leptons (electrons ans muons with |eta|<2.5, pt > 10 GeV)"),
    NTupleVariable("jet1_pt", lambda ev : ev.cleanJets[0].pt() if len(ev.cleanJets)>0 else -99, help="pt of leading central jet"),
    NTupleVariable("jet2_pt", lambda ev : ev.cleanJets[1].pt() if len(ev.cleanJets)>1 else -99, help="pt of second central jet"),
    
    ### for now store the hadronic only
    NTupleVariable("ht_had", lambda ev : ev.htJetXj, help="H_{T} computed from only jets (with |eta|<2.5, pt > 40 GeV)"),
    NTupleVariable("mht_had_pt", lambda ev : ev.mhtJetXj, help="H_{T}^{miss} computed from only jets (with |eta|<2.5, pt > 40 GeV)"),
    NTupleVariable("mht_had_phi", lambda ev : ev.mhtPhiJetXj, help="H_{T}^{miss} #phi computed from only jets (with |eta|<2.5, pt > 40 GeV)"),
    NTupleVariable("diffMetMht_had", lambda ev : ev.diffMetMht_Xj_had, help="abs( vec(mht) - vec(met) ) - only jets"),
    NTupleVariable("deltaPhiMin_had", lambda ev : ev.deltaPhiMin_Xj_had, help="minimal deltaPhi between the MET and the four leading jets with pt>40 and eta<2.4"),

    ##--------------------------------------------------
    # Met definitions
    ##--------------------------------------------------

#    NTupleVariable("met_caloPt", lambda ev : ev.met.caloMETPt(), help="calo met p_{T}"),
#    NTupleVariable("met_caloPhi", lambda ev : ev.met.caloMETPhi(), help="calo met phi"),
#    NTupleVariable("met_caloSumEt", lambda ev : ev.met.caloMETSumEt(), help="calo met sumEt"),
    NTupleVariable("met_caloPt", lambda ev : ev.metUncor.caloMETPt(), help="calo met p_{T}"),
    NTupleVariable("met_caloPhi", lambda ev : ev.metUncor.caloMETPhi(), help="calo met phi"),
    NTupleVariable("met_caloSumEt", lambda ev : ev.metUncor.caloMETSumEt(), help="calo met sumEt"),

    NTupleVariable("met_miniaodPt", lambda ev : ev.metUncor.pt(), help="pfmet p_{T} as from miniAOD (for pfmet/calomet filter)"),

    NTupleVariable("met_trkPt", lambda ev : ev.tkMet.pt() if  hasattr(ev,'tkMet') else  0, help="tkmet p_{T}"),
    NTupleVariable("met_trkPhi", lambda ev : ev.tkMet.phi() if  hasattr(ev,'tkMet') else  0, help="tkmet phi"),
    NTupleVariable("met_trkSumEt", lambda ev : ev.tkMet.sumEt if  hasattr(ev,'tkMet') else  0 , help="TK sumEt charged dz<0.1 pt"),

    ##--------------------------------------------------
    # Physics object multplicities
    ##--------------------------------------------------
    
    NTupleVariable("nJet20", lambda ev: sum([j.pt() > 20 for j in ev.cleanJets]), int, help="Number of jets with pt > 20, |eta|<2.4"),
    NTupleVariable("nJet20a", lambda ev: sum([j.pt() > 20 for j in ev.cleanJetsAll]), int, help="Number of jets with pt > 20, |eta|<4.7"),
    NTupleVariable("nBJetLoose20", lambda ev: sum([j.btagWP("CSVv2IVFL") for j in ev.cleanJets if j.pt() > 20]), int, help="Number of jets with pt > 20 passing CSV loose"),
    NTupleVariable("nBJetMedium20", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.bjetsMedium if j.pt() > 20]), int, help="Number of jets with pt > 20 passing CSV medium"),
    NTupleVariable("nBJetTight20", lambda ev: sum([j.btagWP("CSVv2IVFT") for j in ev.bjetsMedium if j.pt() > 20]), int, help="Number of jets with pt > 20 passing CSV tight"),

    NTupleVariable("nJet20FailId", lambda ev: sum([j.pt() > 20 for j in ev.cleanJetsFailIdAll]), int, help="Number of jets after photon-cleaning with pt > 20, |eta|<4.7"),
    NTupleVariable("nJet25FailId", lambda ev: sum([j.pt() > 25 for j in ev.cleanJetsFailIdAll]), int, help="Number of jets after photon-cleaning with pt > 25, |eta|<4.7"),
    NTupleVariable("nJet30FailId", lambda ev: sum([j.pt() > 30 for j in ev.cleanJetsFailIdAll]), int, help="Number of jets after photon-cleaning with pt > 30, |eta|<4.7"),
    NTupleVariable("nJet100FailId", lambda ev: sum([j.pt() > 100 for j in ev.cleanJetsFailIdAll]), int, help="Number of jets after photon-cleaning with pt > 100, |eta|<4.7"),

    NTupleVariable("nJet20BadFastsim", lambda ev: sum([j.pt() > 20 and (j.mcJet.pt() if getattr(j,"mcJet",None) else 0.)==0. and j.chargedHadronEnergyFraction()<0.1 for j in ev.cleanJets]), int, help="Number of bad (fast-sim) jets with pt > 20, |eta|<2.5 (FASTSIM VETO)"),

    NTupleVariable("nBJet40", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.cleanJets if j.pt() > 40]), int, help="Number of jets with pt > 40 passing CSV medium"),
    NTupleVariable("nBJet30", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.cleanJets if j.pt() > 30]), int, help="Number of jets with pt > 25 passing CSV medium"),
    NTupleVariable("nBJet25", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.cleanJets if j.pt() > 25]), int, help="Number of jets with pt > 25 passing CSV medium"),
    NTupleVariable("nBJet20", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.cleanJets if j.pt() > 20]), int, help="Number of jets with pt > 20 passing CSV medium"),
#
    NTupleVariable("nBJet40mva", lambda ev: sum([j.btagWP("CMVAv2M") for j in ev.cleanJets if j.pt() > 40]), int, help="Number of jets with pt > 40 passing cMVAv2 medium"),
    NTupleVariable("nBJet30mva", lambda ev: sum([j.btagWP("CMVAv2M") for j in ev.cleanJets if j.pt() > 30]), int, help="Number of jets with pt > 25 passing cMVAv2 medium"),
    NTupleVariable("nBJet25mva", lambda ev: sum([j.btagWP("CMVAv2M") for j in ev.cleanJets if j.pt() > 25]), int, help="Number of jets with pt > 25 passing cMVAv2 medium"),
    NTupleVariable("nBJet20mva", lambda ev: sum([j.btagWP("CMVAv2M") for j in ev.cleanJets if j.pt() > 20]), int, help="Number of jets with pt > 20 passing cMVAv2 medium"),
#
    NTupleVariable("nBJet40csv", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.cleanJets if j.pt() > 40]), int, help="Number of jets with pt > 40 passing CSV medium"),
    NTupleVariable("nBJet30csv", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.cleanJets if j.pt() > 30]), int, help="Number of jets with pt > 25 passing CSV medium"),
    NTupleVariable("nBJet25csv", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.cleanJets if j.pt() > 25]), int, help="Number of jets with pt > 25 passing CSV medium"),
    NTupleVariable("nBJet20csv", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.cleanJets if j.pt() > 20]), int, help="Number of jets with pt > 20 passing CSV medium"),

    NTupleVariable("nMuons10", lambda ev: sum([l.pt() > 10 and abs(l.pdgId()) == 13 for l in ev.selectedLeptons]), int, help="Number of muons with pt > 10"),
    NTupleVariable("nElectrons10", lambda ev: sum([l.pt() > 10 and abs(l.pdgId()) == 11 for l in ev.selectedLeptons]), int, help="Number of electrons with pt > 10"),
    NTupleVariable("nTaus20", lambda ev: sum([l.pt() > 20 for l in ev.selectedTaus]), int, help="Number of taus with pt > 20"),
    NTupleVariable("nGammas20", lambda ev: sum([l.pt() > 20 for l in ev.selectedPhotons]), int, help="Number of photons with pt > 20"),

    
    NTupleVariable("minMTBMet", lambda ev: ev.minMTBMet, float, help="min Mt(b,met)"),
    NTupleVariable("nPFLep5LowMT", lambda ev: ev.nPFLep5LowMT, int, help="number of PF leptons (e,mu) with pt > 5, reliso < 0.2, MT < 100 "),
    NTupleVariable("nPFHad10LowMT", lambda ev: ev.nPFHad10LowMT, int, help="number of PF hadrons with pt > 10, reliso < 0.1, MT < 100 "),
    NTupleVariable("nLepLowMT", lambda ev: ev.nLepLowMT, int, help="number of leptons (POGID and isoTrack ) with MT < 100 "),

    NTupleVariable("nisrMatch", lambda ev: ev.nisrMatch, int, help="number of clean jets matched to ISR"),

    ##--------------------------------------------------
    # MT2
    ##--------------------------------------------------
    NTupleVariable("mt2_had", lambda ev: ev.mt2_Xj_had, float, help="mt2(j1,j2,met) with jets "),
    NTupleVariable("mt2ViaKt_had", lambda ev: ev.mt2ViaKt_Xj_had, float, help="mt2(j1,j2,met) with jets with KT pseudo jets"),
    NTupleVariable("mt2_bb", lambda ev: ev.mt2bb_Xj, float, help="mt2(b1,b2,met) with jets "),
    NTupleVariable("mt2_gen", lambda ev: ev.mt2_Xj_gen, float, mcOnly=True, help="mt2(j1,j2,met) with jets at genInfo"),
    
    NTupleVariable("mt2", lambda ev: ev.mt2_Xj, float, help="mt2(j1,j2,met) with jets and leptons"),
    NTupleVariable("gamma_mt2", lambda ev: ev.mt2_Xj_gamma, float, help="mt2(j1,j2,met) with photons added to met"),
    NTupleVariable("zll_mt2", lambda ev: ev.mt2_Xj_zll, float, help="mt2(j1,j2,met) with zll added to met, only hadrons"),
    NTupleVariable("zllmt_mt2", lambda ev: ev.mt2_Xj_zllmt, float, help="mt2(j1,j2,met) with zll (1 lepton only)  added to met, only hadrons"),
    NTupleVariable("rl_mt2", lambda ev: ev.mt2_Xj_rl, float, help="mt2(j1,j2,met) with 1 lepton added to met, only hadrons"),


    ##--------------------------------------------------
    # MT2
    ##--------------------------------------------------    
    NTupleVariable("mt2_genmet", lambda ev: ev.mt2_Xj_genmet, float, mcOnly=True, help="mt2(j1,j2,genmet) with jets and leptons"),
    NTupleVariable("diffMetMht_genmet", lambda ev : ev.diffMetMht_Xj_genmet, float, mcOnly=True, help="abs( vec(mht) - vec(genmet) ) - with jets and leptons"),
    NTupleVariable("deltaPhiMin_genmet", lambda ev : ev.deltaPhiMin_Xj_genmet, float, mcOnly=True, help="minimal deltaPhi between the genMET and the four leading jets with pt>40 and eta<2.4 and leptons (electrons ans muons with |eta|<2.5, pt > 10 GeV)"),

    

    ##--------------------------------------------------
    # Gamma variables
    ##--------------------------------------------------
    NTupleVariable("gamma_nJet20", lambda ev: sum([j.pt() > 20 for j in ev.gamma_cleanJets]), int, help="Number of jets after photon-cleaning with pt > 20, |eta|<2.4"),
    NTupleVariable("gamma_nJet25", lambda ev: sum([j.pt() > 25 for j in ev.gamma_cleanJets]), int, help="Number of jets after photon-cleaning with pt > 25, |eta|<2.4"),
    NTupleVariable("gamma_nJet30", lambda ev: sum([j.pt() > 30 for j in ev.gamma_cleanJets]), int, help="Number of jets after photon-cleaning with pt > 30, |eta|<2.4"),
    NTupleVariable("gamma_nJet40", lambda ev: sum([j.pt() > 40 for j in ev.gamma_cleanJets]), int, help="Number of jets after photon-cleaning with pt > 40, |eta|<2.4"),
# 
    NTupleVariable("gamma_nBJet20", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.gamma_cleanJets if j.pt() > 20]), int, help="Number jets after photon-cleaning  with pt > 20 passing CSV medium"),
    NTupleVariable("gamma_nBJet25", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.gamma_cleanJets if j.pt() > 25]), int, help="Number jets after photon-cleaning  with pt > 25 passing CSV medium"),
    NTupleVariable("gamma_nBJet30", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.gamma_cleanJets if j.pt() > 30]), int, help="Number jets after photon-cleaning  with pt > 25 passing CSV medium"),
    NTupleVariable("gamma_nBJet40", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.gamma_cleanJets if j.pt() > 40]), int, help="Number jets after photon-cleaning  with pt > 40 passing CSV medium"),
#
    NTupleVariable("gamma_nBJet20mva", lambda ev: sum([j.btagWP("CMVAv2M") for j in ev.gamma_cleanJets if j.pt() > 20]), int, help="Number jets after photon-cleaning  with pt > 20 passing cMVAv2 medium"),
    NTupleVariable("gamma_nBJet25mva", lambda ev: sum([j.btagWP("CMVAv2M") for j in ev.gamma_cleanJets if j.pt() > 25]), int, help="Number jets after photon-cleaning  with pt > 25 passing cMVAv2 medium"),
    NTupleVariable("gamma_nBJet30mva", lambda ev: sum([j.btagWP("CMVAv2M") for j in ev.gamma_cleanJets if j.pt() > 30]), int, help="Number jets after photon-cleaning  with pt > 25 passing cMVAv2 medium"),
    NTupleVariable("gamma_nBJet40mva", lambda ev: sum([j.btagWP("CMVAv2M") for j in ev.gamma_cleanJets if j.pt() > 40]), int, help="Number jets after photon-cleaning  with pt > 40 passing cMVAv2 medium"),
#
    NTupleVariable("gamma_nBJet20csv", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.gamma_cleanJets if j.pt() > 20]), int, help="Number jets after photon-cleaning  with pt > 20 passing CSV medium"),
    NTupleVariable("gamma_nBJet25csv", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.gamma_cleanJets if j.pt() > 25]), int, help="Number jets after photon-cleaning  with pt > 25 passing CSV medium"),
    NTupleVariable("gamma_nBJet30csv", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.gamma_cleanJets if j.pt() > 30]), int, help="Number jets after photon-cleaning  with pt > 25 passing CSV medium"),
    NTupleVariable("gamma_nBJet40csv", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.gamma_cleanJets if j.pt() > 40]), int, help="Number jets after photon-cleaning  with pt > 40 passing CSV medium"),
#
    NTupleVariable("gamma_nJet20FailId", lambda ev: sum([j.pt() > 20 for j in ev.gamma_cleanJetsFailIdAll]), int, help="Number of jets after photon-cleaning with pt > 20, |eta|<4.7"),
    NTupleVariable("gamma_nJet25FailId", lambda ev: sum([j.pt() > 25 for j in ev.gamma_cleanJetsFailIdAll]), int, help="Number of jets after photon-cleaning with pt > 25, |eta|<4.7"),
    NTupleVariable("gamma_nJet30FailId", lambda ev: sum([j.pt() > 30 for j in ev.gamma_cleanJetsFailIdAll]), int, help="Number of jets after photon-cleaning with pt > 30, |eta|<4.7"),
    NTupleVariable("gamma_nJet100FailId", lambda ev: sum([j.pt() > 100 for j in ev.gamma_cleanJetsFailIdAll]), int, help="Number of jets after photon-cleaning with pt > 100, |eta|<4.7"),



    NTupleVariable("gamma_ht", lambda ev : ev.gamma_htJetXj, help="H_{T} computed from only jets (with |eta|<2.5, pt > 40 GeV)"),
    NTupleVariable("gamma_deltaPhiMin", lambda ev : ev.gamma_deltaPhiMin_Xj_had, help="minimal deltaPhi between the MET and the four leading jets with pt>40 and eta<2.4"),
    NTupleVariable("gamma_diffMetMht", lambda ev : ev.gamma_diffMetMht_Xj_had, help="abs( vec(mht) - vec(met) )"),
    NTupleVariable("gamma_mht_pt", lambda ev : ev.gamma_mhtJetXj, help="H_{T}^{miss} computed from jets (with |eta|<2.5, pt > 40 GeV) and leptons (electrons ans muons with |eta|<2.5, pt > 10 GeV)"),
    NTupleVariable("gamma_mht_phi", lambda ev : ev.gamma_mhtPhiJetXj, help="H_{T}^{miss} #phi computed from jets (with |eta|<2.5, pt > 40 GeV) and leptons (electrons ans muons with |eta|<2.5, pt > 10 GeV)"),

    NTupleVariable("gamma_minMTBMet", lambda ev : ev.gamma_minMTBMet, help="min Mt(b,met)"),
    NTupleVariable("gamma_jet1_pt", lambda ev : ev.gamma_cleanJets[0].pt() if len(ev.gamma_cleanJets)>0 else -99, help="pt of leading central jet"),
    NTupleVariable("gamma_jet2_pt", lambda ev : ev.gamma_cleanJets[1].pt() if len(ev.gamma_cleanJets)>1 else -99, help="pt of second central jet"),

    ##--------------------------------------------------
    # Zll variables
    ##--------------------------------------------------
    NTupleVariable("zll_deltaPhiMin", lambda ev : ev.zll_deltaPhiMin_Xj, help="minimal deltaPhi between the zll MET and the four leading jets with pt>40 and eta<2.4"),
    NTupleVariable("zll_diffMetMht", lambda ev : ev.zll_diffMetMht_Xj, help="abs( vec(mht) - vec(met) ) - only jets for mht, jets plus 2 leptons for met"),
    NTupleVariable("zll_mht_pt", lambda ev : ev.zll_mhtJetXj, help="H_{T}^{miss} computed from only jets (with |eta|<2.5, pt > 40 GeV)"),
    NTupleVariable("zll_mht_phi", lambda ev : ev.zll_mhtPhiJetXj, help="H_{T}^{miss} #phi computed from only jets (with |eta|<2.5, pt > 40 GeV)"),
    NTupleVariable("zll_met_pt", lambda ev : ev.zll_met_pt, help="E_{T}^{miss} computed from jets (with |eta|<2.5, pt > 40 GeV) + 2 leptons"),
    NTupleVariable("zll_met_phi", lambda ev : ev.zll_met_phi, help="E_{T}^{miss} #phi computed from jets (with |eta|<2.5, pt > 40 GeV) + 2 leptons"),
    NTupleVariable("zll_ht", lambda ev: ev.zll_ht_Xj, float, help="H_{T} computed from only jets (with |eta|<2.5, pt > 40 GeV)"),

    NTupleVariable("zll_pt", lambda ev : ev.zll_p4.Pt() if ev.zll_p4.P()!=0 else -999., help="Pt of di-lepton system"),
    NTupleVariable("zll_eta", lambda ev : ev.zll_p4.Eta() if ev.zll_p4.P()!=0 else -999., help="Eta of di-lepton system"),
    NTupleVariable("zll_phi", lambda ev : ev.zll_p4.Phi() if ev.zll_p4.P()!=0 else -999., help="Phi of di-lepton system"),
    NTupleVariable("zll_mass", lambda ev : ev.zll_p4.M() if ev.zll_p4.P()!=0 else -999., help="Invariant mass of di-lepton system"),
    NTupleVariable("zll_minMTBMet", lambda ev: ev.zll_minMTBMet, float, help="min Mt(b,met) for zll, same as in main search"),

    # rl variables
    NTupleVariable("rl_deltaPhiMin", lambda ev : ev.rl_deltaPhiMin_Xj, help="minimal deltaPhi between the rl MET and the four leading jets with pt>40 and eta<2.4"),
    NTupleVariable("rl_diffMetMht", lambda ev : ev.rl_diffMetMht_Xj, help="abs( vec(mht) - vec(met) ) - only jets for mht, jets plus 2 leptons for met"),
    NTupleVariable("rl_mht_pt", lambda ev : ev.rl_mhtJetXj, help="H_{T}^{miss} computed from only jets (with |eta|<2.5, pt > 40 GeV)"),
    NTupleVariable("rl_mht_phi", lambda ev : ev.rl_mhtPhiJetXj, help="H_{T}^{miss} #phi computed from only jets (with |eta|<2.5, pt > 40 GeV)"),
    NTupleVariable("rl_met_pt", lambda ev : ev.rl_met_pt, help="E_{T}^{miss} computed from jets (with |eta|<2.5, pt > 40 GeV) + 2 leptons"),
    NTupleVariable("rl_met_phi", lambda ev : ev.rl_met_phi, help="E_{T}^{miss} #phi computed from jets (with |eta|<2.5, pt > 40 GeV) + 2 leptons"),
    NTupleVariable("rl_ht", lambda ev: ev.rl_ht_Xj, float, help="H_{T} computed from only jets (with |eta|<2.5, pt > 40 GeV)"),

    NTupleVariable("rl_pt", lambda ev : ev.rl_p4.Pt() if ev.rl_p4.P()!=0 else -999., help="Pt of di-lepton system"),
    NTupleVariable("rl_eta", lambda ev : ev.rl_p4.Eta() if ev.rl_p4.P()!=0 else -999., help="Eta of di-lepton system"),
    NTupleVariable("rl_phi", lambda ev : ev.rl_p4.Phi() if ev.rl_p4.P()!=0 else -999., help="Phi of di-lepton system"),
    NTupleVariable("rl_mass", lambda ev : ev.rl_p4.M() if ev.rl_p4.P()!=0 else -999., help="Invariant mass of di-lepton system"),
    NTupleVariable("rl_minMTBMet", lambda ev: ev.rl_minMTBMet, float, help="min Mt(b,met) for zll, same as in main search"),
    NTupleVariable("rl_mt", lambda ev: ev.rl_mt, float, help="Mt(l,met) for 1 lepton only"),

    # ZllMT variables
    NTupleVariable("zllmt_deltaPhiMin", lambda ev : ev.zllmt_deltaPhiMin_Xj, help="minimal deltaPhi between the zll MET and the four leading jets with pt>X and eta<2.4"),
    NTupleVariable("zllmt_diffMetMht", lambda ev : ev.zllmt_diffMetMht_Xj, help="abs( vec(mht) - vec(met) ) - only jets for mht, jets plus 2 leptons for met"),
    NTupleVariable("zllmt_mht_pt", lambda ev : ev.zllmt_mhtJetXj, help="H_{T}^{miss} computed from only jets (with |eta|<2.5, pt > X GeV)"),
    NTupleVariable("zllmt_mht_phi", lambda ev : ev.zllmt_mhtPhiJetXj, help="H_{T}^{miss} #phi computed from only jets (with |eta|<2.5, pt > X GeV)"),
    NTupleVariable("zllmt_met_pt", lambda ev : ev.zllmt_met_pt, help="E_{T}^{miss} computed from jets (with |eta|<2.5, pt > X GeV) + 2 leptons"),
    NTupleVariable("zllmt_met_phi", lambda ev : ev.zllmt_met_phi, help="E_{T}^{miss} #phi computed from jets (with |eta|<2.5, pt > X GeV) + 2 leptons"),
    NTupleVariable("zllmt_ht", lambda ev: ev.zllmt_ht_Xj, float, help="H_{T} computed from only jets (with |eta|<2.5, pt > X GeV)"),

    NTupleVariable("zllmt_pt", lambda ev : ev.zllmt_p4.Pt() if ev.zllmt_p4.P()!=0 else -999., help="Pt of di-lepton system"),
    NTupleVariable("zllmt_eta", lambda ev : ev.zllmt_p4.Eta() if ev.zllmt_p4.P()!=0 else -999., help="Eta of di-lepton system"),
    NTupleVariable("zllmt_phi", lambda ev : ev.zllmt_p4.Phi() if ev.zllmt_p4.P()!=0 else -999., help="Phi of di-lepton system"),
    NTupleVariable("zllmt_mass", lambda ev : ev.zllmt_p4.M() if ev.zllmt_p4.P()!=0 else -999., help="Invariant mass of di-lepton system"),
    NTupleVariable("zllmt_minMTBMet", lambda ev: ev.zllmt_minMTBMet, float, help="min Mt(b,met) for zll, same as in main search"),
    NTupleVariable("zllmt_mt", lambda ev: ev.zllmt_mt, float, help="Mt(l,met) for zll (1 lepton only)"),

    ###
]


MT2forJECstudies_globalObjects = susyCore_globalObjects.copy()
MT2forJECstudies_globalObjects.update({
            "gamma_met" : NTupleObject("gamma_met", fourVectorType, help="PF E_{T}^{miss}, plus photon, after type 1 corrections"),
})

# susyFullHad_collections = susyCore_collections.copy()
# susyFullHad_collections.update({
MT2forJECstudies_collections = {
        "selectedLeptons" : NTupleCollection("lep", leptonTypeSusy, 50, help="Leptons after the preselection", filter=lambda l : l.pt()>10 ),
        "selectedTaus"    : NTupleCollection("tau", tauTypeSusy, 50, help="Taus after the preselection"),
        "cleanJetsAll"       : NTupleCollection("jet", jetTypeSusyExtra, 100, help="all jets (w/ x-cleaning, w/ ID applied w/o PUID applied pt>20 |eta|<5.2) , sorted by pt", filter=lambda l : l.pt()>20  ),
        "cleanJetsFailIdAll"       : NTupleCollection("jetFailId", jetTypeSusyExtra, 100, help="all jets (w/ x-cleaning, w/o ID applied w/o PUID applied pt>20 |eta|<5.2) , sorted by pt", filter=lambda l : l.pt()>20 ),
        "selectedPhotons"    : NTupleCollection("gamma", photonTypeSusy, 50, help="photons with pt>20 and loose cut based ID"),
        "selectedIsoTrack"    : NTupleCollection("isoTrack", isoTrackType, 50, help="isoTrack, sorted by pt"),
}            
