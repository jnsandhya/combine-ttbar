import os, sys
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('observable', help='display your observable')
#parser.add_argument('wilson', help='display your wilson coefficient')
#parser.add_argument('asimov',nargs='?', help='set if asimov test', default='')

args = parser.parse_args()
observable = args.observable
#wilson = args.wilson
#asimov = args.asimov

#def asimov_param(w):
#    if asimov == 'asimov':
#        return ['--setParameters',w+'=0','-t','-1']
#    return []

#combine_m_dilep_24bins_2016_card.txt
os.system('cp inputs/2016/combine_'+observable+'_24bins_2016_card.txt .')
os.system('cp inputs/2017/combine_'+observable+'_24bins_2017_card.txt .')

cmd = 'combineCards.py combine_'+observable+'_24bins_2016_card.txt combine_'+observable+'_24bins_2017_card.txt > inputs/Comb/combine_'+observable+'_24bins_Comb_card.txt'
os.system(cmd)

#file = open('inputs/Comb/combine_'+observable+'_24bins_Comb_card.txt','a')
#file.write('timedep group = lumi_stability_2016 lumi_linearity_2016 emu_trig_2016 lumi_stability_2017 lumi_linearity_2017 emu_trig_2017\n')
#file.write('timeindep group = rttx rsingletop rdibosons rvjets syst_elec_reco syst_elec_id syst_muon_id syst_muon_iso syst_pu syst_b syst_pt_top syst_prefiring lumi_flat_uncor_2016 lumi_flat_uncor_2017 lumi_flat_cor CP5 hdamp erdOn QCDinspired GluonMove mtop jec')
#file.close()

os.system('rm combine_'+observable+'_24bins_2016_card.txt')
os.system('rm combine_'+observable+'_24bins_2017_card.txt')

#os.system('python scripts/workspace_multiSignalModel.py '+observable+' Comb')

#os.system('python scripts/fit_alone.py '+observable+' Comb '+wilson+' '+asimov)
