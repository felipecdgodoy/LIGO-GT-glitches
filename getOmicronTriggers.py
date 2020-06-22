from gwpy.table import EventTable
from gwtrigfind import find_trigger_files

def getOmicronTriggers(start, end, channel, snr_cutoff, segs=None):
  cache = find_trigger_files(channel, 'Omicron', start, end)
  t = EventTable.read(cache, format='ligolw', tablename='sngl_burst', selection=['snr>%f'%snr_cutoff])
  if (segs is not None):
    t = t.filter(('peak_time', in_segmentlist, segs))
  return t
