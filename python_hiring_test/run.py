"""Main script for generating output.csv."""
import csv
import pandas as pd

# Max Oelerking/March 20,2018

def main():
    #INPUT DATA FRAME
    PitchingData = pd.read_csv('./data/raw/pitchdata.csv')
#SUB DATA FRAMES FOR PLAYER STATS
#Grouping and Aggregating
    #RIGHT HANDED HITTER
    vsRHH = PitchingData.loc[PitchingData['HitterSide'] == 'R']
    vsRHH = vsRHH.groupby(['PitcherId']).sum()
    vsRHH = vsRHH[vsRHH['PA'] > 24]
    vsRHH['PitcherId'] = vsRHH.index
    vsRHH['AVG'] = round(vsRHH['H']/vsRHH['AB'],3)
    vsRHH['OBP'] = round((vsRHH['H']+vsRHH['BB']+vsRHH['HBP'])/(vsRHH['AB']+vsRHH['BB']+vsRHH['HBP']+vsRHH['SF']),3)
    vsRHH['SLG'] = round(vsRHH['TB']/vsRHH['AB'],3)
    vsRHH['OPS'] = round(vsRHH['OBP']+vsRHH['SLG'],3)
    #LEFT HANDED HITTERS
    vsLHH = PitchingData.loc[PitchingData['HitterSide'] == 'L']
    vsLHH = vsLHH.groupby(['PitcherId']).sum()
    vsLHH = vsLHH[vsLHH['PA'] > 24]
    vsLHH['PitcherId'] = vsLHH.index
    vsLHH['AVG'] = round(vsLHH['H']/vsLHH['AB'],3)
    vsLHH['OBP'] = round((vsLHH['H']+vsLHH['BB']+vsLHH['HBP'])/(vsLHH['AB']+vsLHH['BB']+vsLHH['HBP']+vsLHH['SF']),3)
    vsLHH['SLG'] = round(vsLHH['TB']/vsLHH['AB'],3)
    vsLHH['OPS'] = round(vsLHH['OBP']+vsLHH['SLG'],3)
    #RIGHT HANDED PITCHERS
    vsRHP = PitchingData.loc[PitchingData['PitcherSide'] == 'R']
    vsRHP = vsRHP.groupby(['HitterId']).sum()
    vsRHP = vsRHP[vsRHP['PA'] > 24]
    vsRHP['HitterId'] = vsRHP.index
    vsRHP['AVG'] = round(vsRHP['H']/vsRHP['AB'],3)
    vsRHP['OBP'] = round((vsRHP['H']+vsRHP['BB']+vsRHP['HBP'])/(vsRHP['AB']+vsRHP['BB']+vsRHP['HBP']+vsRHP['SF']),3)
    vsRHP['SLG'] = round(vsRHP['TB']/vsRHP['AB'],3)
    vsRHP['OPS'] = round(vsRHP['OBP']+vsRHP['SLG'],3)
    #LEFT HANDED PITCHERS
    vsLHP = PitchingData.loc[PitchingData['PitcherSide'] == 'L']
    vsLHP = vsLHP.groupby(['HitterId']).sum()
    vsLHP = vsLHP[vsLHP['PA'] > 24]
    vsLHP['HitterId'] = vsLHP.index
    vsLHP['AVG'] = round(vsLHP['H']/vsLHP['AB'],3)
    vsLHP['OBP'] = round((vsLHP['H']+vsLHP['BB']+vsLHP['HBP'])/(vsLHP['AB']+vsLHP['BB']+vsLHP['HBP']+vsLHP['SF']),3)
    vsLHP['SLG'] = round(vsLHP['TB']/vsLHP['AB'],3)
    vsLHP['OPS'] = round(vsLHP['OBP']+vsLHP['SLG'],3)
#SUB DATA FRAMES FOR TEAM STATS
#Grouping and Aggregating
    #RIGHT HANDED HITTERS
    vsRHHt = PitchingData.loc[PitchingData['HitterSide'] == 'R']
    vsRHHt = vsRHHt.groupby(['PitcherTeamId']).sum()
    vsRHHt['PitcherTeamId'] = vsRHHt.index
    vsRHHt['AVG'] = round(vsRHHt['H']/vsRHHt['AB'],3)
    vsRHHt['OBP'] = round((vsRHHt['H']+vsRHHt['BB']+vsRHHt['HBP'])/(vsRHHt['AB']+vsRHHt['BB']+vsRHHt['HBP']+vsRHHt['SF']),3)
    vsRHHt['SLG'] = round(vsRHHt['TB']/vsRHHt['AB'],3)
    vsRHHt['OPS'] = round(vsRHHt['OBP']+vsRHHt['SLG'],3)
    #LEFT HANDED HITTERS
    vsLHHt = PitchingData.loc[PitchingData['HitterSide'] == 'L']
    vsLHHt = vsLHHt.groupby(['PitcherTeamId']).sum()
    vsLHHt['PitcherTeamId'] = vsLHHt.index
    vsLHHt['AVG'] = round(vsLHHt['H']/vsLHHt['AB'],3)
    vsLHHt['OBP'] = round((vsLHHt['H']+vsLHHt['BB']+vsLHHt['HBP'])/(vsLHHt['AB']+vsLHHt['BB']+vsLHHt['HBP']+vsLHHt['SF']),3)
    vsLHHt['SLG'] = round(vsLHHt['TB']/vsLHHt['AB'],3)
    vsLHHt['OPS'] = round(vsLHHt['OBP']+vsLHHt['SLG'],3)
    #RIGHT HANDED PITCHERS
    vsRHPt = PitchingData.loc[PitchingData['PitcherSide'] == 'R']
    vsRHPt = vsRHPt.groupby(['HitterTeamId']).sum()
    vsRHPt['HitterTeamId'] = vsRHPt.index
    vsRHPt['AVG'] = round(vsRHPt['H']/vsRHPt['AB'],3)
    vsRHPt['OBP'] = round((vsRHPt['H']+vsRHPt['BB']+vsRHPt['HBP'])/(vsRHPt['AB']+vsRHPt['BB']+vsRHPt['HBP']+vsRHPt['SF']),3)
    vsRHPt['SLG'] = round(vsRHPt['TB']/vsRHPt['AB'],3)
    vsRHPt['OPS'] = round(vsRHPt['OBP']+vsRHPt['SLG'],3)
    #LEFT HANDED PITCHERS
    vsLHPt = PitchingData.loc[PitchingData['PitcherSide'] == 'L']
    vsLHPt = vsLHPt.groupby(['HitterTeamId']).sum()
    vsLHPt['HitterTeamId'] = vsLHPt.index
    vsLHPt['AVG'] = round(vsLHPt['H']/vsLHPt['AB'],3)
    vsLHPt['OBP'] = round((vsLHPt['H']+vsLHPt['BB']+vsLHPt['HBP'])/(vsLHPt['AB']+vsLHPt['BB']+vsLHPt['HBP']+vsLHPt['SF']),3)
    vsLHPt['SLG'] = round(vsLHPt['TB']/vsLHPt['AB'],3)
    vsLHPt['OPS'] = round(vsLHPt['OBP']+vsLHPt['SLG'],3)
#SUB DATA FRAMES FOR SPLIT COMBINATIONS
    #AVG,HitterId,vs RHP
    o1 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o1['SubjectId'] = vsRHP['HitterId']
    o1['Stat'] = "AVG"
    o1['Split'] = "vs RHP"
    o1['Subject'] = "HitterId"
    o1['Value'] = vsRHP['AVG']
    #OBP,HitterId,vs RHP
    o2 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o2['SubjectId'] = vsRHP['HitterId']
    o2['Stat'] = "OBP"
    o2['Split'] = "vs RHP"
    o2['Subject'] = "HitterId"
    o2['Value'] = vsRHP['OBP']
    #SLG,HitterId,vs RHP
    o3 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o3['SubjectId'] = vsRHP['HitterId']
    o3['Stat'] = "SLG"
    o3['Split'] = "vs RHP"
    o3['Subject'] = "HitterId"
    o3['Value'] = vsRHP['SLG']
    #OPS,HitterId,vs RHP
    o4 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o4['SubjectId'] = vsRHP['HitterId']
    o4['Stat'] = "OPS"
    o4['Split'] = "vs RHP"
    o4['Subject'] = "HitterId"
    o4['Value'] = vsRHP['OPS']
    #AVG,HitterId,vs LHP
    o5 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o5['SubjectId'] = vsLHP['HitterId']
    o5['Stat'] = "AVG"
    o5['Split'] = "vs LHP"
    o5['Subject'] = "HitterId"
    o5['Value'] = vsLHP['AVG']
    #OBP,HitterId,vs LHP
    o6 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o6['SubjectId'] = vsLHP['HitterId']
    o6['Stat'] = "OBP"
    o6['Split'] = "vs LHP"
    o6['Subject'] = "HitterId"
    o6['Value'] = vsLHP['OBP']
    #SLG,HitterId,vs LHP
    o7 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o7['SubjectId'] = vsLHP['HitterId']
    o7['Stat'] = "SLG"
    o7['Split'] = "vs LHP"
    o7['Subject'] = "HitterId"
    o7['Value'] = vsLHP['SLG']
    #OPS,HitterId,vs LHP
    o8 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o8['SubjectId'] = vsLHP['HitterId']
    o8['Stat'] = "OPS"
    o8['Split'] = "vs LHP"
    o8['Subject'] = "HitterId"
    o8['Value'] = vsLHP['OPS']
    #AVG,HitterTeamId,vs RHP
    o9 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o9['SubjectId'] = vsRHPt['HitterTeamId']
    o9['Stat'] = "AVG"
    o9['Split'] = "vs RHP"
    o9['Subject'] = "HitterTeamId"
    o9['Value'] = vsRHPt['AVG']
    #OBP,HitterTeamId,vs RHP
    o10 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o10['SubjectId'] = vsRHPt['HitterTeamId']
    o10['Stat'] = "OBP"
    o10['Split'] = "vs RHP"
    o10['Subject'] = "HitterTeamId"
    o10['Value'] = vsRHPt['OBP']
    #SLG,HitterTeamId,vs RHP
    o11 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o11['SubjectId'] = vsRHPt['HitterTeamId']
    o11['Stat'] = "SLG"
    o11['Split'] = "vs RHP"
    o11['Subject'] = "HitterTeamId"
    o11['Value'] = vsRHPt['SLG']
    #OPS,HitterTeamId,vs RHP
    o12 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o12['SubjectId'] = vsRHPt['HitterTeamId']
    o12['Stat'] = "OPS"
    o12['Split'] = "vs RHP"
    o12['Subject'] = "HitterTeamId"
    o12['Value'] = vsRHPt['OPS']
    #AVG,HitterTeamId,vs LHP
    o13 = pd.DataFrame(columns=['SubjectID','Stat','Split','Subject','Value'])
    o13['SubjectId'] = vsLHPt['HitterTeamId']
    o13['Stat'] = "AVG"
    o13['Split'] = "vs LHP"
    o13['Subject'] = "HitterTeamId"
    o13['Value'] = vsLHPt['AVG']
    #OBP,HitterTeamId,vs LHP
    o14 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o14['SubjectId'] = vsLHPt['HitterTeamId']
    o14['Stat'] = "OBP"
    o14['Split'] = "vs LHP"
    o14['Subject'] = "HitterTeamId"
    o14['Value'] = vsRHPt['OBP']
    #SLG,HitterTeamId,vs LHP
    o15 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o15['SubjectId'] = vsLHPt['HitterTeamId']
    o15['Stat'] = "SLG"
    o15['Split'] = "vs LHP"
    o15['Subject'] = "HitterTeamId"
    o15['Value'] = vsLHPt['SLG']
    #OPS,HitterTeamId,vs LHP
    o16 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o16['SubjectId'] = vsLHPt['HitterTeamId']
    o16['Stat'] = "OPS"
    o16['Split'] = "vs LHP"
    o16['Subject'] = "HitterTeamId"
    o16['Value'] = vsLHPt['OPS']
    #AVG,PitcherId,vs RHH
    o17 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o17['SubjectId'] = vsRHH['PitcherId']
    o17['Stat'] = "AVG"
    o17['Split'] = "vs RHH"
    o17['Subject'] = "PitcherId"
    o17['Value'] = vsRHH['AVG']
    #OBP,PitcherId,vs RHH
    o18 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o18['SubjectId'] = vsRHH['PitcherId']
    o18['Stat'] = "OBP"
    o18['Split'] = "vs RHH"
    o18['Subject'] = "PitcherId"
    o18['Value'] = vsRHH['OBP']
    #SLG,PitcherId,vs RHH
    o19 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o19['SubjectId'] = vsRHH['PitcherId']
    o19['Stat'] = "SLG"
    o19['Split'] = "vs RHH"
    o19['Subject'] = "PitcherId"
    o19['Value'] = vsRHH['SLG']
    #OPS,PitcherId,vs RHH
    o20 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o20['SubjectId'] = vsRHH['PitcherId']
    o20['Stat'] = "OPS"
    o20['Split'] = "vs RHH"
    o20['Subject'] = "PitcherId"
    o20['Value'] = vsRHH['OPS']
    #AVG,PitcherId,vs LHH
    o21 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o21['SubjectId'] = vsLHH['PitcherId']
    o21['Stat'] = "AVG"
    o21['Split'] = "vs LHH"
    o21['Subject'] = "PitcherId"
    o21['Value'] = vsLHH['AVG']
    #OBP,PitcherId,vs LHH
    o22 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o22['SubjectId'] = vsLHH['PitcherId']
    o22['Stat'] = "OBP"
    o22['Split'] = "vs LHH"
    o22['Subject'] = "PitcherId"
    o22['Value'] = vsLHH['OBP']
    #SLG,PitcherId,vs LHH
    o23 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o23['SubjectId'] = vsLHH['PitcherId']
    o23['Stat'] = "SLG"
    o23['Split'] = "vs LHH"
    o23['Subject'] = "PitcherId"
    o23['Value'] = vsLHH['SLG']
    #OPS,PitcherId,vs LHH
    o24 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o24['SubjectId'] = vsLHH['PitcherId']
    o24['Stat'] = "OPS"
    o24['Split'] = "vs LHH"
    o24['Subject'] = "PitcherId"
    o24['Value'] = vsLHH['OPS']
    #AVG,PitcherTeamId,vs RHH
    o25 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o25['SubjectId'] = vsRHHt['PitcherTeamId']
    o25['Stat'] = "AVG"
    o25['Split'] = "vs RHH"
    o25['Subject'] = "PitcherTeamId"
    o25['Value'] = vsRHHt['AVG']
    #OBP,PitcherTeamId,vs RHH
    o26 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o26['SubjectId'] = vsRHHt['PitcherTeamId']
    o26['Stat'] = "OBP"
    o26['Split'] = "vs RHH"
    o26['Subject'] = "PitcherTeamId"
    o26['Value'] = vsRHHt['OBP']
    #SLG,PitcherTeamId,vs RHH
    o27 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o27['SubjectId'] = vsRHHt['PitcherTeamId']
    o27['Stat'] = "SLG"
    o27['Split'] = "vs RHH"
    o27['Subject'] = "PitcherTeamId"
    o27['Value'] = vsRHHt['SLG']
    #OPS,PitcherTeamId,vs RHH
    o28 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o28['SubjectId'] = vsRHHt['PitcherTeamId']
    o28['Stat'] = "OPS"
    o28['Split'] = "vs RHH"
    o28['Subject'] = "PitcherTeamId"
    o28['Value'] = vsRHHt['OPS']
    #AVG,PitcherTeamId,vs LHH
    o29 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o29['SubjectId'] = vsLHHt['PitcherTeamId']
    o29['Stat'] = "AVG"
    o29['Split'] = "vs LHH"
    o29['Subject'] = "PitcherTeamId"
    o29['Value'] = vsLHHt['AVG']
    #OBP,PitcherTeamId,vs LHH
    o30 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o30['SubjectId'] = vsLHHt['PitcherTeamId']
    o30['Stat'] = "OBP"
    o30['Split'] = "vs LHH"
    o30['Subject'] = "PitcherTeamId"
    o30['Value'] = vsLHHt['OBP']
    #SLG,PitcherTeamId,vs LHH
    o31 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o31['SubjectId'] = vsLHHt['PitcherTeamId']
    o31['Stat'] = "SLG"
    o31['Split'] = "vs LHH"
    o31['Subject'] = "PitcherTeamId"
    o31['Value'] = vsLHHt['SLG']
    #OPS,PitcherTeamId,vs LHH
    o32 = pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    o32['SubjectId'] = vsLHHt['PitcherTeamId']
    o32['Stat'] = "OPS"
    o32['Split'] = "vs LHH"
    o32['Subject'] = "PitcherTeamId"
    o32['Value'] = vsLHHt['OPS']
#CREATE DATA FRAME FOR OUTPUT
    #DATA FRAME HEADERS {ID NUMBER   STAT TYPE   SPLIT TYPE   ID TYPE   NUMBER}
    OutPutData=pd.DataFrame(columns=['SubjectId','Stat','Split','Subject','Value'])
    #APPEND ALL CATEGORICAL DATA FRAMES
    OutPutData = o1.append([o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14,o15,o16,o17,o18,o19,o20,o21,o22,o23,o24,o25,o26,o27,o28,o29,o30,o31,o32])
    #SORT FINAL DATA FRAME
    OutPutData.sort_values(["SubjectId","Stat","Split","Subject","Value"],inplace=True,ascending=True)
    #HEADERS FOR CSV FILE
    header = ["SubjectId","Stat","Split","Subject","Value"]
    #MOVE DATA FRAME TO CSV FILE WITH HEADER
    OutPutData.to_csv('./data/reference/output.csv',columns=header,index=False)


if __name__ == '__main__':
    main()
