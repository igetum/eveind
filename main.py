import csv


ores = {
    'veldspar' : {
        'cost': 3,
        'mineral_yeilds' : {
            'tritanium' : 199
        }
    },
    'scordite' : {
        'cost': 4,
        'mineral_yeilds' : {
            'tritanium' : 77.76,
            'pyrite' : 55.2
        }
    },
    'pyroxeres' : {
        'cost': 130,
        'mineral_yeilds' : {
            'tritanium' : 684,
            'pyrite' : 218,
            'mexallon' : 97.5,
            'nocxlum' : 11.7
        }
    },
    'plagioclase' : {
        'cost': 10,
        'mineral_yeilds' : {
            'tritanium' : 24.48,
            'pyrite' : 31.2,
            'mexallon' : 46.56,
        }
    },
    'omber' : {
        'cost': 192,
        'mineral_yeilds' : {
            'tritanium' : 234,
            'pyrite' : 29.64,
            'mexallon' : 21.45,
        }
    },
    'kernite' : {
        'cost': 385,
        'mineral_yeilds' : {
            'tritanium' : 104,
            'mexallon' : 187,
            'isogen' : 18.72
        }
    },
    'jaspet' : {
        'cost': 3313,
        'mineral_yeilds' : {
            'mexallon' : 738,
            'nocxium' : 14.4,
            'zydrine' : 16.8
        }
    },
    'hemorphite' : {
        'cost': 2240,
        'mineral_yeilds' : {
            'tritanium' : 2145,
            'isogen' : 62.4,
            'nocxium' : 5.07,
            'zydrine' : 19.5
        }
    },
    'hedbergite' : {
        'cost': 2252,
        'mineral_yeilds' : {
            'pyerite' : 819,
            'isogen' : 138,
            'nocxium' : 2.7,
            'zydrine' : 4.2
        }
    },
    'spodumain' : {
        'cost': 2252,
        'mineral_yeilds' : {
            'pyerite' : 1459,
            'isogen' : 23.4,
            'mexallon' : 140,
            'tritanium' : 7683,
        }
    },
    'dark ochre' : {
        'cost': 631,
        'mineral_yeilds' : {
            'tritanium' : 374,
            'isogen' : 21.84,
            'nocxium' : 16.77,
        }
    },
    'gneiss' : {
        'cost': 1126,
        'mineral_yeilds' : {
            'pyerite' : 343,
            'isogen' : 71.76,
            'mexallon' : 358,
        }
    },
    'crokite' : {
        'cost': 5300,
        'mineral_yeilds' : {
            'tritanium' : 11640,
            'nocxium' : 28.2,
            'zydrine' : 28.2,
        }
    }
}

minerals_costs = {
    'tritanium': 4,
    'pyrite' : 3,
    'mexallon': 25,
    'nocxlum' : 500,
    'isogen' : 0,
    'zydrine' : 0,
    'megacyte' : 0
}


def get_Data():

    with open('oredata.csv') as orecsv:
        reader = csv.reader(orecsv)


        for row in reader:
            if row[0].lower() in ores:
                ores[row[0]]['cost'] = row[1]

    with open('mineraldata.csv') as mineralcsv:
        reader = csv.reader(mineralcsv)

        for row in reader:
            if row[0].lower() in minerals_costs:
                minerals_costs[row[0]] = row[1]
            else:
                print('not matching mineral ' + row[0])



def calculate(ore, ore_amount) : 

    ore_batches_count = ore_amount / 100
    
    minerals_output = []
    for mineral in ores[ore]['mineral_yeilds']:
        minerals_output.append(mineral)

    mineral_profits_list = []
    mineral_breakout = {}

    for mineral in minerals_output:
        
        mineral_profits_list.append(float(ore_batches_count) * float(ores[ore]['mineral_yeilds'][mineral]) * float(minerals_costs[mineral]))

        mineral_breakout[mineral] = {
            'profit' : float(ore_batches_count) * float(ores[ore]['mineral_yeilds'][mineral]) * float(minerals_costs[mineral]),
            'cost' : float(minerals_costs[mineral]), 
            'units' : float(ore_batches_count) * float(ores[ore]['mineral_yeilds'][mineral])
        }


    total_mineral_profit = 0
    for profit in mineral_profits_list:
        total_mineral_profit = total_mineral_profit + profit


    ore_cost = float(ores[ore]['cost']) * ore_amount

    broker_fee = total_mineral_profit * .075
    corp_tax = total_mineral_profit * .15

    total_profit_tax = total_mineral_profit - broker_fee - corp_tax

  
    print('Total Cost of Ore: '  + str(ore_cost))
    print('\nMineral Breakdown')
    print('-------------------------------------------------------')
    for item in mineral_breakout:
        print('\t' + item + " :\t" + str(mineral_breakout[item]['cost']) + ' isk \t' + str(mineral_breakout[item]['units']) + ' units\t' +  str(mineral_breakout[item]['profit']) + ' isk')

    print('--------------------------------------------------------')
    print('Total Mineral Profits: ' + str(total_mineral_profit))
    print('Total Profits after fees/tax: ' + str(total_profit_tax))

    if (ore_cost > total_profit_tax):
        print("Don't Reprocess - Sell Ore")
    else: 
        print("\nYou make a profit reproccessing the ore (" + str((ore_cost/total_profit_tax)*100) + '% profit)' )

    print('\n\n\nPress Enter to Continue')
    input()   




def main ():

    print("Update the oredata.csv and mineraldata.cvs with updated pricing")
    input()
    get_Data()

    while(True):
    
        print('\n\n\nSelect order to calculate reprocess costs and profits:')
        print('\t1 : Veldspar')
        print('\t2 : Scordite')
        print('\t3 : Pyroxeres')
        print('\t4 : Plagiocase')
        print('\t5 : Omber')
        print('\t6 : Kernite')
        print('\t7 : Jaspet')
        print('\t8 : Hemorphite')
        print('\t9 : Hedbergite')
        print('\t10 : Spodumain')
        print('\t11 : Mercoxit')
        print('\t12 : Dark Orche')
        print('\t13 : Crokite')
        print('\t14 : Bistot')
        print('\t15 : Arkonor')
        print('\t16 : Mercoxit')
        print('\t0 : End Program')

        ore_selection = int(input())

        if(ore_selection == 1):
            print('Amount of Veldspar: ')
            ore_amount = int(input())
            calculate('veldspar', ore_amount)
        elif(ore_selection == 2):
            print('Amount of Scordite: ')
            ore_amount = int(input())
            calculate('scordite', ore_amount)
        elif(ore_selection == 3):
            print('Amount of Pyroxeres: ')
            ore_amount = float(input())
            calculate('pyroxeres', ore_amount)
        elif(ore_selection == 4):
            print('Amount of Plagioclase: ')
            ore_amount = float(input())
            calculate('plagioclase', ore_amount)
        elif(ore_selection == 5):
            print('Amount of Omber: ')
            ore_amount = float(input())
            calculate('omber', ore_amount)
        elif(ore_selection == 6):
            print('Amount of Kernite: ')
            ore_amount = float(input())
            calculate('kernite', ore_amount)
        elif(ore_selection == 7):
            print('Amount of Jaspet: ')
            ore_amount = float(input())
            calculate('jaspet', ore_amount)
        elif(ore_selection == 8):
            print('Amount of Hemorphite: ')
            ore_amount = float(input())
            calculate('hemorphite', ore_amount)
        elif(ore_selection == 9):
            print('Amount of hedbergite: ')
            ore_amount = float(input())
            calculate('hedbergite', ore_amount)
        elif(ore_selection == 10):
            print('Amount of Spodumain: ')
            ore_amount = float(input())
            calculate('Spodumain', ore_amount)
        elif(ore_selection == 11):
            print('Amount of Mercoxit: ')
            ore_amount = float(input())
            calculate('mercoxit', ore_amount)
        elif(ore_selection == 12):
            print('Amount of Dark Ochre: ')
            ore_amount = float(input())
            calculate('dark ochre', ore_amount)
        elif(ore_selection == 13):
            print('Amount of Gneiss: ')
            ore_amount = float(input())
            calculate('Gneiss', ore_amount)
        elif(ore_selection == 14):
            print('Amount of Crokite: ')
            ore_amount = float(input())
            calculate('crokite', ore_amount)
        elif(ore_selection == 15):
            print('Amount of Bistot: ')
            ore_amount = float(input())
            calculate('bistot', ore_amount)
        elif(ore_selection == 16):
            print('Amount of Arkonor: ')
            ore_amount = float(input())
            calculate('arkonor', ore_amount)    
        elif(ore_selection == 0):
            break
        else:
            print('Invalid Entry')



if __name__ == "__main__":
    main()