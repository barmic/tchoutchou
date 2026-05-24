#!/usr/bin/env python3

import itertools
import urllib.request
import urllib

materiel = [ 'TGVDASYE', 'TGVPSE', 'TGVA', 'TGVR', 'TGVDuplex', 'TGVRDuplex', 'TGVPOS', 'TGV2N2', 'TGVM', 'TGVLyria', 'eurostar_e320', 'TGVReseau', 'ICE3', 'TGVReseauItalie', 'TGVNeoDuplex', 'TGVEuroDuplex3UA', 'Regiolis', 'TGVAtlantique', 'TGVEuroDuplex', 'CoradiaLiner', 'Regio2N' ]
commercial = [ 'Oceane', 'Atlantique', 'Cassiopee', 'OmneoPremium', 'Mediterranee', 'Reseau', 'Lyria', 'Sud-Est', 'Lacroix', 'Tallon', 'CoradiaLiner', 'OUIGO', 'OUIGOTango', 'BR407', 'INTERCITES' ]
orientation = [ 'firstToSecond', 'secondToFirst' ]
livree = [ 'carmillon', 'atlantique', 'inoui', 'ouigo', 'lyria', 'lacroix', 'blueGreenMobigo', 'db', 'yellowRemi' ]
voitures = [ '8C', '7C', '10C', '8R', '6C' ]


for mat in materiel:
    for com in commercial:
        for ori in orientation:
            for liv in livree:
                for voit in voitures:
                    imgName = f"{mat}-{com}_{ori}_{liv}_{voit}.png"
                    imgEncName = f"{mat}%E2%80%94{com}_{ori}_{liv}_{voit}.png"
                    url = f"https://www.sncf-connect.com/staticsTrainComposition/{imgEncName}"
                    print(url)
                    imgName = f"{mat}_{ori}_{liv}_{voit}.png"
                    imgEncName = f"{mat}_{ori}_{liv}_{voit}.png"
                    url = f"https://www.sncf-connect.com/staticsTrainComposition/{imgEncName}"
                    print(url)
                    #urllib.request.urlretrieve(url, imgName)
                    # https://www.sncf-connect.com/staticsTrainComposition/TGVDASYE%E2%80%94Oceane_firstToSecond_carmillon_8C.png
# https://www.sncf-connect.com/staticsTrainComposition/TGVReseau%E2%80%94Lacroix_firstToSecond_carmillon_8C.png
# https://www.sncf-connect.com/staticsTrainComposition/TGVNeoDuplex_firstToSecond_carmillon_8C.png
# https://www.sncf-connect.com/staticsTrainComposition/TGVEuroDuplex3UA_firstToSecond_carmillon_8C.png
# https://www.sncf-connect.com/staticsTrainComposition/2NNG_blueAURA_3C.png
# https://www.sncf-connect.com/staticsTrainComposition/2NNGR_blueAURA_3C.png
# https://www.sncf-connect.com/staticsTrainComposition/AGC_redOccitanieLio_3C.png
# https://www.sncf-connect.com/staticsTrainComposition/AGCR_redOccitanieLio_3C.png
# https://www.sncf-connect.com/staticsTrainComposition/AGC_bluePACA_4C.png
# https://www.sncf-connect.com/staticsTrainComposition/AGC_redLanguedoc_4C.png
# https://www.sncf-connect.com/staticsTrainComposition/AGC_blueZouSud_4C.png
# https://www.sncf-connect.com/staticsTrainComposition/AGC_redLanguedoc_4C.png
# https://www.sncf-connect.com/staticsTrainComposition/AGC_blueZouSud_4C.png
# https://www.sncf-connect.com/staticsTrainComposition/TGVNeoDuplex_firstToSecond_carmillon_8C.png
# https://www.sncf-connect.com/staticsTrainComposition/AGC_blueRedOccitanieLio_3C.png
# https://www.sncf-connect.com/staticsTrainComposition/Regiolis_orangePACA_4C.png
# https://www.sncf-connect.com/staticsTrainComposition/TGVEuroDuplex%E2%80%94Oceane_firstToSecond_carmillon_8C.png
# https://www.sncf-connect.com/staticsTrainComposition/Regiolis%E2%80%94CoradiaLiner_firstToSecond_blueGreenMobigo_6C.png
# https://www.sncf-connect.com/staticsTrainComposition/TGVDASYE%E2%80%94OUIGO_firstToSecond_ouigo_8C.png
# https://www.sncf-connect.com/staticsTrainComposition/TGVDASYE%E2%80%94OUIGOTango_firstToSecond_ouigo_8C.png
# https://www.sncf-connect.com/staticsTrainComposition/TGVAtlantique%E2%80%94Lacroix_firstToSecond_carmillon_10C.png
# https://www.sncf-connect.com/staticsTrainComposition/TGVEuroDuplex%E2%80%94Oceane_firstToSecond_carmillon_8C.png
# https://www.sncf-connect.com/staticsTrainComposition/Regio2N_blackBretagne_6C.png
# https://www.sncf-connect.com/staticsTrainComposition/Regio2N_blackBretagne_8C.png
# https://www.sncf-connect.com/staticsTrainComposition/BB22200_beton_0C.png
# https://www.sncf-connect.com/staticsTrainComposition/Regiolis_blueOccitanieLio_4C.png
# https://www.sncf-connect.com/staticsTrainComposition/AGC_redNouvelleAquitaine_3C.png
# https://www.sncf-connect.com/staticsTrainComposition/BB7200_beton_0C.png
# https://www.sncf-connect.com/staticsTrainComposition/AGC_greenAndBlueHDF_4C.png
# https://www.sncf-connect.com/staticsTrainComposition/AGC_greenAndBlueHDF_4C.png
# https://www.sncf-connect.com/staticsTrainComposition/2NNG_yellowNPDC_3C.png
# https://www.sncf-connect.com/staticsTrainComposition/Regiolis%E2%80%94CoradiaLiner_greenAndBlueHDF_6C.png
# https://www.sncf-connect.com/staticsTrainComposition/Regiolis_greenHDF_6C.png
# https://www.sncf-connect.com/staticsTrainComposition/2NNGR_blueHDF_3C.png
# https://www.sncf-connect.com/staticsTrainComposition/AGC_blueAlsace_4C.png
# https://www.sncf-connect.com/staticsTrainComposition/BB26000_fluoGrandEst_0C.png
# https://www.sncf-connect.com/staticsTrainComposition/Regiolis_fluoGrandEst_6C.png
# https://www.sncf-connect.com/staticsTrainComposition/AGC_blueFrancheComte_3C.png
# https://www.sncf-connect.com/staticsTrainComposition/Regiolis_firstToSecond_blueGreenMobigo_4C.png
# https://www.sncf-connect.com/staticsTrainComposition/CoradiaLiner_secondToFirst_carmillon_6C.png
# https://www.sncf-connect.com/staticsTrainComposition/BB22200_beton_0C.png
# https://www.sncf-connect.com/staticsTrainComposition/Regiolis_redNouvelleAquitaine_4C.png
# https://www.sncf-connect.com/staticsTrainComposition/BB22200_beton_0C.png
# https://www.sncf-connect.com/staticsTrainComposition/ATER_redNouvelleAquitaine_1C.png
# https://www.sncf-connect.com/staticsTrainComposition/Regiolis_blueOccitanieLio_4C.png
# https://www.sncf-connect.com/staticsTrainComposition/AGCR_blueAURA_3C.png
# https://www.sncf-connect.com/staticsTrainComposition/Z100TrainJaune_redLanguedoc_1C.png
# https://www.sncf-connect.com/staticsTrainComposition/2NNG_redMonaco_4C.png
# https://www.sncf-connect.com/staticsTrainComposition/Regio2N_orangePACA_8C.png
# https://www.sncf-connect.com/staticsTrainComposition/ICE3%E2%80%94BR407_firstToSecond_db_8C.png
# https://www.sncf-connect.com/staticsTrainComposition/RABe522FlirtLEX_redLex_4C.png
# https://www.sncf-connect.com/staticsTrainComposition/TGVReseauItalie%E2%80%94Lacroix_secondToFirst_carmillon_8C.png
# https://www.sncf-connect.com/staticsTrainComposition/Corail%E2%80%94INTERCITES_firstToSecond_carmillon_9C.png
# https://www.sncf-connect.com/staticsTrainComposition/Regiolis_redOccitanieLio_4C.png
# https://www.sncf-connect.com/staticsTrainComposition/ATER_blueAURA_1C.png
# https://www.sncf-connect.com/staticsTrainComposition/ATER_redNouvelleAquitaine_1C.png
# https://www.sncf-connect.com/staticsTrainComposition/AGC_yellowChampagne_3C.png
# https://www.sncf-connect.com/staticsTrainComposition/AGC_neutralFluo_3C.png
# https://www.sncf-connect.com/staticsTrainComposition/Regiolis_firstToSecond_blueGreenMobigo_4C.png

# https://www.sncf-connect.com/staticsTrainComposition/Regiolis_normandieFortVert_6C.png
# https://www.sncf-connect.com/staticsTrainComposition/Regio2N%E2%80%94OmneoPremium_firstToSecond_yellowRemi_8C.png


# TER
first = [ '2NNG', '2NNGR', 'AGC', 'AGCR', 'Regiolis', 'Regio2N', 'BB22200', 'BB7200', f'Regiolis%E2%80%94CoradiaLiner', 'BB26000', 'ATER', 'Z100TrainJaune', 'RABe522FlirtLEX' ]
second = [ 'blueAURA', 'redOccitanieLio', 'bluePACA', 'redLanguedoc', 'blueZouSud', 'blueRedOccitanieLio', 'neutralFluo', 'yellowChampagne', 'orangePACA', 'blueGreenMobigo', 'redLex', 'blackBretagne', 'redMonaco', 'beton', 'blueOccitanieLio', 'redNouvelleAquitaine', 'greenAndBlueHDF', 'yellowNPDC', 'greenHDF', 'blueHDF', 'blueAlsace', 'fluoGrandEst', 'blueFrancheComte', 'blueAURA', 'normandieFortVert' ]
third = [ '3C', '4C', '6C', '8C', '0C', '1C' ]

for f in first:
    for s in second:
        for t in third:
            imgName = f"{f}_{s}_{t}.png"
            url = f"https://www.sncf-connect.com/staticsTrainComposition/{imgName}"
            print(url)
