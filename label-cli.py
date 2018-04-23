import json
import argparse
import webbrowser
import os

if __name__ == '__main__':
    # parse program arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, help="Input json file path")
    args = parser.parse_args()

    adverts = json.load(open(args.path))
    label_input_dict = []

    for item in adverts:
      ad_dict = {}
      url = 'https://www.sahibinden.com/%s' % item.get('uid')
      webbrowser.open_new_tab(url)
      print('ID: %s' % item.get('uid'))
      ad_dict.update({'uid' : ('%s' % item.get('uid'))})
      print('Paint: %s' % item.get('numberOfChangedParts'))
      print('Cahnge: %s' % item.get('numberOfPaintedParts'))
      print('Wasted: %s' % item.get('damageStatus'))
      var_0 = input("Painted Parts? : ")
      ad_dict.update({'paint' : ('%s' % var_0)})
      var_1 = input("Changed Parts? : ")
      ad_dict.update({'change' : ('%s' % var_1)})
      var_2 = input("Is it WASTED? : ")
      ad_dict.update({'wasted' : ('%s' % var_2)})
      label_input_dict.append(ad_dict)
      input("Press any key to continue...")
      os.system('reset')

    # print(label_input_dict)

    filename = input("What is the name of the output file? : ")
    with open(('%s.json' % filename), 'w') as outfile:
      json.dump(label_input_dict, outfile)
      

