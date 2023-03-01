import yaml
import oyaml
import json

fname = "data.yaml"

def load_data():
    with open(fname, 'r') as stream:
        global data
        global tconfig
        tconfig = yaml.safe_load(stream)
        data = tconfig['data']

def tprint(dic):
        print(json.dumps(dic, indent=2, sort_keys=False))

def write_data():
    with open(fname, 'w') as yaml_file:
        yaml_file.write( oyaml.dump(tconfig, default_flow_style=False))

def tlist():
    for datum in data:
        print(f"{datum['id']} : {datum['tag']}")

def tinfo(id, key=None):
    issue = (next(x for x in data if x['id'] == id))
    if key:
        tprint(issue)
        return issue[key]
    else:
        return issue

def ttraces(id): 
    tprint(tinfo(id, 'traces'))

def ttraces(id, traces): 
    issue = tinfo(id)
    issue['traces'].append(traces)
    write_data()

def tcr(id):
    tprint(tinfo(id, 'cr'))

def tcr(id, cr): 
    issue = tinfo(id)
    issue['cr'] = cr
    write_data()


def tnotes(id):
    tprint(tinfo(id, 'notes'))

def tnotes(id, notes): 
    issue = tinfo(id)
    issue['notes'] = notes
    write_data()

def ttat(id):
    tprint(tinfo(id, 'tat'))

def twho(id):
    tprint(tinfo(id, 'who'))

def tthreads(id):
    ret = tinfo(id, 'threads')
    threads = list(x['name'] for x in ret)
    print(threads)

def tcrms(id):
    ret = tinfo(id, 'threads')
    crms = list({'name': x['name'], 'crms': x['crms']} for x in ret)
    tprint(crms)

def tlogs(id):
    ret = tinfo(id, 'threads')
    logs = list({'name': x['name'], 'logs': x['logs']} for x in ret)
    tprint(logs)

def tcreate(tag):
    tdatum = {}
    tdatum['id'] = max(x['id'] for x in data) + 1
    tdatum['tag'] = tag
    tdatum['open'] = True
    tdatum['team'] = 'wrf'
    tdatum['who'] = 'hak'
    tdatum['cr'] = ''
    tdatum['traces'] = []
    tdatum['notes'] = ''
    tdatum['tat'] = ''
    tdatum['thread'] = [{'name':'', 'logs': [], 'crms':[] }]
    data.append(tdatum)
    write_data()

    

load_data()
# listall(data)