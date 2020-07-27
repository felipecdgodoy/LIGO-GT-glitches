source /home/detchar/opt/gwpysoft/bin/activate

from gwpy.table import EventTable
from gwtrigfind import find_trigger_files
import pandas as pd

def getOmicronTriggers(start, end, channel, max_snr, segs=None):
    try:
        cache = find_trigger_files(channel, 'OMICRON', start, end)
        t = EventTable.read(cache, format='ligolw', tablename='sngl_burst', selection=['snr<=%f'%max_snr])
        if (segs is not None):
            t = t.filter(('peak_time', in_segmentlist, segs))
        print("SUCCESS fetch for " + str(channel))
        return t
    except:
        print("failed fetch for " + str(channel))

def getTriggerDf(start, end, channel_list, max_snr, segs=None):
    table_list = list()
    for c in channel_list:
        t = getOmicronTriggers(start, end, c, max_snr, segs)
        try:
            t = t.to_pandas()
            table_list.append(t)
        except:
            print("failed conversion for " + str(c))
    df = pd.concat(table_list)
    return df
